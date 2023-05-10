#
# Purpur Tentakel
# Cocking Book
# 04.05.2023
#

import os
from pdf import recipePDF as rP
from helper import log, dirs, return_message

_recipe_pdf: rP.RecipePDF | None = None


def _check_recipe_pdf() -> None:
    global _recipe_pdf
    if not _recipe_pdf:
        _recipe_pdf = rP.RecipePDF()


def _get_export_file(my_path: str) -> return_message.ReturnMessage:
    if not my_path:
        log.message(log.LogType.ERROR, "pdfHandler.py", "export_recipe()", "no path provided")
        return return_message.ReturnMessageNone(False)

    _, file_name = os.path.split(my_path)
    result = file_name.split('.')

    if len(result) == 0:
        log.message(log.LogType.ERROR, "pdfHandler.py", "export_recipe()", "no arguments for filename")
        return return_message.ReturnMessageNone(False)
    elif len(result) == 1:
        file_name = file_name + dirs.FileType.EXPORT.value
    elif len(result) == 2:
        name, _type = result
        _type = '.' + _type
        if not _type == dirs.FileType.EXPORT.value:
            log.message(log.LogType.ERROR, "pdfHandler.py", "export_recipe()", "wrong ending for recipe pdf")
            return return_message.ReturnMessageNone(False)
    if len(result) > 2:
        log.message(log.LogType.ERROR, "pdfHandler.py", "export_recipe()", "too many arguments in filename")
        return return_message.ReturnMessageNone(False)

    return return_message.ReturnMessageStr(file_name, True)


def export_recipe(ID: int, my_path: str) -> bool:
    _check_recipe_pdf()

    result = _get_export_file(my_path)
    if not result.valid:
        return False
    file_name: str = result.entry
    dirs.check_and_make_dir(dirs.DirType.EXPORT)

    return _recipe_pdf.export(dirs.get_dir_from_file(dirs.FileType.EXPORT), file_name, ID)


def open_pdf() -> bool:
    if not _recipe_pdf:
        return False

    return _recipe_pdf.open_last_export()
