#
# Purpur Tentakel
# Cocking Book
# 12.04.2023
#

import os
from enum import Enum

from helper import log


# @formatter:off
class DirType(Enum):
    SAVES =         "saves"
    LOGS =          "logs"
    DATABASE =      "database"
    TEST_DATABASE = "test_database"
    CONFIG =        "config"


class FileType(Enum):
    LOG_ENDING =      ".CB_LOG"
    DATABASE =        "recipes.CB_DB"
    TEST_DATABASE =   "test_database.CB_DB"
    DATABASE_CONFIG = "create.sql"
# @formatter:on


def get_dir_from_enum(path_type: DirType) -> str:
    match path_type:
        case DirType.SAVES:
            return os.path.join(os.getcwd(), DirType.SAVES.value)
        case DirType.LOGS:
            return os.path.join(os.getcwd(), DirType.SAVES.value, DirType.LOGS.value)
        case DirType.DATABASE:
            return os.path.join(os.getcwd(), DirType.SAVES.value, DirType.DATABASE.value)
        case DirType.TEST_DATABASE:
            return os.path.join(os.getcwd(),DirType.SAVES.value, DirType.TEST_DATABASE.value)
        case DirType.CONFIG:
            return os.path.join(os.getcwd(), DirType.CONFIG.value)


def _create_dir(my_path: str) -> bool:
    if os.path.exists(my_path):
        return True

    os.makedirs(my_path)

    if os.path.exists(my_path):
        log.message(log.LogType.GENERATED, "dirs.py", "_create_dir()", f"generated path '{my_path}'")
        return True
    else:
        log.message(log.LogType.ERROR, "dirs.py", "_create_dir()", f"failed to generate path '{my_path}'")
        return False


def check_and_make_dir(dir_type: DirType) -> bool:
    my_path: str = get_dir_from_enum(dir_type)
    return _create_dir(my_path)


def get_dir_from_file(file_type: FileType) -> str:
    match file_type:
        case FileType.LOG_ENDING:
            return get_dir_from_enum(DirType.LOGS)
        case FileType.DATABASE:
            return get_dir_from_enum(DirType.DATABASE)
        case FileType.TEST_DATABASE:
            return get_dir_from_enum(DirType.TEST_DATABASE)
