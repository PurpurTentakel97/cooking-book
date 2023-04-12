#
# Purpur Tentakel
# Cocking Book
# 12.04.2023
#

import pytest

from tests import test_helper as t_h
from validation import v_database as v_d


# select
@pytest.mark.parametrize(("ID", "expected"), [
    (1, True),
    (33, False)  # ID not existing
])
def test_select_raw_type_by_ID(ID, expected) -> None:
    t_h.generate_temporary_database()
    v_d.select_raw_type_by_ID(ID)
    t_h.delete_temporary_database()


@pytest.mark.parametrize(("value", "expected"), [
    ("Mittagessen", True),
    ("Nachtisch", False)  # value not existing
])
def test_select_raw_type_by_name(value, expected) -> None:
    t_h.generate_temporary_database()
    v_d.select_raw_type_by_name(value)
    t_h.delete_temporary_database()


# /select

# add
@pytest.mark.parametrize(("value", "expected"), [
    ("Mitternachtssnack", True),
    ("Abendessen", False),  # already exists
])
def test_add_raw_type(value, expected) -> None:
    t_h.generate_temporary_database()
    v_d.add_raw_type(value)
    t_h.delete_temporary_database()


# /add

# update
@pytest.mark.parametrize(("ID", "value", "expected"), [
    (1, "Mitternachtssnack", True),
    (2, "Frühstück", False),  # value already exists
    (20, "Hamsterbraten", False),  # ID doesn't exists
])
def test_update_raw_type_by_ID(ID, value, expected) -> None:
    t_h.generate_temporary_database()
    v_d.update_raw_type_by_ID(ID, value)
    t_h.delete_temporary_database()


@pytest.mark.parametrize(("old_value", "new_value", "expected"), [
    ("Abendessen", "Mitternachtssnack", True),
    ("Mittagsessen", "Frühstück", False),  # new value already existing
    ("Mitternachtssnack", "Tote", False),  # old value not existing
])
def test_update_raw_type_by_name(old_value, new_value, expected) -> None:
    t_h.generate_temporary_database()
    v_d.update_raw_type_by_name(old_value, new_value)
    t_h.delete_temporary_database()


# /update

# delete
@pytest.mark.parametrize(("ID", "expected"), [
    (1, True),
    (33, False)  # ID not existing
])
def test_delete_raw_type_by_ID(ID, expected) -> None:
    t_h.generate_temporary_database()
    v_d.delete_raw_type_by_ID(ID)
    t_h.delete_temporary_database()


@pytest.mark.parametrize(("value", "expected"), [
    ("Abendessen", True),
    ("Mitternachtssnack", False),  # value not existing
])
def test_delete_raw_type_by_name(value, expected) -> None:
    t_h.generate_temporary_database()
    v_d.delete_raw_type_by_name(value)
    t_h.delete_temporary_database()
# /delete
