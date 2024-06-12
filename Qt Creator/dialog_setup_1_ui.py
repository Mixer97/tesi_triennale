# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_setup_1.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Canale_1_Setup(object):
    def setupUi(self, Canale_1_Setup):
        if not Canale_1_Setup.objectName():
            Canale_1_Setup.setObjectName(u"Canale_1_Setup")
        Canale_1_Setup.setWindowModality(Qt.WindowModal)
        Canale_1_Setup.setEnabled(True)
        Canale_1_Setup.resize(600, 400)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Canale_1_Setup.sizePolicy().hasHeightForWidth())
        Canale_1_Setup.setSizePolicy(sizePolicy)
        Canale_1_Setup.setMinimumSize(QSize(600, 400))
        Canale_1_Setup.setMaximumSize(QSize(600, 400))
        Canale_1_Setup.setBaseSize(QSize(600, 400))
        Canale_1_Setup.setAutoFillBackground(False)
        Canale_1_Setup.setStyleSheet(u"QWidget {\n"
"	background-color:rgb(0,0,0); \n"
"}\n"
"")
        self.horizontalLayout = QHBoxLayout(Canale_1_Setup)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.widget = QWidget(Canale_1_Setup)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 0))
        self.widget.setStyleSheet(u"QWidget {\n"
"	background-color:rgb(126, 126, 126); \n"
"	border-style: outset;\n"
"    border-width: 4px;\n"
"    border-color: rgb(88, 88, 88);\n"
"}")
        self.gridLayout_7 = QGridLayout(self.widget)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.label_ch1_setup = QLabel(self.widget)
        self.label_ch1_setup.setObjectName(u"label_ch1_setup")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_ch1_setup.sizePolicy().hasHeightForWidth())
        self.label_ch1_setup.setSizePolicy(sizePolicy1)
        self.label_ch1_setup.setMinimumSize(QSize(0, 70))
        self.label_ch1_setup.setStyleSheet(u"QLabel {\n"
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

        self.gridLayout_4.addWidget(self.label_ch1_setup, 0, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_4, 0, 0, 1, 1)

        self.gridWidget_3 = QWidget(self.widget)
        self.gridWidget_3.setObjectName(u"gridWidget_3")
        self.gridWidget_3.setStyleSheet(u"QWidget {\n"
"    border: 2px solid black;\n"
"    border-radius: 10px;\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 20px;\n"
"}\n"
"")
        self.gridLayout_2 = QGridLayout(self.gridWidget_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.lineEdit = QLineEdit(self.gridWidget_3)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setPointSize(16)
        font.setItalic(True)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(255, 255, 255); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 20;\n"
"	color: rgb(0,0,0);\n"
"}")
        self.lineEdit.setCursorPosition(27)
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.lineEdit.setClearButtonEnabled(False)

        self.gridLayout_5.addWidget(self.lineEdit, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_5, 0, 1, 1, 2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_sensib_setup_ch1 = QLabel(self.gridWidget_3)
        self.label_sensib_setup_ch1.setObjectName(u"label_sensib_setup_ch1")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_sensib_setup_ch1.sizePolicy().hasHeightForWidth())
        self.label_sensib_setup_ch1.setSizePolicy(sizePolicy3)
        self.label_sensib_setup_ch1.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 20px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.label_sensib_setup_ch1, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.pushButton = QPushButton(self.gridWidget_3)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy4)
        self.pushButton.setMinimumSize(QSize(0, 70))
        font1 = QFont()
        font1.setPointSize(15)
        self.pushButton.setFont(font1)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QWidget{\n"
"	background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0.965909, stop:0 rgba(255, 220, 129, 236), stop:1 rgba(255, 110, 110, 242)); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 20px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")

        self.gridLayout_9.addWidget(self.pushButton, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_9, 3, 0, 1, 3)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.lineEdit_2 = QLineEdit(self.gridWidget_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy2.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy2)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(255, 255, 255); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 20;\n"
"	color: rgb(0,0,0);\n"
"}")
        self.lineEdit_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.lineEdit_2, 0, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_6, 2, 1, 1, 2)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_fondoscala_setup_ch1 = QLabel(self.gridWidget_3)
        self.label_fondoscala_setup_ch1.setObjectName(u"label_fondoscala_setup_ch1")
        sizePolicy3.setHeightForWidth(self.label_fondoscala_setup_ch1.sizePolicy().hasHeightForWidth())
        self.label_fondoscala_setup_ch1.setSizePolicy(sizePolicy3)
        self.label_fondoscala_setup_ch1.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 20px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.label_fondoscala_setup_ch1, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_3, 2, 0, 1, 1)


        self.gridLayout_7.addWidget(self.gridWidget_3, 1, 0, 1, 1)


        self.horizontalLayout.addWidget(self.widget)


        self.retranslateUi(Canale_1_Setup)

        QMetaObject.connectSlotsByName(Canale_1_Setup)
    # setupUi

    def retranslateUi(self, Canale_1_Setup):
        Canale_1_Setup.setWindowTitle(QCoreApplication.translate("Canale_1_Setup", u"Dialog", None))
        self.label_ch1_setup.setText(QCoreApplication.translate("Canale_1_Setup", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:700; color:#00aa00;\">CANALE 1</span></p></body></html>", None))
        self.lineEdit.setText(QCoreApplication.translate("Canale_1_Setup", u"inserire qui la sensibilit\u00e0", None))
        self.label_sensib_setup_ch1.setText(QCoreApplication.translate("Canale_1_Setup", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">SENSIBILITA'</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("Canale_1_Setup", u"AZZERAMENTO TARA", None))
        self.lineEdit_2.setText(QCoreApplication.translate("Canale_1_Setup", u"inserire qui il fondoscala", None))
        self.label_fondoscala_setup_ch1.setText(QCoreApplication.translate("Canale_1_Setup", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">FONDOSCALA</span></p></body></html>", None))
    # retranslateUi

