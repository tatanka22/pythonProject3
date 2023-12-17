# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ip-check.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(838, 749)
        MainWindow.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(110, 20, 551, 681))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_main = QtWidgets.QWidget()
        self.tab_main.setObjectName("tab_main")
        self.lbl_upsince_date_val = QtWidgets.QLabel(self.tab_main)
        self.lbl_upsince_date_val.setGeometry(QtCore.QRect(420, 40, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.lbl_upsince_date_val.setFont(font)
        self.lbl_upsince_date_val.setObjectName("lbl_upsince_date_val")
        self.label = QtWidgets.QLabel(self.tab_main)
        self.label.setGeometry(QtCore.QRect(200, 90, 151, 91))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.label.setFont(font)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("check.PNG"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.lbl_upsince = QtWidgets.QLabel(self.tab_main)
        self.lbl_upsince.setGeometry(QtCore.QRect(420, 0, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.lbl_upsince.setFont(font)
        self.lbl_upsince.setObjectName("lbl_upsince")
        self.lbl_lastip_since_date = QtWidgets.QLabel(self.tab_main)
        self.lbl_lastip_since_date.setGeometry(QtCore.QRect(470, 220, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.lbl_lastip_since_date.setFont(font)
        self.lbl_lastip_since_date.setObjectName("lbl_lastip_since_date")
        self.btn_set_interval = QtWidgets.QPushButton(self.tab_main)
        self.btn_set_interval.setGeometry(QtCore.QRect(470, 330, 41, 23))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.btn_set_interval.setFont(font)
        self.btn_set_interval.setCheckable(False)
        self.btn_set_interval.setObjectName("btn_set_interval")
        self.lbl_next_ipcheck_val = QtWidgets.QLabel(self.tab_main)
        self.lbl_next_ipcheck_val.setGeometry(QtCore.QRect(110, 340, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.lbl_next_ipcheck_val.setFont(font)
        self.lbl_next_ipcheck_val.setObjectName("lbl_next_ipcheck_val")
        self.lbl_last_ipcheck_time_val = QtWidgets.QLabel(self.tab_main)
        self.lbl_last_ipcheck_time_val.setGeometry(QtCore.QRect(110, 320, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.lbl_last_ipcheck_time_val.setFont(font)
        self.lbl_last_ipcheck_time_val.setObjectName("lbl_last_ipcheck_time_val")
        self.lbl_lastipcheck = QtWidgets.QLabel(self.tab_main)
        self.lbl_lastipcheck.setGeometry(QtCore.QRect(30, 310, 130, 39))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.lbl_lastipcheck.setFont(font)
        self.lbl_lastipcheck.setObjectName("lbl_lastipcheck")
        self.lbl_ipcheckevery = QtWidgets.QLabel(self.tab_main)
        self.lbl_ipcheckevery.setGeometry(QtCore.QRect(370, 310, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.lbl_ipcheckevery.setFont(font)
        self.lbl_ipcheckevery.setObjectName("lbl_ipcheckevery")
        self.lbl_upsince_time_val = QtWidgets.QLabel(self.tab_main)
        self.lbl_upsince_time_val.setGeometry(QtCore.QRect(420, 10, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(18)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(False)
        self.lbl_upsince_time_val.setFont(font)
        self.lbl_upsince_time_val.setObjectName("lbl_upsince_time_val")
        self.lbl_date_val = QtWidgets.QLabel(self.tab_main)
        self.lbl_date_val.setGeometry(QtCore.QRect(30, 40, 130, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.lbl_date_val.setFont(font)
        self.lbl_date_val.setObjectName("lbl_date_val")
        self.lbl_current_ip = QtWidgets.QLabel(self.tab_main)
        self.lbl_current_ip.setGeometry(QtCore.QRect(230, 180, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.lbl_current_ip.setFont(font)
        self.lbl_current_ip.setObjectName("lbl_current_ip")
        self.lbl_s = QtWidgets.QLabel(self.tab_main)
        self.lbl_s.setGeometry(QtCore.QRect(440, 340, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.lbl_s.setFont(font)
        self.lbl_s.setObjectName("lbl_s")
        self.lbl_nextipcheck = QtWidgets.QLabel(self.tab_main)
        self.lbl_nextipcheck.setGeometry(QtCore.QRect(30, 340, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.lbl_nextipcheck.setFont(font)
        self.lbl_nextipcheck.setObjectName("lbl_nextipcheck")
        self.lbl_lastip_since_time_val = QtWidgets.QLabel(self.tab_main)
        self.lbl_lastip_since_time_val.setGeometry(QtCore.QRect(410, 220, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(8)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(False)
        self.lbl_lastip_since_time_val.setFont(font)
        self.lbl_lastip_since_time_val.setObjectName("lbl_lastip_since_time_val")
        self.lbl_lastipsince = QtWidgets.QLabel(self.tab_main)
        self.lbl_lastipsince.setGeometry(QtCore.QRect(370, 220, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.lbl_lastipsince.setFont(font)
        self.lbl_lastipsince.setObjectName("lbl_lastipsince")
        self.lbl_lastip_val = QtWidgets.QLabel(self.tab_main)
        self.lbl_lastip_val.setGeometry(QtCore.QRect(220, 210, 131, 39))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_lastip_val.setFont(font)
        self.lbl_lastip_val.setObjectName("lbl_lastip_val")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_main)
        self.lineEdit.setGeometry(QtCore.QRect(370, 340, 61, 20))
        self.lineEdit.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.lineEdit.setFont(font)
        self.lineEdit.setWhatsThis("")
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit.setObjectName("lineEdit")
        self.lbl_time_val = QtWidgets.QLabel(self.tab_main)
        self.lbl_time_val.setGeometry(QtCore.QRect(30, 10, 121, 39))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(18)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.lbl_time_val.setFont(font)
        self.lbl_time_val.setObjectName("lbl_time_val")
        self.tabWidget.addTab(self.tab_main, "")
        self.tab_domains = QtWidgets.QWidget()
        self.tab_domains.setObjectName("tab_domains")
        self.treeView = QtWidgets.QTreeView(self.tab_domains)
        self.treeView.setGeometry(QtCore.QRect(30, 30, 391, 611))
        self.treeView.setObjectName("treeView")
        self.btn_domains = QtWidgets.QPushButton(self.tab_domains)
        self.btn_domains.setGeometry(QtCore.QRect(340, 50, 75, 23))
        self.btn_domains.setObjectName("btn_domains")
        self.tabWidget.addTab(self.tab_domains, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableView = QtWidgets.QTableView(self.tab)
        self.tableView.setGeometry(QtCore.QRect(0, 30, 511, 621))
        self.tableView.setObjectName("tableView")
        self.btn_table = QtWidgets.QPushButton(self.tab)
        self.btn_table.setGeometry(QtCore.QRect(440, 0, 75, 23))
        self.btn_table.setObjectName("btn_table")
        self.tabWidget.addTab(self.tab, "")
        self.tab_account = QtWidgets.QWidget()
        self.tab_account.setObjectName("tab_account")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_account)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 50, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_account)
        self.lineEdit_3.setGeometry(QtCore.QRect(210, 90, 271, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_2 = QtWidgets.QLabel(self.tab_account)
        self.label_2.setGeometry(QtCore.QRect(140, 50, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab_account)
        self.label_3.setGeometry(QtCore.QRect(140, 100, 47, 13))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.tab_account)
        self.pushButton.setGeometry(QtCore.QRect(370, 130, 111, 23))
        self.pushButton.setObjectName("pushButton")
        self.checkBox = QtWidgets.QCheckBox(self.tab_account)
        self.checkBox.setGeometry(QtCore.QRect(210, 130, 101, 21))
        self.checkBox.setObjectName("checkBox")
        self.tabWidget.addTab(self.tab_account, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 838, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionMy_Help = QtWidgets.QAction(MainWindow)
        self.actionMy_Help.setObjectName("actionMy_Help")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionSound_alerts = QtWidgets.QAction(MainWindow)
        self.actionSound_alerts.setCheckable(True)
        self.actionSound_alerts.setChecked(True)
        self.actionSound_alerts.setObjectName("actionSound_alerts")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuSettings.addAction(self.actionSound_alerts)
        self.menuHelp.addAction(self.actionMy_Help)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_upsince_date_val.setText(_translate("MainWindow", "12.12.1923"))
        self.lbl_upsince.setText(_translate("MainWindow", "Up since:"))
        self.lbl_lastip_since_date.setText(_translate("MainWindow", "12.12.1923"))
        self.btn_set_interval.setText(_translate("MainWindow", "Set"))
        self.lbl_next_ipcheck_val.setText(_translate("MainWindow", "TextLabel"))
        self.lbl_last_ipcheck_time_val.setText(_translate("MainWindow", "TextLabel"))
        self.lbl_lastipcheck.setText(_translate("MainWindow", "Last ip-check:"))
        self.lbl_ipcheckevery.setText(_translate("MainWindow", "IP-check every:"))
        self.lbl_upsince_time_val.setText(_translate("MainWindow", "00:00:00"))
        self.lbl_date_val.setText(_translate("MainWindow", "12.12.1923"))
        self.lbl_current_ip.setText(_translate("MainWindow", "Current IP"))
        self.lbl_s.setText(_translate("MainWindow", "s."))
        self.lbl_nextipcheck.setText(_translate("MainWindow", "Next ip-check"))
        self.lbl_lastip_since_time_val.setText(_translate("MainWindow", "00:00:00"))
        self.lbl_lastipsince.setText(_translate("MainWindow", "Since:"))
        self.lbl_lastip_val.setText(_translate("MainWindow", "88.223.66.89"))
        self.lineEdit.setToolTip(_translate("MainWindow", "<html><head/><body><p>test</p></body></html>"))
        self.lbl_time_val.setText(_translate("MainWindow", "00:00:00"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_main), _translate("MainWindow", "Main"))
        self.btn_domains.setText(_translate("MainWindow", "Domains"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_domains), _translate("MainWindow", "Domains"))
        self.btn_table.setText(_translate("MainWindow", "Load Domains"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Table view"))
        self.label_2.setText(_translate("MainWindow", "Token"))
        self.label_3.setText(_translate("MainWindow", "Secret"))
        self.pushButton.setText(_translate("MainWindow", "Submit credentials"))
        self.checkBox.setText(_translate("MainWindow", "Save credentials"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_account), _translate("MainWindow", "Account"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionMy_Help.setText(_translate("MainWindow", "My Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as..."))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionSound_alerts.setText(_translate("MainWindow", "Sound alerts"))
