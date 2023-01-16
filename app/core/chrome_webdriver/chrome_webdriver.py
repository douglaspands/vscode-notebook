from __future__ import annotations

import traceback
from pathlib import Path
from typing import Union

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from seleniumwire.request import Request
from seleniumwire.webdriver import Chrome

from app import config

from .chromedriver_installer import download_chromedriver


class ChromeWebDriver:
    def __init__(
        self,
        implicitly_wait: int = 0,
        headers: dict[str, str] = None,
        headless: bool = True,
        window_size: str = "1920x1080",
        download_path: Union[Path, str] = Path("./files"),
    ):
        if isinstance(download_path, str):
            download_path = Path(download_path)
        download_path.mkdir(parents=True, exist_ok=True)
        config.CHROME_PATH.mkdir(parents=True, exist_ok=True)
        self._chromedriver_path = download_chromedriver(
            path=config.CHROME_PATH, no_ssl=False
        )
        self._window_size = ",".join(window_size.split("x"))
        self._webdriver: WebDriver = None
        self._implicitly_wait = implicitly_wait
        self._headers = {}
        if headers and isinstance(headers, dict):
            self._headers.update(headers)
        self._options = Options()
        prefs = {
            "download.default_directory": str(download_path.resolve()),
            "download.prompt_for_download": False,
            "directory_upgrade": True,
            "safebrowsing.enabled": True,
        }
        self._options.add_experimental_option("prefs", prefs)
        self._options.add_experimental_option(
            "excludeSwitches", ["load-extension", "enable-automation"]
        )
        self._options.add_argument("--disable-extensions")
        if headless:
            self._options.add_argument("--headless")
        # self._options.add_argument("--no-sandbox")
        self._options.add_argument("--disable-dev-shm-usage")
        self._options.add_argument("window-size=" + self._window_size)

    def __enter__(self) -> WebDriver:
        return self.webdriver

    def __exit__(self, exc_type, exc_value, exc_traceback) -> None:
        if exc_type:
            print(
                "".join(traceback.format_exception(exc_type, exc_value, exc_traceback))
            )
        self.quit()
        self.__del__()

    def __del__(self) -> None:
        del self

    def _interceptor(self, request: Request):
        for hk, hv in self._headers.items():
            if request.headers.get(hk):
                del request.headers[hk]
            request.headers[hk] = hv

    @property
    def webdriver(self) -> WebDriver:
        if not self._webdriver:
            # self._webdriver = Chrome("chromedriver", options=self._options)
            self._webdriver = Chrome(self._chromedriver_path, options=self._options)
            self._webdriver.request_interceptor = self._interceptor
            if self._implicitly_wait:
                self._webdriver.implicitly_wait(self._implicitly_wait)
        return self._webdriver

    def quit(self):
        if self._webdriver:
            self._webdriver.quit()
