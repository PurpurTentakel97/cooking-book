#
# Purpur Tentakel
# Cocking Book
# Python 3.11
# 11.04.2023
#

import time

from helper import log
from helper import init

if __name__ == "__main__":
    init.init()

    log.message(log.LogType.INFO, "main.py", "__name__ == __main__()", "info text")
    time.sleep(2)
    log.message(log.LogType.INFO, "main.py", "__name__ == __main__()", "info text")
    time.sleep(2)
    log.message(log.LogType.INFO, "main.py", "__name__ == __main__()", "info text")

    log.export()
