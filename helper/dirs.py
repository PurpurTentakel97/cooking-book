#
# Purpur Tentakel
# Cocking Book
# 12.04.2023
#

import os
from enum import Enum

import helper.log as log


class DirType(Enum):
    SAVES = "saves"
    LOGS = "logs"


class FileType(Enum):
    LOG = ".log"


def _get_dir_from_enum(path_type: DirType) -> str:
    match path_type:
        case DirType.SAVES:
            return f"{DirType.SAVES.value}"
        case DirType.LOGS:
            return f"{DirType.SAVES.value}/{DirType.LOGS.value}"


def _crate_dir(my_path: str) -> bool:

    if os.path.exists(my_path):
        return True

    os.makedirs(my_path)

    if os.path.exists(my_path):
        log.message(log.LogType.INFO, "dirs.py", "_create_dir", f"generated path \"{my_path}\"")
        return True
    else:
        log.message(log.LogType.ERROR, "dirs.py", "_create_dir", f"failed to generate path \"{my_path}\"")
        return False


def check_and_make_dir(dir_type: DirType) -> bool:
    my_path: str = _get_dir_from_enum(dir_type)
    return _crate_dir(my_path)
