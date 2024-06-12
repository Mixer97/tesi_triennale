# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QT_Finestra_#2.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout, QDialog,
    QLCDNumber, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
import Controller_Client_TCP_Laumas as Controller_Client_TCP_Laumas
from time import sleep
from Dialog_setup_1_ui import Ui_Canale_Setup_1
from Dialog_setup_2_ui import Ui_Canale_Setup_2
from Dialog_setup_3_ui import Ui_Canale_Setup_3
from Dialog_setup_4_ui import Ui_Canale_Setup_4
from Dialog_setup_SG600_ui import Ui_SG600_Setup

var = False

class Canale_Setup_1(QDialog):
    def __init__(self):
        super().__init__()
        # Create an instance of the generated UI class
        self.ui = Ui_Canale_Setup_1()
        # Setup the user interface
        self.ui.setupUi(self)
        
class Canale_Setup_2(QDialog):
    def __init__(self):
        super().__init__()
        # Create an instance of the generated UI class
        self.ui = Ui_Canale_Setup_2()
        # Setup the user interface
        self.ui.setupUi(self)
                
class Canale_Setup_3(QDialog):
    def __init__(self):
        super().__init__()
        # Create an instance of the generated UI class
        self.ui = Ui_Canale_Setup_3()
        # Setup the user interface
        self.ui.setupUi(self)
        
class Canale_Setup_4(QDialog):
    def __init__(self):
        super().__init__()
        # Create an instance of the generated UI class
        self.ui = Ui_Canale_Setup_4()
        # Setup the user interface
        self.ui.setupUi(self)
                        
class Canale_Setup_SG600(QDialog):
    def __init__(self):
        super().__init__()
        # Create an instance of the generated UI class
        self.ui = Ui_SG600_Setup()
        # Setup the user interface
        self.ui.setupUi(self)

class Ui_SetupWindow(object):
    
    update_status = False
    list_status_checkbox = [0,0,0,0]   #[CH4, CH3, CH2, CH1]     
    status_timer = False  
          
    def setupUi(self, MainWindow):
            
        while self.list_status_checkbox == [0,0,0,0]:     
            self.list_status_checkbox=Controller_Client_TCP_Laumas.WORKING.read_channels_active() 
            
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(976, 611)
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
"	background-color:rgb(180, 191, 168); \n"
"	border-style: outset;\n"
"    border-width: 3px;\n"
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
"	Background-color: white;\n"
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
"	background-color:rgb(180, 191, 168); \n"
"	border-style: outset;\n"
"    border-width: 3px;\n"
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
"	Background-color: white;\n"
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
"	background-color:rgb(180, 191, 168); \n"
"	border-style: outset;\n"
"    border-width: 3px;\n"
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
"	Background-color: white;\n"
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
"	background-color:rgb(180, 191, 168); \n"
"	border-style: outset;\n"
"    border-width: 3px;\n"
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
        self.lcdNumber_CH4 = QLCDNumber(self.widget_5)
        self.lcdNumber_CH4.setObjectName(u"lcdNumber_CH4")
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

        self.gridLayout_22.addWidget(self.lcdNumber_CH4, 2, 0, 1, 1)

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
"	Background-color: white;\n"
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

        self.lcdNumber_CH4_2 = QLCDNumber(self.widget_5)
        self.lcdNumber_CH4_2.setObjectName(u"lcdNumber_CH4_2")
        self.lcdNumber_CH4_2.setMinimumSize(QSize(0, 0))
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

        self.gridLayout_24.addWidget(self.lcdNumber_CH4_2, 1, 0, 1, 2)


        self.gridLayout_20.addLayout(self.gridLayout_24, 2, 0, 2, 1)


        self.verticalLayout.addWidget(self.widget_5)


        self.Lay_L.addWidget(self.Wid_L)


        self.horizontalLayout_7.addLayout(self.Lay_L)

        self.Lay_R = QHBoxLayout()
        self.Lay_R.setObjectName(u"Lay_R")
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(178, 193, 255);\n"
"	border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: black;\n"
"}\n"
"")
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_27 = QGridLayout()
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.pushButton_concludi_setup = QPushButton(self.widget_2)
        self.pushButton_concludi_setup.setObjectName(u"pushButton_concludi_setup")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_concludi_setup.sizePolicy().hasHeightForWidth())
        self.pushButton_concludi_setup.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(25)
        self.pushButton_concludi_setup.setFont(font1)
        self.pushButton_concludi_setup.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_concludi_setup.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(255, 236, 89);\n"
"	border-style: outset;\n"
"    border-width: 6px;\n"
"	border-color: rgb(211, 181, 13);\n"
"	border-style: outset;\n"
"	border-radius: 20px;\n"
"}\n"
"QPushButton{\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")

        self.gridLayout_27.addWidget(self.pushButton_concludi_setup, 1, 0, 1, 1)

        self.widget = QWidget(self.widget_2)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(215, 230, 255);\n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"	border-color: rgb(169, 152, 255);\n"
"	border-radius: 20px;\n"
"}")
        self.gridLayout_12 = QGridLayout(self.widget)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(7)
        self.gridLayout_2.setVerticalSpacing(0)
        self.label_CHSG600 = QLabel(self.widget)
        self.label_CHSG600.setObjectName(u"label_CHSG600")
        self.label_CHSG600.setStyleSheet(u"QLabel {\n"
"    border: 2px solid black;\n"
"    border-radius: 0px;\n"
"	background-color: rgb(198, 213, 255);\n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"	border-color: rgb(95, 140, 212);\n"
"}\n"
"QLabel{\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_CHSG600.setTextFormat(Qt.RichText)

        self.gridLayout_2.addWidget(self.label_CHSG600, 0, 0, 1, 1)

        self.lcdNumber_fondoscala_CHSG600 = QLCDNumber(self.widget)
        self.lcdNumber_fondoscala_CHSG600.setObjectName(u"lcdNumber_fondoscala_CHSG600")
        self.lcdNumber_fondoscala_CHSG600.setStyleSheet(u"QWidget {\n"
"	background-color:white; \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"	border-radius: 0px;\n"
"}\n"
"QLCDNumber{\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")

        self.gridLayout_2.addWidget(self.lcdNumber_fondoscala_CHSG600, 1, 0, 1, 1)


        self.gridLayout_12.addLayout(self.gridLayout_2, 1, 0, 1, 1)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.checkBox_CHSG600 = QCheckBox(self.widget)
        self.checkBox_CHSG600.setObjectName(u"checkBox_CHSG600")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.checkBox_CHSG600.sizePolicy().hasHeightForWidth())
        self.checkBox_CHSG600.setSizePolicy(sizePolicy1)
        self.checkBox_CHSG600.setCursor(QCursor(Qt.PointingHandCursor))
        self.checkBox_CHSG600.setStyleSheet(u"QCheckBox {\n"
"    spacing: 10px;\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(198, 170, 255);\n"
"	padding: 10px;\n"
"	font: 700 12pt \"Segoe UI\";\n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"	border-color: rgb(95, 140, 212);\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QCheckBox::checked {\n"
"	background-color: rgb(198, 213, 255);\n"
"}\n"
"\n"
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
"	Background-color: white;\n"
"	border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    border-style: outset;\n"
"}\n"
"\n"
"\n"
"")

        self.gridLayout_10.addWidget(self.checkBox_CHSG600, 0, 0, 1, 1)


        self.gridLayout_12.addLayout(self.gridLayout_10, 0, 0, 1, 1)

        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.pushButton_setup_CHSG600 = QPushButton(self.widget)
        self.pushButton_setup_CHSG600.setObjectName(u"pushButton_setup_CHSG600")
        self.pushButton_setup_CHSG600.setMaximumSize(QSize(20000, 20000))
        self.pushButton_setup_CHSG600.setFont(font)
        self.pushButton_setup_CHSG600.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_setup_CHSG600.setStyleSheet(u"QWidget {\n"
"	background-color:rgb(180, 191, 168); \n"
"	border-style: outset;\n"
"    border-width: 3px;\n"
"    border-color:rgb(200, 200, 200);\n"
"	border-radius: 20px;\n"
"}\n"
"QPushButton{\n"
"	color: rgb(0,0,0);\n"
"}")

        self.gridLayout_11.addWidget(self.pushButton_setup_CHSG600, 0, 0, 1, 1)


        self.gridLayout_12.addLayout(self.gridLayout_11, 0, 2, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setVerticalSpacing(0)
        self.label_sensCHSG600 = QLabel(self.widget)
        self.label_sensCHSG600.setObjectName(u"label_sensCHSG600")
        self.label_sensCHSG600.setStyleSheet(u"QLabel {\n"
"    border: 2px solid black;\n"
"    border-radius: 0px;\n"
"	background-color: rgb(198, 213, 255);\n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"	border-color: rgb(95, 140, 212);\n"
"}\n"
"QLabel{\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_sensCHSG600.setTextFormat(Qt.RichText)

        self.gridLayout_5.addWidget(self.label_sensCHSG600, 0, 0, 1, 1)

        self.lcdNumber_sens_CHSG600 = QLCDNumber(self.widget)
        self.lcdNumber_sens_CHSG600.setObjectName(u"lcdNumber_sens_CHSG600")
        self.lcdNumber_sens_CHSG600.setMinimumSize(QSize(0, 0))
        self.lcdNumber_sens_CHSG600.setStyleSheet(u"QWidget {\n"
"	background-color:white; \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"	border-radius: 0px;\n"
"}\n"
"QLCDNumber{\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")

        self.gridLayout_5.addWidget(self.lcdNumber_sens_CHSG600, 1, 0, 1, 1)


        self.gridLayout_12.addLayout(self.gridLayout_5, 1, 2, 1, 1)


        self.gridLayout_27.addWidget(self.widget, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_27, 4, 0, 1, 2)

        self.label_Impost_SG600 = QLabel(self.widget_2)
        self.label_Impost_SG600.setObjectName(u"label_Impost_SG600")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_Impost_SG600.sizePolicy().hasHeightForWidth())
        self.label_Impost_SG600.setSizePolicy(sizePolicy2)
        self.label_Impost_SG600.setMaximumSize(QSize(16777215, 100))
        self.label_Impost_SG600.setStyleSheet(u"QLabel{\n"
"	color: rgb(0,0,0);\n"
"	background-color: rgb(32, 151, 255);\n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(133, 10, 255);\n"
"	border-radius: 10px;\n"
"	background: \n"
"\n"
"qlineargradient(spread:pad, x1:0.502, y1:0, x2:0.479, y2:1, stop:0.028169 rgba(255, 67, 67, 255), stop:1 rgba(84, 184, 255, 255))\n"
"}\n"
"")
        self.label_Impost_SG600.setTextFormat(Qt.RichText)

        self.gridLayout.addWidget(self.label_Impost_SG600, 0, 0, 1, 2)


        self.Lay_R.addWidget(self.widget_2)


        self.horizontalLayout_7.addLayout(self.Lay_R)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi
    
    
    
    #------------------------------------------------------------------------------------------------------------------# 

        # controllo i canali attivi nella scheda e faccio corrispodere la grafica
        if self.list_status_checkbox[3] == 1:
                self.checkBox_CH1.setChecked(True)
        if self.list_status_checkbox[2] == 1:
                self.checkBox_CH2.setChecked(True)
        if self.list_status_checkbox[1] == 1:
                self.checkBox_CH3.setChecked(True)
        if self.list_status_checkbox[0] == 1:
                self.checkBox_CH4.setChecked(True)
        
        # setup dei segnali
        self.checkBox_CH1.stateChanged.connect(lambda: self.on_click(1))
        self.checkBox_CH2.stateChanged.connect(lambda: self.on_click(2))
        self.checkBox_CH3.stateChanged.connect(lambda: self.on_click(3))
        self.checkBox_CH4.stateChanged.connect(lambda: self.on_click(4))
        self.pushButton_concludi_setup.clicked.connect(self.finalizing_setup)
        self.pushButton_setup_CH1.clicked.connect(self.open_setup_CH1_window)
        self.pushButton_setup_CH2.clicked.connect(self.open_setup_CH2_window)
        self.pushButton_setup_CH3.clicked.connect(self.open_setup_CH3_window)
        self.pushButton_setup_CH4.clicked.connect(self.open_setup_CH4_window)
        self.pushButton_setup_CHSG600.clicked.connect(self.open_setup_SG600_window)

    def open_setup_CH1_window(self):
        self.setup_window = Canale_Setup_1()
        self.setup_window.show()
        
    def open_setup_CH2_window(self):
        self.setup_window = Canale_Setup_2()
        self.setup_window.show()

    def open_setup_CH3_window(self):
        self.setup_window = Canale_Setup_3()
        self.setup_window.show()

    def open_setup_CH4_window(self):
        self.setup_window = Canale_Setup_4()
        self.setup_window.show()
        
    def open_setup_SG600_window(self):
        self.setup_window = Canale_Setup_SG600()
        self.setup_window.show()
    
    # Funzione per gestire i canali attivi/disattivi con un click
    def on_click(self, ID):  
        if self.list_status_checkbox[abs(ID-4)] == 0:
            self.list_status_checkbox[abs(ID-4)] = 1       # ENABLED CHANNEL
        else:
            self.list_status_checkbox[abs(ID-4)] = 0       # DISABLED CHANNEL
        print("STATUS CHN" + str(ID) + " = " + str(self.list_status_checkbox[abs(ID-4)]) + "; status-checkbox = " + str(self.list_status_checkbox))
    
    # Impostazioni vengono salvate definitivamente nella scheda a seguito di questa funzione
    def finalizing_setup(self):
        print(self.list_status_checkbox)
        Controller_Client_TCP_Laumas.DATA_INTERACTIONS.setup_full_update(self.list_status_checkbox)
        sleep(0.2)

    #------------------------------------------------------------------------------------------------------------------# 
    
    

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Setup Window", None))
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
        self.pushButton_concludi_setup.setText(QCoreApplication.translate("MainWindow", u"CONCLUSIONE SETUP", None))
        self.label_CHSG600.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">FONDOSCALA [?]</span></p></body></html>", None))
        self.checkBox_CHSG600.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.pushButton_setup_CHSG600.setText(QCoreApplication.translate("MainWindow", u"SETUP", None))
        self.label_sensCHSG600.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">SENS. [mV/V]</span></p></body></html>", None))
        self.label_Impost_SG600.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">IMPOSTAZIONI SG600</span></p></body></html>", None))
    # retranslateUi

