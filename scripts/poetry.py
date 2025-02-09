from __future__ import annotations

import re
import shlex
from functools import cache
from pathlib import Path
import subprocess

APP_PATH = Path("./app")


def run_makerequirements():
    run_shell(
        "poetry export -f requirements.txt --without-hashes --output requirements.txt"
    )


def run_shell(cmd: str):
    print(f"$ {cmd}")
    subprocess.run(cmd, check=True, shell=True)


def get_app_folder() -> str:
    @cache
    def wrapper() -> str:
        return shlex.quote(str(APP_PATH.resolve()))

    return wrapper()


def run_pycache_remove():
    pycache_regex = re.compile(r"^.+__pycache__$")

    for pycache_dir in APP_PATH.rglob("__pycache__"):
        if pycache_dir.is_dir() and pycache_regex.search(str(pycache_dir)):
            run_shell(f"rm -Rf {pycache_dir!s}")
            print(f"Folder removed {shlex.quote(str(pycache_dir))}")


def run_ruff_sort():
    cmd = [
        "ruff check --select I --fix",
        get_app_folder(),
    ]
    run_shell(" ".join(cmd))


def run_ruff_format():
    cmd = [
        "ruff format",
        get_app_folder(),
    ]
    run_shell(" ".join(cmd))


def run_format():
    run_ruff_sort()
    run_ruff_format()
