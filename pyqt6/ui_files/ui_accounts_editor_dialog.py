# Form implementation generated from reading ui file '.\accountsEditorDialog.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QDialog


class Ui_AccountsEditorDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("AccountsEditorDialog")
        self.resize(472, 263)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self._label = QtWidgets.QLabel(self)
        self._label.setObjectName("_label")
        self.verticalLayout.addWidget(self._label)
        self._formLayout = QtWidgets.QFormLayout()
        self._formLayout.setObjectName("_formLayout")
        self.label_oshibori = QtWidgets.QLabel(self)
        self.label_oshibori.setObjectName("label_oshibori")
        self._formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_oshibori)
        self.lineEdit_oshibori = QtWidgets.QLineEdit(self)
        self.lineEdit_oshibori.setObjectName("lineEdit_oshibori")
        self._formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_oshibori)
        self.lineEdit_kujoki = QtWidgets.QLineEdit(self)
        self.lineEdit_kujoki.setObjectName("lineEdit_kujoki")
        self._formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_kujoki)
        self.label_risueki = QtWidgets.QLabel(self)
        self.label_risueki.setObjectName("label_risueki")
        self._formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_risueki)
        self.lineEdit_risueki = QtWidgets.QLineEdit(self)
        self.lineEdit_risueki.setObjectName("lineEdit_risueki")
        self._formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_risueki)
        self.label_chosakuken = QtWidgets.QLabel(self)
        self.label_chosakuken.setObjectName("label_chosakuken")
        self._formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_chosakuken)
        self.lineEdit_chosakuken = QtWidgets.QLineEdit(self)
        self.lineEdit_chosakuken.setObjectName("lineEdit_chosakuken")
        self._formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_chosakuken)
        self.label_karaoke = QtWidgets.QLabel(self)
        self.label_karaoke.setObjectName("label_karaoke")
        self._formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_karaoke)
        self.lineEdit_karaoke = QtWidgets.QLineEdit(self)
        self.lineEdit_karaoke.setObjectName("lineEdit_karaoke")
        self._formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_karaoke)
        self.label_kujoki = QtWidgets.QLabel(self)
        self.label_kujoki.setObjectName("label_kujoki")
        self._formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_kujoki)
        self.verticalLayout.addLayout(self._formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel |
                                          QtWidgets.QDialogButtonBox.StandardButton.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi()
        # self.buttonBox.accepted.connect(self.accept) # type: ignore
        # self.buttonBox.rejected.connect(self.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("AccountsEditorDialog", "勘定科目の編集"))
        self._label.setText(_translate("AccountsEditorDialog", "固定費として事前入力したい金額を変更できます"))
        self.label_oshibori.setText(_translate("AccountsEditorDialog", "おしぼり"))
        self.label_risueki.setText(_translate("AccountsEditorDialog", "リース植木"))
        self.label_chosakuken.setText(_translate("AccountsEditorDialog", "著作権"))
        self.label_karaoke.setText(_translate("AccountsEditorDialog", "カラオケ"))
        self.label_kujoki.setText(_translate("AccountsEditorDialog", "駆除器"))
