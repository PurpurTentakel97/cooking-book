#
# Purpur Tentakel
# Cocking Book
# 12.04.2023
#

from helper import log
from database import select
from helper import return_message as r_m


def add_raw_type(name: str) -> bool:
    result: r_m.ReturnMessage = select.select_all_raw_types()
    if not type(result.entry) == tuple():
        log.message(log.LogType.INVALID_ARGUMENT, "v_database.py", "add_raw_type()",
                    "invalid datatype. should be tuple.")
        return False

    if name in result.entry:
        log.message(log.LogType.INFO, "v_database.py", "add_raw_type()", "raw type is already existing.")
        return False

    return True
