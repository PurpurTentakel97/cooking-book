#
# Purpur Tentakel
# Cocking Book
# 12.04.2023
#

from enum import Enum
from datetime import datetime


# @formatter:off
class LogType(Enum):
    DEBUG =          "DEBUG             ",
    INFO =           "INFO              ",

    SAVED =          "SAVED             ",
    LOADED =         "LOADED            ",

    BREAKING_ERROR = "[[ERROR BREAKING]]",
    ERROR =          "[ERROR]           ",
    EXPECTED_ERROR = "ERROR EXPECTED    ",
# @formatter:on

class _Log:
    def __init__(self, log_type: LogType, file: str, function: str, text: str):
        self.log_type: LogType = log_type
        self.file: str = file
        self.function: str = function
        self.text: str = text
        self.timestamp: datetime = datetime.now()

    def __str__(self):
        date: str = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        return f"[{date}] | {self.log_type.value[0]} | {self.file}.{self.function} | {self.text}"


_logs: list[_Log, ...] = list()


def message(log_type: LogType, file: str, function: str, text: str) -> None:
    log: _Log = _Log(log_type, file, function, text)
    _logs.append(log)
    print(log)


def export() -> None:  # @todo actually export the log
    for log in _logs:
        log: _Log
        print(log)
