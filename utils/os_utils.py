import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)


def create_results_dir(dir_name: str) -> str:
    if not Path(dir_name).exists():
        Path(dir_name).mkdir(parents=True)
    return dir_name


def create_python_files(files_dir: str, filenames: list) -> list:
    for filename in filenames:
        with open(files_dir + "/" + filename + ".py", "w"):
            pass

    return filenames
