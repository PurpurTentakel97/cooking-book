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


@pytest.mark.parametrize("data", [
    # @formatter:off
    ([
        [1, "Nudelauflauf",  "Beschreibung 1" ],
        [2, "Braten",        "Beschreibung 2" ],
        [3, "Schokopudding", "Beschreibung 3" ],
        [4, "Salat",         "Beschreibung 4" ],
        [5, "Brot",          "Beschreibung 5" ],  # all data the database should have
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


@pytest.mark.parametrize(("ID", "title", "description", "expected"), [
    # @formatter:off
    (1,  "Nudelauflauf", "Beschreibung 1", True ),  # ID is existing
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
    # @formatter:off
    (1,  "Nudelauflauf", "Beschreibung 1", True  ),  # title is existing
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

@pytest.mark.parametrize(("ID", "title", "description", "expected"), [
    # @formatter:off
    (6, "Lasagne",      "Beschreibung 6", True  ),  # new title and description
    (6, "Lasagne",      "Beschreibung 1", True  ),  # new title
    (6, "Nudelauflauf", "Beschreibung 6", False ),  # title already existing
    (6, "Lasagne",      "",               False ),  # no description
    (6, "",             "Beschreibung 6", False ),  # no title
    # @formatter:on
])
def test_add_recipe(ID, title, description, expected, database_fixture) -> None:
    result = a.add.add_recipe(title, description)

    assert result.valid == expected
    if expected:
        s_result = s.select.select_recipe_by_ID(result.entry)
        assert s_result.valid
        s_ID, s_title, s_description = s_result.entry
        assert s_ID == ID
        assert s_title == title
        assert s_description == description


# /add
# update
@pytest.mark.parametrize(("ID", "title", "description", "expected"), [
    # @formatter:off
    (1,  "Nachtisch",    "Beschreibung 6", True ),  # new title and new description
    (1,  "Nachtisch",    "Beschreibung 1", True ),  # new title
    (1,  "Nudelauflauf", "Beschreibung 6", True ),  # new description
    (20, "test",         "test",           False),  # ID not existing
    (1,  "Braten",       "Beschreibung 1", False),  # title already existing
    (1,  "Nudelauflauf", "",               False),  # no description
    (1,  "",             "Beschreibung 1", False),  # no title

    # @formatter:on
])
def test_update_recipe_by_ID(ID, title, description, expected, database_fixture) -> None:
    result = u.update.update_recipe_by_ID(ID, title, description)
    s_result = s.select.select_recipe_by_ID(ID)

    assert result.valid == expected

    if expected:
        s_ID, s_title, s_description = s_result.entry
        assert s_ID == ID
        assert s_title == title
        assert s_description == description


@pytest.mark.parametrize(("old_title", "new_title", "description", "expected"), [
    # @formatter:off
    ("Nudelauflauf", "Nachtisch",    "Beschreibung 6", True ),  # new description and new title
    ("Nudelauflauf", "Nachtisch",    "Beschreibung 1", True ),  # new title
    ("Nudelauflauf", "Nudelauflauf", "Beschreibung 6", True ),  # new description
    ("Nachtisch",    "test",         "test",           False),  # old title not existing
    ("Nudelauflauf", "Braten",       "test",           False),  # new title already existing
    ("Nudelauflauf", "",             "test",           False),  # no new title
    ("Nudelauflauf", "Braten",       "",               False),  # no description

    # @formatter:on
])
def test_update_recipe_by_title(old_title, new_title, description, expected, database_fixture) -> None:
    result = u.update.update_recipe_by_title(old_title, new_title, description)
    s_result = s.select.select_recipe_by_title(new_title)

    assert result.valid == expected

    if expected:
        _, s_title, s_description = s_result.entry
        assert s_title == new_title
        assert s_description == description


# /update

# delete
@pytest.mark.parametrize(("ID", "expected"), [
    # @formatter:off
    (1,  True ),  # ID is existing
    (20, False),  # ID not existing
    # @formatter:on
])
def test_delete_recipe_by_ID(ID, expected, database_fixture) -> None:
    result = d.delete.delete_recipe_by_ID(ID)
    s_result = s.select.select_recipe_by_ID(ID)

    assert result.valid == expected

    if expected:
        assert not s_result.valid


@pytest.mark.parametrize(("title", "expected"), [
    # @formatter:off
    ("Nudelauflauf", True ),  # title is existing
    ("Nachtisch",    False),  # title not existing
    # @formatter:on
])
def test_delete_recipe_by_title(title, expected, database_fixture) -> None:
    result = d.delete.delete_recipe_by_title(title)
    s_result = s.select.select_recipe_by_title(title)

    assert result.valid == expected

    if expected:
        assert not s_result.valid

# /delete
