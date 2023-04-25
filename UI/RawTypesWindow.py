#
# Purpur Tentakel
# Cocking Book
# 25.04.2023
#

from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QListWidget, QListWidgetItem, QHBoxLayout, QVBoxLayout


class RawTypesWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self._initialize()
        self._setLayout()

    def _initialize(self) -> None:
        self.setWindowTitle("types")
        self._input: QLineEdit = QLineEdit()
        self._input.setPlaceholderText("type")

        self._accept_btn: QPushButton = QPushButton("accept")
        self._cancel_btn: QPushButton = QPushButton("cancel")

        self._list: QListWidget = QListWidget()

    def _setLayout(self) -> None:
        global_vbox: QVBoxLayout = QVBoxLayout()
        global_vbox.addWidget(self._input)

        btn_hbox: QHBoxLayout = QHBoxLayout()
        btn_hbox.addWidget(self._cancel_btn)
        btn_hbox.addWidget(self._accept_btn)

        global_vbox.addLayout(btn_hbox)
        global_vbox.addWidget(self._list)

        self.setLayout(global_vbox)
        self.show()
