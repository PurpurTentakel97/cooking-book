#
# Purpur Tentakel
# Cocking Book
# 12.04.2023
#

from helper import log
from database import select
from helper import return_message as r_m


# raw type
def add_raw_type(value: str) -> bool:
    result: r_m.ReturnMessage = select.select.select_all_raw_types()
    if not result.valid:
        log.message(log.LogType.INFO, "v_database.py", "add_raw_type()", "ResultMassage not valid")
        return False

    for _, raw_type in result.entry:
        if value == raw_type:
            log.message(log.LogType.INFO, "v_database.py", "add_raw_type()",
                        f"raw type is already existing -> {raw_type}")
            return False

    return True


def update_raw_type_by_ID(ID: int, value: str) -> bool:
    result: r_m.ReturnMessage = select.select.select_all_raw_types()
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
    result: r_m.ReturnMessage = select.select.select_all_raw_types()
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
