# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QT_Creator_App_testing.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect, QTimer,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLCDNumber, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import Controller_Client_TCP as Controller_Client_TCP

startStop = False
startStop_logger = False
status_pulsante_interfaccia = 1
status_pulsante_registrazione = 1

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1101, 679)
        MainWindow.setStyleSheet(u"QWidget {\n"
"	background-color:black; \n"
"	border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: black;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget {\n"
"	background-color:black; \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"}\n"
"")
        self.horizontalLayout_7 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.Lay_L = QHBoxLayout()
        self.Lay_L.setObjectName(u"Lay_L")
        self.Wid_L = QWidget(self.centralwidget)
        self.Wid_L.setObjectName(u"Wid_L")
        self.Wid_L.setStyleSheet(u"QWidget {\n"
"	background-color:orange; \n"
"	border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: black;\n"
"}\n"
"")
        self.verticalLayout_5 = QVBoxLayout(self.Wid_L)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.Wid_L)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QWidget {\n"
"	background-color:orange; \n"
"	border-style: outset;\n"
"    border-width: 0px;\n"
"    border-color: black;\n"
"}\n"
"")
        self.gridLayout_3 = QGridLayout(self.widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.comboBox_1 = QComboBox(self.widget)
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.setObjectName(u"comboBox_1")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_1.sizePolicy().hasHeightForWidth())
        self.comboBox_1.setSizePolicy(sizePolicy)
        self.comboBox_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_1.setMouseTracking(False)
        self.comboBox_1.setAutoFillBackground(False)
        self.comboBox_1.setStyleSheet(u"QComboBox {\n"
"    border: 3px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox{\n"
"	color: rgb(0,0,0);\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox"
                        "::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(/usr/share/icons/crystalsvg/16x16/actions/1downarrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}")
        self.comboBox_1.setIconSize(QSize(30, 30))

        self.gridLayout_3.addWidget(self.comboBox_1, 0, 1, 1, 1)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_1 = QLabel(self.widget)
        self.label_1.setObjectName(u"label_1")
        font = QFont()
        font.setPointSize(17)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet(u"QLabel{\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")

        self.verticalLayout_9.addWidget(self.label_1, 0, Qt.AlignHCenter)


        self.gridLayout_3.addLayout(self.verticalLayout_9, 0, 0, 1, 1)

        self.lcdNumber_1 = QLCDNumber(self.widget)
        self.lcdNumber_1.setObjectName(u"lcdNumber_1")
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(False)
        self.lcdNumber_1.setFont(font1)
        self.lcdNumber_1.setStyleSheet(u"QWidget {\n"
"	background-color:white; \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"}\n"
"QLCDNumber{\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.lcdNumber_1.setDigitCount(7)
        self.lcdNumber_1.setProperty("value", 0.000000000000000)

        self.gridLayout_3.addWidget(self.lcdNumber_1, 1, 0, 1, 2)


        self.verticalLayout.addWidget(self.widget)


        self.verticalLayout_5.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_3 = QWidget(self.Wid_L)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"QWidget {\n"
"	background-color:orange; \n"
"	border-style: outset;\n"
"    border-width: 0px;\n"
"    border-color: black;\n"
"}\n"
"")
        self.gridLayout_4 = QGridLayout(self.widget_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.comboBox_2 = QComboBox(self.widget_3)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)
        self.comboBox_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_2.setMouseTracking(False)
        self.comboBox_2.setAutoFillBackground(False)
        self.comboBox_2.setStyleSheet(u"QComboBox {\n"
"    border: 3px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox{\n"
"	color: rgb(0,0,0);\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox"
                        "::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(/usr/share/icons/crystalsvg/16x16/actions/1downarrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}")
        self.comboBox_2.setIconSize(QSize(30, 30))

        self.gridLayout_4.addWidget(self.comboBox_2, 0, 1, 1, 1)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"QLabel{\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")

        self.verticalLayout_10.addWidget(self.label_2, 0, Qt.AlignHCenter)


        self.gridLayout_4.addLayout(self.verticalLayout_10, 0, 0, 1, 1)

        self.lcdNumber_2 = QLCDNumber(self.widget_3)
        self.lcdNumber_2.setObjectName(u"lcdNumber_2")
        self.lcdNumber_2.setStyleSheet(u"QWidget {\n"
"	background-color:white; \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"}\n"
"QLCDNumber{\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.lcdNumber_2.setDigitCount(7)

        self.gridLayout_4.addWidget(self.lcdNumber_2, 1, 0, 1, 2)


        self.verticalLayout_2.addWidget(self.widget_3)


        self.verticalLayout_5.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_4 = QWidget(self.Wid_L)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setStyleSheet(u"QWidget {\n"
"	background-color:orange; \n"
"	border-style: outset;\n"
"    border-width: 0px;\n"
"    border-color: black;\n"
"}\n"
"")
        self.gridLayout_5 = QGridLayout(self.widget_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.comboBox_3 = QComboBox(self.widget_4)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        sizePolicy.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy)
        self.comboBox_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_3.setMouseTracking(False)
        self.comboBox_3.setAutoFillBackground(False)
        self.comboBox_3.setStyleSheet(u"QComboBox {\n"
"    border: 3px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox{\n"
"	color: rgb(0,0,0);\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox"
                        "::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(/usr/share/icons/crystalsvg/16x16/actions/1downarrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}")
        self.comboBox_3.setIconSize(QSize(30, 30))

        self.gridLayout_5.addWidget(self.comboBox_3, 0, 1, 1, 1)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_3 = QLabel(self.widget_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"QLabel{\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")

        self.verticalLayout_7.addWidget(self.label_3, 0, Qt.AlignHCenter)


        self.gridLayout_5.addLayout(self.verticalLayout_7, 0, 0, 1, 1)

        self.lcdNumber_3 = QLCDNumber(self.widget_4)
        self.lcdNumber_3.setObjectName(u"lcdNumber_3")
        font2 = QFont()
        font2.setBold(False)
        font2.setKerning(True)
        self.lcdNumber_3.setFont(font2)
        self.lcdNumber_3.setStyleSheet(u"QWidget {\n"
"	background-color:white; \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"}\n"
"QLCDNumber{\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.lcdNumber_3.setDigitCount(7)

        self.gridLayout_5.addWidget(self.lcdNumber_3, 1, 0, 1, 2)


        self.verticalLayout_3.addWidget(self.widget_4)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_5 = QWidget(self.Wid_L)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setStyleSheet(u"QWidget {\n"
"	background-color:orange; \n"
"	border-style: outset;\n"
"    border-width: 0px;\n"
"    border-color: black;\n"
"}\n"
"")
        self.gridLayout_6 = QGridLayout(self.widget_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_4 = QLabel(self.widget_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"QLabel{\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")

        self.verticalLayout_11.addWidget(self.label_4, 0, Qt.AlignHCenter)


        self.gridLayout_6.addLayout(self.verticalLayout_11, 0, 0, 1, 1)

        self.comboBox_4 = QComboBox(self.widget_5)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        sizePolicy.setHeightForWidth(self.comboBox_4.sizePolicy().hasHeightForWidth())
        self.comboBox_4.setSizePolicy(sizePolicy)
        self.comboBox_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_4.setMouseTracking(False)
        self.comboBox_4.setAutoFillBackground(False)
        self.comboBox_4.setStyleSheet(u"QComboBox {\n"
"    border: 3px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox{\n"
"	color: rgb(0,0,0);\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox"
                        "::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(/usr/share/icons/crystalsvg/16x16/actions/1downarrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}")
        self.comboBox_4.setIconSize(QSize(30, 30))

        self.gridLayout_6.addWidget(self.comboBox_4, 0, 1, 1, 1)

        self.lcdNumber_4 = QLCDNumber(self.widget_5)
        self.lcdNumber_4.setObjectName(u"lcdNumber_4")
        self.lcdNumber_4.setStyleSheet(u"QWidget {\n"
"	background-color:white; \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"}\n"
"QLCDNumber{\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.lcdNumber_4.setDigitCount(7)

        self.gridLayout_6.addWidget(self.lcdNumber_4, 1, 0, 1, 2)


        self.verticalLayout_4.addWidget(self.widget_5)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)


        self.Lay_L.addWidget(self.Wid_L)


        self.horizontalLayout_7.addLayout(self.Lay_L)

        self.Lay_R = QHBoxLayout()
        self.Lay_R.setObjectName(u"Lay_R")
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"QWidget {\n"
"	background-color:orange; \n"
"	border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: black;\n"
"}\n"
"")
        self.verticalLayout_14 = QVBoxLayout(self.widget_2)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget_12 = QWidget(self.widget_2)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setMaximumSize(QSize(16777215, 16777215))
        self.widget_12.setStyleSheet(u"QWidget {\n"
"	background-color:orange; \n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color: black;\n"
"}\n"
"")
        self.gridLayout_2 = QGridLayout(self.widget_12)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label = QLabel(self.widget_12)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setStyleSheet(u"QWidget {\n"
"	background-color:orange; \n"
"	border-style: outset;\n"
"    border-width: 0px;\n"
"    border-color: black;\n"
"}\n"
"QLabel{\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")

        self.horizontalLayout_6.addWidget(self.label, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.pushButton_Interfaccia = QPushButton(self.widget_12)
        self.pushButton_Interfaccia.setObjectName(u"pushButton_Interfaccia")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_Interfaccia.sizePolicy().hasHeightForWidth())
        self.pushButton_Interfaccia.setSizePolicy(sizePolicy1)
        self.pushButton_Interfaccia.setMinimumSize(QSize(200, 150))
        self.pushButton_Interfaccia.setMaximumSize(QSize(300, 200))
        font3 = QFont()
        font3.setPointSize(30)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setUnderline(False)
        font3.setStrikeOut(False)
        self.pushButton_Interfaccia.setFont(font3)
        self.pushButton_Interfaccia.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_Interfaccia.setStyleSheet(u"QWidget {\n"
"	background-color:green; \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"}\n"
"QPushButton{\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")

        self.horizontalLayout_6.addWidget(self.pushButton_Interfaccia)


        self.gridLayout_2.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_5 = QLabel(self.widget_12)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"QWidget {\n"
"	background-color:orange; \n"
"	border-style: outset;\n"
"    border-width: 0px;\n"
"    border-color: black;\n"
"}\n"
"QLabel{\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")

        self.horizontalLayout_8.addWidget(self.label_5, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.pushButton_Registrazione = QPushButton(self.widget_12)
        self.pushButton_Registrazione.setObjectName(u"pushButton_Registrazione")
        sizePolicy1.setHeightForWidth(self.pushButton_Registrazione.sizePolicy().hasHeightForWidth())
        self.pushButton_Registrazione.setSizePolicy(sizePolicy1)
        self.pushButton_Registrazione.setMinimumSize(QSize(200, 150))
        self.pushButton_Registrazione.setMaximumSize(QSize(300, 200))
        font4 = QFont()
        font4.setPointSize(30)
        font4.setBold(True)
        self.pushButton_Registrazione.setFont(font4)
        self.pushButton_Registrazione.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_Registrazione.setStyleSheet(u"QWidget {\n"
"	background-color:green; \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"}\n"
"QPushButton{\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")

        self.horizontalLayout_8.addWidget(self.pushButton_Registrazione)


        self.gridLayout_2.addLayout(self.horizontalLayout_8, 1, 0, 1, 1)


        self.verticalLayout_6.addWidget(self.widget_12)


        self.verticalLayout_14.addLayout(self.verticalLayout_6)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.widget_6 = QWidget(self.widget_2)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setStyleSheet(u"QWidget {\n"
"	background-color:orange; \n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color: black;\n"
"}\n"
"")
        self.verticalLayout_16 = QVBoxLayout(self.widget_6)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")

        self.verticalLayout_16.addLayout(self.horizontalLayout_9)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")

        self.verticalLayout_16.addLayout(self.verticalLayout_19)


        self.verticalLayout_12.addWidget(self.widget_6)


        self.verticalLayout_14.addLayout(self.verticalLayout_12)


        self.Lay_R.addWidget(self.widget_2)


        self.horizontalLayout_7.addLayout(self.Lay_R)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    
    #------------------------------------------------------------------------------------------------------------------#
    # Codice aggiunto da me
        lcdDisplay_list=[self.lcdNumber_1,self.lcdNumber_2,self.lcdNumber_3,self.lcdNumber_4]
    
    # setup segnali
        self.pushButton_Interfaccia.clicked.connect(self.pulsante_interfaccia_click)
        self.pushButton_Registrazione.clicked.connect(self.pulsante_registrazione_click)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        #self.comboBox_1.activated.connect(self.cambio unita di misura)
        
    
    def pulsante_interfaccia_click(self):
        # Check della condizione del pulsante e poi cambio il tipo e gestisco il timer
        global status_pulsante_interfaccia
        if status_pulsante_interfaccia % 2 != 0:
            self.timer.start(100)          # In millisecondi
            self.pushButton_Interfaccia.setText("STOP")
            self.pushButton_Interfaccia.setStyleSheet("background-color: red; border-style: outset; border-width: 2px; border-color: black; color: black")
            status_pulsante_interfaccia = status_pulsante_interfaccia + 1
        else:     
            self.timer.stop()
            self.lcdNumber_1.display(0)
            self.lcdNumber_2.display(0)
            self.lcdNumber_3.display(0)
            self.lcdNumber_4.display(0)         
            self.pushButton_Interfaccia.setStyleSheet("background-color: green; border-style: outset; border-width: 2px; border-color: black; color: black")
            self.pushButton_Interfaccia.setText("START")
            status_pulsante_interfaccia = status_pulsante_interfaccia + 1
    
    def pulsante_registrazione_click(self):
        # Check della condizione del pulsante e poi cambio il tipo e gestisco il logger
        global startStop_logger
        global status_pulsante_registrazione
        if status_pulsante_registrazione % 2 != 0:       
            startStop_logger = True
            self.pushButton_Registrazione.setText("STOP")
            self.pushButton_Registrazione.setStyleSheet("background-color: red; border-style: outset; border-width: 2px; border-color: black; color: black")
            status_pulsante_registrazione = status_pulsante_registrazione + 1
        else:     
            startStop_logger = False     
            self.pushButton_Registrazione.setText("START")     
            self.pushButton_Registrazione.setStyleSheet("background-color: green; border-style: outset; border-width: 2px; border-color: black; color: black")
            status_pulsante_registrazione = status_pulsante_registrazione + 1
        
        
    def update(self):
            list = Controller_Client_TCP.DATA_INTERACTIONS.get_mv()
            self.lcdNumber_1.display(list[0])
            self.lcdNumber_2.display(list[1])
            self.lcdNumber_3.display(list[2])
            self.lcdNumber_4.display(list[3])
                
    
    
    
    #------------------------------------------------------------------------------------------------------------------# 
    


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.comboBox_1.setItemText(0, QCoreApplication.translate("MainWindow", u"mV", None))
        self.comboBox_1.setItemText(1, QCoreApplication.translate("MainWindow", u"Nm", None))
        self.comboBox_1.setItemText(2, QCoreApplication.translate("MainWindow", u"Kg", None))
        self.comboBox_1.setItemText(3, QCoreApplication.translate("MainWindow", u"N", None))

        self.comboBox_1.setCurrentText(QCoreApplication.translate("MainWindow", u"mV", None))
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"Channel 1", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"mV", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Nm", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Kg", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"N", None))

        self.comboBox_2.setCurrentText(QCoreApplication.translate("MainWindow", u"mV", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Channel 2", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"mV", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"Nm", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"Kg", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("MainWindow", u"N", None))

        self.comboBox_3.setCurrentText(QCoreApplication.translate("MainWindow", u"mV", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Channel 3", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Channel 4", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"mV", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("MainWindow", u"Nm", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("MainWindow", u"Kg", None))
        self.comboBox_4.setItemText(3, QCoreApplication.translate("MainWindow", u"N", None))

        self.comboBox_4.setCurrentText(QCoreApplication.translate("MainWindow", u"mV", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"INTERFACCIA", None))
        self.pushButton_Interfaccia.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"REGISTRAZIONE", None))
        self.pushButton_Registrazione.setText(QCoreApplication.translate("MainWindow", u"START", None))
    # retranslateUi

