from __future__ import annotations

import time
from pathlib import Path
from typing import Union
from uuid import uuid4

from selenium.webdriver.chrome.webdriver import WebDriver


class WebDriverTools:
    INFINITE_SCROLL_TIME = 5

    def __init__(
        self,
        webdriver: WebDriver,
        download_path: Union[Path, str] = Path("./files"),
    ):
        self.webdriver = webdriver
        if isinstance(download_path, str):
            download_path = Path(download_path)
        self.download_path = download_path
        self.download_path.mkdir(exist_ok=True)
        self.screenshot_path = self.download_path.joinpath("prints")
        self.screenshot_path.mkdir(exist_ok=True)

    def save_screen(self):
        file_path = str(self.screenshot_path.joinpath(f"{uuid4()!s}.png"))
        self.webdriver.save_screenshot(file_path)
        print(f">> print {self.webdriver.current_url=} / {file_path=}")

    def scroll_to_end(self):
        screen_height = self.webdriver.execute_script("return window.screen.height;")
        i = 1
        while True:
            self.webdriver.execute_script(
                "window.scrollTo(0, {screen_height}*{i});".format(
                    screen_height=screen_height, i=i
                )
            )
            i += 1
            time.sleep(self.INFINITE_SCROLL_TIME)
            scroll_height = self.webdriver.execute_script(
                "return document.body.scrollHeight;"
            )
            if (screen_height) * i > scroll_height:
                break
