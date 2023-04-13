#
# Purpur Tentakel
# Cocking Book
# 12.04.2023
#

from helper import log
from database import select as s
from helper import return_message as r_m


# raw type
# select
def select_raw_type_by_ID(ID: int) -> bool:
    if type(ID) != int:
        log.message(log.LogType.INVALID_ARGUMENT, "v_database.py", "select_raw_type_by_ID()",
                    f"provided id is no int -> {ID}")
        return False

    result: r_m.ReturnMessage = s.select.select_all_raw_types()
    if not result.valid:
        log.message(log.LogType.INFO, "v_database.py", "select_raw_type_by_ID()", "ResultMassage not valid")
        return False

    for id, _ in result.entry:
        if id == ID:
            return True

    log.message(log.LogType.INFO, "v_database.py", "select_raw_type_by_ID()", f"raw type ID not existing -> {ID}")
    return False


def select_raw_type_ID_by_name(value: str) -> bool:
    if type(value) != str:
        log.message(log.LogType.INFO, "v_database.py", "select_raw_type_ID_by_name()",
                    f"provided value is no string -> {value}")
        return False

    result: r_m.ReturnMessage = s.select.select_all_raw_types()
    if not result.valid:
        log.message(log.LogType.INFO, "v_database.py", "select_raw_type_by_name()", "ReturnMessage not valid")
        return False

    for _, name in result.entry:
        if name == value:
            return True

    log.message(log.LogType.INFO, "v_database.py", "select_raw_type_by_name()",
                f"raw type name not existing -> {value}")
    return False


# /select


# add
def add_raw_type(value: str) -> bool:
    if type(value) != str:
        log.message(log.LogType.INFO, "v_database.py", "add_raw_type()",
                    f"provided value is no string -> {value}")
        return False

    result: r_m.ReturnMessage = s.select.select_all_raw_types()
    if not result.valid:
        log.message(log.LogType.INFO, "v_database.py", "add_raw_type()", "ResultMassage not valid")
        return False

    for _, raw_type in result.entry:
        if value == raw_type:
            log.message(log.LogType.INFO, "v_database.py", "add_raw_type()",
                        f"raw type is already existing -> {raw_type}")
            return False

    return True


# /add


# update
def update_raw_type_by_ID(ID: int, value: str) -> bool:
    if type(value) != str:
        log.message(log.LogType.INFO, "v_database.py", "update_raw_type_by_ID()",
                    f"provided value is no string -> {value}")
        return False
    if type(ID) != int:
        log.message(log.LogType.INFO, "v_database.py", "update_raw_type_by_ID()",
                    f"provided ID is no int -> {ID}")
        return False

    result: r_m.ReturnMessage = s.select.select_all_raw_types()
    if not result.valid:
        log.message(log.LogType.INFO, "v_database.py", "update_raw_type_by_ID()", "ResultMassage not valid")
        return False

    for _, raw_type in result.entry:
        if value == raw_type:
            log.message(log.LogType.INFO, "v_database.py", "update_raw_type_by_ID()",
                        f"raw type is already existing -> {value}")
            return False

    for raw_id, _ in result.entry:
        if raw_id == ID:
            return True

    log.message(log.LogType.INFO, "v_database.py", "update_raw_type_by_ID()",
                f"update raw type ID not found -> {ID}")
    return False


def update_raw_type_by_name(old_type: str, new_type: str) -> bool:
    if type(old_type) != str:
        log.message(log.LogType.INFO, "v_database.py", "update_raw_type_by_name()",
                    f"provided value is no string -> {old_type}")
    if type(new_type) != str:
        log.message(log.LogType.INFO, "v_database.py", "update_raw_type_by_name()",
                    f"provided value is no string -> {new_type}")

    result: r_m.ReturnMessage = s.select.select_all_raw_types()
    if not result.valid:
        log.message(log.LogType.INFO, "v_database.py", "update_raw_type_by_type()", "ResultMassage not valid")
        return False

    for _, raw_type in result.entry:
        if new_type == raw_type:
            log.message(log.LogType.INFO, "v_database.py", "update_raw_type_by_name()",
                        f"raw type is already existing -> {new_type}")
            return False

    for _, raw_type in result.entry:
        if raw_type == old_type:
            return True

    log.message(log.LogType.INFO, "v_database.py", "update_raw_type_by_name()",
                f"update old raw type not found -> {old_type}")
    return False


# /update


# delete
def delete_raw_type_by_ID(ID: int) -> bool:
    if type(ID) != int:
        log.message(log.LogType.INFO, "v_database.py", "delete_raw_type_by_ID()",
                    f"provided ID is no int -> {ID}")
        return False

    result: r_m.ReturnMessage = s.select.select_all_raw_types()
    if not result.valid:
        log.message(log.LogType.INFO, "v_database.py", "delete_raw_type_by_ID()", "ResultMassage not valid")
        return False

    for old_ID, _ in result.entry:
        if old_ID == ID:
            return True

    log.message(log.LogType.INFO, "v_database.py", "delete_raw_type_by_ID()",
                f"not entry ID found to delete -> {ID}")
    return False


def delete_raw_type_by_name(value: str) -> bool:
    if type(value) != str:
        log.message(log.LogType.INFO, "v_database.py", "delete_raw_type_by_name()",
                    f"provided value is no string -> {value}")

    result: r_m.ReturnMessage = s.select.select_all_raw_types()
    if not result.valid:
        log.message(log.LogType.INFO, "v_database.py", "delete_raw_type_by_ID()", "ResultMassage not valid")
        return False

    for _, old_value in result.entry:
        if old_value == value:
            return True

    log.message(log.LogType.INFO, "v_database.py", "delete_raw_type_by_ID()",
                f"not entry value found to delete -> {value}")
    return False
# /delete
# /raw types
