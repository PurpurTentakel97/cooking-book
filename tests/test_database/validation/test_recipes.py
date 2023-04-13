#
# Purpur Tentakel
# Cooking Book
# 13.04.2023
#

import pytest

from tests import test_helper as t_h
from validation import v_database as v_d


# select
# @formatter:off
@pytest.mark.parametrize(("ID", "expected"), [
    (1,      True ),
    (20,     False),  # ID not existing
    (bool(), False),  # wrong datatype
# @formatter:on
])
def test_select_recipe_by_ID(ID, expected) -> None:
    t_h.generate_temporary_database()
    result = v_d.select_raw_type_by_ID(ID)
    t_h.delete_temporary_database()
    assert result == expected


# @formatter:off
@pytest.mark.parametrize(("title", "expected"), [
    ("Nudelauflauf", True ),
    ("Pfannekuchen", False),  # title not existing
    (bool(),         False),  # wrong datatype
# @formatter:on
])
def test_select_recipe_by_title(title, expected) -> None:
    t_h.generate_temporary_database()
    result = v_d.select_recipe_by_title(title)
    t_h.delete_temporary_database()
    assert result == expected


# /select
# add

# @formatter:off
@pytest.mark.parametrize(("title", "description", "expected"), [
    ("Pfannekuchen", "Beschreibung 6", True),
    ("Pfannekuchen", "Beschreibung 1", True),
    ("Nudelauflauf", "Beschreibung 6", False),  # title already existing
    (bool(),         "Beschreibung 6", False),  # wrong datatype
    ("Pfannekuchen",  bool(),          False),  # wrong datatype
# @formatter:on
])
def test_add_recipe(title, description, expected) -> None:
    t_h.generate_temporary_database()
    result = v_d.add_recipe(title, description)
    t_h.delete_temporary_database()
    assert result == expected
# /add
