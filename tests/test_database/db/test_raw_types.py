#
# Purpur Tentakel
# Cocking Book
# 12.04.2023
#
import pytest

from tests import test_helper as t_h
from database import add as a
from database import update as u
from database import delete as d
from database import select as s


# select
@pytest.mark.parametrize("expected", [
    [(1, "Frühstück"),
     (2, "Mittagessen"),
     (3, "Abendessen")],
])
def test_select_all_raw_types(expected):
    expected.sort(key=lambda x: x[1])
    t_h.generate_temporary_database()
    values = s.select.select_all_raw_types()

    assert values.valid

    for (p_id, p_value), (l_id, l_value) in zip(expected, values.entry):
        assert p_id == l_id
        assert p_value == l_value

    t_h.delete_temporary_database()


@pytest.mark.parametrize(("ID", "value", "expected"), [
    (1, "Frühstück", True),
    (20, "", False),  # ID not existing
])
def test_select_raw_type_by_ID(ID, value, expected) -> None:
    t_h.generate_temporary_database()

    result = s.select.select_raw_type_by_ID(ID)
    assert result.valid == expected
    if expected:
        assert result.entry == value

    t_h.delete_temporary_database()


@pytest.mark.parametrize(("value", "ID", "expected"), [
    ("Mittagessen", 2, True),
    ("Salat", 0, False),
])
def test_select_raw_type_ID_by_name(value, ID, expected) -> None:
    t_h.generate_temporary_database()

    result = s.select.select_raw_type_ID_by_name(value)
    assert result.valid == expected
    if expected:
        assert result.entry == ID

    t_h.delete_temporary_database()


# /select

# add
@pytest.mark.parametrize(("value", "ID", "expected"), [
    ("Nachtisch", 4, True),
    ("Frühstück", 0, False),  # value already exists
])
def test_add_raw_type(value, ID, expected) -> None:
    t_h.generate_temporary_database()
    result = a.add.add_raw_type(value)

    assert result.valid == expected

    if expected:
        s_result = s.select.select_raw_type_by_ID(4)
        assert s_result.valid
        assert s_result.entry == value

    t_h.delete_temporary_database()


# /add
# update
@pytest.mark.parametrize(("ID", "value", "expected"), [
    (1, "Nachtisch", True),
    (10, "Nachtisch", False),  # ID not existing
    (2, "Frühstück", False),  # value already existing
])
def test_update_raw_type_by_ID(ID, value, expected) -> None:
    t_h.generate_temporary_database()

    result = u.update.update_raw_type_by_ID(ID, value)
    assert result.valid == expected

    if expected:
        result = s.select.select_raw_type_by_ID(ID)
        assert result.valid
        assert result.entry == value

        result = s.select.select_raw_type_ID_by_name(value)
        assert result.valid
        assert result.entry == ID

    t_h.delete_temporary_database()


@pytest.mark.parametrize(("old_value", "new_value", "expected"), [
    ("Frühstück", "Nachtisch", True),
    ("Nachtisch", "Suppe", False),  # old_value not existing
    ("Frühstück", "Mittagessen", False),  # new_value already existing
])
def test_update_raw_type_by_name(old_value, new_value, expected) -> None:
    t_h.generate_temporary_database()

    result = u.update.update_raw_type_by_name(old_value, new_value)
    assert result.valid == expected

    if expected:
        result = s.select.select_raw_type_ID_by_name(new_value)
        assert result.valid

    t_h.delete_temporary_database()


# /update
# delete
@pytest.mark.parametrize(("ID", "expected"), [
    (1, True),
    (20, False),  # ID not existing
])
def test_delete_raw_type_by_ID(ID, expected) -> None:
    t_h.generate_temporary_database()

    result = d.delete.delete_raw_type_by_ID(ID)
    assert result.valid == expected

    if expected:
        result = s.select.select_raw_type_by_ID(ID)
        assert not result.valid

    t_h.delete_temporary_database()


@pytest.mark.parametrize(("value", "expected"), [
    ("Frühstück", True),
    ("Nachtisch", False),  # value not existing
])
def test_delete_raw_type_by_name(value, expected) -> None:
    t_h.generate_temporary_database()

    result = d.delete.delete_raw_type_by_name(value)
    assert result.valid == expected

    if expected:
        result = s.select.select_raw_type_ID_by_name(value)
        assert not result.valid

    t_h.delete_temporary_database()

# /delete
