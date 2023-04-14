#
# Purpur Tentakel
# Cooking Book
# 12.04.2023
#

import pytest

from database import add as a
from database import update as u
from database import delete as d
from database import select as s
from tests.test_fixtures import database_fixture


# select

@pytest.mark.parametrize("expected", [
    # @formatter:off
    [(1, "Frühstück"  ),
     (2, "Mittagessen"),
     (3, "Abendessen")],  # all data in the database
    # @formatter:on
])
def test_select_all_raw_types(expected, database_fixture):
    expected.sort(key=lambda x: x[1])
    values = s.select.select_all_raw_types()

    assert values.valid
    for (p_id, p_value), (l_id, l_value) in zip(expected, values.entry):
        assert p_id == l_id
        assert p_value == l_value


@pytest.mark.parametrize(("ID", "value", "expected"), [
    # @formatter:off
    (1, "Frühstück", True ),  # ID is existing
    (20, "test",     False),  # ID not existing
    # @formatter:on
])
def test_select_raw_type_by_ID(ID, value, expected, database_fixture) -> None:
    result = s.select.select_raw_type_by_ID(ID)

    assert result.valid == expected
    if expected:
        assert result.entry == value


@pytest.mark.parametrize(("value", "ID", "expected"), [
    # @formatter:off
    ("Mittagessen", 2, True ),  # title is existing
    ("Salat",       0, False),  # title not existing
    # @formatter:on
])
def test_select_raw_type_ID_by_name(value, ID, expected, database_fixture) -> None:
    result = s.select.select_raw_type_ID_by_name(value)

    assert result.valid == expected
    if expected:
        assert result.entry == ID


# /select

# add

@pytest.mark.parametrize(("value", "expected"), [
    # @formatter:off
    ("Nachtisch", True ),  # value not existing
    ("Frühstück", False),  # value already exists
    (""         , False),  # no value
    # @formatter:on
])
def test_add_raw_type(value, expected, database_fixture) -> None:
    result = a.add.add_raw_type(value)

    assert result.valid == expected
    if expected:
        s_result = s.select.select_raw_type_by_ID(result.entry)
        assert s_result.valid
        assert s_result.entry == value


# /add
# update

@pytest.mark.parametrize(("ID", "value", "expected"), [
    # @formatter:off
    (1,  "Nachtisch",   True ),  # new value
    (10, "Nachtisch",   False),  # ID not existing
    (1,  "Mittagessen", False),  # value already existing
    (1,  ""           , False),  # no value
    # @formatter:on
])
def test_update_raw_type_by_ID(ID, value, expected, database_fixture) -> None:
    result = u.update.update_raw_type_by_ID(ID, value)
    s1_result = s.select.select_raw_type_by_ID(ID)
    s2_result = s.select.select_raw_type_ID_by_name(value)

    assert result.valid == expected
    if expected:
        assert s1_result.valid
        assert s1_result.entry == value

        assert s2_result.valid
        assert s2_result.entry == ID


@pytest.mark.parametrize(("old_value", "new_value", "expected"), [
    # @formatter:off
    ("Frühstück", "Nachtisch",   True ),  # new new_value
    ("Nachtisch", "Suppe",       False),  # old_value not existing
    ("Frühstück", "Mittagessen", False),  # new_value already existing
    ("Frühstück", "",            False),  # no new_value
    # @formatter:on
])
def test_update_raw_type_by_name(old_value, new_value, expected, database_fixture) -> None:
    result = u.update.update_raw_type_by_name(old_value, new_value)
    s_result = s.select.select_raw_type_ID_by_name(new_value)

    assert result.valid == expected
    if expected:
        assert s_result.valid


# /update
# delete

@pytest.mark.parametrize(("ID", "expected"), [
    # @formatter:off
    (1,  True ),  # ID is existing
    (20, False),  # ID not existing
    # @formatter:on
])
def test_delete_raw_type_by_ID(ID, expected, database_fixture) -> None:
    result = d.delete.delete_raw_type_by_ID(ID)
    s_result = s.select.select_raw_type_by_ID(ID)

    assert result.valid == expected
    if expected:
        assert not s_result.valid


@pytest.mark.parametrize(("value", "expected"), [
    # @formatter:off
    ("Frühstück", True ),  # value is existing
    ("Nachtisch", False),  # value not existing
    # @formatter:on
])
def test_delete_raw_type_by_name(value, expected, database_fixture) -> None:
    result = d.delete.delete_raw_type_by_name(value)
    s_result = s.select.select_raw_type_ID_by_name(value)

    assert result.valid == expected
    if expected:
        assert not s_result.valid

# /delete
