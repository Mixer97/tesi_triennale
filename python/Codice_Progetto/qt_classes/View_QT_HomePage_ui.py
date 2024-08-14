# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'View_QT_HomePage.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLCDNumber, QLabel, QLayout,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(972, 664)
        MainWindow.setMinimumSize(QSize(853, 664))
        MainWindow.setStyleSheet(u"QWidget {\n"
"	background-color:black; \n"
"	border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: black;\n"
"}\n"
"")
        MainWindow.setIconSize(QSize(20, 20))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget {\n"
"	background-color:black; \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"}\n"
"")
        self.gridLayout_12 = QGridLayout(self.centralwidget)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setVerticalSpacing(2)
        self.gridLayout_12.setContentsMargins(-1, 5, -1, -1)
        self.Lay_R = QHBoxLayout()
        self.Lay_R.setObjectName(u"Lay_R")
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"QWidget {\n"
"	background-color:orange; \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"}\n"
"")
        self.gridLayout_9 = QGridLayout(self.widget_2)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.widget_12 = QWidget(self.widget_2)
        self.widget_12.setObjectName(u"widget_12")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_12.sizePolicy().hasHeightForWidth())
        self.widget_12.setSizePolicy(sizePolicy)
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
        self.widget_sfondo_registrazione = QWidget(self.widget_12)
        self.widget_sfondo_registrazione.setObjectName(u"widget_sfondo_registrazione")
        self.widget_sfondo_registrazione.setStyleSheet(u"QWidget {\n"
"	background-color:rgb(125, 225, 10); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color:rgb(63, 156, 23);\n"
"	border-radius: 20px;\n"
"}")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_sfondo_registrazione)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_5 = QLabel(self.widget_sfondo_registrazione)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setPointSize(17)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"QWidget {\n"
"	background-color:rgb(125, 225, 10); \n"
"	border-style: outset;\n"
"    border-width: 0px;\n"
"    border-color:rgb(63, 156, 23);\n"
"	border-radius: 20px;\n"
"}\n"
"QLabel{\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")

        self.horizontalLayout_8.addWidget(self.label_5, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.pushButton_Registrazione = QPushButton(self.widget_sfondo_registrazione)
        self.pushButton_Registrazione.setObjectName(u"pushButton_Registrazione")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_Registrazione.sizePolicy().hasHeightForWidth())
        self.pushButton_Registrazione.setSizePolicy(sizePolicy1)
        self.pushButton_Registrazione.setMinimumSize(QSize(200, 0))
        self.pushButton_Registrazione.setMaximumSize(QSize(300, 200))
        font1 = QFont()
        font1.setPointSize(30)
        font1.setBold(False)
        self.pushButton_Registrazione.setFont(font1)
        self.pushButton_Registrazione.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_Registrazione.setStyleSheet(u"QWidget {\n"
"	background-color:green; \n"
"	border-style: outset;\n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"	border-radius: 20px;\n"
"}\n"
"QPushButton{\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")

        self.horizontalLayout_8.addWidget(self.pushButton_Registrazione)


        self.gridLayout_2.addWidget(self.widget_sfondo_registrazione, 1, 0, 1, 1)

        self.frame_3 = QFrame(self.widget_12)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 30))
        self.frame_3.setMaximumSize(QSize(16777215, 30))
        self.frame_3.setStyleSheet(u"border-width: 0px")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_nome_reg = QLabel(self.frame_3)
        self.label_nome_reg.setObjectName(u"label_nome_reg")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_nome_reg.sizePolicy().hasHeightForWidth())
        self.label_nome_reg.setSizePolicy(sizePolicy2)
        self.label_nome_reg.setStyleSheet(u"QWidget {\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 20px;\n"
"}\n"
"QLabel{\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.label_nome_reg)

        self.label_nome_reg_display = QLabel(self.frame_3)
        self.label_nome_reg_display.setObjectName(u"label_nome_reg_display")
        self.label_nome_reg_display.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(255, 255, 255); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 20;\n"
"	color: rgb(0,0,0);\n"
"}")
        self.label_nome_reg_display.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_nome_reg_display)


        self.gridLayout_2.addWidget(self.frame_3, 2, 0, 1, 1)

        self.widget_sfond_interfaccia = QWidget(self.widget_12)
        self.widget_sfond_interfaccia.setObjectName(u"widget_sfond_interfaccia")
        sizePolicy.setHeightForWidth(self.widget_sfond_interfaccia.sizePolicy().hasHeightForWidth())
        self.widget_sfond_interfaccia.setSizePolicy(sizePolicy)
        self.widget_sfond_interfaccia.setStyleSheet(u"QWidget { background-color:rgb(255, 69, 72); border-style: outset; border-width: 2px; border-color:rgb(255, 111, 113); border-radius: 20px; }")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_sfond_interfaccia)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label = QLabel(self.widget_sfond_interfaccia)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setStyleSheet(u"QWidget {\n"
"	background-color:rgb(125, 225, 10); \n"
"	border-style: outset;\n"
"    border-width: 0px;\n"
"    border-color:rgb(63, 156, 23);\n"
"	border-radius: 20px;\n"
"}\n"
"QLabel{\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")

        self.horizontalLayout_6.addWidget(self.label, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.pushButton_Interfaccia = QPushButton(self.widget_sfond_interfaccia)
        self.pushButton_Interfaccia.setObjectName(u"pushButton_Interfaccia")
        sizePolicy1.setHeightForWidth(self.pushButton_Interfaccia.sizePolicy().hasHeightForWidth())
        self.pushButton_Interfaccia.setSizePolicy(sizePolicy1)
        self.pushButton_Interfaccia.setMinimumSize(QSize(200, 0))
        self.pushButton_Interfaccia.setMaximumSize(QSize(300, 200))
        font2 = QFont()
        font2.setPointSize(30)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setStrikeOut(False)
        self.pushButton_Interfaccia.setFont(font2)
        self.pushButton_Interfaccia.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_Interfaccia.setStyleSheet(u"QPushButton {\n"
"	background-color:green; \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"	border-radius: 20px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")

        self.horizontalLayout_6.addWidget(self.pushButton_Interfaccia)


        self.gridLayout_2.addWidget(self.widget_sfond_interfaccia, 0, 0, 1, 1)


        self.gridLayout_10.addWidget(self.widget_12, 0, 0, 1, 1)


        self.gridLayout_9.addLayout(self.gridLayout_10, 2, 0, 1, 1)

        self.widget_6 = QWidget(self.widget_2)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy3)
        self.widget_6.setStyleSheet(u"QWidget {\n"
"	background-color:orange; \n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color: black;\n"
"}\n"
"")
        self.gridLayout = QGridLayout(self.widget_6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget_7 = QWidget(self.widget_6)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy)
        self.widget_7.setStyleSheet(u"QWidget {\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 20px;\n"
"}")
        self.gridLayout_7 = QGridLayout(self.widget_7)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.label_SG600 = QLabel(self.widget_7)
        self.label_SG600.setObjectName(u"label_SG600")
        sizePolicy.setHeightForWidth(self.label_SG600.sizePolicy().hasHeightForWidth())
        self.label_SG600.setSizePolicy(sizePolicy)
        self.label_SG600.setMinimumSize(QSize(225, 0))
        self.label_SG600.setFont(font)
        self.label_SG600.setStyleSheet(u"QLabel{\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")

        self.gridLayout_11.addWidget(self.label_SG600, 1, 0, 1, 1)

        self.comboBox_5 = QComboBox(self.widget_7)
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setEnabled(True)
        sizePolicy.setHeightForWidth(self.comboBox_5.sizePolicy().hasHeightForWidth())
        self.comboBox_5.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setPointSize(15)
        self.comboBox_5.setFont(font3)
        self.comboBox_5.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.comboBox_5.setMouseTracking(True)
        self.comboBox_5.setAutoFillBackground(False)
        self.comboBox_5.setStyleSheet(u"QComboBox {\n"
"    border: 3px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 1px 1px 10px;\n"
"    min-width: 6em;\n"
"    color: rgb(0, 0, 0); /* Colore del testo del QComboBox */\n"
"}\n"
"\n"
"QComboBox:hover, QPushButton:hover\n"
"{\n"
"    border: 1px solid rgb(202, 203, 194);\n"
"    color: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}\n"
"\n"
"\n"
"/* Stile della tendina del QComboBox */\n"
"QComboBox QAbstractItemView {\n"
"    background-color:	qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3); ; /* Colore di sfondo della tendina */\n"
"    selection-background-color: #3399FF; /* Colore di sfondo dell'eleme"
                        "nto selezionato */\n"
"    selection-color:rgb(106, 112, 113); /* Colore del testo dell'elemento selezionato */\n"
"    border: 3px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"    color: rgb(0, 0, 0); /* Colore del testo del QComboBox */\n"
"}")
        self.comboBox_5.setIconSize(QSize(30, 30))

        self.gridLayout_11.addWidget(self.comboBox_5, 1, 1, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_11, 0, 0, 1, 2)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.lcdNumber_temperature_SG600 = QLCDNumber(self.widget_7)
        self.lcdNumber_temperature_SG600.setObjectName(u"lcdNumber_temperature_SG600")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lcdNumber_temperature_SG600.sizePolicy().hasHeightForWidth())
        self.lcdNumber_temperature_SG600.setSizePolicy(sizePolicy4)
        font4 = QFont()
        font4.setPointSize(9)
        font4.setBold(False)
        self.lcdNumber_temperature_SG600.setFont(font4)
        self.lcdNumber_temperature_SG600.setStyleSheet(u"QWidget {\n"
"	background-color:white; \n"
"	border-style: outset;\n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"	border-radius: 10px;\n"
"}\n"
"QLCDNumber{\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.lcdNumber_temperature_SG600.setDigitCount(7)
        self.lcdNumber_temperature_SG600.setProperty("value", 0.000000000000000)

        self.gridLayout_8.addWidget(self.lcdNumber_temperature_SG600, 1, 1, 1, 1)

        self.lcdNumber_main_SG600 = QLCDNumber(self.widget_7)
        self.lcdNumber_main_SG600.setObjectName(u"lcdNumber_main_SG600")
        sizePolicy4.setHeightForWidth(self.lcdNumber_main_SG600.sizePolicy().hasHeightForWidth())
        self.lcdNumber_main_SG600.setSizePolicy(sizePolicy4)
        self.lcdNumber_main_SG600.setStyleSheet(u"QWidget {\n"
"	background-color:white; \n"
"	border-style: outset;\n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"	border-radius: 10px;\n"
"}\n"
"QLCDNumber{\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.lcdNumber_main_SG600.setDigitCount(7)
        self.lcdNumber_main_SG600.setProperty("value", 0.000000000000000)

        self.gridLayout_8.addWidget(self.lcdNumber_main_SG600, 0, 1, 1, 1)

        self.label_6 = QLabel(self.widget_7)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(225, 0))
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"QWidget {\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 20px;\n"
"}\n"
"QLabel{\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")

        self.gridLayout_8.addWidget(self.label_6, 0, 0, 1, 1)

        self.label_7 = QLabel(self.widget_7)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(225, 0))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"QWidget {\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 20px;\n"
"}\n"
"QLabel{\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")

        self.gridLayout_8.addWidget(self.label_7, 1, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_8, 1, 0, 2, 2)


        self.gridLayout.addWidget(self.widget_7, 0, 0, 2, 1)


        self.gridLayout_9.addWidget(self.widget_6, 0, 0, 1, 1)


        self.Lay_R.addWidget(self.widget_2)


        self.gridLayout_12.addLayout(self.Lay_R, 1, 1, 1, 1)

        self.Lay_L = QHBoxLayout()
        self.Lay_L.setObjectName(u"Lay_L")
        self.Wid_L = QWidget(self.centralwidget)
        self.Wid_L.setObjectName(u"Wid_L")
        self.Wid_L.setStyleSheet(u"QWidget {\n"
"	background-color:orange; \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"}\n"
"")
        self.verticalLayout_5 = QVBoxLayout(self.Wid_L)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.Wid_L)
        self.widget.setObjectName(u"widget")
        self.widget.setEnabled(False)
        self.widget.setStyleSheet(u"QWidget {\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 20px;\n"
"}")
        self.gridLayout_3 = QGridLayout(self.widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.comboBox_1 = QComboBox(self.widget)
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.setObjectName(u"comboBox_1")
        sizePolicy.setHeightForWidth(self.comboBox_1.sizePolicy().hasHeightForWidth())
        self.comboBox_1.setSizePolicy(sizePolicy)
        self.comboBox_1.setFont(font3)
        self.comboBox_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.comboBox_1.setMouseTracking(True)
        self.comboBox_1.setAutoFillBackground(False)
        self.comboBox_1.setStyleSheet(u"QComboBox {\n"
"    border: 3px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 1px 1px 10px;\n"
"    min-width: 6em;\n"
"    color: rgb(0, 0, 0); /* Colore del testo del QComboBox */\n"
"}\n"
"\n"
"QComboBox:hover, QPushButton:hover\n"
"{\n"
"    border: 1px solid rgb(202, 203, 194);\n"
"    color: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}\n"
"\n"
"\n"
"/* Stile della tendina del QComboBox */\n"
"QComboBox QAbstractItemView {\n"
"    background-color:	qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3); ; /* Colore di sfondo della tendina */\n"
"    selection-background-color: #3399FF; /* Colore di sfondo dell'eleme"
                        "nto selezionato */\n"
"    selection-color:rgb(106, 112, 113); /* Colore del testo dell'elemento selezionato */\n"
"    border: 3px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"    color: rgb(0, 0, 0); /* Colore del testo del QComboBox */\n"
"}")
        self.comboBox_1.setIconSize(QSize(30, 30))

        self.gridLayout_3.addWidget(self.comboBox_1, 0, 1, 1, 1)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_1 = QLabel(self.widget)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setFont(font)
        self.label_1.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 20px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")

        self.verticalLayout_9.addWidget(self.label_1)


        self.gridLayout_3.addLayout(self.verticalLayout_9, 0, 0, 1, 1)

        self.lcdNumber_1 = QLCDNumber(self.widget)
        self.lcdNumber_1.setObjectName(u"lcdNumber_1")
        self.lcdNumber_1.setFont(font4)
        self.lcdNumber_1.setStyleSheet(u"QWidget {\n"
"	background-color:white; \n"
"	border-style: outset;\n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"	border-radius: 10px;\n"
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
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 20px;\n"
"}")
        self.gridLayout_4 = QGridLayout(self.widget_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.comboBox_2 = QComboBox(self.widget_3)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)
        self.comboBox_2.setFont(font3)
        self.comboBox_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.comboBox_2.setMouseTracking(True)
        self.comboBox_2.setAutoFillBackground(False)
        self.comboBox_2.setStyleSheet(u"QComboBox {\n"
"    border: 3px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 1px 1px 10px;\n"
"    min-width: 6em;\n"
"    color: rgb(0, 0, 0); /* Colore del testo del QComboBox */\n"
"}\n"
"\n"
"QComboBox:hover, QPushButton:hover\n"
"{\n"
"    border: 1px solid rgb(202, 203, 194);\n"
"    color: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}\n"
"\n"
"\n"
"/* Stile della tendina del QComboBox */\n"
"QComboBox QAbstractItemView {\n"
"    background-color:	qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3); ; /* Colore di sfondo della tendina */\n"
"    selection-background-color: #3399FF; /* Colore di sfondo dell'eleme"
                        "nto selezionato */\n"
"    selection-color:rgb(106, 112, 113); /* Colore del testo dell'elemento selezionato */\n"
"    border: 3px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"    color: rgb(0, 0, 0); /* Colore del testo del QComboBox */\n"
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

        self.verticalLayout_10.addWidget(self.label_2)


        self.gridLayout_4.addLayout(self.verticalLayout_10, 0, 0, 1, 1)

        self.lcdNumber_2 = QLCDNumber(self.widget_3)
        self.lcdNumber_2.setObjectName(u"lcdNumber_2")
        self.lcdNumber_2.setStyleSheet(u"QWidget {\n"
"	background-color:white; \n"
"	border-style: outset;\n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"	border-radius: 10px;\n"
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
        self.widget_4.setEnabled(False)
        self.widget_4.setStyleSheet(u"QWidget {\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 20px;\n"
"}")
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
        self.comboBox_3.setFont(font3)
        self.comboBox_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.comboBox_3.setMouseTracking(True)
        self.comboBox_3.setAutoFillBackground(False)
        self.comboBox_3.setStyleSheet(u"QComboBox {\n"
"    border: 3px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 1px 1px 10px;\n"
"    min-width: 6em;\n"
"    color: rgb(0, 0, 0); /* Colore del testo del QComboBox */\n"
"}\n"
"\n"
"QComboBox:hover, QPushButton:hover\n"
"{\n"
"    border: 1px solid rgb(202, 203, 194);\n"
"    color: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}\n"
"\n"
"\n"
"/* Stile della tendina del QComboBox */\n"
"QComboBox QAbstractItemView {\n"
"    background-color:	qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3); ; /* Colore di sfondo della tendina */\n"
"    selection-background-color: #3399FF; /* Colore di sfondo dell'eleme"
                        "nto selezionato */\n"
"    selection-color:rgb(106, 112, 113); /* Colore del testo dell'elemento selezionato */\n"
"    border: 3px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"    color: rgb(0, 0, 0); /* Colore del testo del QComboBox */\n"
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

        self.verticalLayout_7.addWidget(self.label_3)


        self.gridLayout_5.addLayout(self.verticalLayout_7, 0, 0, 1, 1)

        self.lcdNumber_3 = QLCDNumber(self.widget_4)
        self.lcdNumber_3.setObjectName(u"lcdNumber_3")
        font5 = QFont()
        font5.setBold(False)
        font5.setKerning(True)
        self.lcdNumber_3.setFont(font5)
        self.lcdNumber_3.setStyleSheet(u"QWidget {\n"
"	background-color:white; \n"
"	border-style: outset;\n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"	border-radius: 10px;\n"
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
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 20px;\n"
"}")
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

        self.verticalLayout_11.addWidget(self.label_4)


        self.gridLayout_6.addLayout(self.verticalLayout_11, 0, 0, 1, 1)

        self.comboBox_4 = QComboBox(self.widget_5)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        sizePolicy.setHeightForWidth(self.comboBox_4.sizePolicy().hasHeightForWidth())
        self.comboBox_4.setSizePolicy(sizePolicy)
        self.comboBox_4.setFont(font3)
        self.comboBox_4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.comboBox_4.setMouseTracking(True)
        self.comboBox_4.setAutoFillBackground(False)
        self.comboBox_4.setStyleSheet(u"QComboBox {\n"
"    border: 3px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 1px 1px 10px;\n"
"    min-width: 6em;\n"
"    color: rgb(0, 0, 0); /* Colore del testo del QComboBox */\n"
"}\n"
"\n"
"QComboBox:hover, QPushButton:hover\n"
"{\n"
"    border: 1px solid rgb(202, 203, 194);\n"
"    color: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}\n"
"\n"
"\n"
"/* Stile della tendina del QComboBox */\n"
"QComboBox QAbstractItemView {\n"
"    background-color:	qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3); ; /* Colore di sfondo della tendina */\n"
"    selection-background-color: #3399FF; /* Colore di sfondo dell'eleme"
                        "nto selezionato */\n"
"    selection-color:rgb(106, 112, 113); /* Colore del testo dell'elemento selezionato */\n"
"    border: 3px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"    color: rgb(0, 0, 0); /* Colore del testo del QComboBox */\n"
"}")
        self.comboBox_4.setIconSize(QSize(30, 30))

        self.gridLayout_6.addWidget(self.comboBox_4, 0, 1, 1, 1)

        self.lcdNumber_4 = QLCDNumber(self.widget_5)
        self.lcdNumber_4.setObjectName(u"lcdNumber_4")
        self.lcdNumber_4.setStyleSheet(u"QWidget {\n"
"	background-color:white; \n"
"	border-style: outset;\n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"	border-radius: 10px;\n"
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


        self.gridLayout_12.addLayout(self.Lay_L, 1, 0, 1, 1)

        self.frame_navigation = QFrame(self.centralwidget)
        self.frame_navigation.setObjectName(u"frame_navigation")
        self.frame_navigation.setMinimumSize(QSize(0, 40))
        self.frame_navigation.setMaximumSize(QSize(16777215, 40))
        self.frame_navigation.setStyleSheet(u"QWidget {\n"
"	background-color:rgb(138, 137, 135); \n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color: rgb(71, 71, 71);\n"
"}\n"
"")
        self.frame_navigation.setFrameShape(QFrame.StyledPanel)
        self.frame_navigation.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_navigation)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_navigation)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_setup_page = QPushButton(self.frame)
        self.pushButton_setup_page.setObjectName(u"pushButton_setup_page")
        sizePolicy4.setHeightForWidth(self.pushButton_setup_page.sizePolicy().hasHeightForWidth())
        self.pushButton_setup_page.setSizePolicy(sizePolicy4)
        self.pushButton_setup_page.setMaximumSize(QSize(200, 16777215))
        font6 = QFont()
        font6.setPointSize(14)
        font6.setBold(False)
        font6.setItalic(False)
        font6.setStrikeOut(False)
        self.pushButton_setup_page.setFont(font6)
        self.pushButton_setup_page.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_setup_page.setStyleSheet(u"QPushButton{\n"
"	border-width: 1px;\n"
"	background-color:rgb(107, 107, 107);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	border-width: 1px;\n"
"	background-color:rgb(56, 56, 56);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_2.addWidget(self.pushButton_setup_page)

        self.pushButton_setup_registrazione = QPushButton(self.frame)
        self.pushButton_setup_registrazione.setObjectName(u"pushButton_setup_registrazione")
        self.pushButton_setup_registrazione.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.pushButton_setup_registrazione.sizePolicy().hasHeightForWidth())
        self.pushButton_setup_registrazione.setSizePolicy(sizePolicy4)
        self.pushButton_setup_registrazione.setMaximumSize(QSize(200, 16777215))
        self.pushButton_setup_registrazione.setFont(font6)
        self.pushButton_setup_registrazione.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_setup_registrazione.setStyleSheet(u"QPushButton{\n"
"	border-width: 1px;\n"
"	background-color:rgb(107, 107, 107);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	border-width: 1px;\n"
"	background-color:rgb(56, 56, 56);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton::disabled{\n"
"	border-width: 1px;\n"
"	background-color:rgb(140, 140, 140);\n"
"	color:rgb(140, 140, 140);\n"
"}")

        self.horizontalLayout_2.addWidget(self.pushButton_setup_registrazione)

        self.pushButton_grafico = QPushButton(self.frame)
        self.pushButton_grafico.setObjectName(u"pushButton_grafico")
        sizePolicy4.setHeightForWidth(self.pushButton_grafico.sizePolicy().hasHeightForWidth())
        self.pushButton_grafico.setSizePolicy(sizePolicy4)
        self.pushButton_grafico.setMaximumSize(QSize(200, 16777215))
        self.pushButton_grafico.setFont(font6)
        self.pushButton_grafico.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_grafico.setStyleSheet(u"QPushButton{\n"
"	border-width: 1px;\n"
"	background-color:rgb(107, 107, 107);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	border-width: 1px;\n"
"	background-color:rgb(56, 56, 56);\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"\n"
"}")

        self.horizontalLayout_2.addWidget(self.pushButton_grafico)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"    border-width: 0px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_2)


        self.horizontalLayout_3.addWidget(self.frame)


        self.gridLayout_12.addWidget(self.frame_navigation, 0, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">REGISTRAZIONE</p></body></html>", None))
        self.pushButton_Registrazione.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.label_nome_reg.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#060606;\">Nome registrazione</span></p></body></html>", None))
        self.label_nome_reg_display.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">INTERFACCIA</p></body></html>", None))
        self.pushButton_Interfaccia.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.label_SG600.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">SG-600</p></body></html>", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("MainWindow", u"V", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("MainWindow", u"Nm", None))

        self.comboBox_5.setCurrentText(QCoreApplication.translate("MainWindow", u"V", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Main Channel</p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Temperature [\u00b0C]</p></body></html>", None))
        self.comboBox_1.setItemText(0, QCoreApplication.translate("MainWindow", u"mV", None))
        self.comboBox_1.setItemText(1, QCoreApplication.translate("MainWindow", u"Nm", None))
        self.comboBox_1.setItemText(2, QCoreApplication.translate("MainWindow", u"Kg", None))
        self.comboBox_1.setItemText(3, QCoreApplication.translate("MainWindow", u"N", None))

        self.comboBox_1.setCurrentText(QCoreApplication.translate("MainWindow", u"mV", None))
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#99875e;\">Channel 1</span></p></body></html>", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"mV", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Kg", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"N", None))

        self.comboBox_2.setCurrentText(QCoreApplication.translate("MainWindow", u"mV", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Cella di carico</p></body></html>", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"mV", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"Nm", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"Kg", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("MainWindow", u"N", None))

        self.comboBox_3.setCurrentText(QCoreApplication.translate("MainWindow", u"mV", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#99875e;\">Channel 3</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Torsiometro</p></body></html>", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"mV", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("MainWindow", u"Nm", None))

        self.comboBox_4.setCurrentText(QCoreApplication.translate("MainWindow", u"mV", None))
        self.pushButton_setup_page.setText(QCoreApplication.translate("MainWindow", u"SETUP", None))
        self.pushButton_setup_registrazione.setText(QCoreApplication.translate("MainWindow", u"REGISTRAZIONE", None))
        self.pushButton_grafico.setText(QCoreApplication.translate("MainWindow", u"GRAFICO", None))
    # retranslateUi

