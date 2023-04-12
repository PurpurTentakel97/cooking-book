#
# Purpur Tentakel
# Cocking Book
# Python 3.11
# 11.04.2023
#

import time

from helper import log
from database import database

if __name__ == "__main__":
    database.create_database()

    log.message(log.LogType.INFO, "main.py", "__name__ == __main__()", "info text")
    time.sleep(2)
    log.message(log.LogType.INFO, "main.py", "__name__ == __main__()", "info text")
    time.sleep(2)
    log.message(log.LogType.INFO, "main.py", "__name__ == __main__()", "info text")

    log.export()
