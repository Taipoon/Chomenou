# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(872, 757)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(872, 757))
        self.setMaximumSize(QtCore.QSize(872, 757))
        self._widget_centralWidget = QtWidgets.QWidget(self)
        self._widget_centralWidget.setObjectName("_widget_centralWidget")
        self.dateEdit_dateInputViewer = QtWidgets.QDateEdit(self._widget_centralWidget)
        self.dateEdit_dateInputViewer.setGeometry(QtCore.QRect(10, 10, 411, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.dateEdit_dateInputViewer.setFont(font)
        self.dateEdit_dateInputViewer.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.dateEdit_dateInputViewer.setFrame(False)
        self.dateEdit_dateInputViewer.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.dateEdit_dateInputViewer.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.dateEdit_dateInputViewer.setCurrentSection(QtWidgets.QDateTimeEdit.Section.YearSection)
        self.dateEdit_dateInputViewer.setCalendarPopup(False)
        self.dateEdit_dateInputViewer.setObjectName("dateEdit_dateInputViewer")
        self.calenderWidget_calenderViewer = QtWidgets.QCalendarWidget(self._widget_centralWidget)
        self.calenderWidget_calenderViewer.setGeometry(QtCore.QRect(10, 40, 411, 241))
        self.calenderWidget_calenderViewer.setStyleSheet("")
        self.calenderWidget_calenderViewer.setGridVisible(True)
        self.calenderWidget_calenderViewer.setVerticalHeaderFormat(
            QtWidgets.QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader)
        self.calenderWidget_calenderViewer.setNavigationBarVisible(True)
        self.calenderWidget_calenderViewer.setObjectName("calenderWidget_calenderViewer")
        self._grpBx_accountButtonSelector = QtWidgets.QGroupBox(self._widget_centralWidget)
        self._grpBx_accountButtonSelector.setGeometry(QtCore.QRect(10, 370, 410, 350))
        self._grpBx_accountButtonSelector.setObjectName("_grpBx_accountButtonSelector")
        self.pshBtn_shiire = QtWidgets.QPushButton(self._grpBx_accountButtonSelector)
        self.pshBtn_shiire.setGeometry(QtCore.QRect(10, 10, 110, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pshBtn_shiire.sizePolicy().hasHeightForWidth())
        self.pshBtn_shiire.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pshBtn_shiire.setFont(font)
        self.pshBtn_shiire.setAutoFillBackground(False)
        self.pshBtn_shiire.setStyleSheet("")
        self.pshBtn_shiire.setCheckable(True)
        self.pshBtn_shiire.setChecked(True)
        self.pshBtn_shiire.setAutoExclusive(True)
        self.pshBtn_shiire.setObjectName("pshBtn_shiire")
        self.pshBtn_settai = QtWidgets.QPushButton(self._grpBx_accountButtonSelector)
        self.pshBtn_settai.setGeometry(QtCore.QRect(150, 10, 110, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pshBtn_settai.sizePolicy().hasHeightForWidth())
        self.pshBtn_settai.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pshBtn_settai.setFont(font)
        self.pshBtn_settai.setCheckable(True)
        self.pshBtn_settai.setAutoExclusive(True)
        self.pshBtn_settai.setObjectName("pshBtn_settai")
        self.pshBtn_zappi = QtWidgets.QPushButton(self._grpBx_accountButtonSelector)
        self.pshBtn_zappi.setGeometry(QtCore.QRect(290, 10, 110, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pshBtn_zappi.sizePolicy().hasHeightForWidth())
        self.pshBtn_zappi.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pshBtn_zappi.setFont(font)
        self.pshBtn_zappi.setCheckable(True)
        self.pshBtn_zappi.setAutoExclusive(True)
        self.pshBtn_zappi.setObjectName("pshBtn_zappi")
        self.pshBtn_shomohin = QtWidgets.QPushButton(self._grpBx_accountButtonSelector)
        self.pshBtn_shomohin.setGeometry(QtCore.QRect(10, 50, 110, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pshBtn_shomohin.setFont(font)
        self.pshBtn_shomohin.setCheckable(True)
        self.pshBtn_shomohin.setAutoExclusive(True)
        self.pshBtn_shomohin.setObjectName("pshBtn_shomohin")
        self.pshBtn_yachin = QtWidgets.QPushButton(self._grpBx_accountButtonSelector)
        self.pshBtn_yachin.setGeometry(QtCore.QRect(150, 50, 110, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pshBtn_yachin.setFont(font)
        self.pshBtn_yachin.setCheckable(True)
        self.pshBtn_yachin.setAutoExclusive(True)
        self.pshBtn_yachin.setObjectName("pshBtn_yachin")
        self.pshBtn_aisu = QtWidgets.QPushButton(self._grpBx_accountButtonSelector)
        self.pshBtn_aisu.setGeometry(QtCore.QRect(290, 50, 110, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pshBtn_aisu.setFont(font)
        self.pshBtn_aisu.setCheckable(True)
        self.pshBtn_aisu.setAutoExclusive(True)
        self.pshBtn_aisu.setObjectName("pshBtn_aisu")
        self.pshBtn_osakagas = QtWidgets.QPushButton(self._grpBx_accountButtonSelector)
        self.pshBtn_osakagas.setGeometry(QtCore.QRect(10, 90, 110, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pshBtn_osakagas.setFont(font)
        self.pshBtn_osakagas.setCheckable(True)
        self.pshBtn_osakagas.setAutoExclusive(True)
        self.pshBtn_osakagas.setObjectName("pshBtn_osakagas")
        self.pshBtn_hoken = QtWidgets.QPushButton(self._grpBx_accountButtonSelector)
        self.pshBtn_hoken.setGeometry(QtCore.QRect(150, 90, 110, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pshBtn_hoken.setFont(font)
        self.pshBtn_hoken.setCheckable(True)
        self.pshBtn_hoken.setAutoExclusive(True)
        self.pshBtn_hoken.setObjectName("pshBtn_hoken")
        self.pshBtn_tsushinhi = QtWidgets.QPushButton(self._grpBx_accountButtonSelector)
        self.pshBtn_tsushinhi.setGeometry(QtCore.QRect(290, 90, 110, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pshBtn_tsushinhi.setFont(font)
        self.pshBtn_tsushinhi.setCheckable(True)
        self.pshBtn_tsushinhi.setAutoExclusive(True)
        self.pshBtn_tsushinhi.setObjectName("pshBtn_tsushinhi")
        self.pshBtn_shuzenhi = QtWidgets.QPushButton(self._grpBx_accountButtonSelector)
        self.pshBtn_shuzenhi.setGeometry(QtCore.QRect(10, 130, 110, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pshBtn_shuzenhi.setFont(font)
        self.pshBtn_shuzenhi.setCheckable(True)
        self.pshBtn_shuzenhi.setAutoExclusive(True)
        self.pshBtn_shuzenhi.setObjectName("pshBtn_shuzenhi")
        self.pshBtn_kokokuhi = QtWidgets.QPushButton(self._grpBx_accountButtonSelector)
        self.pshBtn_kokokuhi.setGeometry(QtCore.QRect(150, 130, 110, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pshBtn_kokokuhi.setFont(font)
        self.pshBtn_kokokuhi.setCheckable(True)
        self.pshBtn_kokokuhi.setAutoExclusive(True)
        self.pshBtn_kokokuhi.setObjectName("pshBtn_kokokuhi")
        self.pshBtn_jidoshazei = QtWidgets.QPushButton(self._grpBx_accountButtonSelector)
        self.pshBtn_jidoshazei.setGeometry(QtCore.QRect(290, 130, 110, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pshBtn_jidoshazei.setFont(font)
        self.pshBtn_jidoshazei.setCheckable(True)
        self.pshBtn_jidoshazei.setAutoExclusive(True)
        self.pshBtn_jidoshazei.setObjectName("pshBtn_jidoshazei")
        self.pshBtn_sakadai = QtWidgets.QPushButton(self._grpBx_accountButtonSelector)
        self.pshBtn_sakadai.setGeometry(QtCore.QRect(10, 170, 110, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pshBtn_sakadai.setFont(font)
        self.pshBtn_sakadai.setCheckable(True)
        self.pshBtn_sakadai.setAutoExclusive(True)
        self.pshBtn_sakadai.setObjectName("pshBtn_sakadai")
        self.pshBtn_bihin = QtWidgets.QPushButton(self._grpBx_accountButtonSelector)
        self.pshBtn_bihin.setGeometry(QtCore.QRect(150, 170, 110, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pshBtn_bihin.setFont(font)
        self.pshBtn_bihin.setCheckable(True)
        self.pshBtn_bihin.setAutoExclusive(True)
        self.pshBtn_bihin.setObjectName("pshBtn_bihin")
        self._line_horizontalSeparater1 = QtWidgets.QFrame(self._grpBx_accountButtonSelector)
        self._line_horizontalSeparater1.setGeometry(QtCore.QRect(10, 200, 391, 21))
        self._line_horizontalSeparater1.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self._line_horizontalSeparater1.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self._line_horizontalSeparater1.setObjectName("_line_horizontalSeparater1")
        self.pshBtn_oshibori = QtWidgets.QPushButton(self._grpBx_accountButtonSelector)
        self.pshBtn_oshibori.setGeometry(QtCore.QRect(10, 220, 110, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pshBtn_oshibori.setFont(font)
        self.pshBtn_oshibori.setCheckable(True)
        self.pshBtn_oshibori.setAutoExclusive(True)
        self.pshBtn_oshibori.setObjectName("pshBtn_oshibori")
        self.pshBtn_kujoki = QtWidgets.QPushButton(self._grpBx_accountButtonSelector)
        self.pshBtn_kujoki.setGeometry(QtCore.QRect(150, 220, 110, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pshBtn_kujoki.setFont(font)
        self.pshBtn_kujoki.setCheckable(True)
        self.pshBtn_kujoki.setAutoExclusive(True)
        self.pshBtn_kujoki.setObjectName("pshBtn_kujoki")
        self.pshBtn_risueki = QtWidgets.QPushButton(self._grpBx_accountButtonSelector)
        self.pshBtn_risueki.setGeometry(QtCore.QRect(290, 220, 110, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pshBtn_risueki.setFont(font)
        self.pshBtn_risueki.setCheckable(True)
        self.pshBtn_risueki.setAutoExclusive(True)
        self.pshBtn_risueki.setObjectName("pshBtn_risueki")
        self.pshBtn_chosakuken = QtWidgets.QPushButton(self._grpBx_accountButtonSelector)
        self.pshBtn_chosakuken.setGeometry(QtCore.QRect(10, 260, 110, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pshBtn_chosakuken.setFont(font)
        self.pshBtn_chosakuken.setCheckable(True)
        self.pshBtn_chosakuken.setAutoExclusive(True)
        self.pshBtn_chosakuken.setObjectName("pshBtn_chosakuken")
        self.pshBtn_karaoke = QtWidgets.QPushButton(self._grpBx_accountButtonSelector)
        self.pshBtn_karaoke.setGeometry(QtCore.QRect(150, 260, 110, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pshBtn_karaoke.setFont(font)
        self.pshBtn_karaoke.setCheckable(True)
        self.pshBtn_karaoke.setAutoExclusive(True)
        self.pshBtn_karaoke.setObjectName("pshBtn_karaoke")
        self._line_horizontalSeparater2 = QtWidgets.QFrame(self._grpBx_accountButtonSelector)
        self._line_horizontalSeparater2.setGeometry(QtCore.QRect(10, 290, 391, 21))
        self._line_horizontalSeparater2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self._line_horizontalSeparater2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self._line_horizontalSeparater2.setObjectName("_line_horizontalSeparater2")
        self.pshBtn_uriage = QtWidgets.QPushButton(self._grpBx_accountButtonSelector)
        self.pshBtn_uriage.setGeometry(QtCore.QRect(10, 310, 391, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pshBtn_uriage.setFont(font)
        self.pshBtn_uriage.setStyleSheet("")
        self.pshBtn_uriage.setCheckable(True)
        self.pshBtn_uriage.setAutoExclusive(True)
        self.pshBtn_uriage.setObjectName("pshBtn_uriage")
        self.cmbBx_variableCostSelector = QtWidgets.QComboBox(self._grpBx_accountButtonSelector)
        self.cmbBx_variableCostSelector.setGeometry(QtCore.QRect(290, 170, 110, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cmbBx_variableCostSelector.setFont(font)
        self.cmbBx_variableCostSelector.setCurrentText("")
        self.cmbBx_variableCostSelector.setInsertPolicy(QtWidgets.QComboBox.InsertPolicy.NoInsert)
        self.cmbBx_variableCostSelector.setFrame(False)
        self.cmbBx_variableCostSelector.setObjectName("cmbBx_variableCostSelector")
        self.cmbBx_fixedCostSelector = QtWidgets.QComboBox(self._grpBx_accountButtonSelector)
        self.cmbBx_fixedCostSelector.setGeometry(QtCore.QRect(290, 260, 110, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cmbBx_fixedCostSelector.setFont(font)
        self.cmbBx_fixedCostSelector.setInsertPolicy(QtWidgets.QComboBox.InsertPolicy.NoInsert)
        self.cmbBx_fixedCostSelector.setFrame(False)
        self.cmbBx_fixedCostSelector.setObjectName("cmbBx_fixedCostSelector")
        self.tableWidget_dailySummaryViewer = QtWidgets.QTableWidget(self._widget_centralWidget)
        self.tableWidget_dailySummaryViewer.setGeometry(QtCore.QRect(440, 10, 420, 310))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_dailySummaryViewer.sizePolicy().hasHeightForWidth())
        self.tableWidget_dailySummaryViewer.setSizePolicy(sizePolicy)
        self.tableWidget_dailySummaryViewer.setMaximumSize(QtCore.QSize(16777215, 500))
        self.tableWidget_dailySummaryViewer.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget_dailySummaryViewer.setAlternatingRowColors(False)
        self.tableWidget_dailySummaryViewer.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget_dailySummaryViewer.setTextElideMode(QtCore.Qt.TextElideMode.ElideLeft)
        self.tableWidget_dailySummaryViewer.setHorizontalScrollMode(
            QtWidgets.QAbstractItemView.ScrollMode.ScrollPerItem)
        self.tableWidget_dailySummaryViewer.setObjectName("tableWidget_dailySummaryViewer")
        self.tableWidget_dailySummaryViewer.setColumnCount(2)
        self.tableWidget_dailySummaryViewer.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidget_dailySummaryViewer.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_dailySummaryViewer.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_dailySummaryViewer.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidget_dailySummaryViewer.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidget_dailySummaryViewer.setItem(0, 1, item)
        self.tableWidget_dailySummaryViewer.horizontalHeader().setVisible(True)
        self.tableWidget_dailySummaryViewer.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_dailySummaryViewer.horizontalHeader().setMinimumSectionSize(30)
        self.tableWidget_dailySummaryViewer.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_dailySummaryViewer.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_dailySummaryViewer.verticalHeader().setVisible(False)
        self.tableWidget_dailySummaryViewer.verticalHeader().setHighlightSections(True)
        self.treeWidget_monthlySummaryViewer = QtWidgets.QTreeWidget(self._widget_centralWidget)
        self.treeWidget_monthlySummaryViewer.setGeometry(QtCore.QRect(440, 370, 420, 350))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget_monthlySummaryViewer.sizePolicy().hasHeightForWidth())
        self.treeWidget_monthlySummaryViewer.setSizePolicy(sizePolicy)
        self.treeWidget_monthlySummaryViewer.setMaximumSize(QtCore.QSize(16777215, 500))
        self.treeWidget_monthlySummaryViewer.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.treeWidget_monthlySummaryViewer.setHeaderHidden(False)
        self.treeWidget_monthlySummaryViewer.setObjectName("treeWidget_monthlySummaryViewer")
        self.treeWidget_monthlySummaryViewer.headerItem().setTextAlignment(0, QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.treeWidget_monthlySummaryViewer.headerItem().setFont(0, font)
        self.treeWidget_monthlySummaryViewer.headerItem().setTextAlignment(1,
                                                                           QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignVCenter)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.treeWidget_monthlySummaryViewer.headerItem().setFont(1, font)
        self.pshBtn_showHistory = QtWidgets.QPushButton(self._widget_centralWidget)
        self.pshBtn_showHistory.setGeometry(QtCore.QRect(440, 330, 420, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pshBtn_showHistory.setFont(font)
        self.pshBtn_showHistory.setObjectName("pshBtn_showHistory")
        self.pshBtn_goBackOneDay = QtWidgets.QPushButton(self._widget_centralWidget)
        self.pshBtn_goBackOneDay.setGeometry(QtCore.QRect(30, 290, 110, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pshBtn_goBackOneDay.setFont(font)
        self.pshBtn_goBackOneDay.setObjectName("pshBtn_goBackOneDay")
        self.pshBtn_goToday = QtWidgets.QPushButton(self._widget_centralWidget)
        self.pshBtn_goToday.setGeometry(QtCore.QRect(160, 290, 111, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pshBtn_goToday.setFont(font)
        self.pshBtn_goToday.setObjectName("pshBtn_goToday")
        self.pshBtn_goForwardOneDay = QtWidgets.QPushButton(self._widget_centralWidget)
        self.pshBtn_goForwardOneDay.setGeometry(QtCore.QRect(290, 290, 110, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pshBtn_goForwardOneDay.setFont(font)
        self.pshBtn_goForwardOneDay.setObjectName("pshBtn_goForwardOneDay")
        self.lineEdit_amountEntryField = QtWidgets.QLineEdit(self._widget_centralWidget)
        self.lineEdit_amountEntryField.setGeometry(QtCore.QRect(100, 330, 181, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_amountEntryField.sizePolicy().hasHeightForWidth())
        self.lineEdit_amountEntryField.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_amountEntryField.setFont(font)
        self.lineEdit_amountEntryField.setAcceptDrops(True)
        self.lineEdit_amountEntryField.setMaxLength(15)
        self.lineEdit_amountEntryField.setFrame(False)
        self.lineEdit_amountEntryField.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_amountEntryField.setClearButtonEnabled(True)
        self.lineEdit_amountEntryField.setObjectName("lineEdit_amountEntryField")
        self.label_yen = QtWidgets.QLabel(self._widget_centralWidget)
        self.label_yen.setGeometry(QtCore.QRect(290, 330, 27, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_yen.setFont(font)
        self.label_yen.setObjectName("label_yen")
        self.pshBtn_executeRegistration = QtWidgets.QPushButton(self._widget_centralWidget)
        self.pshBtn_executeRegistration.setGeometry(QtCore.QRect(320, 330, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pshBtn_executeRegistration.setFont(font)
        self.pshBtn_executeRegistration.setObjectName("pshBtn_executeRegistration")
        self._line_verticalSeparater = QtWidgets.QFrame(self._widget_centralWidget)
        self._line_verticalSeparater.setGeometry(QtCore.QRect(420, 20, 20, 691))
        self._line_verticalSeparater.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self._line_verticalSeparater.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self._line_verticalSeparater.setObjectName("_line_verticalSeparater")
        self.label_selectedAccount = QtWidgets.QLabel(self._widget_centralWidget)
        self.label_selectedAccount.setGeometry(QtCore.QRect(20, 325, 81, 41))
        self.label_selectedAccount.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_selectedAccount.setObjectName("label_selectedAccount")
        self._grpBx_accountButtonSelector.raise_()
        self.dateEdit_dateInputViewer.raise_()
        self.calenderWidget_calenderViewer.raise_()
        self.tableWidget_dailySummaryViewer.raise_()
        self.treeWidget_monthlySummaryViewer.raise_()
        self.pshBtn_showHistory.raise_()
        self.pshBtn_goBackOneDay.raise_()
        self.pshBtn_goToday.raise_()
        self.pshBtn_goForwardOneDay.raise_()
        self.lineEdit_amountEntryField.raise_()
        self.label_yen.raise_()
        self.pshBtn_executeRegistration.raise_()
        self._line_verticalSeparater.raise_()
        self.label_selectedAccount.raise_()
        self.setCentralWidget(self._widget_centralWidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 872, 36))
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_fileOutput = QtWidgets.QMenu(self.menu_file)
        self.menu_fileOutput.setObjectName("menu_fileOutput")
        self.menu_edit = QtWidgets.QMenu(self.menubar)
        self.menu_edit.setObjectName("menu_edit")
        self.menu_tools = QtWidgets.QMenu(self.menubar)
        self.menu_tools.setObjectName("menu_tools")
        self.setMenuBar(self.menubar)
        self.action_create = QtGui.QAction(self)
        self.action_create.setObjectName("action_create")
        self.action_open = QtGui.QAction(self)
        self.action_open.setObjectName("action_open")
        self.action_outputExcel = QtGui.QAction(self)
        self.action_outputExcel.setObjectName("action_outputExcel")
        self.action_outputCsv = QtGui.QAction(self)
        self.action_outputCsv.setObjectName("action_outputCsv")
        self.action_quit = QtGui.QAction(self)
        self.action_quit.setObjectName("action_quit")
        self.action_editAccounts = QtGui.QAction(self)
        self.action_editAccounts.setObjectName("action_editAccounts")
        self.action_bulkInsertion = QtGui.QAction(self)
        self.action_bulkInsertion.setObjectName("action_bulkInsertion")
        self.action_showStatistics = QtGui.QAction(self)
        self.action_showStatistics.setObjectName("action_showStatistics")
        self.action_showYearToYearComparison = QtGui.QAction(self)
        self.action_showYearToYearComparison.setObjectName("action_showYearToYearComparison")
        self.action_balancing = QtGui.QAction(self)
        self.action_balancing.setObjectName("action_balancing")
        self.menu_fileOutput.addAction(self.action_outputExcel)
        self.menu_fileOutput.addAction(self.action_outputCsv)
        self.menu_file.addAction(self.action_create)
        self.menu_file.addAction(self.action_open)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.menu_fileOutput.menuAction())
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_quit)
        self.menu_edit.addAction(self.action_editAccounts)
        self.menu_edit.addAction(self.action_bulkInsertion)
        self.menu_tools.addAction(self.action_showStatistics)
        self.menu_tools.addAction(self.action_showYearToYearComparison)
        self.menu_tools.addSeparator()
        self.menu_tools.addAction(self.action_balancing)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_edit.menuAction())
        self.menubar.addAction(self.menu_tools.menuAction())

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Chomenou"))
        self.dateEdit_dateInputViewer.setDisplayFormat(_translate("MainWindow", "yyyy年MM月dd日"))
        self.pshBtn_shiire.setText(_translate("MainWindow", "仕入"))
        self.pshBtn_settai.setText(_translate("MainWindow", "接待"))
        self.pshBtn_zappi.setText(_translate("MainWindow", "雑費"))
        self.pshBtn_shomohin.setText(_translate("MainWindow", "消耗品"))
        self.pshBtn_yachin.setText(_translate("MainWindow", "家賃"))
        self.pshBtn_aisu.setText(_translate("MainWindow", "アイス"))
        self.pshBtn_osakagas.setText(_translate("MainWindow", "大阪ガス"))
        self.pshBtn_hoken.setText(_translate("MainWindow", "保険"))
        self.pshBtn_tsushinhi.setText(_translate("MainWindow", "通信費"))
        self.pshBtn_shuzenhi.setText(_translate("MainWindow", "修繕費"))
        self.pshBtn_kokokuhi.setText(_translate("MainWindow", "広告費"))
        self.pshBtn_jidoshazei.setText(_translate("MainWindow", "自動車税"))
        self.pshBtn_sakadai.setText(_translate("MainWindow", "酒代"))
        self.pshBtn_bihin.setText(_translate("MainWindow", "備品"))
        self.pshBtn_oshibori.setText(_translate("MainWindow", "おしぼり"))
        self.pshBtn_kujoki.setText(_translate("MainWindow", "駆除器"))
        self.pshBtn_risueki.setText(_translate("MainWindow", "リース植木"))
        self.pshBtn_chosakuken.setText(_translate("MainWindow", "著作権"))
        self.pshBtn_karaoke.setText(_translate("MainWindow", "カラオケ"))
        self.pshBtn_uriage.setText(_translate("MainWindow", "売上"))
        self.tableWidget_dailySummaryViewer.setSortingEnabled(False)
        item = self.tableWidget_dailySummaryViewer.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "記録"))
        item = self.tableWidget_dailySummaryViewer.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "勘定科目"))
        item = self.tableWidget_dailySummaryViewer.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "合計金額"))
        __sortingEnabled = self.tableWidget_dailySummaryViewer.isSortingEnabled()
        self.tableWidget_dailySummaryViewer.setSortingEnabled(False)
        self.tableWidget_dailySummaryViewer.setSortingEnabled(__sortingEnabled)
        self.treeWidget_monthlySummaryViewer.headerItem().setText(0, _translate("MainWindow", "勘定科目"))
        self.treeWidget_monthlySummaryViewer.headerItem().setText(1, _translate("MainWindow", "金額"))
        self.pshBtn_showHistory.setText(_translate("MainWindow", "入力履歴を表示"))
        self.pshBtn_goBackOneDay.setText(_translate("MainWindow", "1日戻る"))
        self.pshBtn_goToday.setText(_translate("MainWindow", "今日へ移動"))
        self.pshBtn_goForwardOneDay.setText(_translate("MainWindow", "1日進む"))
        self.label_yen.setText(_translate("MainWindow", "円"))
        self.pshBtn_executeRegistration.setText(_translate("MainWindow", "記帳"))
        self.label_selectedAccount.setText(_translate("MainWindow", "---"))
        self.menu_file.setTitle(_translate("MainWindow", "ファイル"))
        self.menu_fileOutput.setTitle(_translate("MainWindow", "書き出し"))
        self.menu_edit.setTitle(_translate("MainWindow", "編集"))
        self.menu_tools.setTitle(_translate("MainWindow", "ツール"))
        self.action_create.setText(_translate("MainWindow", "新規作成"))
        self.action_create.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.action_open.setText(_translate("MainWindow", "開く"))
        self.action_open.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.action_outputExcel.setText(_translate("MainWindow", "Excel"))
        self.action_outputExcel.setShortcut(_translate("MainWindow", "Ctrl+Shift+E"))
        self.action_outputCsv.setText(_translate("MainWindow", "CSV"))
        self.action_outputCsv.setShortcut(_translate("MainWindow", "Ctrl+Shift+C"))
        self.action_quit.setText(_translate("MainWindow", "終了"))
        self.action_quit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.action_editAccounts.setText(_translate("MainWindow", "勘定科目の編集"))
        self.action_editAccounts.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.action_bulkInsertion.setText(_translate("MainWindow", "月を指定して一括登録"))
        self.action_bulkInsertion.setShortcut(_translate("MainWindow", "Ctrl+Shift+I"))
        self.action_showStatistics.setText(_translate("MainWindow", "統計情報をグラフで表示"))
        self.action_showStatistics.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.action_showYearToYearComparison.setText(_translate("MainWindow", "他年度との比較"))
        self.action_showYearToYearComparison.setShortcut(_translate("MainWindow", "Ctrl+Shift+C"))
        self.action_balancing.setText(_translate("MainWindow", "帳尻合わせモード"))
        self.action_balancing.setShortcut(_translate("MainWindow", "Ctrl+Shift+B"))
