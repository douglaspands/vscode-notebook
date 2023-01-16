from __future__ import annotations

import os
import re
import shlex
from functools import cache
from pathlib import Path

APP_PATH = Path("./app")


def run_makerequirements():
    os.system(
        "poetry export -f requirements.txt --without-hashes --output requirements.txt"
    )


def run_shell(cmd: str):
    print(f"$ {cmd}")
    os.system(cmd)


def get_app_folder() -> str:
    @cache
    def wrapper() -> str:
        return shlex.quote(str(APP_PATH.resolve()))

    return wrapper()


def run_make_init():
    def create_init(dir: Path):
        if (init_file := dir.joinpath("__init__.py")).is_file():
            return
        init_file.touch()
        print(f"File created '{init_file!s}'")

    pycache_regex = re.compile(r"^.+__pycache__.+$")
    hidden_regex = re.compile(r"^.+\/\.\w+.+$")

    create_init(APP_PATH)

    for dir in APP_PATH.rglob("*"):
        if (
            any((regex.search(str(dir)) for regex in (pycache_regex, hidden_regex)))
            or dir.is_file()
        ):
            continue
        create_init(dir)


def run_pycache_remove():
    pycache_regex = re.compile(r"^.+__pycache__$")

    for pycache_dir in APP_PATH.rglob("__pycache__"):
        if pycache_dir.is_dir() and pycache_regex.search(str(pycache_dir)):
            os.system(f"rm -Rf {pycache_dir!s}")
            print(f"Folder removed {shlex.quote(str(pycache_dir))}")


def run_isort():
    cmd = [
        "isort",
        get_app_folder(),
    ]
    run_shell(" ".join(cmd))


def run_black():
    cmd = [
        "black",
        get_app_folder(),
    ]
    run_shell(" ".join(cmd))


def run_autoflake():
    cmd = [
        "autoflake",
        "--in-place",
        "--recursive",
        "--remove-all-unused-imports",
        "--ignore-init-module-imports",
        get_app_folder(),
    ]
    run_shell(" ".join(cmd))


def run_format():
    run_make_init()
    run_black()
    run_autoflake()
    run_isort()
