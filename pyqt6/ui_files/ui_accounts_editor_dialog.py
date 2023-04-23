# Form implementation generated from reading ui file 'accountsEditorDialog.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_AccountsEditorDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("AccountsEditorDialog")
        self.resize(324, 278)
        self.setMinimumSize(QtCore.QSize(324, 278))
        self.setMaximumSize(QtCore.QSize(324, 278))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.setFont(font)
        self._label = QtWidgets.QLabel(self)
        self._label.setGeometry(QtCore.QRect(12, 12, 286, 18))
        self._label.setObjectName("_label")
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(6, 227, 155, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.StandardButton.Cancel | QtWidgets.QDialogButtonBox.StandardButton.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.label_oshibori_yen = QtWidgets.QLabel(self)
        self.label_oshibori_yen.setGeometry(QtCore.QRect(220, 70, 52, 18))
        self.label_oshibori_yen.setObjectName("label_oshibori_yen")
        self.label_kujoki_yen = QtWidgets.QLabel(self)
        self.label_kujoki_yen.setGeometry(QtCore.QRect(220, 100, 52, 18))
        self.label_kujoki_yen.setObjectName("label_kujoki_yen")
        self.label_risueki_yen = QtWidgets.QLabel(self)
        self.label_risueki_yen.setGeometry(QtCore.QRect(220, 130, 52, 18))
        self.label_risueki_yen.setObjectName("label_risueki_yen")
        self.label_chosakuken_yen = QtWidgets.QLabel(self)
        self.label_chosakuken_yen.setGeometry(QtCore.QRect(220, 160, 52, 18))
        self.label_chosakuken_yen.setObjectName("label_chosakuken_yen")
        self.label_karaoke_yen = QtWidgets.QLabel(self)
        self.label_karaoke_yen.setGeometry(QtCore.QRect(220, 190, 52, 18))
        self.label_karaoke_yen.setObjectName("label_karaoke_yen")
        self.lineEdit_chosakuken = QtWidgets.QLineEdit(self)
        self.lineEdit_chosakuken.setGeometry(QtCore.QRect(90, 158, 125, 21))
        self.lineEdit_chosakuken.setObjectName("lineEdit_chosakuken")
        self.label_karaoke = QtWidgets.QLabel(self)
        self.label_karaoke.setGeometry(QtCore.QRect(30, 189, 52, 18))
        self.label_karaoke.setObjectName("label_karaoke")
        self.lineEdit_karaoke = QtWidgets.QLineEdit(self)
        self.lineEdit_karaoke.setGeometry(QtCore.QRect(90, 189, 125, 21))
        self.lineEdit_karaoke.setObjectName("lineEdit_karaoke")
        self.label_kujoki = QtWidgets.QLabel(self)
        self.label_kujoki.setGeometry(QtCore.QRect(43, 96, 39, 18))
        self.label_kujoki.setObjectName("label_kujoki")
        self.label_chosakuken = QtWidgets.QLabel(self)
        self.label_chosakuken.setGeometry(QtCore.QRect(43, 158, 39, 18))
        self.label_chosakuken.setObjectName("label_chosakuken")
        self.lineEdit_kujoki = QtWidgets.QLineEdit(self)
        self.lineEdit_kujoki.setGeometry(QtCore.QRect(90, 96, 125, 21))
        self.lineEdit_kujoki.setObjectName("lineEdit_kujoki")
        self.label_risueki = QtWidgets.QLabel(self)
        self.label_risueki.setGeometry(QtCore.QRect(17, 127, 65, 18))
        self.label_risueki.setObjectName("label_risueki")
        self.lineEdit_risueki = QtWidgets.QLineEdit(self)
        self.lineEdit_risueki.setGeometry(QtCore.QRect(90, 127, 125, 21))
        self.lineEdit_risueki.setObjectName("lineEdit_risueki")
        self.label_oshibori = QtWidgets.QLabel(self)
        self.label_oshibori.setGeometry(QtCore.QRect(30, 65, 52, 18))
        self.label_oshibori.setObjectName("label_oshibori")
        self.lineEdit_oshibori = QtWidgets.QLineEdit(self)
        self.lineEdit_oshibori.setGeometry(QtCore.QRect(90, 65, 125, 21))
        self.lineEdit_oshibori.setObjectName("lineEdit_oshibori")

        self.retranslateUi()
        self.buttonBox.accepted.connect(self.accept)  # type: ignore
        self.buttonBox.rejected.connect(self.reject)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("AccountsEditorDialog", "勘定科目の編集"))
        self._label.setText(_translate("AccountsEditorDialog", "固定費として事前入力したい金額を変更できます"))
        self.label_oshibori_yen.setText(_translate("AccountsEditorDialog", "円"))
        self.label_kujoki_yen.setText(_translate("AccountsEditorDialog", "円"))
        self.label_risueki_yen.setText(_translate("AccountsEditorDialog", "円"))
        self.label_chosakuken_yen.setText(_translate("AccountsEditorDialog", "円"))
        self.label_karaoke_yen.setText(_translate("AccountsEditorDialog", "円"))
        self.label_karaoke.setText(_translate("AccountsEditorDialog", "カラオケ"))
        self.label_kujoki.setText(_translate("AccountsEditorDialog", "駆除器"))
        self.label_chosakuken.setText(_translate("AccountsEditorDialog", "著作権"))
        self.label_risueki.setText(_translate("AccountsEditorDialog", "リース植木"))
        self.label_oshibori.setText(_translate("AccountsEditorDialog", "おしぼり"))
