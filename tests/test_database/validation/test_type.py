#
# Purpur Tentakel
# Cooking Book
# 15.04.2023
#

import pytest

from validation import v_database as v_d
from tests.test_fixtures import database_fixture


# select
@pytest.mark.parametrize(("ID", "expected"), [
    # @formatter:off
    (1,  True ),  # ID is existing
    (20, False),  # ID not existing
    # @formatter:on
])
def test_check_select_type_by_ID(ID, expected, database_fixture) -> None:
    result = v_d.check_select_type_by_ID(ID)
    assert result == expected


@pytest.mark.parametrize(("recipe_ID", "expected"), [
    # @formatter:off
    (1,  True ),  # recipe ID is existing
    (20, False),  # recipe ID not existing

    # @formatter:on
])
def test_check_select_type_by_recipe_ID(recipe_ID, expected, database_fixture) -> None:
    result = v_d.check_select_type_by_recipe_ID(recipe_ID)
    assert result == expected


@pytest.mark.parametrize(("raw_type_ID", "expected"), [
    # @formatter:off
    (1,  True ),  # raw type ID is existing
    (20, False),  # raw type ID not existing
    # @formatter:on
])
def test_check_select_type_by_raw_type_ID(raw_type_ID, expected, database_fixture) -> None:
    result = v_d.check_select_type_by_raw_type_ID(raw_type_ID)
    assert result == expected


# /select
# add

@pytest.mark.parametrize(("recipe_ID", "raw_type_ID", "expected"), [
    # @formatter:off
    (1,  1,  True ),  # ID are existing and available (Nudelauflauf Frühstück)
    (20, 1,  False),  # recipe ID not existing  (?, Frühstück)
    (1,  20, False),  # raw_type_ID not existing (Nudelauflauf, ?)
    (1,  2,  False),  # IDs already existing (Nudelauflauf, Mittagessen)
    # @formatter:on
])
def test_check_add_type(recipe_ID, raw_type_ID, expected, database_fixture) -> None:
    result = v_d.check_add_type(recipe_ID, raw_type_ID)
    assert result == expected


# /add

# update
# no update functions to test
# /update

# delete

@pytest.mark.parametrize(("ID", "expected"), [
    # @formatter:off
    (1,  True ),  # ID is existing
    (20, False),  # ID not existing
    # @formatter:on
])
def test_check_delete_type_by_ID(ID, expected, database_fixture) -> None:
    result = v_d.check_delete_type_by_ID(ID)
    assert result == expected


@pytest.mark.parametrize(("recipe_ID", "expected"), [
    # @formatter:off
    (1,  True ),  # recipe ID is existing
    (20, False),  # recipe ID not existing
    # @formatter:on
])
def test_check_delete_type_by_recipe_ID(recipe_ID, expected, database_fixture) -> None:
    result = v_d.check_delete_type_by_recipe_ID(recipe_ID)
    assert result == expected


@pytest.mark.parametrize(("raw_type_ID", "expected"), [
    # @formatter:off
    (1,  True ),  # raw type ID is existing
    (20, False),  # raw type ID not existing
    # @formatter:on
])
def test_check_delete_type_by_raw_type_ID(raw_type_ID, expected, database_fixture) -> None:
    result = v_d.check_delete_type_by_raw_type_ID(raw_type_ID)
    assert result == expected


@pytest.mark.parametrize(("recipe_ID", "raw_type_ID", "expected"), [
    # @formatter:off
    (1,  2,  True ),  # IDs are existing
    (20, 2,  False),  # recipe ID not existing
    (1,  20, False),  # raw type ID not existing
    (1,  1,  False),  # type with these IDs not existing
    # @formatter:on
])
def test_check_delete_type_by_recipe_ID_and_raw_type_ID(recipe_ID, raw_type_ID, expected, database_fixture) -> None:
    result = v_d.check_delete_type_by_recipe_ID_and_raw_type_ID(recipe_ID, raw_type_ID)
    assert result == expected

# /delete
