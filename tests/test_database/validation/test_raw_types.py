#
# Purpur Tentakel
# Cooking Book
# 12.04.2023
#

import pytest

from validation import v_database as v_d
from tests.test_fixtures import database_fixture


# select

@pytest.mark.parametrize(("ID", "expected"), [
    # @formatter:off
    (1,       True ),  # ID is existing
    (33,      False),  # ID not existing
    # @formatter:on
])
def test_check_select_raw_type_by_ID(ID, expected, database_fixture) -> None:
    result = v_d.check_select_raw_type_by_ID(ID)
    assert result == expected


@pytest.mark.parametrize(("value", "expected"), [
    # @formatter:off
    ("Mittagessen", True ),  # value is existing
    ("Nachtisch",   False),  # value not existing
    # @formatter:on
])
def test_check_select_raw_type_ID_by_name(value, expected, database_fixture) -> None:
    result = v_d.check_select_raw_type_ID_by_name(value)
    assert result == expected


# /select

# add

@pytest.mark.parametrize(("value", "expected"), [
    # @formatter:off
    ("Mitternachtssnack", True ),  # new
    ("Abendessen",        False),  # already exists
    # @formatter:on
])
def test_check_add_raw_type(value, expected, database_fixture) -> None:
    result = v_d.check_add_raw_type(value)
    assert result == expected


# /add

# update
@pytest.mark.parametrize(("ID", "value", "expected"), [
    # @formatter:off
    (1,  "Mitternachtssnack", True ),  # new value
    (2,  "Frühstück",         False),  # value already exists
    (20, "Hamsterbraten",     False),  # ID doesn't exists
    # @formatter:on
])
def test_check_update_raw_type_by_ID(ID, value, expected, database_fixture) -> None:
    result = v_d.check_update_raw_type_by_ID(ID, value)
    assert result == expected


@pytest.mark.parametrize(("old_value", "new_value", "expected"), [
    # @formatter:off
    ("Abendessen",        "Mitternachtssnack", True ),  # new values
    ("Mittagsessen",      "Frühstück",         False),  # new value already existing
    ("Mitternachtssnack", "Tote",              False),  # old value not existing
    # @formatter:on
])
def test_check_update_raw_type_by_name(old_value, new_value, expected, database_fixture) -> None:
    result = v_d.check_update_raw_type_by_name(old_value, new_value)
    assert result == expected


# /update

# delete
@pytest.mark.parametrize(("ID", "expected"), [
    # @formatter:off
    (1,  True ),  # ID is existing
    (33, False),  # ID not existing
    # @formatter:on
])
def test_check_delete_raw_type_by_ID(ID, expected, database_fixture) -> None:
    result = v_d.check_delete_raw_type_by_ID(ID)
    assert result == expected


@pytest.mark.parametrize(("value", "expected"), [
    # @formatter:off
    ("Abendessen",        True ),  # new value
    ("Mitternachtssnack", False),  # value not existing
    # @formatter:on
])
def test_check_delete_raw_type_by_name(value, expected, database_fixture) -> None:
    result = v_d.check_delete_raw_type_by_name(value)
    assert result == expected
# /delete
