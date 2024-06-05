# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QT_Finestra_#2.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QLCDNumber, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
import Controller_Client_TCP as Controller_Client_TCP

class Ui_SetupWindow(object):
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
        self.verticalLayout = QVBoxLayout(self.Wid_L)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_8 = QWidget(self.Wid_L)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setStyleSheet(u"QWidget {\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 20px;\n"
"}")
        self.gridLayout_40 = QGridLayout(self.widget_8)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.gridLayout_41 = QGridLayout()
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.label_toggle_CHN_1 = QLabel(self.widget_8)
        self.label_toggle_CHN_1.setObjectName(u"label_toggle_CHN_1")
        self.label_toggle_CHN_1.setStyleSheet(u"QLabel {\n"
"    border: 2px solid black;\n"
"    border-radius: 10px;\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 20px;\n"
"}\n"
"QLabel{\n"
"	color: rgb(0,0,0);\n"
"}")

        self.gridLayout_41.addWidget(self.label_toggle_CHN_1, 0, 0, 1, 1)


        self.gridLayout_40.addLayout(self.gridLayout_41, 0, 2, 4, 1)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.pushButton_setup_CH1 = QPushButton(self.widget_8)
        self.pushButton_setup_CH1.setObjectName(u"pushButton_setup_CH1")
        self.pushButton_setup_CH1.setMaximumSize(QSize(20000, 20000))
        font = QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        self.pushButton_setup_CH1.setFont(font)
        self.pushButton_setup_CH1.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_setup_CH1.setStyleSheet(u"QWidget {\n"
"	background-color:rgb(160, 171, 168); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color:rgb(200, 200, 200);\n"
"	border-radius: 20px;\n"
"}\n"
"QPushButton{\n"
"	color: rgb(0,0,0);\n"
"}")

        self.gridLayout_9.addWidget(self.pushButton_setup_CH1, 0, 0, 2, 1)


        self.gridLayout_40.addLayout(self.gridLayout_9, 0, 1, 2, 1)

        self.gridLayout_42 = QGridLayout()
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.gridLayout_42.setVerticalSpacing(0)
        self.lcdNumber_CH1 = QLCDNumber(self.widget_8)
        self.lcdNumber_CH1.setObjectName(u"lcdNumber_CH1")
        self.lcdNumber_CH1.setStyleSheet(u"QWidget {\n"
"	background-color:white; \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"}\n"
"QLCDNumber{\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")

        self.gridLayout_42.addWidget(self.lcdNumber_CH1, 2, 0, 1, 1)

        self.label_sensCH1 = QLabel(self.widget_8)
        self.label_sensCH1.setObjectName(u"label_sensCH1")
        self.label_sensCH1.setStyleSheet(u"QLabel{\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_sensCH1.setTextFormat(Qt.RichText)

        self.gridLayout_42.addWidget(self.label_sensCH1, 1, 0, 1, 1)


        self.gridLayout_40.addLayout(self.gridLayout_42, 2, 1, 2, 1)

        self.gridLayout_43 = QGridLayout()
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.checkBox_CH1 = QCheckBox(self.widget_8)
        self.checkBox_CH1.setObjectName(u"checkBox_CH1")
        self.checkBox_CH1.setCursor(QCursor(Qt.PointingHandCursor))
        self.checkBox_CH1.setStyleSheet(u"QCheckBox {\n"
"    spacing: 10px;\n"
"	color: rgb(0, 0, 0);\n"
"	Background-color:orange;\n"
"	padding: 10px;\n"
"	font: 700 12pt \"Segoe UI\";\n"
"}\n"
"\n"
"QCheckBox:checked {Background-color: rgb(255, 207, 84); border-width: 2px;}"
"QCheckBox::indicator {\n"
"    width: 26px;\n"
"    height: 26px;\n"
"	Background-color: green;\n"
"	border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    border-style: outset;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"	width: 26px;\n"
"    height: 26px;\n"
"	Background-color: red;\n"
"	border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    border-style: outset;\n"
"}\n"
"\n"
"\n"
"")

        self.gridLayout_43.addWidget(self.checkBox_CH1, 0, 0, 1, 1)


        self.gridLayout_40.addLayout(self.gridLayout_43, 0, 0, 2, 1)

        self.gridLayout_44 = QGridLayout()
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.gridLayout_44.setVerticalSpacing(0)
        self.label_CH1 = QLabel(self.widget_8)
        self.label_CH1.setObjectName(u"label_CH1")
        self.label_CH1.setStyleSheet(u"QLabel{\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_CH1.setTextFormat(Qt.RichText)

        self.gridLayout_44.addWidget(self.label_CH1, 0, 0, 1, 2)

        self.lcdNumber_CH1_2 = QLCDNumber(self.widget_8)
        self.lcdNumber_CH1_2.setObjectName(u"lcdNumber_CH1_2")
        self.lcdNumber_CH1_2.setMinimumSize(QSize(0, 0))
        self.lcdNumber_CH1_2.setStyleSheet(u"QWidget {\n"
"	background-color:white; \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"}\n"
"QLCDNumber{\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")

        self.gridLayout_44.addWidget(self.lcdNumber_CH1_2, 1, 0, 1, 2)


        self.gridLayout_40.addLayout(self.gridLayout_44, 2, 0, 2, 1)


        self.verticalLayout.addWidget(self.widget_8)

        self.widget_7 = QWidget(self.Wid_L)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setStyleSheet(u"QWidget {\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 20px;\n"
"}")
        self.gridLayout_35 = QGridLayout(self.widget_7)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.gridLayout_36 = QGridLayout()
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.label_toggle_CHN_2 = QLabel(self.widget_7)
        self.label_toggle_CHN_2.setObjectName(u"label_toggle_CHN_2")
        self.label_toggle_CHN_2.setStyleSheet(u"QLabel {\n"
"    border: 2px solid black;\n"
"    border-radius: 10px;\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 20px;\n"
"}\n"
"QLabel{\n"
"	color: rgb(0,0,0);\n"
"}")

        self.gridLayout_36.addWidget(self.label_toggle_CHN_2, 0, 0, 1, 1)


        self.gridLayout_35.addLayout(self.gridLayout_36, 0, 2, 4, 1)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.pushButton_setup_CH2 = QPushButton(self.widget_7)
        self.pushButton_setup_CH2.setObjectName(u"pushButton_setup_CH2")
        self.pushButton_setup_CH2.setMaximumSize(QSize(20000, 20000))
        self.pushButton_setup_CH2.setFont(font)
        self.pushButton_setup_CH2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_setup_CH2.setStyleSheet(u"QWidget {\n"
"	background-color:rgb(160, 171, 168); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color:rgb(200, 200, 200);\n"
"	border-radius: 20px;\n"
"}\n"
"QPushButton{\n"
"	color: rgb(0,0,0);\n"
"}")

        self.gridLayout_8.addWidget(self.pushButton_setup_CH2, 0, 0, 2, 1)


        self.gridLayout_35.addLayout(self.gridLayout_8, 0, 1, 2, 1)

        self.gridLayout_37 = QGridLayout()
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.gridLayout_37.setVerticalSpacing(0)
        self.lcdNumber_CH2 = QLCDNumber(self.widget_7)
        self.lcdNumber_CH2.setObjectName(u"lcdNumber_CH2")
        self.lcdNumber_CH2.setStyleSheet(u"QWidget {\n"
"	background-color:white; \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"}\n"
"QLCDNumber{\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")

        self.gridLayout_37.addWidget(self.lcdNumber_CH2, 2, 0, 1, 1)

        self.label_CH2 = QLabel(self.widget_7)
        self.label_CH2.setObjectName(u"label_CH2")
        self.label_CH2.setStyleSheet(u"QLabel{\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_CH2.setTextFormat(Qt.RichText)

        self.gridLayout_37.addWidget(self.label_CH2, 1, 0, 1, 1)


        self.gridLayout_35.addLayout(self.gridLayout_37, 2, 1, 2, 1)

        self.gridLayout_38 = QGridLayout()
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.checkBox_CH2 = QCheckBox(self.widget_7)
        self.checkBox_CH2.setObjectName(u"checkBox_CH2")
        self.checkBox_CH2.setCursor(QCursor(Qt.PointingHandCursor))
        self.checkBox_CH2.setStyleSheet(u"QCheckBox {\n"
"    spacing: 10px;\n"
"	color: rgb(0, 0, 0);\n"
"	Background-color:orange;\n"
"	padding: 10px;\n"
"	font: 700 12pt \"Segoe UI\";\n"
"}\n"
"\n"
"QCheckBox:checked {Background-color: rgb(255, 207, 84); border-width: 2px;}"
"QCheckBox::indicator {\n"
"    width: 26px;\n"
"    height: 26px;\n"
"	Background-color: green;\n"
"	border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    border-style: outset;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"	width: 26px;\n"
"    height: 26px;\n"
"	Background-color: red;\n"
"	border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    border-style: outset;\n"
"}\n"
"\n"
"\n"
"")

        self.gridLayout_38.addWidget(self.checkBox_CH2, 0, 0, 1, 1)


        self.gridLayout_35.addLayout(self.gridLayout_38, 0, 0, 2, 1)

        self.gridLayout_39 = QGridLayout()
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.gridLayout_39.setVerticalSpacing(0)
        self.label_CH2_2 = QLabel(self.widget_7)
        self.label_CH2_2.setObjectName(u"label_CH2_2")
        self.label_CH2_2.setStyleSheet(u"QLabel{\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_CH2_2.setTextFormat(Qt.RichText)

        self.gridLayout_39.addWidget(self.label_CH2_2, 0, 0, 1, 2)

        self.lcdNumber_CH2_2 = QLCDNumber(self.widget_7)
        self.lcdNumber_CH2_2.setObjectName(u"lcdNumber_CH2_2")
        self.lcdNumber_CH2_2.setMinimumSize(QSize(0, 0))
        self.lcdNumber_CH2_2.setStyleSheet(u"QWidget {\n"
"	background-color:white; \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"}\n"
"QLCDNumber{\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")

        self.gridLayout_39.addWidget(self.lcdNumber_CH2_2, 1, 0, 1, 2)


        self.gridLayout_35.addLayout(self.gridLayout_39, 2, 0, 2, 1)


        self.verticalLayout.addWidget(self.widget_7)

        self.widget_6 = QWidget(self.Wid_L)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setStyleSheet(u"QWidget {\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 20px;\n"
"}")
        self.gridLayout_30 = QGridLayout(self.widget_6)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.gridLayout_31 = QGridLayout()
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.label_toggle_CHN_3 = QLabel(self.widget_6)
        self.label_toggle_CHN_3.setObjectName(u"label_toggle_CHN_3")
        self.label_toggle_CHN_3.setStyleSheet(u"QLabel {\n"
"    border: 2px solid black;\n"
"    border-radius: 10px;\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 20px;\n"
"}\n"
"QLabel{\n"
"	color: rgb(0,0,0);\n"
"}")

        self.gridLayout_31.addWidget(self.label_toggle_CHN_3, 0, 0, 1, 1)


        self.gridLayout_30.addLayout(self.gridLayout_31, 0, 2, 4, 1)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.pushButton_setup_CH3 = QPushButton(self.widget_6)
        self.pushButton_setup_CH3.setObjectName(u"pushButton_setup_CH3")
        self.pushButton_setup_CH3.setMaximumSize(QSize(20000, 20000))
        self.pushButton_setup_CH3.setFont(font)
        self.pushButton_setup_CH3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_setup_CH3.setStyleSheet(u"QWidget {\n"
"	background-color:rgb(160, 171, 168); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color:rgb(200, 200, 200);\n"
"	border-radius: 20px;\n"
"}\n"
"QPushButton{\n"
"	color: rgb(0,0,0);\n"
"}")

        self.gridLayout_7.addWidget(self.pushButton_setup_CH3, 0, 0, 2, 1)


        self.gridLayout_30.addLayout(self.gridLayout_7, 0, 1, 2, 1)

        self.gridLayout_32 = QGridLayout()
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.gridLayout_32.setVerticalSpacing(0)
        self.lcdNumber_CH3 = QLCDNumber(self.widget_6)
        self.lcdNumber_CH3.setObjectName(u"lcdNumber_CH3")
        self.lcdNumber_CH3.setStyleSheet(u"QWidget {\n"
"	background-color:white; \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"}\n"
"QLCDNumber{\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")

        self.gridLayout_32.addWidget(self.lcdNumber_CH3, 2, 0, 1, 1)

        self.label_CH3 = QLabel(self.widget_6)
        self.label_CH3.setObjectName(u"label_CH3")
        self.label_CH3.setStyleSheet(u"QLabel{\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_CH3.setTextFormat(Qt.RichText)

        self.gridLayout_32.addWidget(self.label_CH3, 1, 0, 1, 1)


        self.gridLayout_30.addLayout(self.gridLayout_32, 2, 1, 2, 1)

        self.gridLayout_33 = QGridLayout()
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.checkBox_CH3 = QCheckBox(self.widget_6)
        self.checkBox_CH3.setObjectName(u"checkBox_CH3")
        self.checkBox_CH3.setCursor(QCursor(Qt.PointingHandCursor))
        self.checkBox_CH3.setStyleSheet(u"QCheckBox {\n"
"    spacing: 10px;\n"
"	color: rgb(0, 0, 0);\n"
"	Background-color:orange;\n"
"	padding: 10px;\n"
"	font: 700 12pt \"Segoe UI\";\n"
"}\n"
"\n"
"QCheckBox:checked {Background-color: rgb(255, 207, 84); border-width: 2px;}"
"QCheckBox::indicator {\n"
"    width: 26px;\n"
"    height: 26px;\n"
"	Background-color: green;\n"
"	border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    border-style: outset;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"	width: 26px;\n"
"    height: 26px;\n"
"	Background-color: red;\n"
"	border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    border-style: outset;\n"
"}\n"
"\n"
"\n"
"")

        self.gridLayout_33.addWidget(self.checkBox_CH3, 0, 0, 1, 1)


        self.gridLayout_30.addLayout(self.gridLayout_33, 0, 0, 2, 1)

        self.gridLayout_34 = QGridLayout()
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.gridLayout_34.setVerticalSpacing(0)
        self.label_CH3_2 = QLabel(self.widget_6)
        self.label_CH3_2.setObjectName(u"label_CH3_2")
        self.label_CH3_2.setStyleSheet(u"QLabel{\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_CH3_2.setTextFormat(Qt.RichText)

        self.gridLayout_34.addWidget(self.label_CH3_2, 0, 0, 1, 2)

        self.lcdNumber_CH3_2 = QLCDNumber(self.widget_6)
        self.lcdNumber_CH3_2.setObjectName(u"lcdNumber_CH3_2")
        self.lcdNumber_CH3_2.setMinimumSize(QSize(0, 0))
        self.lcdNumber_CH3_2.setStyleSheet(u"QWidget {\n"
"	background-color:white; \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"}\n"
"QLCDNumber{\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")

        self.gridLayout_34.addWidget(self.lcdNumber_CH3_2, 1, 0, 1, 2)


        self.gridLayout_30.addLayout(self.gridLayout_34, 2, 0, 2, 1)


        self.verticalLayout.addWidget(self.widget_6)

        self.widget_5 = QWidget(self.Wid_L)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setStyleSheet(u"QWidget {\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 20px;\n"
"}")
        self.gridLayout_20 = QGridLayout(self.widget_5)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_21 = QGridLayout()
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.label_toggle_CHN_4 = QLabel(self.widget_5)
        self.label_toggle_CHN_4.setObjectName(u"label_toggle_CHN_4")
        self.label_toggle_CHN_4.setStyleSheet(u"QLabel {\n"
"    border: 2px solid black;\n"
"    border-radius: 10px;\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 20px;\n"
"}\n"
"QLabel{\n"
"	color: rgb(0,0,0);\n"
"}")

        self.gridLayout_21.addWidget(self.label_toggle_CHN_4, 0, 0, 1, 1)


        self.gridLayout_20.addLayout(self.gridLayout_21, 0, 2, 4, 1)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.pushButton_setup_CH4 = QPushButton(self.widget_5)
        self.pushButton_setup_CH4.setObjectName(u"pushButton_setup_CH4")
        self.pushButton_setup_CH4.setMaximumSize(QSize(20000, 20000))
        self.pushButton_setup_CH4.setFont(font)
        self.pushButton_setup_CH4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_setup_CH4.setStyleSheet(u"QWidget {\n"
"	background-color:rgb(160, 171, 168); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color:rgb(200, 200, 200);\n"
"	border-radius: 20px;\n"
"}\n"
"QPushButton{\n"
"	color: rgb(0,0,0);\n"
"}")

        self.gridLayout_6.addWidget(self.pushButton_setup_CH4, 0, 0, 2, 1)


        self.gridLayout_20.addLayout(self.gridLayout_6, 0, 1, 2, 1)

        self.gridLayout_22 = QGridLayout()
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setVerticalSpacing(0)
        self.lcdNumber_CH4_2 = QLCDNumber(self.widget_5)
        self.lcdNumber_CH4_2.setObjectName(u"lcdNumber_CH4_2")
        self.lcdNumber_CH4_2.setStyleSheet(u"QWidget {\n"
"	background-color:white; \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"}\n"
"QLCDNumber{\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")

        self.gridLayout_22.addWidget(self.lcdNumber_CH4_2, 2, 0, 1, 1)

        self.label_CH4_2 = QLabel(self.widget_5)
        self.label_CH4_2.setObjectName(u"label_CH4_2")
        self.label_CH4_2.setStyleSheet(u"QLabel{\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_CH4_2.setTextFormat(Qt.RichText)

        self.gridLayout_22.addWidget(self.label_CH4_2, 1, 0, 1, 1)


        self.gridLayout_20.addLayout(self.gridLayout_22, 2, 1, 2, 1)

        self.gridLayout_23 = QGridLayout()
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.checkBox_CH4 = QCheckBox(self.widget_5)
        self.checkBox_CH4.setObjectName(u"checkBox_CH4")
        self.checkBox_CH4.setCursor(QCursor(Qt.PointingHandCursor))
        self.checkBox_CH4.setStyleSheet(u"QCheckBox {\n"
"    spacing: 10px;\n"
"	color: rgb(0, 0, 0);\n"
"	Background-color:orange;\n"
"	padding: 10px;\n"
"	font: 700 12pt \"Segoe UI\";\n"
"}\n"
"\n"
"QCheckBox:checked {Background-color: rgb(255, 207, 84); border-width: 2px;}"
"QCheckBox::indicator {\n"
"    width: 26px;\n"
"    height: 26px;\n"
"	Background-color: green;\n"
"	border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    border-style: outset;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"	width: 26px;\n"
"    height: 26px;\n"
"	Background-color: red;\n"
"	border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    border-style: outset;\n"
"}\n"
"\n"
"\n"
"")

        self.gridLayout_23.addWidget(self.checkBox_CH4, 0, 0, 1, 1)


        self.gridLayout_20.addLayout(self.gridLayout_23, 0, 0, 2, 1)

        self.gridLayout_24 = QGridLayout()
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_24.setVerticalSpacing(0)
        self.label_CH4 = QLabel(self.widget_5)
        self.label_CH4.setObjectName(u"label_CH4")
        self.label_CH4.setStyleSheet(u"QLabel{\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_CH4.setTextFormat(Qt.RichText)

        self.gridLayout_24.addWidget(self.label_CH4, 0, 0, 1, 2)

        self.lcdNumber_CH4 = QLCDNumber(self.widget_5)
        self.lcdNumber_CH4.setObjectName(u"lcdNumber_CH4")
        self.lcdNumber_CH4.setMinimumSize(QSize(0, 0))
        self.lcdNumber_CH4.setStyleSheet(u"QWidget {\n"
"	background-color:white; \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"}\n"
"QLCDNumber{\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")

        self.gridLayout_24.addWidget(self.lcdNumber_CH4, 1, 0, 1, 2)


        self.gridLayout_20.addLayout(self.gridLayout_24, 2, 0, 2, 1)


        self.verticalLayout.addWidget(self.widget_5)


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
        self.gridLayout_26 = QGridLayout(self.widget_2)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.gridLayout_27 = QGridLayout()
        self.gridLayout_27.setObjectName(u"gridLayout_27")

        self.gridLayout_26.addLayout(self.gridLayout_27, 2, 0, 1, 1)

        self.gridLayout_25 = QGridLayout()
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"QLabel{\n"
"	color: rgb(0,0,0);\n"
"	background-color: rgb(32, 151, 255);\n"
"	border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: rgb(133, 10, 255);\n"
"	border-radius: 10px;\n"
"	background: \n"
"\n"
"qlineargradient(spread:pad, x1:0.502, y1:0, x2:0.479, y2:1, stop:0.028169 rgba(255, 67, 67, 255), stop:1 rgba(84, 184, 255, 255))\n"
"}\n"
"")
        self.label_3.setTextFormat(Qt.RichText)

        self.gridLayout_25.addWidget(self.label_3, 0, 0, 1, 1)

        self.gridLayout_29 = QGridLayout()
        self.gridLayout_29.setObjectName(u"gridLayout_29")

        self.gridLayout_25.addLayout(self.gridLayout_29, 1, 0, 1, 1)


        self.gridLayout_26.addLayout(self.gridLayout_25, 0, 0, 1, 1)

        self.gridLayout_28 = QGridLayout()
        self.gridLayout_28.setObjectName(u"gridLayout_28")

        self.gridLayout_26.addLayout(self.gridLayout_28, 1, 0, 1, 1)


        self.Lay_R.addWidget(self.widget_2)


        self.horizontalLayout_7.addLayout(self.Lay_R)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi
    
    #------------------------------------------------------------------------------------------------------------------# 

        self.checkBox_CH1.clicked.connect(lambda: Controller_Client_TCP.WORKING.set_channel_status(1))
        self.checkBox_CH2.clicked.connect(lambda: Controller_Client_TCP.WORKING.set_channel_status(2))
        self.checkBox_CH3.clicked.connect(lambda: Controller_Client_TCP.WORKING.set_channel_status(3))
        self.checkBox_CH4.clicked.connect(lambda: Controller_Client_TCP.WORKING.set_channel_status(4))























    #------------------------------------------------------------------------------------------------------------------# 


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_toggle_CHN_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700; color:#00aa00;\">CANALE 1</span></p></body></html>", None))
        self.pushButton_setup_CH1.setText(QCoreApplication.translate("MainWindow", u"SETUP", None))
        self.label_sensCH1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">SENS. [mV/V]</span></p></body></html>", None))
        self.checkBox_CH1.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.label_CH1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">FONDOSCALA [?]</span></p></body></html>", None))
        self.label_toggle_CHN_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700; color:#00aa00;\">CANALE 2</span></p></body></html>", None))
        self.pushButton_setup_CH2.setText(QCoreApplication.translate("MainWindow", u"SETUP", None))
        self.label_CH2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">SENS. [mV/V]</span></p></body></html>", None))
        self.checkBox_CH2.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.label_CH2_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">FONDOSCALA [?]</span></p></body></html>", None))
        self.label_toggle_CHN_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700; color:#00aa00;\">CANALE 3</span></p></body></html>", None))
        self.pushButton_setup_CH3.setText(QCoreApplication.translate("MainWindow", u"SETUP", None))
        self.label_CH3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">SENS. [mV/V]</span></p></body></html>", None))
        self.checkBox_CH3.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.label_CH3_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">FONDOSCALA [?]</span></p></body></html>", None))
        self.label_toggle_CHN_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700; color:#00aa00;\">CANALE 4</span></p></body></html>", None))
        self.pushButton_setup_CH4.setText(QCoreApplication.translate("MainWindow", u"SETUP", None))
        self.label_CH4_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">SENS. [mV/V]</span></p></body></html>", None))
        self.checkBox_CH4.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.label_CH4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">FONDOSCALA [?]</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">IMPOSTAZIONI SG600</span></p></body></html>", None))
    # retranslateUi

