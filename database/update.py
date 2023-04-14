#
# Purpur Tentakel
# Cooking Book
# 12.04.2023
#

import sys

from helper import log
from database.database import Database
from helper import return_message as r_m
from validation import v_database as v_d

update: "Update"


class Update:
    def __init__(self, db: Database):
        self.db: Database = db

    # raw types
    def update_raw_type_by_ID(self, ID: int, value: str) -> r_m.ReturnMessage:
        value = value.strip()
        if not v_d.update_raw_type_by_ID(ID, value):
            return r_m.ReturnMessageStr("no valid arguments for updating raw type", False)

        sql_command: str = f"""UPDATE raw_types SET type = ? WHERE ID is ?;"""
        try:
            self.db.cursor.execute(sql_command, (value, ID))
            self.db.connection.commit()

            log.message(log.LogType.UPDATED, "update.py", "self.update_raw_type_by_ID()",
                        f"updated raw type -> {value}")
            return r_m.ReturnMessageNone(True)

        except self.db.OperationalError:
            log.error(log.LogType.ERROR, "update.py", "self.update_raw_type_by_ID()", sys.exc_info())
            return r_m.ReturnMessageStr(f"not able to update raw type -> {value}", False)

    def update_raw_type_by_name(self, old_value: str, new_value: str) -> r_m.ReturnMessage:
        old_value, new_value = old_value.strip(), new_value.strip()
        if not v_d.update_raw_type_by_name(old_value, new_value):
            return r_m.ReturnMessageStr("no valid arguments for updating raw type", False)

        sql_command: str = f"""UPDATE raw_types SET type = ? WHERE type is ?;"""
        try:
            self.db.cursor.execute(sql_command, (new_value, old_value))
            self.db.connection.commit()

            log.message(log.LogType.UPDATED, "update.py", "self.update_raw_type_by_name()",
                        f"updated raw type -> {new_value}")
            return r_m.ReturnMessageNone(True)
        except self.db.OperationalError:
            log.error(log.LogType.ERROR, "update.py", "self.update_raw_type_by_name()", sys.exc_info())
            return r_m.ReturnMessageStr(f"not able to update raw type -> {new_value}", False)

    # /raw types

    # recipes
    def update_recipe_by_ID(self, ID: int, title: str, description: str) -> r_m.ReturnMessage:
        title, description = title.strip(), description.strip()
        if not v_d.update_recipe_by_ID(ID, title, description):
            return r_m.ReturnMessageStr("no valid argument for updating recipe", False)

        sql_command: str = f"""UPDATE recipes SET title = ?, description = ? WHERE ID is ?;"""
        try:
            self.db.cursor.execute(sql_command, (title, description, ID))
            self.db.connection.commit()

            log.message(log.LogType.UPDATED, "update.py", "self.update_recipe_by_ID()", f"updated recipy -> {title}")
            return r_m.ReturnMessageNone(True)
        except self.db.OperationalError:
            log.error(log.LogType.ERROR, "update.py", "self.update_recipe_by_ID()", sys.exc_info())
            return r_m.ReturnMessageStr(f"not able to update recipe -> {title}", False)

    def update_recipe_by_title(self, old_title: str, new_title: str, description: str) -> r_m.ReturnMessage:
        old_title, new_title, description = old_title.strip(), new_title.strip(), description.strip()
        if not v_d.update_recipe_by_title(old_title, new_title, description):
            return r_m.ReturnMessageStr("no valid argument for updating recipe", False)

        sql_command: str = f"""UPDATE recipes SET title = ?, description = ? WHERE title is ?;"""
        try:
            self.db.cursor.execute(sql_command, (new_title, description, old_title))
            self.db.connection.commit()

            log.message(log.LogType.UPDATED, "update.py", "self.update_recipe_by_title()",
                        f"updated recipy -> {new_title}")
            return r_m.ReturnMessageNone(True)
        except self.db.OperationalError:
            log.error(log.LogType.ERROR, "update.py", "self.update_recipe_by_title()", sys.exc_info())
            return r_m.ReturnMessageStr(f"not able to update recipe -> {old_title}", False)

    # /recipes

    # ingredients
    def update_ingredient_by_ID(self, ID: int, amount: float, unit: str, ingredient: str) -> r_m.ReturnMessage:
        unit, ingredient = unit.strip(), ingredient.strip()
        if not v_d.update_ingredient_by_ID(ID, amount, unit, ingredient):
            return r_m.ReturnMessageStr("no valid argument for updating recipe", False)

        sql_command: str = f"""UPDATE ingredients SET amount = ?, unit = ?, ingredient = ? WHERE ID is ?;"""
        try:
            self.db.cursor.execute(sql_command, (amount, unit, ingredient, ID))
            self.db.connection.commit()

            log.message(log.LogType.UPDATED, "update.py", "self.update_by_ID()",
                        f"updated ingredient -> {ingredient}")
            return r_m.ReturnMessageNone(True)
        except self.db.OperationalError:
            log.error(log.LogType.ERROR, "update.py", "self.update_by_ID()", sys.exc_info())
            return r_m.ReturnMessageStr(f"not able to update ingredient -> {ingredient}", False)

    # /ingredients


def create_update(db: Database):
    global update
    update = Update(db)
