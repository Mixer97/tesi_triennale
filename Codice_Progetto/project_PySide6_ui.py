# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'project.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLCDNumber, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import client_Sinc_TCP

startStop = False

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
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_1 = QLabel(self.widget)
        self.label_1.setObjectName(u"label_1")
        font = QFont()
        font.setPointSize(20)
        self.label_1.setFont(font)

        self.verticalLayout_9.addWidget(self.label_1, 0, Qt.AlignHCenter)


        self.verticalLayout_17.addLayout(self.verticalLayout_9)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.lcdNumber_1 = QLCDNumber(self.widget)
        self.lcdNumber_1.setObjectName(u"lcdNumber_1")
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
        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout_11.addWidget(self.label_2, 0, Qt.AlignHCenter)


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
        self.label_3 = QLabel(self.widget_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.verticalLayout_14.addWidget(self.label_3, 0, Qt.AlignHCenter)


        self.verticalLayout_19.addLayout(self.verticalLayout_14)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.lcdNumber_3 = QLCDNumber(self.widget_4)
        self.lcdNumber_3.setObjectName(u"lcdNumber_3")
        font1 = QFont()
        font1.setBold(False)
        font1.setKerning(True)
        self.lcdNumber_3.setFont(font1)
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
        self.label_4 = QLabel(self.widget_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout_16.addWidget(self.label_4, 0, Qt.AlignHCenter)


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
        self.verticalLayout_8 = QVBoxLayout(self.widget_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pushButton_Start = QPushButton(self.widget_2)
        self.pushButton_Start.setObjectName(u"pushButton_Start")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Start.sizePolicy().hasHeightForWidth())
        self.pushButton_Start.setSizePolicy(sizePolicy)
        self.pushButton_Start.setMinimumSize(QSize(300, 200))
        self.pushButton_Start.setMaximumSize(QSize(300, 200))
        font2 = QFont()
        font2.setPointSize(30)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setStrikeOut(False)
        self.pushButton_Start.setFont(font2)
        self.pushButton_Start.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_Start.setStyleSheet(u"QWidget {\n"
"	background-color:green; \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"}\n"
"")

        self.verticalLayout_6.addWidget(self.pushButton_Start, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_8.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.pushButton_Stop = QPushButton(self.widget_2)
        self.pushButton_Stop.setObjectName(u"pushButton_Stop")
        sizePolicy.setHeightForWidth(self.pushButton_Stop.sizePolicy().hasHeightForWidth())
        self.pushButton_Stop.setSizePolicy(sizePolicy)
        self.pushButton_Stop.setMinimumSize(QSize(300, 200))
        self.pushButton_Stop.setMaximumSize(QSize(300, 200))
        font3 = QFont()
        font3.setPointSize(30)
        font3.setBold(True)
        self.pushButton_Stop.setFont(font3)
        self.pushButton_Stop.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_Stop.setStyleSheet(u"QWidget {\n"
"	background-color:red; \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"}\n"
"")

        self.verticalLayout_7.addWidget(self.pushButton_Stop, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_8.addLayout(self.verticalLayout_7)


        self.Lay_R.addWidget(self.widget_2)


        self.horizontalLayout_7.addLayout(self.Lay_R)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    #------------------------------------------------------------------------------------------------------------------#
    # Codice aggiunto da me
    
    # setup segnali
    
        self.pushButton_Start.clicked.connect(self.start_mV)
        self.pushButton_Stop.clicked.connect(self.stop_mV)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update0)
        
        
    
    def stop_mV(self):
            self.timer.stop()
            
    def start_mV(self):           
            self.timer.start(100)  # Update every second
    
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
        self.pushButton_Start.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.pushButton_Stop.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
    # retranslateUi

