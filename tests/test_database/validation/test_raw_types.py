#
# Purpur Tentakel
# Cooking Book
# 12.04.2023
#

import pytest

from tests.test_fixtures import database_fixture
from validation import v_database as v_d


# select
# @formatter:off
@pytest.mark.parametrize(("ID", "expected"), [
    (1,       True),
    (33,      False),  # ID not existing
    (bool(),  False),  # wrong datatype
# @formatter:on
])
def test_select_raw_type_by_ID(ID, expected, database_fixture) -> None:
    result = v_d.select_raw_type_by_ID(ID)
    assert result == expected


# @formatter:off
@pytest.mark.parametrize(("value", "expected"), [
    ("Mittagessen", True),
    ("Nachtisch",   False),  # value not existing
    (bool(),  False),  # wrong datatype
# @formatter:on
])
def test_select_raw_type_ID_by_name(value, expected, database_fixture) -> None:
    result = v_d.select_raw_type_ID_by_name(value)
    assert result == expected


# /select

# add
# @formatter:off
@pytest.mark.parametrize(("value", "expected"), [
    ("Mitternachtssnack", True),
    ("Abendessen",        False),  # already exists
    (bool(),  False),  # wrong datatype
# @formatter:on
])
def test_add_raw_type(value, expected, database_fixture) -> None:
    result = v_d.add_raw_type(value)
    assert result == expected


# /add

# update
# @formatter:off
@pytest.mark.parametrize(("ID", "value", "expected"), [
    (1,  "Mitternachtssnack", True),
    (2,  "Frühstück",         False),  # value already exists
    (20, "Hamsterbraten",     False),  # ID doesn't exists
    (bool(),  str(),   False),  # wrong first datatype
    (int(),   bool(),  False),  # wrong second datatype
# @formatter:on
])
def test_update_raw_type_by_ID(ID, value, expected, database_fixture) -> None:
    result = v_d.update_raw_type_by_ID(ID, value)
    assert result == expected


# @formatter:off
@pytest.mark.parametrize(("old_value", "new_value", "expected"), [
    ("Abendessen",        "Mitternachtssnack", True),
    ("Mittagsessen",      "Frühstück",         False),  # new value already existing
    ("Mitternachtssnack", "Tote",              False),  # old value not existing
    (bool(),  str(),    False),  # wrong first datatype
    (str(),   bool(),   False),  # wrong second datatype
# @formatter:on
])
def test_update_raw_type_by_name(old_value, new_value, expected, database_fixture) -> None:
    result = v_d.update_raw_type_by_name(old_value, new_value)
    assert result == expected


# /update

# delete
# @formatter:off
@pytest.mark.parametrize(("ID", "expected"), [
    (1,  True),
    (33, False),  # ID not existing
    (bool(),  False),  # wrong datatype

# @formatter:on
])
def test_delete_raw_type_by_ID(ID, expected, database_fixture) -> None:
    result = v_d.delete_raw_type_by_ID(ID)
    assert result == expected


# @formatter:off
@pytest.mark.parametrize(("value", "expected"), [
    ("Abendessen",        True),
    ("Mitternachtssnack", False),  # value not existing
    (bool(),  False),  # wrong datatype
# @formatter:on
])
def test_delete_raw_type_by_name(value, expected, database_fixture) -> None:
    result = v_d.delete_raw_type_by_name(value)
    assert result == expected
# /delete
