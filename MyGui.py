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
        MainWindow.resize(602, 403)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(90, 20, 491, 251))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_lastipcheck = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lbl_lastipcheck.setObjectName("lbl_lastipcheck")
        self.gridLayout.addWidget(self.lbl_lastipcheck, 2, 1, 1, 1)
        self.lbl_lastipsince = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lbl_lastipsince.setObjectName("lbl_lastipsince")
        self.gridLayout.addWidget(self.lbl_lastipsince, 4, 1, 1, 1)
        self.lbl_lastip_val = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lbl_lastip_val.setObjectName("lbl_lastip_val")
        self.gridLayout.addWidget(self.lbl_lastip_val, 2, 3, 1, 1)
        self.label_upsince_val = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_upsince_val.setObjectName("label_upsince_val")
        self.gridLayout.addWidget(self.label_upsince_val, 1, 2, 1, 1)
        self.lbl_lastipsincetime_val = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lbl_lastipsincetime_val.setObjectName("lbl_lastipsincetime_val")
        self.gridLayout.addWidget(self.lbl_lastipsincetime_val, 4, 2, 1, 1)
        self.lbl_lastipsincedate_val = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lbl_lastipsincedate_val.setObjectName("lbl_lastipsincedate_val")
        self.gridLayout.addWidget(self.lbl_lastipsincedate_val, 4, 3, 1, 1)
        self.lbl_lastipchecktime_val = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lbl_lastipchecktime_val.setObjectName("lbl_lastipchecktime_val")
        self.gridLayout.addWidget(self.lbl_lastipchecktime_val, 2, 2, 1, 1)
        self.SetBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.SetBtn.setCheckable(False)
        self.SetBtn.setObjectName("SetBtn")
        self.gridLayout.addWidget(self.SetBtn, 6, 4, 1, 1)
        self.lbl_upsince = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lbl_upsince.setObjectName("lbl_upsince")
        self.gridLayout.addWidget(self.lbl_upsince, 1, 1, 1, 1)
        self.lbl_nextipcheck = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lbl_nextipcheck.setObjectName("lbl_nextipcheck")
        self.gridLayout.addWidget(self.lbl_nextipcheck, 3, 1, 1, 1)
        self.lbl_nextipcheck_val = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lbl_nextipcheck_val.setObjectName("lbl_nextipcheck_val")
        self.gridLayout.addWidget(self.lbl_nextipcheck_val, 3, 2, 1, 1)
        self.lbl_s = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lbl_s.setObjectName("lbl_s")
        self.gridLayout.addWidget(self.lbl_s, 6, 3, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 6, 2, 1, 1)
        self.lbl_ipcheckevery = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lbl_ipcheckevery.setObjectName("lbl_ipcheckevery")
        self.gridLayout.addWidget(self.lbl_ipcheckevery, 6, 1, 1, 1)
        self.lbl_time = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lbl_time.setObjectName("lbl_time")
        self.gridLayout.addWidget(self.lbl_time, 0, 1, 1, 1)
        self.lbl_time_val = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lbl_time_val.setObjectName("lbl_time_val")
        self.gridLayout.addWidget(self.lbl_time_val, 0, 2, 1, 1)
        self.lbl_date = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lbl_date.setObjectName("lbl_date")
        self.gridLayout.addWidget(self.lbl_date, 0, 3, 1, 1)
        self.lbl_date_val = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lbl_date_val.setObjectName("lbl_date_val")
        self.gridLayout.addWidget(self.lbl_date_val, 0, 4, 1, 1)
        self.lbl_upsince_date_val = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lbl_upsince_date_val.setObjectName("lbl_upsince_date_val")
        self.gridLayout.addWidget(self.lbl_upsince_date_val, 1, 3, 1, 1)
        self.lbl_ipcheckevery.raise_()
        self.lbl_lastipchecktime_val.raise_()
        self.lbl_lastipcheck.raise_()
        self.lbl_time.raise_()
        self.lbl_nextipcheck_val.raise_()
        self.lbl_nextipcheck.raise_()
        self.lbl_lastipsincetime_val.raise_()
        self.lbl_lastipsince.raise_()
        self.lineEdit.raise_()
        self.lbl_s.raise_()
        self.SetBtn.raise_()
        self.lbl_lastipsincedate_val.raise_()
        self.lbl_lastip_val.raise_()
        self.lbl_upsince.raise_()
        self.label_upsince_val.raise_()
        self.lbl_time_val.raise_()
        self.lbl_date.raise_()
        self.lbl_date_val.raise_()
        self.lbl_upsince_date_val.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 602, 26))
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
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionMy_Help)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_lastipcheck.setText(_translate("MainWindow", "Last ip-check:"))
        self.lbl_lastipsince.setText(_translate("MainWindow", "Last ip since:"))
        self.lbl_lastip_val.setText(_translate("MainWindow", "TextLabel"))
        self.label_upsince_val.setText(_translate("MainWindow", "TextLabel"))
        self.lbl_lastipsincetime_val.setText(_translate("MainWindow", "TextLabel"))
        self.lbl_lastipsincedate_val.setText(_translate("MainWindow", "TextLabel"))
        self.lbl_lastipchecktime_val.setText(_translate("MainWindow", "TextLabel"))
        self.SetBtn.setText(_translate("MainWindow", "Set"))
        self.lbl_upsince.setText(_translate("MainWindow", "Up since:"))
        self.lbl_nextipcheck.setText(_translate("MainWindow", "Next ip-check"))
        self.lbl_nextipcheck_val.setText(_translate("MainWindow", "TextLabel"))
        self.lbl_s.setText(_translate("MainWindow", "s."))
        self.lbl_ipcheckevery.setText(_translate("MainWindow", "IP-check every:"))
        self.lbl_time.setText(_translate("MainWindow", "Time:"))
        self.lbl_time_val.setText(_translate("MainWindow", "TextLabel"))
        self.lbl_date.setText(_translate("MainWindow", "Date:"))
        self.lbl_date_val.setText(_translate("MainWindow", "TextLabel"))
        self.lbl_upsince_date_val.setText(_translate("MainWindow", "TextLabel"))
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
