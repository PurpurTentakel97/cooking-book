#
# Purpur Tentakel
# Cocking Book
# 12.04.2023
#

from helper import log
from database import select as s
from helper import return_message as r_m
from validation import v_helper as v_h


# raw type
# select
def check_select_raw_type_by_ID(ID: int) -> bool:
    if not v_h.is_valid_ID(ID):
        return False

    result: r_m.ReturnMessage = s.select.select_all_raw_types()
    if not result.valid:
        log.message(log.LogType.INFO, "v_database.py", "select_raw_type_by_ID()", "ResultMassage not valid")
        return False

    for id, _ in result.entry:
        if id == ID:
            return True

    log.message(log.LogType.INVALID_ARGUMENT, "v_database.py", "select_raw_type_by_ID()",
                f"raw type ID not existing -> {ID}")
    return False


def check_select_raw_type_ID_by_name(value: str) -> bool:
    if not v_h.is_valid_string(value):
        return False

    result: r_m.ReturnMessage = s.select.select_all_raw_types()
    if not result.valid:
        log.message(log.LogType.INFO, "v_database.py", "select_raw_type_by_name()", "ReturnMessage not valid")
        return False

    for _, name in result.entry:
        if name == value:
            return True

    log.message(log.LogType.INVALID_ARGUMENT, "v_database.py", "select_raw_type_by_name()",
                f"raw type name not existing -> {value}")
    return False


# /select


# add
def check_add_raw_type(value: str) -> bool:
    if not v_h.is_valid_string(value):
        return False

    result: r_m.ReturnMessage = s.select.select_all_raw_types()
    if not result.valid:
        log.message(log.LogType.INFO, "v_database.py", "add_raw_type()", "ResultMassage not valid")
        return False

    for _, raw_type in result.entry:
        if value == raw_type:
            log.message(log.LogType.INVALID_ARGUMENT, "v_database.py", "add_raw_type()",
                        f"raw type is already existing -> {raw_type}")
            return False

    return True


# /add


# update
def check_update_raw_type_by_ID(ID: int, value: str) -> bool:
    if not v_h.is_valid_string(value):
        return False

    if not v_h.is_valid_ID(ID):
        return False

    result: r_m.ReturnMessage = s.select.select_all_raw_types()
    if not result.valid:
        log.message(log.LogType.INVALID_ARGUMENT, "v_database.py", "update_raw_type_by_ID()", "ResultMassage not valid")
        return False

    for _, raw_type in result.entry:
        if value == raw_type:
            log.message(log.LogType.INVALID_ARGUMENT, "v_database.py", "update_raw_type_by_ID()",
                        f"raw type is already existing -> {value}")
            return False

    for raw_id, _ in result.entry:
        if raw_id == ID:
            return True

    log.message(log.LogType.INFO, "v_database.py", "update_raw_type_by_ID()",
                f"update raw type ID not found -> {ID}")
    return False


def check_update_raw_type_by_name(old_type: str, new_type: str) -> bool:
    if not v_h.is_valid_string(old_type):
        return False

    if not v_h.is_valid_string(new_type):
        return False

    result: r_m.ReturnMessage = s.select.select_all_raw_types()
    if not result.valid:
        log.message(log.LogType.INFO, "v_database.py", "update_raw_type_by_type()", "ResultMassage not valid")
        return False

    for _, raw_type in result.entry:
        if new_type == raw_type:
            log.message(log.LogType.INVALID_ARGUMENT, "v_database.py", "update_raw_type_by_name()",
                        f"raw type is already existing -> {new_type}")
            return False

    for _, raw_type in result.entry:
        if raw_type == old_type:
            return True

    log.message(log.LogType.INVALID_ARGUMENT, "v_database.py", "update_raw_type_by_name()",
                f"update old raw type not found -> {old_type}")
    return False


# /update


# delete
def check_delete_raw_type_by_ID(ID: int) -> bool:
    if not v_h.is_valid_ID(ID):
        return False

    result: r_m.ReturnMessage = s.select.select_all_raw_types()
    if not result.valid:
        log.message(log.LogType.INFO, "v_database.py", "delete_raw_type_by_ID()", "ResultMassage not valid")
        return False

    for old_ID, _ in result.entry:
        if old_ID == ID:
            return True

    log.message(log.LogType.INVALID_ARGUMENT, "v_database.py", "delete_raw_type_by_ID()",
                f"not entry ID found to delete -> {ID}")
    return False


def check_delete_raw_type_by_name(value: str) -> bool:
    if not v_h.is_valid_string(value):
        return False

    result: r_m.ReturnMessage = s.select.select_all_raw_types()
    if not result.valid:
        log.message(log.LogType.INFO, "v_database.py", "delete_raw_type_by_ID()", "ResultMassage not valid")
        return False

    for _, old_value in result.entry:
        if old_value == value:
            return True

    log.message(log.LogType.INVALID_ARGUMENT, "v_database.py", "delete_raw_type_by_ID()",
                f"not entry value found to delete -> {value}")
    return False


# /delete
# /raw types

# recipes
# select

def check_select_recipe_by_ID(ID: int) -> bool:
    if not v_h.is_valid_ID(ID):
        return False

    result: r_m.ReturnMessage = s.select.select_all_recipes()
    if not result.valid:
        log.message(log.LogType.INFO, "v_database.py", "select_recipe_by_ID()", "ResultMassage not valid")
        return False

    for _id, *_ in result.entry:
        if _id == ID:
            return True

    log.message(log.LogType.INVALID_ARGUMENT, "v_database.py", "select_recipe_by_ID()",
                f"no recipe with ID found -> {ID}")
    return False


def check_select_recipe_by_title(title: str) -> bool:
    if not v_h.is_valid_string(title):
        return False

    result: r_m.ReturnMessage = s.select.select_all_recipes()
    if not result.valid:
        log.message(log.LogType.INFO, "v_database.py", "select_recipe_by_title()", "ResultMassage not valid")
        return False

    for _, s_title, _ in result.entry:
        if s_title == title:
            return True

    log.message(log.LogType.INVALID_ARGUMENT, "v_database.py", "select_recipe_by_title()",
                f"no recipe with title found -> {title}")
    return False


# /select
# add

def check_add_recipe(title: str, description: str) -> bool:
    if not v_h.is_valid_string(title):
        return False
    if not v_h.is_valid_string(description):
        return False

    result: r_m.ReturnMessage = s.select.select_all_recipes()
    if not result.valid:
        log.message(log.LogType.INFO, "v_database.py", "add_recipe()", "ResultMassage not valid")
        return False

    for _, s_title, _ in result.entry:
        if s_title == title:
            log.message(log.LogType.INVALID_ARGUMENT, "v_database.py", "add_recipe()",
                        f"recipe title already existing -> {title}")
            return False

    return True


# /add
# update
def check_update_recipe_by_ID(ID: int, title: str, description: str) -> bool:
    if not v_h.is_valid_ID(ID):
        return False
    if not v_h.is_valid_string(title):
        return False
    if not v_h.is_valid_string(description):
        return False

    result = s.select.select_all_recipes()
    if not result.valid:
        log.message(log.LogType.INFO, "v_database.py", "update_recipe_by_ID()", "ResultMassage not valid")
        return False

    for s_ID, s_title, _ in result.entry:
        if s_title == title and s_ID != ID:
            log.message(log.LogType.INVALID_ARGUMENT, "v_database.py", "update_recipe_by_ID()",
                        f"recipe with title already exists -> {title}")
            return False

    for s_ID, _, _ in result.entry:
        if s_ID == ID:
            return True

    log.message(log.LogType.INVALID_ARGUMENT, "v_database.py", "update_recipe_by_ID()",
                f"no recipe with ID found -> {ID}")
    return False


def check_update_recipe_by_title(old_title: str, new_title: str, description: str) -> bool:
    if not v_h.is_valid_string(old_title):
        return False
    if not v_h.is_valid_string(new_title):
        return False
    if not v_h.is_valid_string(description):
        return False

    result = s.select.select_all_recipes()
    if not result.valid:
        log.message(log.LogType.INFO, "v_database.py", "update_recipe_by_title()", "ResultMassage not valid")
        return False

    if new_title != old_title:
        for _, s_title, _ in result.entry:
            if s_title == new_title:
                log.message(log.LogType.INVALID_ARGUMENT, "v_database.py", "update_recipe_by_title()",
                            f"recipe with title already exists -> {new_title}")
                return False

    for _, s_title, _ in result.entry:
        if s_title == old_title:
            return True

    log.message(log.LogType.INVALID_ARGUMENT, "v_database.py", "update_recipe_by_ID()",
                f"no recipe with title found -> {old_title}")
    return False


# /update

# delete
def check_delete_recipe_by_ID(ID: int) -> bool:
    if not v_h.is_valid_ID(ID):
        return False

    result = s.select.select_all_recipes()

    if not result.valid:
        log.message(log.LogType.INFO, "v_database.py", "delete_recipe_by_ID()", "ResultMessage not valid")

    for s_ID, _, _ in result.entry:
        if s_ID == ID:
            return True

    log.message(log.LogType.INVALID_ARGUMENT, "v_database.py", "delete_recipe_by_ID()",
                f"no recipe with ID found -> {ID}")
    return False


def check_delete_recipe_by_title(title: str) -> bool:
    if not v_h.is_valid_string(title):
        return False

    result = s.select.select_all_recipes()

    if not result.valid:
        log.message(log.LogType.INFO, "v_database.py", "delete_recipe_by_title()", "ResultMessage not valid")

    for _, s_title, _ in result.entry:
        if s_title == title:
            return True

    log.message(log.LogType.INVALID_ARGUMENT, "v_database.py", "delete_recipe_by_title()",
                f"no recipe with title found -> {title}")
    return False


# /delete
# /recipes

# ingredients
# select
def check_select_all_ingredients_from_recipe(recipe_ID: int) -> bool:
    if not v_h.is_valid_ID(recipe_ID):
        return False

    result = s.select.select_all_recipes()

    if not result.valid:
        log.message(log.LogType.INFO, "v_database.py", "select_all_ingredients_from_recipe()",
                    "ReturnMassage not valid")
        return False

    for ID, _, _ in result.entry:
        if ID == recipe_ID:
            return True

    log.message(log.LogType.INVALID_ARGUMENT, "v_database.py", "select_ingredient_by_ID()",
                f"no recipe with ID found -> {recipe_ID}")
    return False


def check_select_ingredient_by_ID(ID: int) -> bool:
    if not v_h.is_valid_ID(ID):
        return False

    result = s.select.select_all_ingredients()

    if not result.valid:
        log.message(log.LogType.INFO, "v_database.py", "select_ingredient_by_ID()",
                    "ReturnMassage not valid")
        return False

    for s_ID, *_, in result.entry:
        if s_ID == ID:
            return True

    log.message(log.LogType.INVALID_ARGUMENT, "v_database.py", "select_ingredient_by_ID()",
                f"no ingredient with ID found -> {ID}")
    return False


# /select

# add
def check_add_ingredient(recipe_id: int, amount: float, unit: str, ingredient: str) -> bool:
    if not v_h.is_valid_ID(recipe_id):
        return False
    if not v_h.is_valid_positive_float(amount):
        return False
    if not v_h.is_valid_empty_string(unit):
        return False
    if not v_h.is_valid_string(ingredient):
        return False

    recipe_result = s.select.select_all_recipes()
    ingredients_result = s.select.select_all_ingredients_from_recipe(recipe_id)

    if not v_h.is_valid_Return_Message(recipe_result):
        return False
    if not v_h.is_valid_Return_Message(ingredients_result):
        return False

    for _, _, _, _, s_ingredient in ingredients_result.entry:
        if s_ingredient == ingredient:
            log.message(log.LogType.INVALID_ARGUMENT, "v_database.py", "add_ingredient()",
                        f"ingredient already existing -> {ingredient}")
            return False

    for s_recipe_ID, *_ in recipe_result.entry:
        if s_recipe_ID == recipe_id:
            return True

    log.message(log.LogType.INVALID_ARGUMENT, "v_database.py", "add_ingredient()",
                f"no recipe with ID found -> {recipe_id}")
    return False


# /add

# update

def check_update_ingredient_by_ID(ID: int, amount: float, unit: str, ingredient: str) -> bool:
    if not v_h.is_valid_ID(ID):
        return False
    if not v_h.is_valid_positive_float(amount):
        return False
    if not v_h.is_valid_empty_string(unit):
        return False
    if not v_h.is_valid_string(ingredient):
        return False

    ingredient_result = s.select.select_ingredient_by_ID(ID)
    if not v_h.is_valid_Return_Message(ingredient_result):
        log.message(log.LogType.INVALID_ARGUMENT, "v_database.py", "update_ingredient_by_ID()", f"ID not valid -> {ID}")
        return False

    i_ID, i_recipe_ID, i_amount, i_unit, i_ingredient = ingredient_result.entry

    recipe_result = s.select.select_all_ingredients_from_recipe(i_recipe_ID)
    if not v_h.is_valid_Return_Message(recipe_result):
        return False

    for s_ID, s_recipe_ID, s_amount, s_unit, s_ingredient in recipe_result.entry:
        if s_ID == ID:
            continue
        if ingredient == s_ingredient:
            log.message(log.LogType.INVALID_ARGUMENT, "v_database.py", "update_ingredient_by_ID()",
                        f"ingredient already existing in that recipe -> {ingredient}")
            return False

    return True


# /update

# delete
def check_delete_ingredient_by_ID(ID: int) -> bool:
    if not v_h.is_valid_ID(ID):
        return False

    result = s.select.select_all_ingredients()
    if not v_h.is_valid_Return_Message(result):
        return False

    for s_ID, *_ in result.entry:
        if s_ID == ID:
            return True

    log.message(log.LogType.INVALID_ARGUMENT, "v_database.py", "check_delete_ingredient_by_ID()",
                f"no ingredient with ID found -> {ID}")
    return False


def check_delete_ingredients_by_recipe_ID(recipe_ID: int) -> bool:
    if not v_h.is_valid_ID(recipe_ID):
        return False

    result = s.select.select_all_recipes()
    if not v_h.is_valid_Return_Message(result):
        return False

    for s_ID, *_ in result.entry:
        if s_ID == recipe_ID:
            return True

    log.message(log.LogType.INVALID_ARGUMENT, "v_database.py", "check_delete_ingredients_by_recipe_ID()",
                f"no recipe with ID found -> {recipe_ID}")
    return False


# /delete
# /ingredients

# types
# select

def check_select_type_by_ID(ID: int) -> bool:
    if not v_h.is_valid_ID(ID):
        return False

    result = s.select.select_all_types()
    if not v_h.is_valid_Return_Message(result):
        return False

    for s_ID, *_ in result.entry:
        if s_ID == ID:
            return True

    log.message(log.LogType.INVALID_ARGUMENT, "v_database.py", "check_select_type_by_ID()",
                f"no type with ID found -> {ID}")
    return False


def check_select_type_by_recipe_ID(recipe_ID: int) -> bool:
    if not v_h.is_valid_ID(recipe_ID):
        return False

    result = s.select.select_all_recipes()
    if not v_h.is_valid_Return_Message(result):
        return False

    for ID, *_ in result.entry:
        if ID == recipe_ID:
            return True

    log.message(log.LogType.INVALID_ARGUMENT, "v_database.py", "check_select_type_by_recipe_ID()",
                f"no recipe with ID found -> {recipe_ID}")
    return False


def check_select_type_by_raw_type_ID(raw_type_ID: int) -> bool:
    if not v_h.is_valid_ID(raw_type_ID):
        return False

    result = s.select.select_all_raw_types()
    if not v_h.is_valid_Return_Message(result):
        return False

    for ID, *_ in result.entry:
        if ID == raw_type_ID:
            return True

    log.message(log.LogType.INVALID_ARGUMENT, "v_database.py", "check_select_type_by_raw_type_ID()",
                f"no raw type with ID found -> {raw_type_ID}")
    return False


# /select
# add

def check_add_type(recipe_ID: int, raw_type_ID: int) -> bool:
    if not v_h.is_valid_ID(recipe_ID):
        return False
    if not v_h.is_valid_ID(raw_type_ID):
        return False

    # check recipe ID
    ID_found: bool = False

    result = s.select.select_all_recipes()
    if not v_h.is_valid_Return_Message(result):
        return False

    for ID, *_ in result.entry:
        if ID == recipe_ID:
            ID_found = True
            break

    if not ID_found:
        log.message(log.LogType.INVALID_ARGUMENT, "v_database.py", "check_add_type()",
                    f"no recipe with ID found -> {recipe_ID}")
        return False

    # check raw type ID
    ID_found = False

    result = s.select.select_all_raw_types()
    if not v_h.is_valid_Return_Message(result):
        return False

    for ID, *_ in result.entry:
        if ID == raw_type_ID:
            ID_found = True
            break

    if not ID_found:
        log.message(log.LogType.INVALID_ARGUMENT, "v_database.py", "check_add_type()",
                    f"no raw type with ID found -> {raw_type_ID}")
        return False

    # check if type existing
    result = s.select.select_all_types()
    if not v_h.is_valid_Return_Message(result):
        return False

    for s_ID, s_recipe_ID, s_raw_type_ID in result.entry:
        if s_recipe_ID == recipe_ID and s_raw_type_ID == raw_type_ID:
            log.message(log.LogType.INVALID_ARGUMENT, "v_database.py", "check_add_type()",
                        f"type with ID already existing -> {recipe_ID} | {raw_type_ID}")
            return False

    return True


# /add

# update
# no need for validation functions because there are no update methods
# /update

# delete

def check_delete_type_by_ID(ID: int) -> bool:
    if not v_h.is_valid_ID(ID):
        return False

    result = s.select.select_all_types()
    if not v_h.is_valid_Return_Message(result):
        return False

    for s_ID, *_ in result.entry:
        if s_ID == ID:
            return True

    log.message(log.LogType.INVALID_ARGUMENT, "v_database.py", "check_delete_type_by_ID()",
                f"no type with ID found -> {ID}")
    return False


def check_delete_type_by_recipe_ID(recipe_ID: int) -> bool:
    if not v_h.is_valid_ID(recipe_ID):
        return False

    result = s.select.select_all_recipes()
    if not v_h.is_valid_Return_Message(result):
        return False

    for ID, *_ in result.entry:
        if ID == recipe_ID:
            return True

    log.message(log.LogType.INVALID_ARGUMENT, "v_database.py", "check_delete_type_by_recipe_ID()",
                f"no recipe with ID found -> {recipe_ID}")
    return False


def check_delete_type_by_raw_type_ID(raw_type_ID: int) -> bool:
    if not v_h.is_valid_ID(raw_type_ID):
        return False

    result = s.select.select_all_raw_types()
    if not v_h.is_valid_Return_Message(result):
        return False

    for ID, *_ in result.entry:
        if ID == raw_type_ID:
            return True

    log.message(log.LogType.INVALID_ARGUMENT, "v_database.py", "check_delete_type_by_raw_type_ID()",
                f"no raw type with ID found -> {raw_type_ID}")
    return False


def check_delete_type_by_recipe_ID_and_raw_type_ID(recipe_ID: int, raw_type_ID: int) -> bool:
    if not v_h.is_valid_ID(recipe_ID):
        return False
    if not v_h.is_valid_ID(raw_type_ID):
        return False

    # check recipe
    ID_found: bool = False
    result = s.select.select_all_recipes()
    if not v_h.is_valid_Return_Message(result):
        return False

    for ID, *_ in result.entry:
        if ID == recipe_ID:
            ID_found = True
            break

    if not ID_found:
        log.message(log.LogType.INVALID_ARGUMENT, "v_database.py", "check_delete_type_by_recipe_ID_and_raw_type_ID()",
                    f"no recipe with ID found -> {recipe_ID}")
        return False

    # check raw type
    ID_found = False
    result = s.select.select_all_raw_types()
    if not v_h.is_valid_Return_Message(result):
        return False

    for ID, *_ in result.entry:
        if ID == raw_type_ID:
            ID_found = True
            break

    if not ID_found:
        log.message(log.LogType.INVALID_ARGUMENT, "v_database.py", "check_delete_type_by_recipe_ID_and_raw_type_ID()",
                    f"no raw type with ID found -> {raw_type_ID}")
        return False

    # check types
    ID_found = False
    result = s.select.select_all_types()
    if not v_h.is_valid_Return_Message(result):
        return False

    for _, s_recipe_ID, s_raw_type_ID in result.entry:
        if s_recipe_ID == recipe_ID and s_raw_type_ID == raw_type_ID:
            ID_found = True

    if not ID_found:
        log.message(log.LogType.INVALID_ARGUMENT, "v_database.py", "check_delete_type_by_recipe_ID_and_raw_type_ID()",
                    f"no type with recipe ID and raw type ID found -> {recipe_ID} | {raw_type_ID}")
        return False

    return True

# /delete
# /types
