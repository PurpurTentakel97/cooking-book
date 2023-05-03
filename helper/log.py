#
# Purpur Tentakel
# Cooking Book
# 12.04.2023
#

import os.path
from enum import Enum
from datetime import datetime

from helper import dirs
import json


# @formatter:off
class LogType(Enum):
    DEBUG =            "DEBUG             "
    INFO =             "INFO              "

    SAVED =            "SAVED             "
    LOADED =           "LOADED            "
    UPDATED =          "UPDATED           "
    DELETED =          "DELETED           "
    GENERATED =        "GENERATED         "
    INITIALIZED =      "INITIALIZED       "

    INVALID_ARGUMENT = "INVALID ARGUMENT  "

    BREAKING_ERROR =   "[[ERROR BREAKING]]"
    ERROR =            "[ERROR]           "
    EXPECTED_ERROR =   "ERROR EXPECTED    "
# @formatter:on


class _Log:
    def __init__(self, log_type: LogType, file: str, function: str, text: str):
        self.timestamp: datetime = datetime.now()
        self.log_type: LogType = log_type
        self.file: str = file
        self.function: str = function
        self.text: str = text

    def __str__(self):
        return f"[{self.date_as_string()}] | {self.log_type.value} | {self.file}.{self.function} | {self.text}"

    def date_as_string(self):
        return self.timestamp.strftime("%d-%m-%Y %H:%M:%S")

    def as_dict(self) -> dict[str, str]:
        return {
            "date": self.date_as_string(),
            "log type": self.log_type.value.strip(),
            "file": self.file,
            "function": self.function,
            "text": self.text
        }


_logs: list[_Log, ...] = list()
_log_file_name: str = ""
_is_exporting: bool = True


def _create_log_file() -> None:
    global _is_exporting
    if not _is_exporting:
        return

    dirs.check_and_make_dir(dirs.DirType.LOGS)

    global _log_file_name
    if os.path.exists(_log_file_name):
        return

    log_dir_name: str = dirs.get_dir_from_file(dirs.FileType.LOG_ENDING)
    _log_file_name = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    _log_file_name = f"{log_dir_name}/{_log_file_name}{dirs.FileType.LOG_ENDING.value}"

    with open(_log_file_name, "w") as _:
        var = None
        message(LogType.GENERATED, "log.py", "_create_log_file()", f"generated file '{_log_file_name}'")


def message(log_type: LogType, file: str, function: str, text: str) -> None:
    log: _Log = _Log(log_type, file, function, text.strip())

    print(log)
    _logs.append(log)
    export()


def error(log_type: LogType, file: str, function: str, error_tuple: tuple) -> None:
    error_str: str = f"{error_tuple[0]} | {error_tuple[1]} | {error_tuple[2]}"
    message(log_type, file, function, error_str)


def export(printing: bool = False) -> None:
    global _is_exporting
    if not _is_exporting:
        return

    out: list[dict[str, str]] = list()
    global _log_file_name
    if len(_log_file_name) == 0:
        _create_log_file()

    for log in _logs:
        log: _Log

        out.append(log.as_dict())

    out: str = json.dumps(out, indent=4)

    if os.path.exists(_log_file_name):
        with open(_log_file_name, "w") as file:
            file.write(out)

    if printing:
        print(out)


def _set_exporting(is_exporting:bool):
    global _is_exporting
    _is_exporting = is_exporting