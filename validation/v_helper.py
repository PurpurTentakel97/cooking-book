#
# Purpur Tentakel
# Cocking Book
# 12.04.2023
#

from helper import log
from helper import return_message as r_h


def is_valid_ID(ID: int) -> bool:
    if type(ID) != int:
        log.message(log.LogType.INVALID_ARGUMENT, "v_helper.py", "is_valid_ID()", f"provided ID is no int -> {ID}")
        return False

    if ID <= 0:
        log.message(log.LogType.INVALID_ARGUMENT, "v_helper.py", "is_valid_ID()",
                    f"provided ID is lower than 0 or 0 -> {ID}")
        return False

    return True


def is_valid_positive_float(value: float) -> bool:
    if type(value) != float:
        log.message(log.LogType.INVALID_ARGUMENT, "v_helper.py", "is_valid_float()",
                    f"provided number is no float -> {value}")
        return False

    if value <= 0.0:
        log.message(log.LogType.INVALID_ARGUMENT, "v_helper.py", "is_valid_positive_float()",
                    f"provided number is lover that 0.0f -> {value}")
        return False

    return True


def is_valid_string(value: str) -> bool:
    if not is_valid_empty_string(value):
        return False

    if len(value.strip()) == 0:
        log.message(log.LogType.INVALID_ARGUMENT, "v_helper.py", "is_valid_string()",
                    f"provided value is empty -> {value}")
        return False

    return True


def is_valid_empty_string(value: str) -> bool:
    if type(value) != str:
        log.message(log.LogType.INVALID_ARGUMENT, "v_helper.py", "is_valid_string()",
                    f"provided value is no string -> {value}")
        return False

    return True


def is_valid_Return_Message(message: r_h.ReturnMessage) -> bool:
    if not message.valid:
        log.message(log.LogType.INFO, "v_helper.py", "is_valid_Return_Message()",
                    "ReturnMassage not valid")
        return False

    return True
