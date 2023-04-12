#
# Purpur Tentakel
# Cocking Book
# 12.04.2023
#

import sys

from helper import log
from database import database as d
from helper import return_message as r_m


# raw types
def select_all_raw_types() -> r_m.ReturnMessage:
    sql_command: str = f"""SELECT type FROM raw_types ORDER BY name ASC;"""
    try:
        result: tuple = d.cursor.execute(sql_command).fetchall()
        log.message(log.LogType.LOADED, "select.py", "select_all_raw_types()", f"selected All -> {result}")
        return r_m.ReturnMessageTuple(result, True)
    except d.OperationalError:
        log.message(log.LogType.ERROR, "select.py", "select_raw_type_by_ID()", sys.exc_info())
        return r_m.ReturnMessageStr(f"could not load all raw types.", False)


def select_raw_type_by_ID(ID: int) -> r_m.ReturnMessage:
    sql_command: str = f"""SELECT type FROM raw_types WHERE ID = ?;"""
    try:
        result: str = d.cursor.execute(sql_command, ID).fetchone()
        log.message(log.LogType.LOADED, "select.py", "select_raw_type_by_ID()", f"selected ID {ID} -> {result}")
        return r_m.ReturnMessageStr(result, True)
    except d.OperationalError:
        log.message(log.LogType.ERROR, "select.py", "select_raw_type_by_ID()", sys.exc_info())
        return r_m.ReturnMessageStr(f"could not load raw type with ID {ID}", False)


def select_raw_type_by_name(name: str) -> r_m.ReturnMessage:
    sql_command: str = f"""SELECT type FROM raw_types WHERE name = ?;"""
    try:
        result: str = d.cursor.execute(sql_command, name).fetchone()
        log.message(log.LogType.LOADED, "select.py", "select_raw_type_by_ID()", f"selected name {name} -> {result}")
        return r_m.ReturnMessageStr(result, True)
    except d.OperationalError:
        log.message(log.LogType.ERROR, "select.py", "select_raw_type_by_ID()", sys.exc_info())
        return r_m.ReturnMessageStr(f"could not load raw type with ID {name}", False)
