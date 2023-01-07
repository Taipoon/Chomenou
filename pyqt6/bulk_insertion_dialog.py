import os

from PyQt6 import uic
from PyQt6.QtWidgets import QDialog


class BulkInsertionDialog(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.join(os.path.dirname(__file__), "ui_files", "accountsEditorDialog.ui"), self)
        self._bind()

    def _bind(self):
        pass
