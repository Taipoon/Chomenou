# Form implementation generated from reading ui file '.\bulkInsertionDialog.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QDialog


class Ui_BulkInsertionDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("BulkInsertionDialog")
        self.resize(301, 300)
        self.setMinimumSize(QtCore.QSize(0, 0))
        self.setMaximumSize(QtCore.QSize(400, 300))
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(20, 260, 261, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.StandardButton.Cancel |
            QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.grpBx_monthSelector = QtWidgets.QGroupBox(self)
        self.grpBx_monthSelector.setGeometry(QtCore.QRect(20, 20, 261, 121))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.grpBx_monthSelector.setFont(font)
        self.grpBx_monthSelector.setCheckable(False)
        self.grpBx_monthSelector.setChecked(False)
        self.grpBx_monthSelector.setObjectName("grpBx_monthSelector")
        self.gridLayout = QtWidgets.QGridLayout(self.grpBx_monthSelector)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox_month2 = QtWidgets.QCheckBox(self.grpBx_monthSelector)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.checkBox_month2.setFont(font)
        self.checkBox_month2.setObjectName("checkBox_month2")
        self.gridLayout.addWidget(self.checkBox_month2, 0, 1, 1, 1)
        self.checkBox_month4 = QtWidgets.QCheckBox(self.grpBx_monthSelector)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.checkBox_month4.setFont(font)
        self.checkBox_month4.setObjectName("checkBox_month4")
        self.gridLayout.addWidget(self.checkBox_month4, 1, 0, 1, 1)
        self.checkBox_month5 = QtWidgets.QCheckBox(self.grpBx_monthSelector)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.checkBox_month5.setFont(font)
        self.checkBox_month5.setObjectName("checkBox_month5")
        self.gridLayout.addWidget(self.checkBox_month5, 1, 1, 1, 1)
        self.checkBox_month3 = QtWidgets.QCheckBox(self.grpBx_monthSelector)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.checkBox_month3.setFont(font)
        self.checkBox_month3.setObjectName("checkBox_month3")
        self.gridLayout.addWidget(self.checkBox_month3, 0, 2, 1, 1)
        self.checkBox_month7 = QtWidgets.QCheckBox(self.grpBx_monthSelector)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.checkBox_month7.setFont(font)
        self.checkBox_month7.setObjectName("checkBox_month7")
        self.gridLayout.addWidget(self.checkBox_month7, 2, 0, 1, 1)
        self.checkBox_month6 = QtWidgets.QCheckBox(self.grpBx_monthSelector)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.checkBox_month6.setFont(font)
        self.checkBox_month6.setObjectName("checkBox_month6")
        self.gridLayout.addWidget(self.checkBox_month6, 1, 2, 1, 1)
        self.checkBox_month8 = QtWidgets.QCheckBox(self.grpBx_monthSelector)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.checkBox_month8.setFont(font)
        self.checkBox_month8.setObjectName("checkBox_month8")
        self.gridLayout.addWidget(self.checkBox_month8, 2, 1, 1, 1)
        self.checkBox_month9 = QtWidgets.QCheckBox(self.grpBx_monthSelector)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.checkBox_month9.setFont(font)
        self.checkBox_month9.setObjectName("checkBox_month9")
        self.gridLayout.addWidget(self.checkBox_month9, 2, 2, 1, 1)
        self.checkBox_month1 = QtWidgets.QCheckBox(self.grpBx_monthSelector)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.checkBox_month1.setFont(font)
        self.checkBox_month1.setObjectName("checkBox_month1")
        self.gridLayout.addWidget(self.checkBox_month1, 0, 0, 1, 1)
        self.checkBox_month10 = QtWidgets.QCheckBox(self.grpBx_monthSelector)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.checkBox_month10.setFont(font)
        self.checkBox_month10.setObjectName("checkBox_month10")
        self.gridLayout.addWidget(self.checkBox_month10, 3, 0, 1, 1)
        self.checkBox_month11 = QtWidgets.QCheckBox(self.grpBx_monthSelector)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.checkBox_month11.setFont(font)
        self.checkBox_month11.setObjectName("checkBox_month11")
        self.gridLayout.addWidget(self.checkBox_month11, 3, 1, 1, 1)
        self.checkBox_month12 = QtWidgets.QCheckBox(self.grpBx_monthSelector)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.checkBox_month12.setFont(font)
        self.checkBox_month12.setObjectName("checkBox_month12")
        self.gridLayout.addWidget(self.checkBox_month12, 3, 2, 1, 1)
        self.dateEdit_dayInputSelector = QtWidgets.QDateEdit(self)
        self.dateEdit_dayInputSelector.setGeometry(QtCore.QRect(20, 160, 110, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dateEdit_dayInputSelector.setFont(font)
        self.dateEdit_dayInputSelector.setObjectName("dateEdit_dayInputSelector")
        self.lineEdit_amountEntryField = QtWidgets.QLineEdit(self)
        self.lineEdit_amountEntryField.setGeometry(QtCore.QRect(20, 210, 130, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_amountEntryField.setFont(font)
        self.lineEdit_amountEntryField.setObjectName("lineEdit_amountEntryField")
        self._label_yen = QtWidgets.QLabel(self)
        self._label_yen.setGeometry(QtCore.QRect(160, 220, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self._label_yen.setFont(font)
        self._label_yen.setObjectName("_label_yen")
        self.pshBtn_registrationAction = QtWidgets.QPushButton(self)
        self.pshBtn_registrationAction.setGeometry(QtCore.QRect(190, 210, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pshBtn_registrationAction.setFont(font)
        self.pshBtn_registrationAction.setObjectName("pshBtn_registrationAction")
        self.cmbBx_accountSelector = QtWidgets.QComboBox(self)
        self.cmbBx_accountSelector.setGeometry(QtCore.QRect(140, 160, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cmbBx_accountSelector.setFont(font)
        self.cmbBx_accountSelector.setObjectName("cmbBx_accountSelector")

        self.retranslateUi()
        # self.buttonBox.accepted.connect(self.accept)  # type: ignore
        # self.buttonBox.rejected.connect(self.reject)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("BulkInsertionDialog", "月を指定して一括登録"))
        self.checkBox_month2.setText(_translate("BulkInsertionDialog", "2月"))
        self.checkBox_month4.setText(_translate("BulkInsertionDialog", "4月"))
        self.checkBox_month5.setText(_translate("BulkInsertionDialog", "5月"))
        self.checkBox_month3.setText(_translate("BulkInsertionDialog", "3月"))
        self.checkBox_month7.setText(_translate("BulkInsertionDialog", "7月"))
        self.checkBox_month6.setText(_translate("BulkInsertionDialog", "6月"))
        self.checkBox_month8.setText(_translate("BulkInsertionDialog", "8月"))
        self.checkBox_month9.setText(_translate("BulkInsertionDialog", "9月"))
        self.checkBox_month1.setText(_translate("BulkInsertionDialog", "1月"))
        self.checkBox_month10.setText(_translate("BulkInsertionDialog", "10月"))
        self.checkBox_month11.setText(_translate("BulkInsertionDialog", "11月"))
        self.checkBox_month12.setText(_translate("BulkInsertionDialog", "12月"))
        self.dateEdit_dayInputSelector.setDisplayFormat(_translate("BulkInsertionDialog", "d日"))
        self._label_yen.setText(_translate("BulkInsertionDialog", "円"))
        self.pshBtn_registrationAction.setText(_translate("BulkInsertionDialog", "記帳"))
