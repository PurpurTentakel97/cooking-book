#
# Purpur Tentakel
# Cooking Book
# 12.04.2023
#

from database import database
from database import add
from database import select
from database import update
from database import delete


def init(my_path: str):
    database.create_database(my_path)
    add.create_add(database.database)
    select.create_select(database.database)
    update.create_update(database.database)
    delete.create_delete(database.database)
