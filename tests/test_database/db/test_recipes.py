#
# Purpur Tentakel
# Cooking Book
# 13.04.2023
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
    ([
        [1, "Nudelauflauf",  "Beschreibung 1", 2,  6  ],
        [2, "Braten",        "Beschreibung 2", 10, 60 ],
        [3, "Schokopudding", "Beschreibung 3", 30, 50 ],
        [4, "Salat",         "Beschreibung 4", 10, 15 ],
        [5, "Brot",          "Beschreibung 5", 10, 9  ],  # all data the database should have
    ]),
    # @formatter:on
])
def test_select_all_recipes(data, database_fixture) -> None:
    data.sort(key=lambda x: x[1])
    result = s.select.select_all_recipes()

    assert result.valid
    for (s_ID, s_title, s_description, s_st_serving_count, s_scale_serving_count), (
            ID, title, description, st_serving_count, scale_serving_count) in zip(result.entry, data):
        assert s_ID == ID
        assert s_title == title
        assert s_description == description
        assert s_st_serving_count == st_serving_count
        assert s_scale_serving_count == scale_serving_count


@pytest.mark.parametrize(("ID", "title", "description", "standard_serving_count", "scale_serving_count", "expected"), [
    # @formatter:off
    (1,  "Nudelauflauf", "Beschreibung 1", 2,  6,  True ),  # ID is existing
    (20, "",             "",               0,  0,  False),  # ID not existing
    # @formatter:on
])
def test_select_recipe_by_ID(ID, title, description, standard_serving_count, scale_serving_count, expected,
                             database_fixture) -> None:
    result = s.select.select_recipe_by_ID(ID)

    assert result.valid == expected
    if expected:
        s_ID, s_title, s_description, s_standard_serving_count, s_scale_serving_count = result.entry
        assert s_ID == ID
        assert s_title == title
        assert s_description == description
        assert s_standard_serving_count == standard_serving_count
        assert s_scale_serving_count == scale_serving_count


# @formatter:off
@pytest.mark.parametrize(("ID", "title", "description", "standard_serving_count", "scale_serving_count","expected"), [
    # @formatter:off
    (1,  "Nudelauflauf",     "Beschreibung 1", 2,  6, True  ),  # title is existing
    (1,  "  Nudelauflauf  ", "Beschreibung 1", 2,  6, True  ),  # title is existing with stripping
    (1,  "Lasagne",          "",               0,  0, False ),  # title not existing
    # @formatter:on
])
def test_select_recipe_by_title(ID, title, description, standard_serving_count, scale_serving_count, expected,
                                database_fixture) -> None:
    result = s.select.select_recipe_by_title(title)

    assert result.valid == expected
    if expected:
        s_ID, s_title, s_description, s_standard_serving_count, s_scale_serving_count = result.entry
        assert s_ID == ID
        assert s_title == title.strip()
        assert s_description == description
        assert s_standard_serving_count == standard_serving_count
        assert s_scale_serving_count == scale_serving_count


# /select

# add

@pytest.mark.parametrize(("ID", "title", "description", "standard_serving_count", "scale_serving_count", "expected"), [
    # @formatter:off
    (6, "Lasagne",          "Beschreibung 6", 10, 10,  True  ),  # new title and description
    (6, "Lasagne",          "Beschreibung 1", 20, 5,   True  ),  # new title
    (6, "Nudelauflauf",     "Beschreibung 6", 3,  10,  False ),  # title already existing
    (6, "  Nudelauflauf  ", "Beschreibung 6", 5,  20,  False ),  # title already existing with stripping
    (6, "Lasagne",          "",               10, 5,   False ),  # no description
    (6, "",                 "Beschreibung 6", 20, 50,  False ),  # no title
    # @formatter:on
])
def test_add_recipe(ID, title, description, expected, standard_serving_count, scale_serving_count,
                    database_fixture) -> None:
    result = a.add.add_recipe(title, description, standard_serving_count, scale_serving_count)

    assert result.valid == expected
    if expected:
        s_result = s.select.select_recipe_by_ID(result.entry)
        assert s_result.valid
        s_ID, s_title, s_description, s_standard_serving_count, s_scale_serving_count = s_result.entry
        assert s_ID == ID
        assert s_title == title.strip()
        assert s_description == description
        assert s_standard_serving_count == standard_serving_count
        assert s_scale_serving_count == scale_serving_count


# /add
# update
@pytest.mark.parametrize(("ID", "title", "description", "standard_serving_count", "scale_serving_count", "expected"), [
    # @formatter:off
    (1,  "Nachtisch",    "Beschreibung 6", 2,    6,       True ),  # new title and new description
    (1,  "Nachtisch",    "Beschreibung 1", 2,    6,       True ),  # new title
    (1,  "Nudelauflauf", "Beschreibung 6", 2,    6,       True ),  # new description
    (20, "test",         "test",           0,    0,       False),  # ID not existing
    (1,  "Braten",       "Beschreibung 1", 2,    6,       False),  # title already existing
    (1,  "  Braten  ",   "Beschreibung 1", 2,    6,       False),  # title already existing with stripping
    (1,  "Nudelauflauf", "",               2,    6,       False),  # no description
    (1,  "",             "Beschreibung 1", 2,    6,       False),  # no title
    (1,  "Nachtisch",    "Beschreibung 6", -3.0, 6,       False),  # wrong datatype
    (1,  "Nachtisch",    "Beschreibung 6", 2,    "str()", False),  # wrong datatype

    # @formatter:on
])
def test_update_recipe_by_ID(ID, title, description, standard_serving_count, scale_serving_count, expected,
                             database_fixture) -> None:
    result = u.update.update_recipe_by_ID(ID, title, description, standard_serving_count, scale_serving_count)
    s_result = s.select.select_recipe_by_ID(ID)

    assert result.valid == expected

    if expected:
        s_ID, s_title, s_description, s_standard_serving_count, s_scale_serving_count = s_result.entry
        assert s_ID == ID
        assert s_title == title.strip()
        assert s_description == description
        assert s_standard_serving_count == standard_serving_count
        assert s_scale_serving_count == scale_serving_count


@pytest.mark.parametrize(
    ("old_title", "new_title", "description", "standard_serving_count", "scale_serving_count", "expected"), [
        # @formatter:off
    ("Nudelauflauf",   "Nachtisch",    "Beschreibung 6", 2,    6,       True ),  # new description and new title
    ("Nudelauflauf",   "Nachtisch",    "Beschreibung 1", 2,    6,       True ),  # new title
    (" Nudelauflauf ", "Nachtisch",    "Beschreibung 1", 2,    6,       True ),  # new title with stripping
    ("Nudelauflauf",   "Nudelauflauf", "Beschreibung 6", 2,    6,       True ),  # new description
    ("Nachtisch",      "test",         "test",           2,    6,       False),  # old title not existing
    ("Nudelauflauf",   "Braten",       "test",           2,    6,       False),  # new title already existing
    ("Nudelauflauf",   "  Braten  ",   "test",           2,    6,       False),  # new title already existing with stripping
    ("Nudelauflauf",   "",             "test",           2,    6,       False),  # no new title
    ("Nudelauflauf",   "Nachtisch",    "",               0,    0,       False),  # no description
    ("Nudelauflauf",   "Nachtisch",    "Beschreibung 6", -3.0, 6,       False),  # wrong datatype
    ("Nudelauflauf",   "Nachtisch",    "Beschreibung 6", 2,    "str()", False),  # wrong datatype

    # @formatter:on
    ])
def test_update_recipe_by_title(old_title, new_title, description, standard_serving_count, scale_serving_count,
                                expected, database_fixture) -> None:
    result = u.update.update_recipe_by_title(old_title, new_title, description, standard_serving_count,
                                             scale_serving_count)
    s_result = s.select.select_recipe_by_title(new_title)

    assert result.valid == expected

    if expected:
        _, s_title, s_description, s_standard_serving_count, s_scale_serving_count = s_result.entry
        assert s_title == new_title.strip()
        assert s_description == description
        assert s_standard_serving_count == standard_serving_count
        assert s_scale_serving_count == scale_serving_count


# /update

# delete
@pytest.mark.parametrize(("ID", "expected"), [
    # @formatter:off
    (1,  True ),  # ID is existing
    (20, False),  # ID not existing
    # @formatter:on
])
def test_delete_recipe_by_ID(ID, expected, database_fixture) -> None:
    result = d.delete.delete_recipe_by_ID(ID)
    s_result = s.select.select_recipe_by_ID(ID)

    assert result.valid == expected

    if expected:
        assert not s_result.valid


@pytest.mark.parametrize(("title", "expected"), [
    # @formatter:off
    ("Nudelauflauf",   True ),  # title is existing
    (" Nudelauflauf ", True ),  # stripping
    ("Nachtisch",      False),  # title not existing
    # @formatter:on
])
def test_delete_recipe_by_title(title, expected, database_fixture) -> None:
    result = d.delete.delete_recipe_by_title(title)
    s_result = s.select.select_recipe_by_title(title)

    assert result.valid == expected

    if expected:
        assert not s_result.valid

# /delete
