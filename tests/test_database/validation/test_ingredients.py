#
# Purpur Tentakel
# Cooking Book
# 12.04.2023
#

import pytest

from validation import v_database as v_d
from tests.test_fixtures import database_fixture


# select
@pytest.mark.parametrize(("recipe_ID", "expected"), [
    # @formatter:off
    (1,  True ),  # recipe ID is existing
    (20, False),  # recipe ID not existing
    # @formatter:on
])
def test_check_select_all_ingredients_from_recipe(recipe_ID, expected, database_fixture) -> None:
    result = v_d.check_select_all_ingredients_from_recipe(recipe_ID)
    assert result == expected


@pytest.mark.parametrize(("ID", "expected"), [
    # @formatter:off
    (1,  True ),  # ID is existing
    (20, False),  # ID not existing
    # @formatter:on
])
def test_check_select_ingredient_by_ID(ID, expected, database_fixture) -> None:
    result = v_d.check_select_ingredient_by_ID(ID)
    assert result == expected


# /select

# add
@pytest.mark.parametrize(("recipe_id", "amount", "unit", "ingredient", "expected"), [
    # @formatter:off
    (1, 150.0,  "g", "Tomatenmark", True ),  # expected normal input
    (1, 3.0,    "",  "Zwiebeln",    True ),  # input without unit
    (20, 150.0, "g", "Tomatenmark", False),  # recipe ID not existing
    (1, 150.0,  "g", "Nudeln",      False),  # ingredient already existing
    (1, 150.0,  "g", "   Nudeln  ", True ),  # no stripping
    # @formatter:on
])
def test_check_add_ingredient(recipe_id, amount, unit, ingredient, expected, database_fixture) -> None:
    result = v_d.check_add_ingredient(recipe_id, amount, unit, ingredient)
    assert result == expected


# /add

# update
@pytest.mark.parametrize(("ID", "amount", "unit", "ingredient", "expected"), [
    # @formatter:off
    (1,  300.0, "ml", "Milch",     True ),  # expected normal input
    (1,  300.0, ""  , "Milch",     True ),  # normal input without unit
    (1,  300.0, "ml", "Nudeln",    True ),  # normal input with same ingredient
    (20, 300.0, "ml", "Milch",     False),  # ID not existing
    (1,  300.0, "ml", "Tomaten",   False),  # ingredient already existing in recipe
    (1,  300.0, "ml", " Tomaten ", True ),  # no stripping
    (1,  0.0,   "ml", "Milch",     False),  # amount of 0.0
    # @formatter:on
])
def test_check_update_ingredient_by_ID(ID, amount, unit, ingredient, expected, database_fixture) -> None:
    result = v_d.check_update_ingredient_by_ID(ID, amount, unit, ingredient)
    assert result == expected


# /update

# delete
@pytest.mark.parametrize(("ID", "expected"), [
    # @formatter:off
    (1,  True ),  # ID is existing
    (20, False),  # ID not existing
    # @formatter:on
])
def test_check_delete_ingredient_by_ID(ID, expected, database_fixture) -> None:
    result = v_d.check_delete_ingredient_by_ID(ID)
    assert result == expected


@pytest.mark.parametrize(("recipe_ID", "expected"), [
    # @formatter:off
    (1,  True ),  # recipe_ID is existing
    (20, False),  # recipe_ID not existing
    # @formatter:on
])
def test_check_delete_ingredients_by_recipe_ID(recipe_ID, expected, database_fixture) -> None:
    result = v_d.check_delete_ingredients_by_recipe_ID(recipe_ID)
    assert result == expected

# /delete
