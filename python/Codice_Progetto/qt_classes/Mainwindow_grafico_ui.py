# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Mainwindow_grafico.ui'
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
    QHBoxLayout, QLCDNumber, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget

class Ui_GraphWindow(object):
    def setupUi(self, GraphWindow):
        if not GraphWindow.objectName():
            GraphWindow.setObjectName(u"GraphWindow")
        GraphWindow.resize(1120, 664)
        self.centralwidget = QWidget(GraphWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget {\n"
"	background-color:black; \n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color: black;\n"
"}\n"
"")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(2)
        self.gridLayout_2.setContentsMargins(-1, 5, -1, -1)
        self.gridWidget = QWidget(self.centralwidget)
        self.gridWidget.setObjectName(u"gridWidget")
        self.gridWidget.setStyleSheet(u"QWidget {\n"
"	background-color:orange; \n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color: black;\n"
"}\n"
"")
        self.horizontalLayout = QHBoxLayout(self.gridWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.gridWidget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(200, 0))
        self.frame.setStyleSheet(u"    border-width: 2px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_21 = QFrame(self.frame)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setStyleSheet(u"border-width: 1px")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_21)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_main_mV = QLabel(self.frame_21)
        self.label_main_mV.setObjectName(u"label_main_mV")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_main_mV.sizePolicy().hasHeightForWidth())
        self.label_main_mV.setSizePolicy(sizePolicy1)
        self.label_main_mV.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_main_mV.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_main_mV)

        self.lcdNumber_main_mV = QLCDNumber(self.frame_21)
        self.lcdNumber_main_mV.setObjectName(u"lcdNumber_main_mV")
        self.lcdNumber_main_mV.setStyleSheet(u"QWidget {\n"
"	background-color:white; \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"}\n"
"QLCDNumber{\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")

        self.verticalLayout_15.addWidget(self.lcdNumber_main_mV)


        self.verticalLayout_17.addWidget(self.frame_21)

        self.frame_9 = QFrame(self.frame)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"border-width: 1px")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_9)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_main_Nm = QLabel(self.frame_9)
        self.label_main_Nm.setObjectName(u"label_main_Nm")
        sizePolicy1.setHeightForWidth(self.label_main_Nm.sizePolicy().hasHeightForWidth())
        self.label_main_Nm.setSizePolicy(sizePolicy1)
        self.label_main_Nm.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_main_Nm.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_main_Nm)

        self.lcdNumber_main_Nm = QLCDNumber(self.frame_9)
        self.lcdNumber_main_Nm.setObjectName(u"lcdNumber_main_Nm")
        self.lcdNumber_main_Nm.setStyleSheet(u"QWidget {\n"
"	background-color:white; \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"}\n"
"QLCDNumber{\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")

        self.verticalLayout_12.addWidget(self.lcdNumber_main_Nm)


        self.verticalLayout_17.addWidget(self.frame_9)

        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"border-width: 1px")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_4)

        self.lcdNumber_ch2 = QLCDNumber(self.frame_7)
        self.lcdNumber_ch2.setObjectName(u"lcdNumber_ch2")
        self.lcdNumber_ch2.setStyleSheet(u"QWidget {\n"
"	background-color:white; \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"}\n"
"QLCDNumber{\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")

        self.verticalLayout_5.addWidget(self.lcdNumber_ch2)


        self.verticalLayout_17.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"border-width: 1px")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_8)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_8)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_3)

        self.lcdNumber_ch4 = QLCDNumber(self.frame_8)
        self.lcdNumber_ch4.setObjectName(u"lcdNumber_ch4")
        self.lcdNumber_ch4.setStyleSheet(u"QWidget {\n"
"	background-color:white; \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"}\n"
"QLCDNumber{\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")

        self.verticalLayout_11.addWidget(self.lcdNumber_ch4)


        self.verticalLayout_17.addWidget(self.frame_8)

        self.verticalSpacer_2 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_17.addItem(self.verticalSpacer_2)

        self.frame_23 = QFrame(self.frame)
        self.frame_23.setObjectName(u"frame_23")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_23.sizePolicy().hasHeightForWidth())
        self.frame_23.setSizePolicy(sizePolicy2)
        self.frame_23.setStyleSheet(u"border-width: 1px;")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_23)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.frame_23)
        self.label_13.setObjectName(u"label_13")
        sizePolicy2.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy2)
        self.label_13.setStyleSheet(u"QLabel {\n"
"    border: 2px solid black;\n"
"    border-radius: 0px;\n"
"	background-color: rgb(221, 192, 255);\n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"	border-color: rgb(110, 149, 255);\n"
"}\n"
"QLabel{\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_13)

        self.label_step_prossimo_valore = QLabel(self.frame_23)
        self.label_step_prossimo_valore.setObjectName(u"label_step_prossimo_valore")
        sizePolicy2.setHeightForWidth(self.label_step_prossimo_valore.sizePolicy().hasHeightForWidth())
        self.label_step_prossimo_valore.setSizePolicy(sizePolicy2)
        self.label_step_prossimo_valore.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_step_prossimo_valore.setFont(font)
        self.label_step_prossimo_valore.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(255, 255, 255); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0;\n"
"	color: rgb(0,0,0);\n"
"}")
        self.label_step_prossimo_valore.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_step_prossimo_valore)


        self.verticalLayout_17.addWidget(self.frame_23)

        self.frame_20 = QFrame(self.frame)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setStyleSheet(u"border-width: 1px")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_20)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.frame_20)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"QLabel {\n"
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
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_12)

        self.label_step_attuale_valore = QLabel(self.frame_20)
        self.label_step_attuale_valore.setObjectName(u"label_step_attuale_valore")
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.label_step_attuale_valore.setFont(font1)
        self.label_step_attuale_valore.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(255, 255, 255); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0;\n"
"	color: rgb(0,0,0);\n"
"}")
        self.label_step_attuale_valore.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_step_attuale_valore)


        self.verticalLayout_17.addWidget(self.frame_20)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_3 = QFrame(self.gridWidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_3)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy3)
        self.frame_5.setMinimumSize(QSize(0, 400))
        self.frame_5.setMaximumSize(QSize(16777215, 16777215))
        self.frame_5.setStyleSheet(u"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_5)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_SG600 = QStackedWidget(self.frame_5)
        self.stackedWidget_SG600.setObjectName(u"stackedWidget_SG600")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.stackedWidget_SG600.sizePolicy().hasHeightForWidth())
        self.stackedWidget_SG600.setSizePolicy(sizePolicy4)
        self.page_main = QWidget()
        self.page_main.setObjectName(u"page_main")
        self.gridLayout_5 = QGridLayout(self.page_main)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(2, 2, 2, 2)
        self.graphWidget_SG600_solo_main = PlotWidget(self.page_main)
        self.graphWidget_SG600_solo_main.setObjectName(u"graphWidget_SG600_solo_main")
        sizePolicy4.setHeightForWidth(self.graphWidget_SG600_solo_main.sizePolicy().hasHeightForWidth())
        self.graphWidget_SG600_solo_main.setSizePolicy(sizePolicy4)
        self.graphWidget_SG600_solo_main.setStyleSheet(u"background-color: rgb(26, 49, 255);")

        self.gridLayout_5.addWidget(self.graphWidget_SG600_solo_main, 1, 0, 1, 1)

        self.frame_14 = QFrame(self.page_main)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMaximumSize(QSize(50, 16777215))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_14)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton_autorange_solo_main = QPushButton(self.frame_14)
        self.pushButton_autorange_solo_main.setObjectName(u"pushButton_autorange_solo_main")
        sizePolicy4.setHeightForWidth(self.pushButton_autorange_solo_main.sizePolicy().hasHeightForWidth())
        self.pushButton_autorange_solo_main.setSizePolicy(sizePolicy4)
        self.pushButton_autorange_solo_main.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_autorange_solo_main.setStyleSheet(u"QWidget {\n"
"	background-color:rgb(255, 106, 106); \n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color:rgb(255, 137, 137);\n"
"	color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton::checked {\n"
"	background-color:rgb(152, 29, 24);\n"
"    border-color:rgb(77, 33, 33);\n"
"}\n"
"\n"
"")
        self.pushButton_autorange_solo_main.setCheckable(True)
        self.pushButton_autorange_solo_main.setChecked(False)

        self.verticalLayout_4.addWidget(self.pushButton_autorange_solo_main)

        self.pushButton_reset_solo_main = QPushButton(self.frame_14)
        self.pushButton_reset_solo_main.setObjectName(u"pushButton_reset_solo_main")
        self.pushButton_reset_solo_main.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_reset_solo_main.setStyleSheet(u"QPushButton{\n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color:rgb(98, 93, 255);\n"
"	background-color:rgb(93, 117, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"	border-color:rgb(70, 70, 255);\n"
"	background-color:rgb(23, 23, 161);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.verticalLayout_4.addWidget(self.pushButton_reset_solo_main)


        self.gridLayout_5.addWidget(self.frame_14, 0, 1, 3, 1)

        self.stackedWidget_SG600.addWidget(self.page_main)
        self.page_temp = QWidget()
        self.page_temp.setObjectName(u"page_temp")
        self.gridLayout_7 = QGridLayout(self.page_temp)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(2, 2, 2, 2)
        self.graphWidget_SG600_solo_temp = PlotWidget(self.page_temp)
        self.graphWidget_SG600_solo_temp.setObjectName(u"graphWidget_SG600_solo_temp")
        sizePolicy4.setHeightForWidth(self.graphWidget_SG600_solo_temp.sizePolicy().hasHeightForWidth())
        self.graphWidget_SG600_solo_temp.setSizePolicy(sizePolicy4)
        self.graphWidget_SG600_solo_temp.setStyleSheet(u"background-color: rgb(26, 49, 255);")

        self.gridLayout_7.addWidget(self.graphWidget_SG600_solo_temp, 1, 0, 1, 1)

        self.frame_17 = QFrame(self.page_temp)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(50, 16777215))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_17)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton_autorange_solo_temp = QPushButton(self.frame_17)
        self.pushButton_autorange_solo_temp.setObjectName(u"pushButton_autorange_solo_temp")
        sizePolicy4.setHeightForWidth(self.pushButton_autorange_solo_temp.sizePolicy().hasHeightForWidth())
        self.pushButton_autorange_solo_temp.setSizePolicy(sizePolicy4)
        self.pushButton_autorange_solo_temp.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_autorange_solo_temp.setStyleSheet(u"QWidget {\n"
"	background-color:rgb(255, 106, 106); \n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color:rgb(255, 137, 137);\n"
"	color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton::checked {\n"
"	background-color:rgb(152, 29, 24);\n"
"    border-color:rgb(77, 33, 33);\n"
"}\n"
"\n"
"")
        self.pushButton_autorange_solo_temp.setCheckable(True)

        self.verticalLayout_3.addWidget(self.pushButton_autorange_solo_temp)

        self.pushButton_reset_solo_temp = QPushButton(self.frame_17)
        self.pushButton_reset_solo_temp.setObjectName(u"pushButton_reset_solo_temp")
        self.pushButton_reset_solo_temp.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_reset_solo_temp.setStyleSheet(u"QPushButton{\n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color:rgb(98, 93, 255);\n"
"	background-color:rgb(93, 117, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"	border-color:rgb(70, 70, 255);\n"
"	background-color:rgb(23, 23, 161);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.verticalLayout_3.addWidget(self.pushButton_reset_solo_temp)


        self.gridLayout_7.addWidget(self.frame_17, 0, 1, 3, 1)

        self.stackedWidget_SG600.addWidget(self.page_temp)
        self.page_temp_main = QWidget()
        self.page_temp_main.setObjectName(u"page_temp_main")
        self.gridLayout_4 = QGridLayout(self.page_temp_main)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(2, 2, 2, 2)
        self.graphWidget_SG600_main_and_channel = PlotWidget(self.page_temp_main)
        self.graphWidget_SG600_main_and_channel.setObjectName(u"graphWidget_SG600_main_and_channel")
        sizePolicy4.setHeightForWidth(self.graphWidget_SG600_main_and_channel.sizePolicy().hasHeightForWidth())
        self.graphWidget_SG600_main_and_channel.setSizePolicy(sizePolicy4)
        self.graphWidget_SG600_main_and_channel.setStyleSheet(u"background-color: rgb(26, 49, 255);")

        self.gridLayout_4.addWidget(self.graphWidget_SG600_main_and_channel, 1, 0, 1, 1)

        self.frame_11 = QFrame(self.page_temp_main)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy4.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy4)
        self.frame_11.setMaximumSize(QSize(50, 16777215))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_11)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_autorange_main_and_channel = QPushButton(self.frame_11)
        self.pushButton_autorange_main_and_channel.setObjectName(u"pushButton_autorange_main_and_channel")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.pushButton_autorange_main_and_channel.sizePolicy().hasHeightForWidth())
        self.pushButton_autorange_main_and_channel.setSizePolicy(sizePolicy5)
        self.pushButton_autorange_main_and_channel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_autorange_main_and_channel.setStyleSheet(u"QWidget {\n"
"	background-color:rgb(255, 106, 106); \n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color:rgb(255, 137, 137);\n"
"	color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton::checked {\n"
"	background-color:rgb(152, 29, 24);\n"
"    border-color:rgb(77, 33, 33);\n"
"}\n"
"\n"
"")
        self.pushButton_autorange_main_and_channel.setCheckable(True)

        self.verticalLayout_2.addWidget(self.pushButton_autorange_main_and_channel)

        self.pushButton_reset_main_and_channel = QPushButton(self.frame_11)
        self.pushButton_reset_main_and_channel.setObjectName(u"pushButton_reset_main_and_channel")
        self.pushButton_reset_main_and_channel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_reset_main_and_channel.setStyleSheet(u"QPushButton{\n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color:rgb(98, 93, 255);\n"
"	background-color:rgb(93, 117, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"	border-color:rgb(70, 70, 255);\n"
"	background-color:rgb(23, 23, 161);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.verticalLayout_2.addWidget(self.pushButton_reset_main_and_channel)


        self.gridLayout_4.addWidget(self.frame_11, 0, 1, 3, 1)

        self.stackedWidget_SG600.addWidget(self.page_temp_main)

        self.verticalLayout.addWidget(self.stackedWidget_SG600)

        self.stackedWidget_Laumas = QStackedWidget(self.frame_5)
        self.stackedWidget_Laumas.setObjectName(u"stackedWidget_Laumas")
        sizePolicy3.setHeightForWidth(self.stackedWidget_Laumas.sizePolicy().hasHeightForWidth())
        self.stackedWidget_Laumas.setSizePolicy(sizePolicy3)
        self.stackedWidget_Laumas.setMaximumSize(QSize(16777215, 300000))
        self.page_CH1 = QWidget()
        self.page_CH1.setObjectName(u"page_CH1")
        sizePolicy4.setHeightForWidth(self.page_CH1.sizePolicy().hasHeightForWidth())
        self.page_CH1.setSizePolicy(sizePolicy4)
        self.gridLayout_9 = QGridLayout(self.page_CH1)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(2, 2, 2, 2)
        self.graphWidget_solo_channel_1 = PlotWidget(self.page_CH1)
        self.graphWidget_solo_channel_1.setObjectName(u"graphWidget_solo_channel_1")
        self.graphWidget_solo_channel_1.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.graphWidget_solo_channel_1.sizePolicy().hasHeightForWidth())
        self.graphWidget_solo_channel_1.setSizePolicy(sizePolicy4)
        self.graphWidget_solo_channel_1.setStyleSheet(u"background-color: rgb(26, 49, 255);")

        self.gridLayout_9.addWidget(self.graphWidget_solo_channel_1, 0, 0, 2, 1)

        self.frame_16 = QFrame(self.page_CH1)
        self.frame_16.setObjectName(u"frame_16")
        sizePolicy4.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy4)
        self.frame_16.setMaximumSize(QSize(50, 16777215))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_16)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pushButton_autorange_ch1 = QPushButton(self.frame_16)
        self.pushButton_autorange_ch1.setObjectName(u"pushButton_autorange_ch1")
        sizePolicy4.setHeightForWidth(self.pushButton_autorange_ch1.sizePolicy().hasHeightForWidth())
        self.pushButton_autorange_ch1.setSizePolicy(sizePolicy4)
        self.pushButton_autorange_ch1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_autorange_ch1.setStyleSheet(u"QWidget {\n"
"	background-color:rgb(255, 106, 106); \n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color:rgb(255, 137, 137);\n"
"	color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton::checked {\n"
"	background-color:rgb(152, 29, 24);\n"
"    border-color:rgb(77, 33, 33);\n"
"}\n"
"\n"
"")
        self.pushButton_autorange_ch1.setCheckable(True)

        self.verticalLayout_6.addWidget(self.pushButton_autorange_ch1)

        self.pushButton_reset_ch1 = QPushButton(self.frame_16)
        self.pushButton_reset_ch1.setObjectName(u"pushButton_reset_ch1")
        self.pushButton_reset_ch1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_reset_ch1.setStyleSheet(u"QPushButton{\n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color:rgb(98, 93, 255);\n"
"	background-color:rgb(93, 117, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"	border-color:rgb(70, 70, 255);\n"
"	background-color:rgb(23, 23, 161);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.verticalLayout_6.addWidget(self.pushButton_reset_ch1)


        self.gridLayout_9.addWidget(self.frame_16, 0, 1, 1, 1)

        self.stackedWidget_Laumas.addWidget(self.page_CH1)
        self.page_CH2 = QWidget()
        self.page_CH2.setObjectName(u"page_CH2")
        sizePolicy4.setHeightForWidth(self.page_CH2.sizePolicy().hasHeightForWidth())
        self.page_CH2.setSizePolicy(sizePolicy4)
        self.gridLayout_8 = QGridLayout(self.page_CH2)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(2, 2, 2, 2)
        self.graphWidget_solo_channel_2 = PlotWidget(self.page_CH2)
        self.graphWidget_solo_channel_2.setObjectName(u"graphWidget_solo_channel_2")
        sizePolicy4.setHeightForWidth(self.graphWidget_solo_channel_2.sizePolicy().hasHeightForWidth())
        self.graphWidget_solo_channel_2.setSizePolicy(sizePolicy4)
        self.graphWidget_solo_channel_2.setStyleSheet(u"background-color: rgb(26, 49, 255);")

        self.gridLayout_8.addWidget(self.graphWidget_solo_channel_2, 0, 0, 1, 1)

        self.frame_15 = QFrame(self.page_CH2)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(50, 16777215))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_15)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.pushButton_autorange_ch2 = QPushButton(self.frame_15)
        self.pushButton_autorange_ch2.setObjectName(u"pushButton_autorange_ch2")
        sizePolicy4.setHeightForWidth(self.pushButton_autorange_ch2.sizePolicy().hasHeightForWidth())
        self.pushButton_autorange_ch2.setSizePolicy(sizePolicy4)
        self.pushButton_autorange_ch2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_autorange_ch2.setStyleSheet(u"QWidget {\n"
"	background-color:rgb(255, 106, 106); \n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color:rgb(255, 137, 137);\n"
"	color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton::checked {\n"
"	background-color:rgb(152, 29, 24);\n"
"    border-color:rgb(77, 33, 33);\n"
"}\n"
"\n"
"")
        self.pushButton_autorange_ch2.setCheckable(True)

        self.verticalLayout_9.addWidget(self.pushButton_autorange_ch2)

        self.pushButton_reset_ch2 = QPushButton(self.frame_15)
        self.pushButton_reset_ch2.setObjectName(u"pushButton_reset_ch2")
        self.pushButton_reset_ch2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_reset_ch2.setStyleSheet(u"QPushButton{\n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color:rgb(98, 93, 255);\n"
"	background-color:rgb(93, 117, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"	border-color:rgb(70, 70, 255);\n"
"	background-color:rgb(23, 23, 161);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.verticalLayout_9.addWidget(self.pushButton_reset_ch2)


        self.gridLayout_8.addWidget(self.frame_15, 0, 1, 1, 1)

        self.stackedWidget_Laumas.addWidget(self.page_CH2)
        self.page_CH3 = QWidget()
        self.page_CH3.setObjectName(u"page_CH3")
        sizePolicy4.setHeightForWidth(self.page_CH3.sizePolicy().hasHeightForWidth())
        self.page_CH3.setSizePolicy(sizePolicy4)
        self.gridLayout_3 = QGridLayout(self.page_CH3)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(2, 2, 2, 2)
        self.frame_12 = QFrame(self.page_CH3)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(50, 16777215))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_12)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.pushButton_autorange_ch3 = QPushButton(self.frame_12)
        self.pushButton_autorange_ch3.setObjectName(u"pushButton_autorange_ch3")
        sizePolicy4.setHeightForWidth(self.pushButton_autorange_ch3.sizePolicy().hasHeightForWidth())
        self.pushButton_autorange_ch3.setSizePolicy(sizePolicy4)
        self.pushButton_autorange_ch3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_autorange_ch3.setStyleSheet(u"QWidget {\n"
"	background-color:rgb(255, 106, 106); \n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color:rgb(255, 137, 137);\n"
"	color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton::checked {\n"
"	background-color:rgb(152, 29, 24);\n"
"    border-color:rgb(77, 33, 33);\n"
"}\n"
"\n"
"")
        self.pushButton_autorange_ch3.setCheckable(True)

        self.verticalLayout_8.addWidget(self.pushButton_autorange_ch3)

        self.pushButton_reset_ch3 = QPushButton(self.frame_12)
        self.pushButton_reset_ch3.setObjectName(u"pushButton_reset_ch3")
        self.pushButton_reset_ch3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_reset_ch3.setStyleSheet(u"QPushButton{\n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color:rgb(98, 93, 255);\n"
"	background-color:rgb(93, 117, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"	border-color:rgb(70, 70, 255);\n"
"	background-color:rgb(23, 23, 161);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.verticalLayout_8.addWidget(self.pushButton_reset_ch3)


        self.gridLayout_3.addWidget(self.frame_12, 0, 1, 5, 1)

        self.graphWidget_solo_channel_3 = PlotWidget(self.page_CH3)
        self.graphWidget_solo_channel_3.setObjectName(u"graphWidget_solo_channel_3")
        sizePolicy4.setHeightForWidth(self.graphWidget_solo_channel_3.sizePolicy().hasHeightForWidth())
        self.graphWidget_solo_channel_3.setSizePolicy(sizePolicy4)
        self.graphWidget_solo_channel_3.setStyleSheet(u"background-color: rgb(26, 49, 255);")

        self.gridLayout_3.addWidget(self.graphWidget_solo_channel_3, 3, 0, 1, 1)

        self.stackedWidget_Laumas.addWidget(self.page_CH3)
        self.page_CH4 = QWidget()
        self.page_CH4.setObjectName(u"page_CH4")
        sizePolicy4.setHeightForWidth(self.page_CH4.sizePolicy().hasHeightForWidth())
        self.page_CH4.setSizePolicy(sizePolicy4)
        self.gridLayout_6 = QGridLayout(self.page_CH4)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(2, 2, 2, 2)
        self.graphWidget_solo_channel_4 = PlotWidget(self.page_CH4)
        self.graphWidget_solo_channel_4.setObjectName(u"graphWidget_solo_channel_4")
        sizePolicy4.setHeightForWidth(self.graphWidget_solo_channel_4.sizePolicy().hasHeightForWidth())
        self.graphWidget_solo_channel_4.setSizePolicy(sizePolicy4)
        self.graphWidget_solo_channel_4.setStyleSheet(u"background-color: rgb(26, 49, 255);")

        self.gridLayout_6.addWidget(self.graphWidget_solo_channel_4, 0, 0, 1, 1)

        self.frame_13 = QFrame(self.page_CH4)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(50, 16777215))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_13)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.pushButton_autorange_ch4 = QPushButton(self.frame_13)
        self.pushButton_autorange_ch4.setObjectName(u"pushButton_autorange_ch4")
        sizePolicy4.setHeightForWidth(self.pushButton_autorange_ch4.sizePolicy().hasHeightForWidth())
        self.pushButton_autorange_ch4.setSizePolicy(sizePolicy4)
        self.pushButton_autorange_ch4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_autorange_ch4.setStyleSheet(u"QWidget {\n"
"	background-color:rgb(255, 106, 106); \n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color:rgb(255, 137, 137);\n"
"	color: rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton::checked {\n"
"	background-color:rgb(152, 29, 24);\n"
"    border-color:rgb(77, 33, 33);\n"
"}\n"
"\n"
"")
        self.pushButton_autorange_ch4.setCheckable(True)

        self.verticalLayout_7.addWidget(self.pushButton_autorange_ch4)

        self.pushButton_reset_ch4 = QPushButton(self.frame_13)
        self.pushButton_reset_ch4.setObjectName(u"pushButton_reset_ch4")
        self.pushButton_reset_ch4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_reset_ch4.setStyleSheet(u"QPushButton{\n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"    border-color:rgb(98, 93, 255);\n"
"	background-color:rgb(93, 117, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	border-style: outset;\n"
"    border-width: 1px;\n"
"	border-color:rgb(70, 70, 255);\n"
"	background-color:rgb(23, 23, 161);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.verticalLayout_7.addWidget(self.pushButton_reset_ch4)


        self.gridLayout_6.addWidget(self.frame_13, 0, 1, 1, 1)

        self.stackedWidget_Laumas.addWidget(self.page_CH4)

        self.verticalLayout.addWidget(self.stackedWidget_Laumas)

        self.frame_10 = QFrame(self.frame_5)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 100))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_10)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_quadrante = QLabel(self.frame_10)
        self.label_quadrante.setObjectName(u"label_quadrante")
        sizePolicy.setHeightForWidth(self.label_quadrante.sizePolicy().hasHeightForWidth())
        self.label_quadrante.setSizePolicy(sizePolicy)
        self.label_quadrante.setMinimumSize(QSize(100, 0))
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(False)
        self.label_quadrante.setFont(font2)
        self.label_quadrante.setStyleSheet(u"QLabel {\n"
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
        self.label_quadrante.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_quadrante, 1, 0, 2, 1)

        self.graphWidget_visual_euramet = PlotWidget(self.frame_10)
        self.graphWidget_visual_euramet.setObjectName(u"graphWidget_visual_euramet")
        self.graphWidget_visual_euramet.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.graphWidget_visual_euramet.sizePolicy().hasHeightForWidth())
        self.graphWidget_visual_euramet.setSizePolicy(sizePolicy1)
        self.graphWidget_visual_euramet.setStyleSheet(u"background-color: rgb(26, 49, 255);")

        self.gridLayout_10.addWidget(self.graphWidget_visual_euramet, 1, 1, 2, 1)


        self.verticalLayout.addWidget(self.frame_10)


        self.gridLayout.addWidget(self.frame_5, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.gridWidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QSize(200, 0))
        self.frame_2.setStyleSheet(u"    border-width: 1px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_2)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setVerticalSpacing(10)
        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_6)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label = QLabel(self.frame_6)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"")

        self.verticalLayout_10.addWidget(self.label)

        self.comboBox_Main_Temp = QComboBox(self.frame_6)
        self.comboBox_Main_Temp.addItem("")
        self.comboBox_Main_Temp.addItem("")
        self.comboBox_Main_Temp.addItem("")
        self.comboBox_Main_Temp.setObjectName(u"comboBox_Main_Temp")
        self.comboBox_Main_Temp.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.comboBox_Main_Temp.setStyleSheet(u"QComboBox {\n"
"    border: 3px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 1px 1px 10px;\n"
"    min-width: 6em;\n"
"    color: rgb(0, 0, 0); /* Colore del testo del QComboBox */\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
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
"    selection-background-color: #3399FF; /* Colore di sfondo dell'elemento selezionato */\n"
"    selection-color:rgb(106, 112, 113)"
                        "; /* Colore del testo dell'elemento selezionato */\n"
"    border: 3px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"    color: rgb(0, 0, 0); /* Colore del testo del QComboBox */\n"
"}")

        self.verticalLayout_10.addWidget(self.comboBox_Main_Temp)

        self.comboBox_Ch_1234 = QComboBox(self.frame_6)
        self.comboBox_Ch_1234.addItem("")
        self.comboBox_Ch_1234.addItem("")
        self.comboBox_Ch_1234.addItem("")
        self.comboBox_Ch_1234.addItem("")
        self.comboBox_Ch_1234.setObjectName(u"comboBox_Ch_1234")
        self.comboBox_Ch_1234.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.comboBox_Ch_1234.setStyleSheet(u"QComboBox {\n"
"    border: 3px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 1px 1px 10px;\n"
"    min-width: 6em;\n"
"    color: rgb(0, 0, 0); /* Colore del testo del QComboBox */\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
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
"    selection-background-color: #3399FF; /* Colore di sfondo dell'elemento selezionato */\n"
"    selection-color:rgb(106, 112, 113)"
                        "; /* Colore del testo dell'elemento selezionato */\n"
"    border: 3px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"    color: rgb(0, 0, 0); /* Colore del testo del QComboBox */\n"
"}")

        self.verticalLayout_10.addWidget(self.comboBox_Ch_1234)

        self.lineEdit_time_window = QLineEdit(self.frame_6)
        self.lineEdit_time_window.setObjectName(u"lineEdit_time_window")
        self.lineEdit_time_window.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(255, 255, 255); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 20;\n"
"	color: rgb(0,0,0);\n"
"}")
        self.lineEdit_time_window.setMaxLength(20)
        self.lineEdit_time_window.setAlignment(Qt.AlignCenter)
        self.lineEdit_time_window.setClearButtonEnabled(True)

        self.verticalLayout_10.addWidget(self.lineEdit_time_window)


        self.gridLayout_11.addWidget(self.frame_6, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_11.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout_11.addItem(self.verticalSpacer_3, 5, 0, 1, 1)

        self.frame_18 = QFrame(self.frame_2)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy2.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy2)
        self.frame_18.setStyleSheet(u"QWidget	{\n"
"border-width: 0px;\n"
"\n"
"}")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_18)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)
        self.label_7.setMinimumSize(QSize(0, 45))
        self.label_7.setMaximumSize(QSize(120, 45))
        self.label_7.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 15px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_7)

        self.label_led_stabilita = QLabel(self.frame_18)
        self.label_led_stabilita.setObjectName(u"label_led_stabilita")
        self.label_led_stabilita.setMinimumSize(QSize(30, 30))
        self.label_led_stabilita.setMaximumSize(QSize(30, 30))
        self.label_led_stabilita.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(255, 0, 4);\n"
"	border-style: outset;\n"
"    border-width: 3px;\n"
"	border-color: rgb(143, 33, 33);\n"
"	border-radius: 15px;\n"
"	color: rgb(0,0,0);\n"
"}")

        self.horizontalLayout_3.addWidget(self.label_led_stabilita)


        self.gridLayout_11.addWidget(self.frame_18, 6, 0, 1, 1)

        self.frame_22 = QFrame(self.frame_2)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_22)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.pushButton_save_measure = QPushButton(self.frame_22)
        self.pushButton_save_measure.setObjectName(u"pushButton_save_measure")
        self.pushButton_save_measure.setEnabled(False)
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.pushButton_save_measure.sizePolicy().hasHeightForWidth())
        self.pushButton_save_measure.setSizePolicy(sizePolicy6)
        self.pushButton_save_measure.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_save_measure.setStyleSheet(u"QPushButton{\n"
"	border-width: 1px;\n"
"	background-color:rgb(107, 107, 107);\n"
"	color: rgb(0, 0, 0);\n"
"	border-style: outset;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	border-width: 2px;\n"
"	background-color:rgb(56, 56, 56);\n"
"	color: rgb(0, 0, 0);	\n"
"	border-style: outset;\n"
"}\n"
"\n"
"QPushButton::disabled{\n"
"	border-width: 0px;\n"
"	background-color:rgb(193, 145, 33);\n"
"	color: rgb(0, 0, 0);\n"
"	border-style: outset;\n"
"}")

        self.verticalLayout_16.addWidget(self.pushButton_save_measure)


        self.gridLayout_11.addWidget(self.frame_22, 8, 0, 1, 1)

        self.frame_altezza = QFrame(self.frame_2)
        self.frame_altezza.setObjectName(u"frame_altezza")
        self.frame_altezza.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.frame_altezza.sizePolicy().hasHeightForWidth())
        self.frame_altezza.setSizePolicy(sizePolicy2)
        self.frame_altezza.setFrameShape(QFrame.StyledPanel)
        self.frame_altezza.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_altezza)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.frame_altezza)
        self.label_9.setObjectName(u"label_9")
        sizePolicy2.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy2)
        self.label_9.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_9)

        self.lineEdit_altezza = QLineEdit(self.frame_altezza)
        self.lineEdit_altezza.setObjectName(u"lineEdit_altezza")
        self.lineEdit_altezza.setEnabled(True)
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.lineEdit_altezza.sizePolicy().hasHeightForWidth())
        self.lineEdit_altezza.setSizePolicy(sizePolicy7)
        self.lineEdit_altezza.setMinimumSize(QSize(0, 40))
        self.lineEdit_altezza.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(255, 255, 255); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"\n"
"QWidget::disabled{\n"
"	background-color: rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0;\n"
"	color: rgb(255, 172, 88);\n"
"}")
        self.lineEdit_altezza.setAlignment(Qt.AlignCenter)
        self.lineEdit_altezza.setClearButtonEnabled(True)

        self.verticalLayout_14.addWidget(self.lineEdit_altezza)


        self.gridLayout_11.addWidget(self.frame_altezza, 4, 0, 1, 1)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 70))
        self.label_2.setMaximumSize(QSize(16777215, 70))
        self.label_2.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.label_2, 2, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout_11.addItem(self.verticalSpacer_4, 7, 0, 1, 1)


        self.horizontalLayout.addWidget(self.frame_2)


        self.gridLayout_2.addWidget(self.gridWidget, 1, 0, 1, 1)

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
        self.horizontalLayout_2 = QHBoxLayout(self.frame_navigation)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_home = QPushButton(self.frame_navigation)
        self.pushButton_home.setObjectName(u"pushButton_home")
        sizePolicy6.setHeightForWidth(self.pushButton_home.sizePolicy().hasHeightForWidth())
        self.pushButton_home.setSizePolicy(sizePolicy6)
        self.pushButton_home.setMaximumSize(QSize(200, 16777215))
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStrikeOut(False)
        self.pushButton_home.setFont(font3)
        self.pushButton_home.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_home.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_2.addWidget(self.pushButton_home)

        self.pushButton_Euramet = QPushButton(self.frame_navigation)
        self.pushButton_Euramet.setObjectName(u"pushButton_Euramet")
        sizePolicy6.setHeightForWidth(self.pushButton_Euramet.sizePolicy().hasHeightForWidth())
        self.pushButton_Euramet.setSizePolicy(sizePolicy6)
        self.pushButton_Euramet.setMaximumSize(QSize(200, 16777215))
        self.pushButton_Euramet.setFont(font3)
        self.pushButton_Euramet.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_Euramet.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_2.addWidget(self.pushButton_Euramet)

        self.pushButton_Stabilita = QPushButton(self.frame_navigation)
        self.pushButton_Stabilita.setObjectName(u"pushButton_Stabilita")
        sizePolicy6.setHeightForWidth(self.pushButton_Stabilita.sizePolicy().hasHeightForWidth())
        self.pushButton_Stabilita.setSizePolicy(sizePolicy6)
        self.pushButton_Stabilita.setMaximumSize(QSize(200, 16777215))
        self.pushButton_Stabilita.setFont(font3)
        self.pushButton_Stabilita.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_Stabilita.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_2.addWidget(self.pushButton_Stabilita)

        self.frame_4 = QFrame(self.frame_navigation)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_4)


        self.gridLayout_2.addWidget(self.frame_navigation, 0, 0, 1, 1)

        GraphWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(GraphWindow)

        QMetaObject.connectSlotsByName(GraphWindow)
    # setupUi

    def retranslateUi(self, GraphWindow):
        GraphWindow.setWindowTitle(QCoreApplication.translate("GraphWindow", u"MainWindow", None))
        self.label_main_mV.setText(QCoreApplication.translate("GraphWindow", u"main channel [mV]", None))
        self.label_main_Nm.setText(QCoreApplication.translate("GraphWindow", u"main channel [Nm]", None))
        self.label_4.setText(QCoreApplication.translate("GraphWindow", u"Channel 2 [N]", None))
        self.label_3.setText(QCoreApplication.translate("GraphWindow", u"Channel 4 [Nm]", None))
        self.label_13.setText(QCoreApplication.translate("GraphWindow", u"PROSSIMO STEP", None))
        self.label_step_prossimo_valore.setText(QCoreApplication.translate("GraphWindow", u"-", None))
        self.label_12.setText(QCoreApplication.translate("GraphWindow", u"STEP ATTUALE", None))
        self.label_step_attuale_valore.setText(QCoreApplication.translate("GraphWindow", u"-", None))
        self.pushButton_autorange_solo_main.setText("")
        self.pushButton_reset_solo_main.setText(QCoreApplication.translate("GraphWindow", u"RESET", None))
        self.pushButton_autorange_solo_temp.setText("")
        self.pushButton_reset_solo_temp.setText(QCoreApplication.translate("GraphWindow", u"RESET", None))
        self.pushButton_autorange_main_and_channel.setText("")
        self.pushButton_reset_main_and_channel.setText(QCoreApplication.translate("GraphWindow", u"RESET", None))
        self.pushButton_autorange_ch1.setText("")
        self.pushButton_reset_ch1.setText(QCoreApplication.translate("GraphWindow", u"RESET", None))
        self.pushButton_autorange_ch2.setText("")
        self.pushButton_reset_ch2.setText(QCoreApplication.translate("GraphWindow", u"RESET", None))
        self.pushButton_autorange_ch3.setText("")
        self.pushButton_reset_ch3.setText(QCoreApplication.translate("GraphWindow", u"RESET", None))
        self.pushButton_autorange_ch4.setText("")
        self.pushButton_reset_ch4.setText(QCoreApplication.translate("GraphWindow", u"RESET", None))
        self.label_quadrante.setText(QCoreApplication.translate("GraphWindow", u"Q(1/3)", None))
        self.label.setText(QCoreApplication.translate("GraphWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700; color:#0b0b0b;\">Grafico</span></p></body></html>", None))
        self.comboBox_Main_Temp.setItemText(0, QCoreApplication.translate("GraphWindow", u"Main", None))
        self.comboBox_Main_Temp.setItemText(1, QCoreApplication.translate("GraphWindow", u"Temp", None))
        self.comboBox_Main_Temp.setItemText(2, QCoreApplication.translate("GraphWindow", u"Main + Channel", None))

        self.comboBox_Ch_1234.setItemText(0, QCoreApplication.translate("GraphWindow", u"Channel 1", None))
        self.comboBox_Ch_1234.setItemText(1, QCoreApplication.translate("GraphWindow", u"Channel 2", None))
        self.comboBox_Ch_1234.setItemText(2, QCoreApplication.translate("GraphWindow", u"Channel 3", None))
        self.comboBox_Ch_1234.setItemText(3, QCoreApplication.translate("GraphWindow", u"Channel 4", None))

        self.lineEdit_time_window.setText(QCoreApplication.translate("GraphWindow", u"time-window", None))
        self.label_7.setText(QCoreApplication.translate("GraphWindow", u"stabilit\u00e0", None))
        self.label_led_stabilita.setText("")
        self.pushButton_save_measure.setText(QCoreApplication.translate("GraphWindow", u"ACQUISISCI MISURA", None))
        self.label_9.setText(QCoreApplication.translate("GraphWindow", u"Altezza [mm]", None))
        self.lineEdit_altezza.setText(QCoreApplication.translate("GraphWindow", u"0", None))
        self.label_2.setText(QCoreApplication.translate("GraphWindow", u"EURAMET", None))
        self.pushButton_home.setText(QCoreApplication.translate("GraphWindow", u"HOME", None))
        self.pushButton_Euramet.setText(QCoreApplication.translate("GraphWindow", u"EURAMET SETUP", None))
        self.pushButton_Stabilita.setText(QCoreApplication.translate("GraphWindow", u"STABILITA'", None))
    # retranslateUi

