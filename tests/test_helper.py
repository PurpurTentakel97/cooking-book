#
# Purpur Tentakel
# Cooking Book
# 12.04.2023
#

import os

from helper import init
from database import add as a
from database import database as d

# @formatter:off
entries: dict = {
    "raw_types": [
        "Frühstück"  ,  # 1
        "Mittagessen",  # 2
        "Abendessen" ,  # 3
    ],
    "recipes": [
        ["Nudelauflauf",  "Beschreibung 1"],  # 1
        ["Braten",        "Beschreibung 2"],  # 2
        ["Schokopudding", "Beschreibung 3"],  # 3
        ["Salat",         "Beschreibung 4"],  # 4
        ["Brot",          "Beschreibung 5"],  # 5
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
    ]
}
# @formatter: on


def move_working_directory() -> None:
    os.chdir("D:\\dev\\py\\cooking-book")


def generate_temporary_database() -> None:
    move_working_directory()
    init.init(":memory:")
    _add_raw_types_to_database()
    _add_recipes_to_database()
    _add_ingredients_to_database()


def _add_raw_types_to_database() -> None:
    for value in entries["raw_types"]:
        a.add.add_raw_type(value)


def _add_recipes_to_database() -> None:
    for title, description in entries["recipes"]:
        a.add.add_recipe(title, description)


def _add_ingredients_to_database() -> None:
    for recipe_id, amount, unit, ingredient in entries["ingredients"]:
        a.add.add_ingredient(recipe_id, amount, unit, ingredient)


def delete_temporary_database() -> None:
    d.database.drop_connection()
    d._uncreate_database()
