#
# Purpur Tentakel
# Cocking Book
# 12.04.2023
#

from helper import log
from database import select
from helper import return_message as r_m


# raw type
def add_raw_type(name: str) -> bool:
    result: r_m.ReturnMessage = select.select.select_all_raw_types()
    if not result.valid:
        log.message(log.LogType.INFO, "v_database.py", "add_raw_type()", "ResultMassage not valid")

    for _, raw_type in result.entry:
        if name == raw_type:
            log.message(log.LogType.INFO, "v_database.py", "add_raw_type()",
                        f"raw type is already existing -> {raw_type}")
            return False

    return True
