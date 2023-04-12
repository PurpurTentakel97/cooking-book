#
# Purpur Tentakel
# Cocking Book
# Python 3.11
# 11.04.2023
#

from helper import init
from database import add as a
from database import update as u

if __name__ == "__main__":
    init.init()

    a.add.add_raw_type("Frühstück")
    a.add.add_raw_type("Mittagessen")
    a.add.add_raw_type("Abendessen")

    u.update.update_raw_type_by_ID(1, "Nachtisch")
    u.update.update_raw_type_by_name("Mittagessen", "Nachtisch")
    u.update.update_raw_type_by_name("Mittagessen", "Braten")
