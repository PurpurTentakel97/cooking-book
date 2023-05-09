#
# Purpur Tentakel
# Cooking Book
# 12.04.2023
#

import os

from helper import log
from helper import init
from database import add as a
from database import my_database as d
from UI import MyUI

# database
# @formatter:off
entries: dict = {
    "raw_types": [
        "Frühstück"  ,  # 1
        "Mittagessen",  # 2
        "Abendessen" ,  # 3
    ],
    "recipes": [
        ["Nudelauflauf",  "Beschreibung 1", 2,  6 ],  # 1
        ["Braten",        "Beschreibung 2", 10, 60],  # 2
        ["Schokopudding", "Beschreibung 3", 30, 50],  # 3
        ["Salat",         "Beschreibung 4", 10, 15],  # 4
        ["Brot",          "Beschreibung 5", 10, 9 ],  # 5
    ],
    "ingredients": [
        [1, 500.0, "g",  "Nudeln"           ],  # 1
        [1, 500.0, "ml", "passierte Tomaten"],  # 2
        [1, 2.0,   "",   "Tomaten"          ],  # 3

        [2, 500.0, "g", "Hackfleisch" ],  # 4
        [2, 3.5,   "",  "Brötchen"    ],  # 5
        [2, 5.0,   "",  "Eier"        ],  # 6

        [3, 150.0, "ml", "Milch"          ],  # 7
        [3, 50.0,  "g",  "Pudding Pulver" ],  # 8

        [4, 1.0,   "",   "Salat" ],  # 9
        [4, 100.0, "ml", "Öl"    ],  # 10
        [4, 10.6,  "ml", "Essig" ],  # 11

        [5, 1000.0, "g",  "Mehl"         ],  # 12
        [5, 600.0,  "ml", "Wasser"       ],  # 13
        [5, 10.5,   "g",  "Trocken Hefe" ],  # 14
    ],
    "types": [
        [1, 2],  #  1  Nudelauflauf    Mittagessen
        [1, 3],  #  2  Nudelauflauf    Abendessen
        [2, 2],  #  3  Braten          Mittagessen
        [2, 3],  #  4  Braten          Abendessen
        [3, 3],  #  5  Schokopuddung   Abendessen
        [3, 1],  #  6  Schokopudding   Frühstück
        [4, 1],  #  7  Salat           Frühstück
        [4, 2],  #  8  Salat           Mittagessen
        [5, 1],  #  9  Brot            Frühstück
        [5, 3],  # 10  Brot            Abendessen
    ]
}
# @formatter: on


def _move_working_directory() -> None:
    os.chdir("D:/dev/py/cooking-book")


def generate_temporary_database() -> None:
    _move_working_directory()
    log._set_exporting(False)
    init.data_init(":memory:")
    _add_raw_types_to_database()
    _add_recipes_to_database()
    _add_ingredients_to_database()
    _add_types_to_database()


def _add_raw_types_to_database() -> None:
    for value in entries["raw_types"]:
        a.add.add_raw_type(value)


def _add_recipes_to_database() -> None:
    for title, description, standard_serving_count, scale_serving_count in entries["recipes"]:
        a.add.add_recipe(title, description, standard_serving_count, scale_serving_count)


def _add_ingredients_to_database() -> None:
    for recipe_id, amount, unit, ingredient in entries["ingredients"]:
        a.add.add_ingredient(recipe_id, amount, unit, ingredient)


def _add_types_to_database() -> None:
    for recipe_ID, raw_type_ID in entries["types"]:
        a.add.add_type(recipe_ID, raw_type_ID)


def delete_temporary_database() -> None:
    d.database.drop_connection()
    d._uncreate_database()


# UI
def generate_main_window() -> None:
    MyUI.create_application()
    MyUI.create_window()
    MyUI.start_application()


def shut_down_UI() -> None:
    MyUI.shut_down_application()

