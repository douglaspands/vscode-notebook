import os


def makerequirements():
    os.system(
        "poetry export -f requirements.txt --without-hashes --output requirements.txt"
    )
