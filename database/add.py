#
# Purpur Tentakel
# Cocking Book
# 12.04.2023
#

import sys

from helper import log
from database.database import Database
from validation import v_database as v_d
from helper import return_message as r_m

add: "Add"


class Add:
    def __init__(self, db: Database):
        self.db: Database = db

    def add_raw_type(self, new_type: str) -> r_m.ReturnMessage:
        if not v_d.add_raw_type(new_type):
            return r_m.ReturnMessageStr("no valid argument", False)

        sql_command: str = f"""INSERT INTO raw_types (type) VALUES (?);"""
        try:
            self.db.cursor.execute(sql_command, (new_type,))
            self.db.connection.commit()
            log.message(log.LogType.SAVED, "add.py", "add_raw_type()", f"new raw_type added -> {new_type}")
            return r_m.ReturnMessageNone(True)

        except self.db.OperationalError:
            log.error(log.LogType.ERROR, "add.py", "add_raw_type()", sys.exc_info())
            return r_m.ReturnMessageStr("not able to add new type", False)


def create_add(db: Database):
    global add
    add = Add(db)
