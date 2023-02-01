from PyQt6.QtWidgets import QMessageBox, QWidget


class ValueErrorPopup(QMessageBox):
    def __init__(self, parent: QWidget, title: str = "値エラー", content: str = "入力値が正しくありません"):
        super().__init__()
        super().warning(parent, title, content)
