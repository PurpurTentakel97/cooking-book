#
# Purpur Tentakel
# Cocking Book
# 12.04.2023
#

from helper import log


def is_valid_ID(ID: int) -> bool:
    if type(ID) != int:
        log.message(log.LogType.INVALID_ARGUMENT, "v_helper.py", "is_valid_ID()", f"provided ID is no int -> {ID}")
        return False

    if ID <= 0:
        log.message(log.LogType.INVALID_ARGUMENT, "v_helper.py", "is_valid_ID()",
                    f"provided ID is lower than 0 or 0 -> {ID}")
        return False

    return True


def is_valid_string(value: str) -> bool:
    if type(value) != str:
        log.message(log.LogType.INVALID_ARGUMENT, "v_helper.py", "is_valid_string()",
                    f"provided value is no string -> {value}")
        return False

    if len(value.strip()) == 0:
        log.message(log.LogType.INVALID_ARGUMENT, "v_helper.py", "is_valid_string()",
                    f"provided value is empty -> {value}")
        return False

    return True
