#
# Purpur Tentakel
# Cooking Book
# Python 3.11
# 11.04.2023
#

from helper import init, dirs
import os

if __name__ == "__main__":
    init.init(os.path.join(dirs.get_dir_from_enum(dirs.DirType.DATABASE), dirs.FileType.DATABASE.value))
