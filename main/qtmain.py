# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.taskManager = QtWidgets.QTabWidget(self.centralwidget)
        self.taskManager.setFocusPolicy(QtCore.Qt.TabFocus)
        self.taskManager.setElideMode(QtCore.Qt.ElideMiddle)
        self.taskManager.setDocumentMode(True)
        self.taskManager.setTabsClosable(False)
        self.taskManager.setMovable(True)
        self.taskManager.setTabBarAutoHide(False)
        self.taskManager.setObjectName("taskManager")
        self.task1 = QtWidgets.QWidget()
        self.task1.setObjectName("task1")
        self.taskManager.addTab(self.task1, "")
        self.task2 = QtWidgets.QWidget()
        self.task2.setObjectName("task2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.task2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.focusStacking = QtWidgets.QGridLayout()
        self.focusStacking.setObjectName("focusStacking")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.task2)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 713, 465))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.image_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_label.sizePolicy().hasHeightForWidth())
        self.image_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setItalic(True)
        self.image_label.setFont(font)
        self.image_label.setText("")
        self.image_label.setPixmap(QtGui.QPixmap("../focus-stacking/merged.png"))
        self.image_label.setScaledContents(True)
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label.setObjectName("image_label")
        self.verticalLayout_2.addWidget(self.image_label)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.focusStacking.addWidget(self.scrollArea_3, 1, 1, 1, 1)
        self.r_button_2 = QtWidgets.QPushButton(self.task2)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setItalic(True)
        self.r_button_2.setFont(font)
        self.r_button_2.setStyleSheet("border:0px;\n"
"color: black;")
        self.r_button_2.setObjectName("r_button_2")
        self.focusStacking.addWidget(self.r_button_2, 1, 2, 1, 1)
        self.l_button_2 = QtWidgets.QPushButton(self.task2)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setItalic(True)
        self.l_button_2.setFont(font)
        self.l_button_2.setStyleSheet("border:0px;\n"
"color: black;")
        self.l_button_2.setText("<")
        self.l_button_2.setIconSize(QtCore.QSize(40, 40))
        self.l_button_2.setObjectName("l_button_2")
        self.focusStacking.addWidget(self.l_button_2, 1, 0, 1, 1)
        self.filename_label = QtWidgets.QLabel(self.task2)
        self.filename_label.setObjectName("filename_label")
        self.focusStacking.addWidget(self.filename_label, 0, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.focusStacking)
        self.taskManager.addTab(self.task2, "")
        self.task4 = QtWidgets.QWidget()
        self.task4.setObjectName("task4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.task4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.taskManager.addTab(self.task4, "")
        self.task5 = QtWidgets.QWidget()
        self.task5.setObjectName("task5")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.task5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.photochanges = QtWidgets.QGridLayout()
        self.photochanges.setObjectName("photochanges")
        self.l_button = QtWidgets.QPushButton(self.task5)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.l_button.setFont(font)
        self.l_button.setStyleSheet("border:0px;\n"
"color: black;")
        self.l_button.setObjectName("l_button")
        self.photochanges.addWidget(self.l_button, 1, 0, 1, 1)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.task5)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 351, 453))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.secondimages = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.secondimages.sizePolicy().hasHeightForWidth())
        self.secondimages.setSizePolicy(sizePolicy)
        self.secondimages.setText("")
        self.secondimages.setPixmap(QtGui.QPixmap("../focus-stacking/merged.png"))
        self.secondimages.setScaledContents(True)
        self.secondimages.setObjectName("secondimages")
        self.horizontalLayout_3.addWidget(self.secondimages)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.photochanges.addWidget(self.scrollArea_2, 1, 2, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.task5)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 351, 453))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.firstimages = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.firstimages.sizePolicy().hasHeightForWidth())
        self.firstimages.setSizePolicy(sizePolicy)
        self.firstimages.setText("")
        self.firstimages.setPixmap(QtGui.QPixmap("../focus-stacking/merged.png"))
        self.firstimages.setScaledContents(True)
        self.firstimages.setObjectName("firstimages")
        self.horizontalLayout_2.addWidget(self.firstimages)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.photochanges.addWidget(self.scrollArea, 1, 1, 1, 1)
        self.r_button = QtWidgets.QPushButton(self.task5)
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.r_button.setFont(font)
        self.r_button.setStyleSheet("border:0px;\n"
"color: black;")
        self.r_button.setObjectName("r_button")
        self.photochanges.addWidget(self.r_button, 1, 3, 1, 1)
        self.load2images = QtWidgets.QPushButton(self.task5)
        self.load2images.setObjectName("load2images")
        self.photochanges.addWidget(self.load2images, 0, 2, 1, 1)
        self.load1images = QtWidgets.QPushButton(self.task5)
        self.load1images.setObjectName("load1images")
        self.photochanges.addWidget(self.load1images, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.photochanges)
        self.taskManager.addTab(self.task5, "")
        self.task6 = QtWidgets.QWidget()
        self.task6.setObjectName("task6")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.task6)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.colorChanges = QtWidgets.QSplitter(self.task6)
        self.colorChanges.setOrientation(QtCore.Qt.Horizontal)
        self.colorChanges.setObjectName("colorChanges")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.colorChanges)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.listColor = QtWidgets.QListWidget(self.verticalLayoutWidget_2)
        self.listColor.setObjectName("listColor")
        self.verticalLayout_10.addWidget(self.listColor)
        self.findColors = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.findColors.setObjectName("findColors")
        self.verticalLayout_10.addWidget(self.findColors)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.colorChanges)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.scrollArea_4 = QtWidgets.QScrollArea(self.verticalLayoutWidget)
        self.scrollArea_4.setMinimumSize(QtCore.QSize(600, 400))
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 598, 487))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents_5.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_5.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.task6Image = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.task6Image.sizePolicy().hasHeightForWidth())
        self.task6Image.setSizePolicy(sizePolicy)
        self.task6Image.setText("")
        self.task6Image.setPixmap(QtGui.QPixmap("../../Original/2016_0101_000725_002.JPG"))
        self.task6Image.setScaledContents(True)
        self.task6Image.setObjectName("task6Image")
        self.verticalLayout_7.addWidget(self.task6Image)
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_5)
        self.verticalLayout_8.addWidget(self.scrollArea_4)
        self.verticalLayout_11.addWidget(self.colorChanges)
        self.taskManager.addTab(self.task6, "")
        self.horizontalLayout.addWidget(self.taskManager)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAction = QtWidgets.QMenu(self.menuFile)
        self.menuAction.setObjectName("menuAction")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionFind_the_difference = QtWidgets.QAction(MainWindow)
        self.actionFind_the_difference.setObjectName("actionFind_the_difference")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionFocus_stacking = QtWidgets.QAction(MainWindow)
        self.actionFocus_stacking.setObjectName("actionFocus_stacking")
        self.menuAction.addAction(self.actionFind_the_difference)
        self.menuAction.addAction(self.actionFocus_stacking)
        self.menuFile.addAction(self.menuAction.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.taskManager.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.taskManager.setTabText(self.taskManager.indexOf(self.task1), _translate("MainWindow", "Task1"))
        self.r_button_2.setText(_translate("MainWindow", ">"))
        self.filename_label.setText(_translate("MainWindow", "hello.png"))
        self.taskManager.setTabText(self.taskManager.indexOf(self.task2), _translate("MainWindow", "Task2"))
        self.taskManager.setTabText(self.taskManager.indexOf(self.task4), _translate("MainWindow", "Task4"))
        self.l_button.setText(_translate("MainWindow", "<"))
        self.r_button.setText(_translate("MainWindow", ">"))
        self.load2images.setText(_translate("MainWindow", "Second bunch of images"))
        self.load1images.setText(_translate("MainWindow", "First bunch of images"))
        self.taskManager.setTabText(self.taskManager.indexOf(self.task5), _translate("MainWindow", "Task5"))
        self.findColors.setText(_translate("MainWindow", "Find the colors"))
        self.taskManager.setTabText(self.taskManager.indexOf(self.task6), _translate("MainWindow", "Task6"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAction.setTitle(_translate("MainWindow", "Action"))
        self.actionFind_the_difference.setText(_translate("MainWindow", "Find the difference"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionFocus_stacking.setText(_translate("MainWindow", "Focus stacking"))
