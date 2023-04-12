#
# Purpur Tentakel
# Cocking Book
# 12.04.2023
#

import sqlite3
import os
import sys

from helper import log
from helper import dirs

database: "Database"


class Database:
    def __init__(self):
        self.OperationalError = sqlite3.OperationalError
        self.IntegrityError = sqlite3.IntegrityError

        # generate connection
        dirs.check_and_make_dir(dirs.DirType.DATABASE)

        self.connection = sqlite3.connect(
            os.path.join(dirs.get_dir_from_file(dirs.FileType.DATABASE), dirs.FileType.DATABASE.value))

        self.connection.execute("PRAGMA foreign_keys = ON")
        self.cursor = self.connection.cursor()

        # generate tables
        with open(
                os.path.join(dirs.get_dir_from_enum(dirs.DirType.CONFIG), dirs.FileType.DATABASE_CONFIG.value)) as file:
            try:
                self.cursor.executescript(file.read())
            except self.OperationalError:
                log.message(log.LogType.BREAKING_ERROR, "database.py", "self._create_tables()", sys.exc_info())

        self.connection.commit()

        log.message(log.LogType.INITIALIZED, "database.py", "self.__init__()", "databased initialized")

    def drop_connection(self) -> None:
        self.connection.close()


def create_database() -> None:
    global database
    database = Database()
