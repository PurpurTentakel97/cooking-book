#
# Purpur Tentakel
# Cooking Book
# 12.04.2023
#

import pytest

from database import add as a
from database import select as s
from database import update as u
from database import delete as d
from tests.test_fixtures import database_fixture


# select
@pytest.mark.parametrize("data", [
    # @formatter:off
    [(1,  1, 500.0, "g",  "Nudeln"           ),
     (2,  1, 500.0, "ml", "passierte Tomaten"),
     (3,  1, 2.0,   "",   "Tomaten"          ),

     (4,  2, 500.0, "g", "Hackfleisch"       ),
     (5,  2, 3.5,   "",  "Brötchen"          ),
     (6,  2, 5.0,   "",  "Eier"              ),

     (7,  3, 150.0, "ml", "Milch"            ),
     (8,  3, 50.0,  "g",  "Pudding Pulver"   ),

     (9,  4, 1.0,   "",   "Salat"             ),
     (10, 4, 100.0, "ml", "Öl"                ),
     (11, 4, 10.6,  "ml", "Essig"             ),

     (12, 5, 1000.0, "g",  "Mehl"             ),
     (13, 5, 600.0,  "ml", "Wasser"           ),
     (14, 5, 10.5,   "g",  "Trocken Hefe"     ), ],
    # @formatter:on
])
def test_select_all_ingredients(data, database_fixture) -> None:
    data.sort(key=lambda x: x[4])
    values = s.select.select_all_ingredients()

    assert values.valid
    for (p_ID, p_r_ID, p_amount, p_unit, p_ing), (s_ID, s_r_ID, s_amount, s_unit, s_ing) in zip(data, values.entry):
        assert p_ID == s_ID
        assert p_r_ID == s_r_ID
        assert p_amount == s_amount
        assert p_unit == s_unit
        assert p_ing == s_ing


@pytest.mark.parametrize(("recipe_ID", "expected"), [
    # @formatter:off
    (1,  True ),
    (20, False),  # recipe ID not existing
    # @formatter:on
])
def test_select_all_ingredients_from_recipe(recipe_ID, expected, database_fixture) -> None:
    values = s.select.select_all_ingredients_from_recipe(recipe_ID)

    assert values.valid == expected

    if expected:
        for _, ID, *_ in values.entry:
            assert recipe_ID == ID


@pytest.mark.parametrize(("ID", "ingredient", "expected"), [
    # @formatter:off
    (1,  "Nudeln", True ),
    (20, "",       False)  # ID not existing
    # @formatter:on
])
def test_select_ingredient_by_ID(ID, ingredient, expected, database_fixture) -> None:
    value = s.select.select_ingredient_by_ID(ID)

    assert value.valid == expected
    if expected:
        _, _, _, _, s_ingredient = value.entry
        assert s_ingredient == ingredient


# /select

# add
@pytest.mark.parametrize(("recipy_id", "amount", "unit", "ingredient", "expected"), [
    # @formatter:off
    (1,  30.0, "g",    "Mehl",   True ),
    (1,  30.0, "",     "Mehl",   True ),
    (20, 1.0,  "test", "test",   False),  # recipe ID not existing
    (1,  30.0, "",     "Nudeln", False)  # ingredient already exists
    # @formatter:on
])
def test_add_ingredients(recipy_id, amount, unit, ingredient, expected, database_fixture) -> None:
    result = a.add.add_ingredient(recipy_id, amount, unit, ingredient)

    assert result.valid == expected
    if expected:
        s_result = s.select.select_ingredient_by_ID(result.entry)
        assert s_result.valid
        s_ID, s_recipy_id, s_amount, s_unit, s_ingredient = s_result.entry
        assert s_ID == result.entry
        assert s_recipy_id == recipy_id
        assert s_amount == amount
        assert s_unit == unit
        assert s_ingredient == ingredient

# /add
