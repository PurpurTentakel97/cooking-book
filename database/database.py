#
# Purpur Tentakel
# Cooking Book
# 12.04.2023
#

import os
import sys
import sqlite3

from helper import log
from helper import dirs

database: "Database"


class Database:
    def __init__(self, test: bool):
        self.OperationalError = sqlite3.OperationalError
        self.IntegrityError = sqlite3.IntegrityError

        # generate connection
        if not test:
            dirs.check_and_make_dir(dirs.DirType.DATABASE)
            my_path = os.path.join(dirs.get_dir_from_file(dirs.FileType.DATABASE), dirs.FileType.DATABASE.value)
        else:
            dirs.check_and_make_dir(dirs.DirType.TEST_DATABASE)
            my_path = os.path.join(dirs.get_dir_from_file(dirs.FileType.TEST_DATABASE),
                                   dirs.FileType.TEST_DATABASE.value)

        if not os.path.exists(my_path):
            log.message(log.LogType.GENERATED, "database.py", "self.__init__()", "generated new database")
        self.connection = sqlite3.connect(my_path)

        self.connection.execute("PRAGMA foreign_keys = ON")
        self.cursor = self.connection.cursor()

        # generate tables
        file = os.path.join(dirs.get_dir_from_enum(dirs.DirType.CONFIG), dirs.FileType.DATABASE_CONFIG.value)
        with open(file) as file:
            try:
                self.cursor.executescript(file.read())
            except self.OperationalError:
                log.message(log.LogType.BREAKING_ERROR, "database.py", "self._create_tables()", sys.exc_info())

        self.connection.commit()

        log.message(log.LogType.INITIALIZED, "database.py", "self.__init__()", "databased initialized")

    def drop_connection(self) -> None:
        self.connection.close()


def create_database(test: bool) -> None:
    global database
    database = Database(test)
