#
# Purpur Tentakel
# Cooking Book
# 12.04.2023
#

import sys

from database.database import Database
from helper import return_message as r_m
from validation import v_database as v_d
from helper import log

delete: "Delete"


class Delete:
    def __init__(self, db: Database):
        self.db: Database = db

    # raw types
    def delete_raw_type_by_ID(self, ID: int) -> r_m.ReturnMessage:
        if not v_d.check_delete_raw_type_by_ID(ID):
            return r_m.ReturnMessageStr("no valid arguments to delete raw type", False)

        sql_command: str = f"""DELETE FROM raw_types WHERE ID is ?;"""
        try:
            self.db.cursor.execute(sql_command, (ID,))
            self.db.connection.commit()

            log.message(log.LogType.DELETED, "delete.py", "self.delete_raw_type_by_ID()",
                        f"deleted raw type with ID -> {ID}")
            return r_m.ReturnMessageNone(True)
        except self.db.OperationalError:
            log.error(log.LogType.ERROR, "delete.py", "self.delete_raw_type_by_ID()", sys.exc_info())
            return r_m.ReturnMessageStr(f"not able to delete raw type with ID -> {ID}", False)

    def delete_raw_type_by_name(self, value: str) -> r_m.ReturnMessage:
        value = value.strip()
        if not v_d.check_delete_raw_type_by_name(value):
            return r_m.ReturnMessageStr("no valid arguments for deleting raw type", False)

        sql_command: str = f"""DELETE FROM raw_types WHERE type is ?;"""
        try:
            self.db.cursor.execute(sql_command, (value,))
            self.db.connection.commit()

            log.message(log.LogType.DELETED, "delete.py", "self.delete_raw_type_by_name()",
                        f"deleted raw type with name -> {value}")
            return r_m.ReturnMessageNone(True)
        except self.db.OperationalError:
            log.error(log.LogType.ERROR, "delete.py", "self.delete_raw_type_by_name()", sys.exc_info())
            return r_m.ReturnMessageStr(f"not able to delete raw type with name -> {value}", False)

    # /raw types

    # recipes
    def delete_recipe_by_ID(self, ID: int) -> r_m.ReturnMessage:
        if not v_d.check_delete_recipe_by_ID(ID):
            return r_m.ReturnMessageStr("no valid arguments for deleting recipe", False)

        sql_command: str = f"""DELETE FROM recipes WHERE ID is ?;"""
        try:
            self.db.cursor.execute(sql_command, (ID,))
            self.db.connection.commit()

            log.message(log.LogType.DELETED, "delete.py", "self.delete_recipe_by_ID()",
                        f"deleted recipe with ID -> {ID}")
            return r_m.ReturnMessageNone(True)
        except self.db.OperationalError:
            log.error(log.LogType.ERROR, "delete.py", "self.delete_recipe_by_ID()", sys.exc_info())
            return r_m.ReturnMessageStr(f"not able to delete recipe with ID -> {ID}", False)

    def delete_recipe_by_title(self, title: str) -> r_m.ReturnMessage:
        if not v_d.check_delete_recipe_by_title(title):
            return r_m.ReturnMessageStr("no valid arguments fpr deleting recipe", False)

        sql_command: str = f"""DELETE FROM recipes WHERE title is ?;"""
        try:
            self.db.cursor.execute(sql_command, (title,))
            self.db.connection.commit()

            log.message(log.LogType.DELETED, "delete.py", "self.delete_recipe_by_title()",
                        f"deleted recipe with title -> {title}")
            return r_m.ReturnMessageNone(True)
        except self.db.OperationalError:
            log.error(log.LogType.ERROR, "delete.py", "self.delete_recipe_by_title()", sys.exc_info())
            return r_m.ReturnMessageStr(f"not able to delete recipe with title -> {title}", False)

    # /recipes

    # ingredients
    def delete_ingredient_by_ID(self, ID: int) -> r_m.ReturnMessage:
        if not v_d.check_delete_ingredient_by_ID(ID):
            return r_m.ReturnMessageStr("no valid arguments for deleting ingredient", False)

        sql_command: str = f"""DELETE FROM ingredients WHERE ID is ?;"""
        try:
            self.db.cursor.execute(sql_command, (ID,))
            self.db.connection.commit()

            log.message(log.LogType.DELETED, "delete.py", "self.delete_ingredient_by_ID()",
                        f"deleted ingredient with ID -> {ID}")
            return r_m.ReturnMessageNone(True)
        except self.db.OperationalError:
            log.error(log.LogType.ERROR, "delete.py", "self.delete_ingredient_by_ID()", sys.exc_info())
            return r_m.ReturnMessageStr(f"not able to delete ingredient with ID -> {ID}", False)

    def delete_ingredients_by_recipe_ID(self, recipe_ID: int) -> r_m.ReturnMessage:
        if not v_d.check_delete_ingredients_by_recipe_ID(recipe_ID):
            return r_m.ReturnMessageStr("no valid arguments for deleting ingredients by recipe ID", False)

        sql_command: str = f"""DELETE FROM ingredients WHERE recipe_ID is ?;"""
        try:
            self.db.cursor.execute(sql_command, (recipe_ID,))
            self.db.connection.commit()

            log.message(log.LogType.DELETED, "delete.py", "self.delete_ingredients_by_recipe_ID()",
                        f"deleted all ingredients with recipe ID -> {recipe_ID}")
            return r_m.ReturnMessageNone(True)
        except self.db.OperationalError:
            log.error(log.LogType.ERROR, "delete.py", "self.delete_ingredients_by_recipe_ID()", sys.exc_info())
            return r_m.ReturnMessageStr(f"not able to delete all ingredients with recipe ID -> {recipe_ID}", False)

    # /ingredients


def create_delete(db: Database):
    global delete
    delete = Delete(db)
