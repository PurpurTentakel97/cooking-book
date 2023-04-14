#
# Purpur Tentakel
# Cooking Book
# 12.04.2023
#

import sys

from helper import log
from validation import v_database as v_d
from helper import return_message as r_m
from database.my_database import Database

add: "Add"


class Add:
    def __init__(self, db: Database):
        self.db: Database = db

    # raw type
    def add_raw_type(self, new_type: str) -> r_m.ReturnMessage:
        new_type = new_type.strip()
        if not v_d.check_add_raw_type(new_type):
            return r_m.ReturnMessageStr("no valid argument to add raw type", False)

        sql_command: str = f"""INSERT INTO raw_types (type) VALUES (?);"""
        try:
            self.db.cursor.execute(sql_command, (new_type,))
            self.db.connection.commit()
            log.message(log.LogType.SAVED, "add.py", "add_raw_type()", f"new raw_type added -> {new_type}")
            return r_m.ReturnMessageInt(self.db.cursor.lastrowid, True)

        except self.db.OperationalError:
            log.error(log.LogType.ERROR, "add.py", "add_raw_type()", sys.exc_info())
            return r_m.ReturnMessageStr(f"not able to add new type -> {new_type}", False)

    # /raw type

    # recipe
    def add_recipe(self, title: str, description: str) -> r_m.ReturnMessage:
        title, description = title.strip(), description.strip()
        if not v_d.check_add_recipe(title, description):
            return r_m.ReturnMessageStr("no valid argument to add recipe", False)

        sql_command: str = f"""INSERT INTO recipes (title, description) VALUES (? ,?);"""
        try:
            self.db.cursor.execute(sql_command, (title, description))
            self.db.connection.commit()
            log.message(log.LogType.SAVED, "add.py", "self.add_recipe()", f"add new recipe -> {title}")
            return r_m.ReturnMessageInt(self.db.cursor.lastrowid, True)
        except self.db.OperationalError:
            log.error(log.LogType.ERROR, "add.py", "self.add_recipe()", sys.exc_info())
            return r_m.ReturnMessageStr(f"not able to add new recipe -> {title}", False)

    # /recipe

    # ingredients
    def add_ingredient(self, recipe_id: int, amount: float, unit: str, ingredient: str) -> r_m.ReturnMessage:
        unit, ingredient = unit.strip(), ingredient.strip()
        if not v_d.check_add_ingredient(recipe_id, amount, unit, ingredient):
            return r_m.ReturnMessageStr("no valid argument to add ingredient", False)

        sql_command: str = f"""INSERT INTO ingredients (recipe_id, amount, unit, ingredient) VALUES (?,?,?,?);"""
        try:
            self.db.cursor.execute(sql_command, (recipe_id, amount, unit, ingredient))
            self.db.connection.commit()
            log.message(log.LogType.SAVED, "add.py", "self.add_ingredient()", f"add new ingredient -> {ingredient}")
            return r_m.ReturnMessageInt(self.db.cursor.lastrowid, True)
        except self.db.OperationalError:
            log.error(log.LogType.ERROR, "add.py", "self.add_ingredient()", sys.exc_info())
            return r_m.ReturnMessageStr(f" not able to add new ingredient -> {ingredient}", False)

    # /ingredients


def create_add(db: Database):
    global add
    add = Add(db)
