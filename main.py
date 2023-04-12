#
# Purpur Tentakel
# Cocking Book
# Python 3.11
# 11.04.2023
#

import helper.log as log

if __name__ == "__main__":
    print("// logging...")
    log.message(log.LogType.DEBUG, "main.py", "__main__", "Debugging message")
    log.message(log.LogType.INFO, "main.py", "__main__", "Testing message")
    log.message(log.LogType.SAVED, "main.py", "__main__", "Saving message")
    log.message(log.LogType.LOADED, "main.py", "__main__", "Loading message")
    log.message(log.LogType.BREAKING_ERROR, "main.py", "__main__", "Breaking Error message")
    log.message(log.LogType.ERROR, "main.py", "__main__", "Error message")
    log.message(log.LogType.EXPECTED_ERROR, "main.py", "__main__", "Expected Error message")

    print("// \"exporting...\"")
    log.export()