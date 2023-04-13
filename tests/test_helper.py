#
# Purpur Tentakel
# Cooking Book
# 12.04.2023
#

import os

from helper import init
from database import add as a
from database import database as d


def move_working_directory() -> None:
    os.chdir("D:\\dev\\py\\cooking-book")


def generate_temporary_database() -> None:
    move_working_directory()
    init.init(":memory:")
    _add_raw_types_to_database()
    _add_recipes_to_database()


def _add_raw_types_to_database() -> None:
    # @formatter:off
    entries: list[str] = [
        "Frühstück"  ,  # 1
        "Mittagessen",  # 2
        "Abendessen" ,  # 3
    ]
    # @formatter: on

    for value in entries:
        a.add.add_raw_type(value)


def _add_recipes_to_database() -> None:
    # @formatter:off
    entries: list[list[str, ...]] = [
        ["Nudelauflauf",  "Beschreibung 1"],  # 1
        ["Braten",        "Beschreibung 2"],  # 2
        ["Schokopudding", "Beschreibung 3"],  # 3
        ["Salat",         "Beschreibung 4"],  # 4
        ["Brot",          "Beschreibung 5"],  # 5
    ]
    # @formatter:on

    for title, description in entries:
        a.add.add_recipe(title, description)


def delete_temporary_database() -> None:
    d.database.drop_connection()
