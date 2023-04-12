#
# Purpur Tentakel
# Cocking Book
# 12.04.2023
#

import pytest

from tests import test_helper
from database import add as a
from database import update as u
from database import delete as d


@pytest.mark.parametrize(("value", "expected"), [
    ("Mitternachtssnack", True),
    ("Abendessen", False),  # already exists
])
def test_add_raw_type(value, expected) -> None:
    test_helper.generate_temporary_database()
    a.add.add_raw_type(value)
    test_helper.delete_temporary_database()


@pytest.mark.parametrize(("ID", "value", "expected"), [
    (1, "Mitternachtssnack", True),
    (2, "Frühstück", False),  # value already exists
    (20, "Hamsterbraten", False),  # ID doesn't exists
])
def test_update_raw_type_by_ID(ID, value, expected) -> None:
    test_helper.generate_temporary_database()
    u.update.update_raw_type_by_ID(ID, value)
    test_helper.delete_temporary_database()


@pytest.mark.parametrize(("old_value", "new_value", "expected"), [
    ("Abendessen", "Mitternachtssnack", True),
    ("Mittagsessen", "Frühstück", False),  # new value already existing
    ("Mitternachtssnack", "Tote", False),  # old value not existing
])
def test_update_raw_type_by_name(old_value, new_value, expected) -> None:
    test_helper.generate_temporary_database()
    u.update.update_raw_type_by_name(old_value, new_value)
    test_helper.delete_temporary_database()


@pytest.mark.parametrize(("ID", "expected"), [
    (1, True),
    (33, False)  # ID not existing
])
def test_delete_raw_type_by_ID(ID, expected) -> None:
    test_helper.generate_temporary_database()
    d.delete.delete_raw_type_by_ID(ID)
    test_helper.delete_temporary_database()


@pytest.mark.parametrize(("value", "expected"), [
    ("Abendessen", True),
    ("Mitternachtssnack", False),  # value not existing
])
def test_delete_raw_type_by_name(value, expected) -> None:
    test_helper.generate_temporary_database()
    d.delete.delete_raw_type_by_name(value)
    test_helper.delete_temporary_database()
