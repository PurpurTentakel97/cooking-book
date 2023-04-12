#
# Purpur Tentakel
# Cocking Book
# Python 3.11
# 11.04.2023
#

from helper import log
import time

if __name__ == "__main__":
    log.message(log.LogType.INFO, "main.py", "__name__ == __main__()", "info text")
    time.sleep(2)
    log.message(log.LogType.INFO, "main.py", "__name__ == __main__()", "info text")
    time.sleep(2)
    log.message(log.LogType.INFO, "main.py", "__name__ == __main__()", "info text")

    log.export()
