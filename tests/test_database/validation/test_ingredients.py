#
# Purpur Tentakel
# Cooking Book
# 12.04.2023
#

import pytest

from tests.test_fixtures import database_fixture
from validation import v_database as v_d


# select
@pytest.mark.parametrize(("recipe_ID", "expected"), [
    # @formatter:off
    (1,  True ),
    (20, False),  # recipe ID not existing
    # @formatter:on
])
def test_select_all_ingredients_from_recipe(recipe_ID, expected, database_fixture) -> None:
    result = v_d.select_all_ingredients_from_recipe(recipe_ID)
    assert result == expected


@pytest.mark.parametrize(("ID", "expected"), [
    # @formatter:off
    (1,  True ),
    (20, False)  # ID not existing
    # @formatter:on
])
def test_select_ingredient_by_ID(ID, expected, database_fixture) -> None:
    result = v_d.select_ingredient_by_ID(ID)
    assert result == expected


# /select

# add
@pytest.mark.parametrize(("recipe_id", "amount", "unit", "ingredient", "expected"), [
    # @formatter:off
    (1, 150.0,  "g", "Tomatenmark", True ),  # expected normal input
    (1, 3.0,    "",  "Zwiebeln",    True ),  # expected normal input without unit
    (20, 150.0, "g", "Tomatenmark", False),  # recipe ID not existing
    (1, 150.0,  "g", "Nudeln",      False),  # ingredient already existing
    # @formatter:on
])
def test_add_ingredient(recipe_id, amount, unit, ingredient, expected, database_fixture) -> None:
    result = v_d.add_ingredient(recipe_id, amount, unit, ingredient)
    assert result == expected


# /add

# update
@pytest.mark.parametrize(("ID", "amount", "unit", "ingredient", "expected"), [
    # @formatter:off
    (1, 300.0, "ml", "Milch", True),  # expected normal input
    (1, 300.0, "", "Milch", True),  # normal input without unit
    (1, 300.0, "ml", "Nudeln", True),  # normal in with same ingredient
    (20, 300.0, "ml", "Milch", False),  # ID not existing
    (1, 300.0, "ml", "Tomaten", False),  # ingredient already existing in recipe
    # @formatter:on
])
def test_update_ingredient_by_ID(ID, amount, unit, ingredient, expected, database_fixture) -> None:
    result = v_d.update_ingredient_by_ID(ID, amount, unit, ingredient)
    assert result == expected

# /update
