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
# @formatter:off
@pytest.mark.parametrize("expected", [
    [(1, "Frühstück"  ),
     (2, "Mittagessen"),
     (3, "Abendessen")],
# @formatter:on
])
def test_select_all_raw_types(expected, database_fixture):
    expected.sort(key=lambda x: x[1])
    values = s.select.select_all_raw_types()

    assert values.valid
    for (p_id, p_value), (l_id, l_value) in zip(expected, values.entry):
        assert p_id == l_id
        assert p_value == l_value


# @formatter:off
@pytest.mark.parametrize(("ID", "value", "expected"), [
    (1, "Frühstück", True ),
    (20, "",         False),  # ID not existing
# @formatter:on
])
def test_select_raw_type_by_ID(ID, value, expected, database_fixture) -> None:
    result = s.select.select_raw_type_by_ID(ID)

    assert result.valid == expected
    if expected:
        assert result.entry == value


# @formatter:off
@pytest.mark.parametrize(("value", "ID", "expected"), [
    ("Mittagessen", 2, True ),
    ("Salat",       0, False),
# @formatter:on
])
def test_select_raw_type_ID_by_name(value, ID, expected, database_fixture) -> None:
    result = s.select.select_raw_type_ID_by_name(value)

    assert result.valid == expected
    if expected:
        assert result.entry == ID


# /select

# add
# @formatter:off
@pytest.mark.parametrize(("value", "ID", "expected"), [
    ("Nachtisch", 4, True ),
    ("Frühstück", 0, False),  # value already exists
# @formatter:on
])
def test_add_raw_type(value, ID, expected, database_fixture) -> None:
    result = a.add.add_raw_type(value)
    s_result = s.select.select_raw_type_by_ID(4)

    assert result.valid == expected
    if expected:
        assert s_result.valid
        assert s_result.entry == value


# /add
# update
# @formatter:off
@pytest.mark.parametrize(("ID", "value", "expected"), [
    (1,  "Nachtisch", True ),
    (10, "Nachtisch", False),  # ID not existing
    (2,  "Frühstück", False),  # value already existing
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


# @formatter:off
@pytest.mark.parametrize(("old_value", "new_value", "expected"), [
    ("Frühstück", "Nachtisch",   True ),
    ("Nachtisch", "Suppe",       False),  # old_value not existing
    ("Frühstück", "Mittagessen", False),  # new_value already existing
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
# @formatter:off
@pytest.mark.parametrize(("ID", "expected"), [
    (1,  True ),
    (20, False),  # ID not existing
# @formatter:on
])
def test_delete_raw_type_by_ID(ID, expected, database_fixture) -> None:
    result = d.delete.delete_raw_type_by_ID(ID)
    s_result = s.select.select_raw_type_by_ID(ID)

    assert result.valid == expected
    if expected:
        assert not s_result.valid


# @formatter:off
@pytest.mark.parametrize(("value", "expected"), [
    ("Frühstück", True ),
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
