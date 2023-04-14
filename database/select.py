#
# Purpur Tentakel
# Cooking Book
# 12.04.2023
#

import sys

from helper import log
from helper import return_message as r_m
from validation import v_database as v_d
from database.my_database import Database

select: "Select"


class Select:
    def __init__(self, db: Database):
        self.db: Database = db

    # raw types
    def select_all_raw_types(self) -> r_m.ReturnMessage:
        sql_command: str = f"""SELECT ID,type FROM raw_types ORDER BY type ASC;"""
        try:
            result: tuple = self.db.cursor.execute(sql_command).fetchall()
            log.message(log.LogType.LOADED, "select.py", "select_all_raw_types()", f"selected All -> {result}")
            return r_m.ReturnMessageTuple(result, True)
        except self.db.OperationalError:
            log.error(log.LogType.ERROR, "select.py", "select_all_raw_types()", sys.exc_info())
            return r_m.ReturnMessageStr(f"could not load all raw types.", False)

    def select_raw_type_by_ID(self, ID: int) -> r_m.ReturnMessage:
        if not v_d.check_select_raw_type_by_ID(ID):
            return r_m.ReturnMessageStr("no valid arguments for select raw type", False)

        sql_command: str = f"""SELECT type FROM raw_types WHERE ID = ?;"""
        try:
            result: str = self.db.cursor.execute(sql_command, (ID,)).fetchone()[0]
            log.message(log.LogType.LOADED, "select.py", "select_raw_type_by_ID()", f"selected ID {ID} -> {result}")
            return r_m.ReturnMessageStr(result, True)
        except self.db.OperationalError:
            log.error(log.LogType.ERROR, "select.py", "select_raw_type_by_ID()", sys.exc_info())
            return r_m.ReturnMessageStr(f"could not load raw type with ID {ID}", False)

    def select_raw_type_ID_by_name(self, value: str) -> r_m.ReturnMessage:
        value = value.strip()
        if not v_d.check_select_raw_type_ID_by_name(value):
            return r_m.ReturnMessageStr("no valid arguments for select raw type", False)

        sql_command: str = f"""SELECT ID FROM raw_types WHERE type = ?;"""
        try:
            result: int = self.db.cursor.execute(sql_command, (value,)).fetchone()[0]
            log.message(log.LogType.LOADED, "select.py", "select_raw_type_by_name()",
                        f"selected name {value} -> {result}")
            return r_m.ReturnMessageInt(result, True)
        except self.db.OperationalError:
            log.error(log.LogType.ERROR, "select.py", "select_raw_type_by_name()", sys.exc_info())
            return r_m.ReturnMessageStr(f"could not load raw type with ID {value}", False)

    # /raw type
    # recipe
    def select_all_recipes(self) -> r_m.ReturnMessage:
        sql_command: str = f"""SELECT ID, title, description FROM recipes ORDER BY title ASC;"""
        try:
            result: tuple = self.db.cursor.execute(sql_command).fetchall()
            log.message(log.LogType.LOADED, "select.py", "self.select_all_recipes()",
                        f"selected All recipes-> {result}")
            return r_m.ReturnMessageTuple(result, True)
        except self.db.OperationalError:
            log.error(log.LogType.ERROR, "select.py", "self.select_all_recipes()", sys.exc_info())
            return r_m.ReturnMessageStr("could not load all recipes", False)

    def select_recipe_by_ID(self, ID: int) -> r_m.ReturnMessage:
        if not v_d.check_select_recipe_by_ID(ID):
            return r_m.ReturnMessageStr("no valid arguments for selecting recipe", False)

        sql_command: str = f"""SELECT ID,title,description FROM recipes WHERE ID IS ?;"""
        try:
            result: tuple = self.db.cursor.execute(sql_command, (ID,)).fetchone()
            log.message(log.LogType.LOADED, "select.py", "self.select_recipe_by_ID()",
                        f"selected recipe by ID -> {result}")
            return r_m.ReturnMessageTuple(result, True)
        except self.db.OperationalError:
            log.error(log.LogType.ERROR, "select.py", "select.select_recipe_by_ID()", sys.exc_info())
            return r_m.ReturnMessageStr(f"not able to load recipe with ID -> {ID}", False)

    def select_recipe_by_title(self, title: str) -> r_m.ReturnMessage:
        if not v_d.check_select_recipe_by_title(title):
            return r_m.ReturnMessageStr("no valid arguments for select recipe", False)

        sql_command: str = f"""SELECT ID,title,description FROM recipes WHERE title IS ?;"""
        try:
            result: tuple = self.db.cursor.execute(sql_command, (title,)).fetchone()
            log.message(log.LogType.LOADED, "select.py", "self.select_recipe_by_title()",
                        f"selected recipe by name -> {result}")
            return r_m.ReturnMessageTuple(result, True)
        except self.db.OperationalError:
            log.error(log.LogType.ERROR, "select.py", "select.select_recipe_by_title()", sys.exc_info())
            return r_m.ReturnMessageStr(f"not able to load recipe with title -> {title}", False)

    # /recipe

    # ingredients
    def select_all_ingredients(self) -> r_m.ReturnMessage:
        sql_command: str = f"""SELECT ID, recipe_id, amount, unit, ingredient FROM ingredients ORDER BY ingredient ASC;"""
        try:
            result = self.db.cursor.execute(sql_command).fetchall()
            log.message(log.LogType.LOADED, "select.py", "self.select_all_ingredients()",
                        f"selected all ingredients -> {result}")
            return r_m.ReturnMessageList(result, True)
        except self.db.OperationalError:
            log.error(log.LogType.ERROR, "select.py", "self.select_all_ingredients()", sys.exc_info())
            return r_m.ReturnMessageStr("could not load all ingredients", False)

    def select_all_ingredients_from_recipe(self, recipe_ID: int) -> r_m.ReturnMessage:
        if not v_d.check_select_all_ingredients_from_recipe(recipe_ID):
            return r_m.ReturnMessageStr("no valid arguments for selecting ingredients", False)

        sql_command: str = f"""SELECT ID, recipe_id, amount, unit, ingredient FROM ingredients WHERE recipe_id is ? ORDER BY ingredient ASC;"""
        try:
            result = self.db.cursor.execute(sql_command, (recipe_ID,)).fetchall()
            log.message(log.LogType.LOADED, "select.py", "self.select_all_ingredients_from_recipe()",
                        f"selected all ingredients from recipe -> {result}")
            return r_m.ReturnMessageList(result, True)
        except self.db.OperationalError:
            log.error(log.LogType.ERROR, "select.py", "self.select_all_ingredients_from_recipe()", sys.exc_info())
            return r_m.ReturnMessageStr(f"could not load all ingredients from recipe ID ->{recipe_ID}")

    def select_ingredient_by_ID(self, ID: int) -> r_m.ReturnMessage:
        if not v_d.check_select_ingredient_by_ID(ID):
            return r_m.ReturnMessageStr("no valid argument for selecting ingredient", False)

        sql_command: str = f"""SELECT ID, recipe_id, amount, unit, ingredient FROM ingredients WHERE ID is ?;"""
        try:
            result = self.db.cursor.execute(sql_command, (ID,)).fetchone()
            log.message(log.LogType.LOADED, "select.py", "self.select_ingredient_by_ID()",
                        f"selected ingredient -> {result}")
            return r_m.ReturnMessageTuple(result, True)
        except self.db.OperationalError:
            log.error(log.LogType.ERROR, "select.py", "self.select_ingredient_by_ID()", sys.exc_info())
            return r_m.ReturnMessageStr(f"could not load ingredient from ID ->{ID}")

    # /ingredients


def create_select(db: Database):
    global select
    select = Select(db)
