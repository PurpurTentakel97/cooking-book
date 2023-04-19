#
# Purpur Tentakel
# Cooking Book
# 13.04.2023
#

import pytest

from validation import v_database as v_d
from tests.test_fixtures import database_fixture


# select
@pytest.mark.parametrize(("ID", "expected"), [
    # @formatter:off
    (1,      True ),  # ID is existing
    (20,     False),  # ID not existing
    # @formatter:on
])
def test_check_select_recipe_by_ID(ID, expected, database_fixture) -> None:
    result = v_d.check_select_raw_type_by_ID(ID)
    assert result == expected



@pytest.mark.parametrize(("title", "expected"), [
    # @formatter:off
    ("Nudelauflauf",          True ),  # title is existing
    ("Pfannekuchen",          False),  # title not existing
    ("    Pfannekuchen     ", False),  # no striping here
    # @formatter:on
])
def test_check_select_recipe_by_title(title, expected, database_fixture) -> None:
    result = v_d.check_select_recipe_by_title(title)
    assert result == expected


# /select
# add


@pytest.mark.parametrize(("title", "description", "expected"), [
    # @formatter:off
    ("Pfannekuchen",        "Beschreibung 6", True),   # new values
    ("Pfannekuchen",        "Beschreibung 1", True),   # new title, existing description
    ("   Pfannekuchen    ", "Beschreibung 6", True),  # no stripping here
    ("Nudelauflauf",        "Beschreibung 6", False),  # title already existing
    # @formatter:on
])
def test_check_add_recipe(title, description, expected, database_fixture) -> None:
    result = v_d.check_add_recipe(title, description)
    assert result == expected


# /add
# update
@pytest.mark.parametrize(("ID", "title", "description", "expected"), [
    # @formatter:off
    (1,  "Lasagne",      "Beschreibung 1", True ),  # new title
    (1,  "Nudelauflauf", "Beschreibung 6", True ),  # new description
    (1,  "Lasagne",      "Beschreibung 6", True ),  # new title and description
    (2,  "   Lasagne  ", "Beschreibung 1", True ),  # no stripping here
    (20, "Lasagne",      "Beschreibung 6", False),  # ID not existing
    (2,  "Nudelauflauf", "Beschreibung 1", False),  # title already existing
    # @formatter:on
])
def test_check_update_recipe_by_ID(ID, title, description, expected, database_fixture) -> None:
    result = v_d.check_update_recipe_by_ID(ID, title, description)
    assert result == expected


@pytest.mark.parametrize(("old_title", "new_title", "description", "expected"), [
    # @formatter:off
    ("Nudelauflauf", "Lasagne",            "Beschreibung 1", True ),  # new title
    ("Nudelauflauf", "   Nudelauflauf   ", "Beschreibung 1", True ),  # no stripping here
    ("Nudelauflauf", "Nudelauflauf",       "Beschreibung 6", True ),  # new description
    ("Nudelauflauf", "Lasagne",            "Beschreibung 6", True ),  # new title and description
    ("Lasagne",      "Tomaten",            "Beschreibung 2", False),  # old title not existing
    ("Nudelauflauf", "Braten",             "Beschreibung 2", False),  # new title already existing
    # @formatter:on
])
def test_check_update_recipe_by_title(old_title, new_title, description, expected, database_fixture) -> None:
    result = v_d.check_update_recipe_by_title(old_title, new_title, description)
    assert result == expected


# /update

# delete
@pytest.mark.parametrize(("ID", "expected"), [
    # @formatter:off
    (1,  True ),  # ID is existing
    (20, False),  # ID not existing
    # @formatter:on
])
def test_check_delete_recipe_by_ID(ID, expected, database_fixture) -> None:
    result = v_d.check_delete_recipe_by_ID(ID)
    assert result == expected


@pytest.mark.parametrize(("title", "expected"), [
    # @formatter:off
    ("Nudelauflauf",       True ),  # title is existing
    ("   Nudelauflauf   ", False),  # no stripping
    ("Abendessen",         False),  # title not existing
    # @formatter:on
])
def test_check_delete_recipe_by_title(title, expected, database_fixture) -> None:
    result = v_d.check_delete_recipe_by_title(title)
    assert result == expected
