#
# Purpur Tentakel
# Cocking Book
# 18.04.2023
#

import sys
from PyQt5.QtWidgets import QApplication
from UI.MainWindow import MainWindow

app: "QApplication"
window: "MainWindow"


def create_application() -> None:
    global app
    app = QApplication(sys.argv)


def create_window() -> None:
    global window
    window = MainWindow()


def start_application() -> None:
    global app
    app.exec()
