#
# Purpur Tentakel
# Cocking Book
# 18.04.2023
#

from PyQt5.QtWidgets import QMainWindow


class MyWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Cooking Book - Purpur Tentakel")
        self.setMinimumSize(1280, 720)
        self.showMaximized()
        self.show()
