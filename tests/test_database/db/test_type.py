#
# Purpur Tentakel
# Cooking Book
# 15.04.2023
#

import pytest

from database import add as a
from database import update as u
from database import delete as d
from database import select as s
from tests.test_fixtures import database_fixture


# select
@pytest.mark.parametrize("data", [
    # @formatter:off
    [[1,  1, 2],     #  1  Nudelauflauf    Mittagessen
     [2,  1, 3],     #  2  Nudelauflauf    Abendessen
     [3,  2, 2],     #  3  Braten          Mittagessen
     [4,  2, 3],     #  4  Braten          Abendessen
     [5,  3, 3],     #  5  Schokopuddung   Abendessen
     [6,  3, 1],     #  6  Schokopudding   Frühstück
     [7,  4, 1],     #  7  Salat           Frühstück
     [8,  4, 2],     #  8  Salat           Mittagessen
     [9,  5, 1],     #  9  Brot            Frühstück
     [10, 5, 3], ],  # 10  Brot            Abendessen
    # @formatter:on
])
def test_select_all_types(data, database_fixture) -> None:
    data.sort(key=lambda x: x[1])

    result = s.select.select_all_types()
    assert result.valid

    for (s_ID, s_recipe_ID, s_raw_type_ID), (p_ID, p_recipe_ID, p_raw_type_ID) in zip(result.entry, data):
        assert s_ID == p_ID
        assert s_recipe_ID == p_recipe_ID
        assert s_raw_type_ID == p_raw_type_ID


@pytest.mark.parametrize(("ID", "recipe_ID", "raw_type_ID", "expected"), [
    # @formatter:off
    (1,  1, 2, True ),  # ID is existing
    (20, 0, 0, False),  # ID not existing
    # @formatter:on
])
def test_select_type_by_ID(ID, recipe_ID, raw_type_ID, expected, database_fixture) -> None:
    result = s.select.select_type_by_ID(ID)
    assert result.valid == expected

    if expected:
        s_ID, s_recipe_ID, s_raw_type_ID = result.entry
        assert s_ID == ID
        assert s_recipe_ID == recipe_ID
        assert s_raw_type_ID == raw_type_ID


@pytest.mark.parametrize(("recipe_ID", "expected"), [
    # @formatter:off
    (1,  True ),  # recipe ID is existing
    (20, False),  # recipe ID not existing
    # @formatter:on
])
def test_select_type_by_recipe_ID(recipe_ID, expected, database_fixture) -> None:
    result = s.select.select_type_by_recipe_ID(recipe_ID)
    assert result.valid == expected

    if expected:
        for _, s_recipe_ID, _ in result.entry:
            assert s_recipe_ID == recipe_ID


@pytest.mark.parametrize(("raw_type_ID", "expected"), [
    # @formatter:off
    (1,  True ),  # raw type ID is existing
    (20, False),  # raw type ID not existing
    # @formatter:on
])
def test_select_type_by_raw_type_ID(raw_type_ID, expected, database_fixture) -> None:
    result = s.select.select_type_by_raw_type_ID(raw_type_ID)
    assert result.valid == expected

    if expected:
        for _, _, s_raw_type_ID in result.entry:
            assert s_raw_type_ID == raw_type_ID


# /select
# add

@pytest.mark.parametrize(("recipe_ID", "raw_type_ID", "expected"), [
    # @formatter:off
    (1,  1,  True ),  # new IDs
    (20, 1,  False),  # recipe ID not existing
    (1,  20, False),  # raw type ID not existing
    (1,  2,  False),  # entry already existing
    # @formatter:on
])
def test_add_type(recipe_ID, raw_type_ID, expected, database_fixture) -> None:
    result = a.add.add_type(recipe_ID, raw_type_ID)
    assert result.valid == expected

    if expected:
        s_result = s.select.select_type_by_ID(result.entry)
        assert s_result.valid
        s_ID, s_recipe_ID, s_raw_type_ID = s_result.entry
        assert s_ID == result.entry
        assert s_recipe_ID == recipe_ID
        assert s_raw_type_ID == raw_type_ID


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
def test_delete_type_by_ID(ID, expected, database_fixture) -> None:
    result = d.delete.delete_type_by_ID(ID)
    assert result.valid == expected

    if expected:
        s_result = s.select.select_type_by_ID(ID)
        assert not s_result.valid


@pytest.mark.parametrize(("recipe_ID", "expected"), [
    # @formatter:off
    (1,  True ),  # recipe ID is existing
    (20, False),  # recipe ID not existing
    # @formatter:on
])
def test_delete_type_by_recipe_ID(recipe_ID, expected, database_fixture) -> None:
    result = d.delete.delete_type_by_recipe_ID(recipe_ID)
    assert result.valid == expected

    if expected:
        s_result = s.select.select_all_types()
        assert s_result.valid

        for _, s_recipe_ID, _ in s_result.entry:
            assert s_recipe_ID != recipe_ID


@pytest.mark.parametrize(("raw_type_ID", "expected"), [
    # @formatter:off
    (1,  True ),  # raw type ID is existing
    (20, False),  # raw type ID not existing
    # @formatter:on
])
def test_delete_type_by_raw_type_ID(raw_type_ID, expected, database_fixture) -> None:
    result = d.delete.delete_type_by_raw_type_ID(raw_type_ID)
    assert result.valid == expected

    if expected:
        s_result = s.select.select_all_types()
        assert s_result.valid

        for _, _, s_raw_type_ID in s_result.entry:
            assert s_raw_type_ID != raw_type_ID


@pytest.mark.parametrize(("recipe_ID", "raw_type_ID", "expected"), [
    # @formatter:off
    (1,  2,  True ),  # Entry with IDs existing
    (20, 2,  False),  # recipe ID not existing
    (1,  20, False),  # raw type ID not existing
    (1,  1,  False),  # Entry with IDs not existing
    # @formatter:on
])
def test_delete_type_by_recipe_ID_and_raw_type_ID(recipe_ID, raw_type_ID, expected, database_fixture) -> None:
    result = d.delete.delete_type_by_recipe_ID_and_raw_type_ID(recipe_ID, raw_type_ID)
    assert result.valid == expected

    if expected:
        s_result = s.select.select_all_types()
        assert s_result.valid

        for _, s_recipe_ID, s_raw_type_ID in s_result.entry:
            assert s_recipe_ID != recipe_ID or s_raw_type_ID != raw_type_ID

# /delete
