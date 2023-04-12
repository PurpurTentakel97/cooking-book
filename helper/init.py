#
# Purpur Tentakel
# Cocking Book
# 12.04.2023
#

from database import database
from database import add
from database import select
from database import update


def init():
    database.create_database()
    add.create_add(database.database)
    select.create_select(database.database)
    update.create_update(database.database)
