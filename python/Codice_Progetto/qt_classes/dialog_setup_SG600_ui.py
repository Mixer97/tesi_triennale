# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_setup_SG600.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_SG600_Setup(object):
    def setupUi(self, SG600_Setup):
        if not SG600_Setup.objectName():
            SG600_Setup.setObjectName(u"SG600_Setup")
        SG600_Setup.setWindowModality(Qt.WindowModal)
        SG600_Setup.setEnabled(True)
        SG600_Setup.resize(1200, 400)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SG600_Setup.sizePolicy().hasHeightForWidth())
        SG600_Setup.setSizePolicy(sizePolicy)
        SG600_Setup.setMinimumSize(QSize(1200, 400))
        SG600_Setup.setMaximumSize(QSize(1200, 400))
        SG600_Setup.setBaseSize(QSize(600, 400))
        SG600_Setup.setAutoFillBackground(False)
        SG600_Setup.setStyleSheet(u"QWidget {\n"
"	background-color:rgb(0,0,0); \n"
"}\n"
"")
        SG600_Setup.setModal(True)
        self.horizontalLayout = QHBoxLayout(SG600_Setup)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.widget = QWidget(SG600_Setup)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 0))
        self.widget.setStyleSheet(u"QWidget {\n"
"	background-color:rgb(126, 126, 126); \n"
"	border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: rgb(88, 88, 88);\n"
"}")
        self.gridLayout_16 = QGridLayout(self.widget)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridWidget_3 = QWidget(self.widget)
        self.gridWidget_3.setObjectName(u"gridWidget_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.gridWidget_3.sizePolicy().hasHeightForWidth())
        self.gridWidget_3.setSizePolicy(sizePolicy1)
        self.gridWidget_3.setStyleSheet(u"QWidget {\n"
"    border: 2px solid black;\n"
"    border-radius: 10px;\n"
"	background-color: rgb(178, 193, 255);\n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"	border-color: rgb(128, 112, 211);\n"
"	border-radius: 20px;\n"
"}\n"
"")
        self.gridLayout = QGridLayout(self.gridWidget_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.gridWidget_3)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_coefficiente_setup_main = QLabel(self.frame)
        self.label_coefficiente_setup_main.setObjectName(u"label_coefficiente_setup_main")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_coefficiente_setup_main.sizePolicy().hasHeightForWidth())
        self.label_coefficiente_setup_main.setSizePolicy(sizePolicy2)
        self.label_coefficiente_setup_main.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(178, 193, 255);\n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"	border-color: rgb(128, 112, 211);\n"
"	border-radius: 20px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.label_coefficiente_setup_main, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_3, 1, 0, 1, 1)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.lineEdit_coefficiente_main = QLineEdit(self.frame)
        self.lineEdit_coefficiente_main.setObjectName(u"lineEdit_coefficiente_main")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lineEdit_coefficiente_main.sizePolicy().hasHeightForWidth())
        self.lineEdit_coefficiente_main.setSizePolicy(sizePolicy3)
        font = QFont()
        font.setPointSize(16)
        font.setItalic(True)
        self.lineEdit_coefficiente_main.setFont(font)
        self.lineEdit_coefficiente_main.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(255, 255, 255); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"	border-color: rgb(128, 112, 211);\n"
"	border-radius: 20;\n"
"	color: rgb(0,0,0);\n"
"}")
        self.lineEdit_coefficiente_main.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.lineEdit_coefficiente_main, 0, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_6, 1, 1, 1, 1)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.pushButton_azzeramento_main = QPushButton(self.frame)
        self.pushButton_azzeramento_main.setObjectName(u"pushButton_azzeramento_main")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton_azzeramento_main.sizePolicy().hasHeightForWidth())
        self.pushButton_azzeramento_main.setSizePolicy(sizePolicy4)
        self.pushButton_azzeramento_main.setMinimumSize(QSize(0, 70))
        font1 = QFont()
        font1.setPointSize(15)
        self.pushButton_azzeramento_main.setFont(font1)
        self.pushButton_azzeramento_main.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_azzeramento_main.setStyleSheet(u"QWidget{\n"
"	background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(115, 188, 226, 255), stop:0.948357 rgba(112, 99, 193, 223));\n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"	border-color: rgb(128, 112, 211);\n"
"	border-radius: 20px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"QPushButton::pressed{\n"
"	border-width: 2px;\n"
"	background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(112, 99, 193, 223), stop:0.948357 rgba(115, 188, 226, 255) );\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(110, 100, 200)\n"
"}")
        self.pushButton_azzeramento_main.setFlat(False)

        self.gridLayout_9.addWidget(self.pushButton_azzeramento_main, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_9, 2, 0, 1, 2)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 70))
        self.label.setStyleSheet(u"QWidget {\n"
"    border: 2px ;\n"
"    border-radius: 10px;\n"
"	background-color: rgb(160, 180, 255);\n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"	border-color: rgb(128, 112, 211);\n"
"	border-radius: 20px;\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_3 = QFrame(self.gridWidget_3)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(200, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_correzione_lineare = QLabel(self.frame_3)
        self.label_correzione_lineare.setObjectName(u"label_correzione_lineare")
        self.label_correzione_lineare.setStyleSheet(u"QWidget {\n"
"    border: 2px ;\n"
"    border-radius: 10px;\n"
"	background-color: rgb(160, 180, 255);\n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"	border-color: rgb(128, 112, 211);\n"
"	border-radius: 20px;\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.label_correzione_lineare.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_correzione_lineare)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"	border-radius: 0px;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(30, 0))
        self.label_3.setStyleSheet(u"QWidget {\n"
"    border: 2px ;\n"
"    border-radius: 10px;\n"
"	background-color: rgb(160, 180, 255);\n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"	border-color: rgb(128, 112, 211);\n"
"	border-radius: 20px;\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.lineEdit_m_main = QLineEdit(self.frame_4)
        self.lineEdit_m_main.setObjectName(u"lineEdit_m_main")
        sizePolicy1.setHeightForWidth(self.lineEdit_m_main.sizePolicy().hasHeightForWidth())
        self.lineEdit_m_main.setSizePolicy(sizePolicy1)
        self.lineEdit_m_main.setStyleSheet(u"QWidget {\n"
"    border: 2px ;\n"
"    border-radius: 10px;\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"	border-color: rgb(128, 112, 211);\n"
"	border-radius: 0px;\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.lineEdit_m_main.setAlignment(Qt.AlignCenter)
        self.lineEdit_m_main.setClearButtonEnabled(True)

        self.horizontalLayout_2.addWidget(self.lineEdit_m_main)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"	border-radius: 0px;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(30, 0))
        self.label_4.setStyleSheet(u"QWidget {\n"
"    border: 2px ;\n"
"    border-radius: 10px;\n"
"	background-color: rgb(160, 180, 255);\n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"	border-color: rgb(128, 112, 211);\n"
"	border-radius: 20px;\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.lineEdit_q_main = QLineEdit(self.frame_5)
        self.lineEdit_q_main.setObjectName(u"lineEdit_q_main")
        sizePolicy1.setHeightForWidth(self.lineEdit_q_main.sizePolicy().hasHeightForWidth())
        self.lineEdit_q_main.setSizePolicy(sizePolicy1)
        self.lineEdit_q_main.setStyleSheet(u"QWidget {\n"
"    border: 2px ;\n"
"    border-radius: 10px;\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"	border-color: rgb(128, 112, 211);\n"
"	border-radius: 0px;\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.lineEdit_q_main.setAlignment(Qt.AlignCenter)
        self.lineEdit_q_main.setClearButtonEnabled(True)

        self.horizontalLayout_3.addWidget(self.lineEdit_q_main)


        self.verticalLayout.addWidget(self.frame_5)


        self.gridLayout.addWidget(self.frame_3, 0, 1, 1, 1)


        self.gridLayout_15.addWidget(self.gridWidget_3, 1, 0, 1, 1)

        self.gridWidget_4 = QWidget(self.widget)
        self.gridWidget_4.setObjectName(u"gridWidget_4")
        sizePolicy1.setHeightForWidth(self.gridWidget_4.sizePolicy().hasHeightForWidth())
        self.gridWidget_4.setSizePolicy(sizePolicy1)
        self.gridWidget_4.setStyleSheet(u"QWidget {\n"
"    border: 2px solid black;\n"
"    border-radius: 10px;\n"
"	background-color: rgb(178, 193, 255);\n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"	border-color: rgb(128, 112, 211);\n"
"	border-radius: 0px;\n"
"}\n"
"")
        self.gridLayout_5 = QGridLayout(self.gridWidget_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.frame_2 = QFrame(self.gridWidget_4)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.label_coefficiente_setup_temp = QLabel(self.frame_2)
        self.label_coefficiente_setup_temp.setObjectName(u"label_coefficiente_setup_temp")
        sizePolicy2.setHeightForWidth(self.label_coefficiente_setup_temp.sizePolicy().hasHeightForWidth())
        self.label_coefficiente_setup_temp.setSizePolicy(sizePolicy2)
        self.label_coefficiente_setup_temp.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(178, 193, 255);\n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"	border-color: rgb(128, 112, 211);\n"
"	border-radius: 20px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")

        self.gridLayout_14.addWidget(self.label_coefficiente_setup_temp, 0, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_14, 1, 0, 1, 1)

        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.lineEdit_coefficiente_temp = QLineEdit(self.frame_2)
        self.lineEdit_coefficiente_temp.setObjectName(u"lineEdit_coefficiente_temp")
        sizePolicy3.setHeightForWidth(self.lineEdit_coefficiente_temp.sizePolicy().hasHeightForWidth())
        self.lineEdit_coefficiente_temp.setSizePolicy(sizePolicy3)
        self.lineEdit_coefficiente_temp.setFont(font)
        self.lineEdit_coefficiente_temp.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(255, 255, 255); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"	border-color: rgb(128, 112, 211);\n"
"	border-radius: 20;\n"
"	color: rgb(0,0,0);\n"
"}")
        self.lineEdit_coefficiente_temp.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.lineEdit_coefficiente_temp, 0, 1, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_13, 1, 1, 1, 1)

        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.pushButton_azzeramento_main_2 = QPushButton(self.frame_2)
        self.pushButton_azzeramento_main_2.setObjectName(u"pushButton_azzeramento_main_2")
        sizePolicy4.setHeightForWidth(self.pushButton_azzeramento_main_2.sizePolicy().hasHeightForWidth())
        self.pushButton_azzeramento_main_2.setSizePolicy(sizePolicy4)
        self.pushButton_azzeramento_main_2.setMinimumSize(QSize(0, 70))
        self.pushButton_azzeramento_main_2.setFont(font1)
        self.pushButton_azzeramento_main_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_azzeramento_main_2.setStyleSheet(u"QWidget{\n"
"	background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(115, 188, 226, 255), stop:0.948357 rgba(112, 99, 193, 223));\n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"	border-color: rgb(128, 112, 211);\n"
"	border-radius: 20px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"QPushButton::pressed{\n"
"	border-width: 2px;\n"
"	background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(112, 99, 193, 223), stop:0.948357 rgba(115, 188, 226, 255) );\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(110, 100, 200)\n"
"}")

        self.gridLayout_12.addWidget(self.pushButton_azzeramento_main_2, 0, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_12, 2, 0, 1, 2)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 70))
        self.label_2.setStyleSheet(u"QWidget {\n"
"    border: 2px ;\n"
"    border-radius: 10px;\n"
"	background-color: rgb(160, 180, 255);\n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"	border-color: rgb(128, 112, 211);\n"
"	border-radius: 20px;\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"")

        self.gridLayout_7.addWidget(self.label_2, 0, 0, 1, 2)


        self.gridLayout_5.addWidget(self.frame_2, 0, 0, 1, 1)

        self.frame_6 = QFrame(self.gridWidget_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(200, 16777215))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_correzione_lineare_2 = QLabel(self.frame_6)
        self.label_correzione_lineare_2.setObjectName(u"label_correzione_lineare_2")
        self.label_correzione_lineare_2.setStyleSheet(u"QWidget {\n"
"    border: 2px ;\n"
"    border-radius: 10px;\n"
"	background-color: rgb(160, 180, 255);\n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"	border-color: rgb(128, 112, 211);\n"
"	border-radius: 20px;\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.label_correzione_lineare_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_correzione_lineare_2)

        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"	border-radius: 0px;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_7)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(30, 0))
        self.label_5.setStyleSheet(u"QWidget {\n"
"    border: 2px ;\n"
"    border-radius: 10px;\n"
"	background-color: rgb(160, 180, 255);\n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"	border-color: rgb(128, 112, 211);\n"
"	border-radius: 20px;\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_5)

        self.lineEdit_m_temp = QLineEdit(self.frame_7)
        self.lineEdit_m_temp.setObjectName(u"lineEdit_m_temp")
        sizePolicy1.setHeightForWidth(self.lineEdit_m_temp.sizePolicy().hasHeightForWidth())
        self.lineEdit_m_temp.setSizePolicy(sizePolicy1)
        self.lineEdit_m_temp.setStyleSheet(u"QWidget {\n"
"    border: 2px ;\n"
"    border-radius: 10px;\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"	border-color: rgb(128, 112, 211);\n"
"	border-radius: 0px;\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.lineEdit_m_temp.setAlignment(Qt.AlignCenter)
        self.lineEdit_m_temp.setClearButtonEnabled(True)

        self.horizontalLayout_4.addWidget(self.lineEdit_m_temp)


        self.verticalLayout_2.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"	border-radius: 0px;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_8)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(30, 0))
        self.label_6.setStyleSheet(u"QWidget {\n"
"    border: 2px ;\n"
"    border-radius: 10px;\n"
"	background-color: rgb(160, 180, 255);\n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"	border-color: rgb(128, 112, 211);\n"
"	border-radius: 20px;\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_6)

        self.lineEdit_q_temp = QLineEdit(self.frame_8)
        self.lineEdit_q_temp.setObjectName(u"lineEdit_q_temp")
        sizePolicy1.setHeightForWidth(self.lineEdit_q_temp.sizePolicy().hasHeightForWidth())
        self.lineEdit_q_temp.setSizePolicy(sizePolicy1)
        self.lineEdit_q_temp.setStyleSheet(u"QWidget {\n"
"    border: 2px ;\n"
"    border-radius: 10px;\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"	border-color: rgb(128, 112, 211);\n"
"	border-radius: 0px;\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.lineEdit_q_temp.setAlignment(Qt.AlignCenter)
        self.lineEdit_q_temp.setClearButtonEnabled(True)

        self.horizontalLayout_5.addWidget(self.lineEdit_q_temp)


        self.verticalLayout_2.addWidget(self.frame_8)


        self.gridLayout_5.addWidget(self.frame_6, 0, 1, 1, 1)


        self.gridLayout_15.addWidget(self.gridWidget_4, 1, 1, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.label_setup_TITLE = QLabel(self.widget)
        self.label_setup_TITLE.setObjectName(u"label_setup_TITLE")
        sizePolicy1.setHeightForWidth(self.label_setup_TITLE.sizePolicy().hasHeightForWidth())
        self.label_setup_TITLE.setSizePolicy(sizePolicy1)
        self.label_setup_TITLE.setMinimumSize(QSize(0, 70))
        self.label_setup_TITLE.setStyleSheet(u"QLabel {\n"
"    border: 2px solid black;\n"
"    border-radius: 10px;\n"
"	background-color: rgb(178, 193, 255);\n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"	border-color: rgb(128, 112, 211);\n"
"	border-radius: 20px;\n"
"}\n"
"QLabel{\n"
"	color: rgb(0,0,0);\n"
"}")

        self.gridLayout_4.addWidget(self.label_setup_TITLE, 1, 0, 1, 1)


        self.gridLayout_15.addLayout(self.gridLayout_4, 0, 0, 1, 1)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_setup_CHTEMP = QLabel(self.widget)
        self.label_setup_CHTEMP.setObjectName(u"label_setup_CHTEMP")
        sizePolicy1.setHeightForWidth(self.label_setup_CHTEMP.sizePolicy().hasHeightForWidth())
        self.label_setup_CHTEMP.setSizePolicy(sizePolicy1)
        self.label_setup_CHTEMP.setStyleSheet(u"QLabel {\n"
"    border: 2px solid black;\n"
"    border-radius: 10px;\n"
"	background-color: rgb(178, 193, 255);\n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"	border-color: rgb(128, 112, 211);\n"
"	border-radius: 20px;\n"
"}\n"
"QLabel{\n"
"	color: rgb(0,0,0);\n"
"}")

        self.gridLayout_8.addWidget(self.label_setup_CHTEMP, 0, 0, 1, 1)


        self.gridLayout_15.addLayout(self.gridLayout_8, 0, 1, 1, 1)


        self.gridLayout_16.addLayout(self.gridLayout_15, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.widget)


        self.retranslateUi(SG600_Setup)

        QMetaObject.connectSlotsByName(SG600_Setup)
    # setupUi

    def retranslateUi(self, SG600_Setup):
        SG600_Setup.setWindowTitle(QCoreApplication.translate("SG600_Setup", u"Dialog", None))
        self.label_coefficiente_setup_main.setText(QCoreApplication.translate("SG600_Setup", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">COEFFICIENTE</span></p></body></html>", None))
        self.lineEdit_coefficiente_main.setText(QCoreApplication.translate("SG600_Setup", u"-", None))
        self.pushButton_azzeramento_main.setText(QCoreApplication.translate("SG600_Setup", u"ZERO CANALE MAIN", None))
        self.label.setText(QCoreApplication.translate("SG600_Setup", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">coefficienti per calcolo Nm</span></p></body></html>", None))
        self.label_correzione_lineare.setText(QCoreApplication.translate("SG600_Setup", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">correzione lineare</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("SG600_Setup", u"m", None))
        self.lineEdit_m_main.setText(QCoreApplication.translate("SG600_Setup", u"-", None))
        self.label_4.setText(QCoreApplication.translate("SG600_Setup", u"q", None))
        self.lineEdit_q_main.setText(QCoreApplication.translate("SG600_Setup", u"-", None))
        self.label_coefficiente_setup_temp.setText(QCoreApplication.translate("SG600_Setup", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">COEFFICIENTE</span></p></body></html>", None))
        self.lineEdit_coefficiente_temp.setText(QCoreApplication.translate("SG600_Setup", u"-", None))
        self.pushButton_azzeramento_main_2.setText(QCoreApplication.translate("SG600_Setup", u"ZERO CANALE TEMP.", None))
        self.label_2.setText(QCoreApplication.translate("SG600_Setup", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">coefficienti per calcolo \u00b0C</span></p></body></html>", None))
        self.label_correzione_lineare_2.setText(QCoreApplication.translate("SG600_Setup", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">correzione lineare</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("SG600_Setup", u"m", None))
        self.lineEdit_m_temp.setText(QCoreApplication.translate("SG600_Setup", u"-", None))
        self.label_6.setText(QCoreApplication.translate("SG600_Setup", u"q", None))
        self.lineEdit_q_temp.setText(QCoreApplication.translate("SG600_Setup", u"-", None))
        self.label_setup_TITLE.setText(QCoreApplication.translate("SG600_Setup", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:700; color:#00aa00;\">CANALE PRINCIPALE</span></p></body></html>", None))
        self.label_setup_CHTEMP.setText(QCoreApplication.translate("SG600_Setup", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:700; color:#00aa00;\"> CANALE TEMPERATURA</span></p></body></html>", None))
    # retranslateUi

