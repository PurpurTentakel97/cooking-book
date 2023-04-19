#
# Purpur Tentakel
# Cocking Book
# 18.04.2023
#

import sys
from PyQt5.QtWidgets import QApplication
from UI.MyWindow import MyWindow

app: "QApplication"
window: "MyWindow"


def create_application() -> None:
    global app
    app = QApplication(sys.argv)


def create_window() -> None:
    global window
    window = MyWindow()


def start_application() -> None:
    global app
    app.exec()
