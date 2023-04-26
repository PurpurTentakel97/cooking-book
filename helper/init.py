#
# Purpur Tentakel
# Cooking Book
# 12.04.2023
#

from database import my_database
from database import add
from database import select
from database import update
from database import delete
from UI import MyUI


def init(my_path: str):
    my_database.create_database(my_path)
    add.create_add(my_database.database)
    select.create_select(my_database.database)
    update.create_update(my_database.database)
    delete.create_delete(my_database.database)
    MyUI.create_application()
    MyUI.create_window()
    MyUI.start_application()
