# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QT_Creator_dell_App_4.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLCDNumber,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import client_Sinc_TCP

startStop = False
startStop_logger = False
status_pulsante_interfaccia = 0
status_pulsante_registrazione = 0

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
        self.verticalLayout_17 = QVBoxLayout(self.widget)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_1 = QLabel(self.widget)
        self.label_1.setObjectName(u"label_1")
        font = QFont()
        font.setPointSize(17)
        self.label_1.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_1, 0, Qt.AlignHCenter)


        self.verticalLayout_9.addLayout(self.horizontalLayout_4)


        self.verticalLayout_10.addLayout(self.verticalLayout_9)

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
"")
        self.lcdNumber_1.setDigitCount(7)
        self.lcdNumber_1.setProperty("value", 0.000000000000000)

        self.verticalLayout_10.addWidget(self.lcdNumber_1)


        self.verticalLayout_17.addLayout(self.verticalLayout_10)


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
        self.verticalLayout_18 = QVBoxLayout(self.widget_3)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout_9.addWidget(self.label_2, 0, Qt.AlignHCenter)


        self.verticalLayout_11.addLayout(self.horizontalLayout_9)


        self.verticalLayout_18.addLayout(self.verticalLayout_11)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.lcdNumber_2 = QLCDNumber(self.widget_3)
        self.lcdNumber_2.setObjectName(u"lcdNumber_2")
        self.lcdNumber_2.setStyleSheet(u"QWidget {\n"
"	background-color:white; \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"}\n"
"")
        self.lcdNumber_2.setDigitCount(7)

        self.verticalLayout_12.addWidget(self.lcdNumber_2)


        self.verticalLayout_18.addLayout(self.verticalLayout_12)


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
        self.verticalLayout_19 = QVBoxLayout(self.widget_4)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_3 = QLabel(self.widget_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.horizontalLayout_12.addWidget(self.label_3, 0, Qt.AlignHCenter)


        self.verticalLayout_14.addLayout(self.horizontalLayout_12)


        self.verticalLayout_19.addLayout(self.verticalLayout_14)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
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
"")
        self.lcdNumber_3.setDigitCount(7)

        self.verticalLayout_13.addWidget(self.lcdNumber_3)


        self.verticalLayout_19.addLayout(self.verticalLayout_13)


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
        self.verticalLayout_20 = QVBoxLayout(self.widget_5)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_4 = QLabel(self.widget_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.horizontalLayout_15.addWidget(self.label_4, 0, Qt.AlignHCenter)


        self.verticalLayout_16.addLayout(self.horizontalLayout_15)


        self.verticalLayout_20.addLayout(self.verticalLayout_16)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.lcdNumber_4 = QLCDNumber(self.widget_5)
        self.lcdNumber_4.setObjectName(u"lcdNumber_4")
        self.lcdNumber_4.setStyleSheet(u"QWidget {\n"
"	background-color:white; \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"}\n"
"")
        self.lcdNumber_4.setDigitCount(7)

        self.verticalLayout_15.addWidget(self.lcdNumber_4)


        self.verticalLayout_20.addLayout(self.verticalLayout_15)


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
        self.verticalLayout_27 = QVBoxLayout(self.widget_2)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
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
"")

        self.horizontalLayout_6.addWidget(self.label, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.pushButton_Interfaccia = QPushButton(self.widget_12)
        self.pushButton_Interfaccia.setObjectName(u"pushButton_Interfaccia")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Interfaccia.sizePolicy().hasHeightForWidth())
        self.pushButton_Interfaccia.setSizePolicy(sizePolicy)
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
"")

        self.horizontalLayout_8.addWidget(self.label_5, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.pushButton_Registrazione = QPushButton(self.widget_12)
        self.pushButton_Registrazione.setObjectName(u"pushButton_Registrazione")
        sizePolicy.setHeightForWidth(self.pushButton_Registrazione.sizePolicy().hasHeightForWidth())
        self.pushButton_Registrazione.setSizePolicy(sizePolicy)
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
"")

        self.horizontalLayout_8.addWidget(self.pushButton_Registrazione)


        self.gridLayout_2.addLayout(self.horizontalLayout_8, 1, 0, 1, 1)


        self.verticalLayout_6.addWidget(self.widget_12)


        self.verticalLayout_27.addLayout(self.verticalLayout_6)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.lable_Logo_Easting = QLabel(self.widget_2)
        self.lable_Logo_Easting.setObjectName(u"lable_Logo_Easting")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lable_Logo_Easting.sizePolicy().hasHeightForWidth())
        self.lable_Logo_Easting.setSizePolicy(sizePolicy1)
        self.lable_Logo_Easting.setStyleSheet(u"QWidget {\n"
"	background-color:orange; \n"
"	border-style: outset;\n"
"    border-width: 3px;\n"
"    border-color: black;\n"
"}\n"
"")
        self.lable_Logo_Easting.setTextFormat(Qt.RichText)
        self.lable_Logo_Easting.setPixmap(QPixmap(u"C:\\Users\\franc\\OneDrive\\Tirocinio_triennale\\Code_esercizi\\Visual_studio_python\\WebApp_Easting _Electronics\\Immagini\\Screenshot_Easting.jpeg"))
        self.lable_Logo_Easting.setScaledContents(False)

        self.verticalLayout_24.addWidget(self.lable_Logo_Easting, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_27.addLayout(self.verticalLayout_24)


        self.Lay_R.addWidget(self.widget_2)


        self.horizontalLayout_7.addLayout(self.Lay_R)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi


    #------------------------------------------------------------------------------------------------------------------#
    # Codice aggiunto da me
    
    # setup segnali
        self.pushButton_Interfaccia.clicked.connect(self.pulsante_interfaccia_click)
        self.pushButton_Registrazione.clicked.connect(self.pulsante_registrazione_click)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update0)
        
    
    def pulsante_interfaccia_click(self):
        # Check della condizione del pulsante e poi cambio il tipo e gestisco il timer
        global status_pulsante_interfaccia
        if status_pulsante_interfaccia % 2 != 0:
            self.timer.start(100)          # In millisecondi
            self.pushButton_Interfaccia.setStyleSheet("background-color: red; border-style: outset; border-width: 2px; border-color: black;")
            self.pushButton_Interfaccia.setText("STOP")
            status_pulsante_interfaccia = status_pulsante_interfaccia + 1
        else:     
            self.timer.stop()         
            self.pushButton_Interfaccia.setStyleSheet("background-color: green; border-style: outset; border-width: 2px; border-color: black;")
            self.pushButton_Interfaccia.setText("START")
            status_pulsante_interfaccia = status_pulsante_interfaccia + 1
    
    def pulsante_registrazione_click(self):
        # Check della condizione del pulsante e poi cambio il tipo e gestisco il logger
        global startStop_logger
        global status_pulsante_registrazione
        if status_pulsante_registrazione % 2 != 0:       
            startStop_logger = True
            self.pushButton_Registrazione.setStyleSheet("background-color: red; border-style: outset; border-width: 2px; border-color: black;")
            self.pushButton_Registrazione.setText("STOP")
            status_pulsante_registrazione = status_pulsante_registrazione + 1
        else:     
            startStop_logger = False          
            self.pushButton_Registrazione.setStyleSheet("background-color: green; border-style: outset; border-width: 2px; border-color: black;")
            self.pushButton_Registrazione.setText("START")
            status_pulsante_registrazione = status_pulsante_registrazione + 1
        
        
    def update0(self):
            list = client_Sinc_TCP.WORKING.read_holding_registers_mV()
            self.lcdNumber_1.display(list[0])
            self.lcdNumber_2.display(list[1])
            self.lcdNumber_3.display(list[2])
            self.lcdNumber_4.display(list[3])
                
    
    
    
    #------------------------------------------------------------------------------------------------------------------# 




    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"Channel 1", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Channel 2", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Channel 3", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Channel 4", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"INTERFACCIA", None))
        self.pushButton_Interfaccia.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"REGISTRAZIONE", None))
        self.pushButton_Registrazione.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.lable_Logo_Easting.setText("")
    # retranslateUi

