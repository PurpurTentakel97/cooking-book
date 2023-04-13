#
# Purpur Tentakel
# Cooking Book
# Python 3.11
# 11.04.2023
#

import os

from helper import init
from helper import dirs
from database import add as a
from database import update as u
from database import delete as d

if __name__ == "__main__":
    init.init(os.path.join(dirs.get_dir_from_file(dirs.FileType.DATABASE), dirs.FileType.DATABASE.value))

    a.add.add_raw_type("Frühstück")
    a.add.add_raw_type("Mittagessen")
    a.add.add_raw_type("Abendessen")

    u.update.update_raw_type_by_ID(1, "Nachtisch")
    u.update.update_raw_type_by_name("Mittagessen", "Nachtisch")
    u.update.update_raw_type_by_name("Mittagessen", "Braten")

    d.delete.delete_raw_type_by_ID(1)
    d.delete.delete_raw_type_by_name("Abendessen")
