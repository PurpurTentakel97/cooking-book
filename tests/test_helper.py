#
# Purpur Tentakel
# Cocking Book
# 12.04.2023
#

import os
import shutil

from helper import init
from helper import dirs
from database import add as a
from database import database as d


def move_working_directory() -> None:
    os.chdir("D:\\dev\\py\\cocking-book")


def generate_temporary_database() -> None:
    move_working_directory()
    init.init(test=True)
    _add_raw_types_to_database()


def _add_raw_types_to_database() -> None:
    entries: list[str] = [
        "Frühstück",
        "Mittagessen",
        "Abendessen",
    ]

    for value in entries:
        a.add.add_raw_type(value)


def delete_temporary_database() -> None:
    d.database.drop_connection()
    my_path = dirs.get_dir_from_file(dirs.FileType.TEST_DATABASE)
    shutil.rmtree(my_path)
