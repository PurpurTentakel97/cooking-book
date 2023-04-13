#
# Purpur Tentakel
# Cooking Book
# 13.04.2023
#

import pytest

from database import add as a
from database import update as u
from database import delete as d
from database import select as s
from tests.test_fixtures import database_fixture


# select

# @formatter:off
@pytest.mark.parametrize("data", [
    ([
        [1, "Nudelauflauf",  "Beschreibung 1" ],
        [2, "Braten",        "Beschreibung 2" ],
        [3, "Schokopudding", "Beschreibung 3" ],
        [4, "Salat",         "Beschreibung 4" ],
        [5, "Brot",          "Beschreibung 5" ],
    ]),
# @formatter:on
])
def test_select_all_recipes(data, database_fixture) -> None:
    data.sort(key=lambda x: x[1])
    result = s.select.select_all_recipes()

    assert result.valid
    for (s_ID, s_title, s_description), (ID, title, description) in zip(result.entry, data):
        assert s_ID == ID
        assert s_title == title
        assert s_description == description


# @formatter:off
@pytest.mark.parametrize(("ID", "title", "description", "expected"), [
    (1,  "Nudelauflauf", "Beschreibung 1", True ),
    (20, "",             "",               False),  # ID not existing
# @formatter:on
])
def test_select_recipe_by_ID(ID, title, description, expected, database_fixture) -> None:
    result = s.select.select_recipe_by_ID(ID)

    assert result.valid == expected
    if expected:
        _, s_title, s_description = result.entry
        assert s_title == title
        assert s_description == description


# @formatter:off
@pytest.mark.parametrize(("ID", "title", "description", "expected"), [
    (1,  "Nudelauflauf", "Beschreibung 1", True  ),
    (1,  "Lasagne",      "",               False ),  # title not existing
# @formatter:on
])
def test_select_recipe_by_title(ID, title, description, expected, database_fixture) -> None:
    result = s.select.select_recipe_by_title(title)

    assert result.valid == expected
    if expected:
        s_ID, _, s_description = result.entry
        assert s_ID == ID
        assert s_description == description


# /select

# add
# @formatter:off
@pytest.mark.parametrize(("ID","title","description", "expected"), [
    (6, "Lasagne",      "Beschreibung 6", True  ),
    (6, "Lasagne",      "Beschreibung 1", True  ),
    (6, "Nudelauflauf", "Beschreibung 6", False ),  # title already existing
    (6, "Lasagne",      "",               False ),  # no description
# @formatter:on
])
def test_add_recipe(ID, title, description, expected, database_fixture) -> None:
    result = a.add.add_recipe(title, description)
    s1_result = s.select.select_recipe_by_title(title)

    assert result.valid == expected
    if expected:
        s_ID, s_title, s_description = s1_result.entry
        assert s_ID == ID
        assert s_title == title
        assert s_description == description
# /add
