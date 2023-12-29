# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ip-check.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(838, 749)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        MainWindow.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(90, 30, 611, 751))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.tabWidget.setPalette(palette)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_main = QtWidgets.QWidget()
        self.tab_main.setObjectName("tab_main")
        self.lbl_upsince_date_val = QtWidgets.QLabel(self.tab_main)
        self.lbl_upsince_date_val.setGeometry(QtCore.QRect(450, 40, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.lbl_upsince_date_val.setFont(font)
        self.lbl_upsince_date_val.setObjectName("lbl_upsince_date_val")
        self.label = QtWidgets.QLabel(self.tab_main)
        self.label.setGeometry(QtCore.QRect(220, 90, 151, 91))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.label.setFont(font)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Resources/check.PNG"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.lbl_upsince = QtWidgets.QLabel(self.tab_main)
        self.lbl_upsince.setGeometry(QtCore.QRect(450, 0, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.lbl_upsince.setFont(font)
        self.lbl_upsince.setObjectName("lbl_upsince")
        self.lbl_current_ip_since_date_time = QtWidgets.QLabel(self.tab_main)
        self.lbl_current_ip_since_date_time.setGeometry(QtCore.QRect(250, 230, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.lbl_current_ip_since_date_time.setFont(font)
        self.lbl_current_ip_since_date_time.setObjectName("lbl_current_ip_since_date_time")
        self.btn_set_interval = QtWidgets.QPushButton(self.tab_main)
        self.btn_set_interval.setGeometry(QtCore.QRect(510, 340, 41, 23))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.btn_set_interval.setFont(font)
        self.btn_set_interval.setCheckable(False)
        self.btn_set_interval.setObjectName("btn_set_interval")
        self.lbl_next_ipcheck_val = QtWidgets.QLabel(self.tab_main)
        self.lbl_next_ipcheck_val.setGeometry(QtCore.QRect(110, 340, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.lbl_next_ipcheck_val.setFont(font)
        self.lbl_next_ipcheck_val.setObjectName("lbl_next_ipcheck_val")
        self.lbl_last_ipcheck_time_val = QtWidgets.QLabel(self.tab_main)
        self.lbl_last_ipcheck_time_val.setGeometry(QtCore.QRect(110, 320, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.lbl_last_ipcheck_time_val.setFont(font)
        self.lbl_last_ipcheck_time_val.setObjectName("lbl_last_ipcheck_time_val")
        self.lbl_lastipcheck = QtWidgets.QLabel(self.tab_main)
        self.lbl_lastipcheck.setGeometry(QtCore.QRect(30, 320, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.lbl_lastipcheck.setFont(font)
        self.lbl_lastipcheck.setObjectName("lbl_lastipcheck")
        self.lbl_ipcheckevery = QtWidgets.QLabel(self.tab_main)
        self.lbl_ipcheckevery.setGeometry(QtCore.QRect(430, 310, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.lbl_ipcheckevery.setFont(font)
        self.lbl_ipcheckevery.setObjectName("lbl_ipcheckevery")
        self.lbl_upsince_time_val = QtWidgets.QLabel(self.tab_main)
        self.lbl_upsince_time_val.setGeometry(QtCore.QRect(450, 10, 111, 41))
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
        self.lbl_s = QtWidgets.QLabel(self.tab_main)
        self.lbl_s.setGeometry(QtCore.QRect(500, 340, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.lbl_s.setFont(font)
        self.lbl_s.setObjectName("lbl_s")
        self.lbl_nextipcheck = QtWidgets.QLabel(self.tab_main)
        self.lbl_nextipcheck.setGeometry(QtCore.QRect(30, 340, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.lbl_nextipcheck.setFont(font)
        self.lbl_nextipcheck.setObjectName("lbl_nextipcheck")
        self.lbl_since = QtWidgets.QLabel(self.tab_main)
        self.lbl_since.setGeometry(QtCore.QRect(210, 230, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.lbl_since.setFont(font)
        self.lbl_since.setObjectName("lbl_since")
        self.lbl_current_ip = QtWidgets.QLabel(self.tab_main)
        self.lbl_current_ip.setGeometry(QtCore.QRect(210, 200, 181, 39))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_current_ip.setFont(font)
        self.lbl_current_ip.setObjectName("lbl_current_ip")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_main)
        self.lineEdit.setGeometry(QtCore.QRect(430, 340, 61, 20))
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
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 56, 56))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.treeView.setPalette(palette)
        self.treeView.setObjectName("treeView")
        self.btn_domains = QtWidgets.QPushButton(self.tab_domains)
        self.btn_domains.setGeometry(QtCore.QRect(340, 50, 75, 23))
        self.btn_domains.setObjectName("btn_domains")
        self.tabWidget.addTab(self.tab_domains, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.btn_table = QtWidgets.QPushButton(self.tab)
        self.btn_table.setGeometry(QtCore.QRect(440, 0, 75, 23))
        self.btn_table.setObjectName("btn_table")
        self.btn_update_dns = QtWidgets.QPushButton(self.tab)
        self.btn_update_dns.setGeometry(QtCore.QRect(360, 0, 75, 23))
        self.btn_update_dns.setObjectName("btn_update_dns")
        self.tabWidget.addTab(self.tab, "")
        self.tab_account = QtWidgets.QWidget()
        self.tab_account.setObjectName("tab_account")
        self.TokenInput = QtWidgets.QLineEdit(self.tab_account)
        self.TokenInput.setGeometry(QtCore.QRect(210, 110, 113, 20))
        self.TokenInput.setObjectName("TokenInput")
        self.SecretInput = QtWidgets.QLineEdit(self.tab_account)
        self.SecretInput.setGeometry(QtCore.QRect(210, 150, 271, 20))
        self.SecretInput.setObjectName("SecretInput")
        self.label_2 = QtWidgets.QLabel(self.tab_account)
        self.label_2.setGeometry(QtCore.QRect(140, 110, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab_account)
        self.label_3.setGeometry(QtCore.QRect(140, 160, 47, 13))
        self.label_3.setObjectName("label_3")
        self.btn_SubmitCred = QtWidgets.QPushButton(self.tab_account)
        self.btn_SubmitCred.setGeometry(QtCore.QRect(360, 220, 111, 23))
        self.btn_SubmitCred.setObjectName("btn_SubmitCred")
        self.Check_SaveCred = QtWidgets.QCheckBox(self.tab_account)
        self.Check_SaveCred.setGeometry(QtCore.QRect(200, 220, 101, 21))
        self.Check_SaveCred.setObjectName("Check_SaveCred")
        self.RegistrarInput = QtWidgets.QComboBox(self.tab_account)
        self.RegistrarInput.setGeometry(QtCore.QRect(210, 70, 111, 22))
        self.RegistrarInput.setObjectName("RegistrarInput")
        self.lbl_Registrar = QtWidgets.QLabel(self.tab_account)
        self.lbl_Registrar.setGeometry(QtCore.QRect(140, 70, 47, 20))
        self.lbl_Registrar.setObjectName("lbl_Registrar")
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
        self.actionLogging_on = QtWidgets.QAction(MainWindow)
        self.actionLogging_on.setCheckable(True)
        self.actionLogging_on.setChecked(True)
        self.actionLogging_on.setObjectName("actionLogging_on")
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
        self.menuSettings.addAction(self.actionLogging_on)
        self.menuHelp.addAction(self.actionMy_Help)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_upsince_date_val.setText(_translate("MainWindow", "12.12.1923"))
        self.lbl_upsince.setText(_translate("MainWindow", "Up since:"))
        self.lbl_current_ip_since_date_time.setText(_translate("MainWindow", "12.12.1923"))
        self.btn_set_interval.setText(_translate("MainWindow", "Set"))
        self.lbl_next_ipcheck_val.setText(_translate("MainWindow", "TextLabel"))
        self.lbl_last_ipcheck_time_val.setText(_translate("MainWindow", "TextLabel"))
        self.lbl_lastipcheck.setText(_translate("MainWindow", "Last ip-check:"))
        self.lbl_ipcheckevery.setText(_translate("MainWindow", "IP-check every:"))
        self.lbl_upsince_time_val.setText(_translate("MainWindow", "00:00:00"))
        self.lbl_date_val.setText(_translate("MainWindow", "12.12.1923"))
        self.lbl_s.setText(_translate("MainWindow", "s."))
        self.lbl_nextipcheck.setText(_translate("MainWindow", "Next ip-check"))
        self.lbl_since.setText(_translate("MainWindow", "Since:"))
        self.lbl_current_ip.setText(_translate("MainWindow", "88.223.66.89"))
        self.lineEdit.setToolTip(_translate("MainWindow", "<html><head/><body><p>test</p></body></html>"))
        self.lbl_time_val.setText(_translate("MainWindow", "00:00:00"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_main), _translate("MainWindow", "Main"))
        self.btn_domains.setText(_translate("MainWindow", "Domains"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_domains), _translate("MainWindow", "Domains"))
        self.btn_table.setText(_translate("MainWindow", "Load Domains"))
        self.btn_update_dns.setText(_translate("MainWindow", "Update dns"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Table view"))
        self.label_2.setText(_translate("MainWindow", "Token"))
        self.label_3.setText(_translate("MainWindow", "Secret"))
        self.btn_SubmitCred.setText(_translate("MainWindow", "Submit credentials"))
        self.Check_SaveCred.setText(_translate("MainWindow", "Save credentials"))
        self.lbl_Registrar.setText(_translate("MainWindow", "Registrar"))
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
        self.actionLogging_on.setText(_translate("MainWindow", "Logging"))
