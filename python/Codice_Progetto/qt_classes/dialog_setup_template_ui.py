# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_setup_template.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Canale_Setup(object):
    def setupUi(self, Canale_Setup):
        if not Canale_Setup.objectName():
            Canale_Setup.setObjectName(u"Canale_Setup")
        Canale_Setup.setWindowModality(Qt.WindowModal)
        Canale_Setup.setEnabled(True)
        Canale_Setup.resize(600, 400)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Canale_Setup.sizePolicy().hasHeightForWidth())
        Canale_Setup.setSizePolicy(sizePolicy)
        Canale_Setup.setMinimumSize(QSize(600, 400))
        Canale_Setup.setMaximumSize(QSize(600, 400))
        Canale_Setup.setBaseSize(QSize(600, 400))
        Canale_Setup.setAutoFillBackground(False)
        Canale_Setup.setStyleSheet(u"QWidget {\n"
"	background-color:rgb(0,0,0); \n"
"}\n"
"")
        Canale_Setup.setModal(True)
        self.horizontalLayout = QHBoxLayout(Canale_Setup)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.widget = QWidget(Canale_Setup)
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
        self.label_setup_title = QLabel(self.widget)
        self.label_setup_title.setObjectName(u"label_setup_title")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_setup_title.sizePolicy().hasHeightForWidth())
        self.label_setup_title.setSizePolicy(sizePolicy1)
        self.label_setup_title.setMinimumSize(QSize(0, 70))
        self.label_setup_title.setStyleSheet(u"QLabel {\n"
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

        self.gridLayout_4.addWidget(self.label_setup_title, 0, 0, 1, 1)


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
        self.lineEdit_sensibilita = QLineEdit(self.gridWidget_3)
        self.lineEdit_sensibilita.setObjectName(u"lineEdit_sensibilita")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit_sensibilita.sizePolicy().hasHeightForWidth())
        self.lineEdit_sensibilita.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setPointSize(16)
        font.setItalic(True)
        self.lineEdit_sensibilita.setFont(font)
        self.lineEdit_sensibilita.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(255, 255, 255); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 20;\n"
"	color: rgb(0,0,0);\n"
"}")
        self.lineEdit_sensibilita.setCursorPosition(1)
        self.lineEdit_sensibilita.setAlignment(Qt.AlignCenter)
        self.lineEdit_sensibilita.setClearButtonEnabled(False)

        self.gridLayout_5.addWidget(self.lineEdit_sensibilita, 0, 0, 1, 1)

        self.comboBox_sens = QComboBox(self.gridWidget_3)
        self.comboBox_sens.addItem("")
        self.comboBox_sens.setObjectName(u"comboBox_sens")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.comboBox_sens.sizePolicy().hasHeightForWidth())
        self.comboBox_sens.setSizePolicy(sizePolicy3)
        self.comboBox_sens.setMinimumSize(QSize(100, 0))
        self.comboBox_sens.setMaximumSize(QSize(100, 16777215))
        font1 = QFont()
        font1.setPointSize(15)
        self.comboBox_sens.setFont(font1)
        self.comboBox_sens.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.comboBox_sens.setStyleSheet(u"QComboBox {\n"
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

        self.gridLayout_5.addWidget(self.comboBox_sens, 0, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_5, 0, 1, 1, 2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_sensib_setup = QLabel(self.gridWidget_3)
        self.label_sensib_setup.setObjectName(u"label_sensib_setup")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_sensib_setup.sizePolicy().hasHeightForWidth())
        self.label_sensib_setup.setSizePolicy(sizePolicy4)
        self.label_sensib_setup.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 20px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.label_sensib_setup, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.pushButton_azzeramento_tara = QPushButton(self.gridWidget_3)
        self.pushButton_azzeramento_tara.setObjectName(u"pushButton_azzeramento_tara")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.pushButton_azzeramento_tara.sizePolicy().hasHeightForWidth())
        self.pushButton_azzeramento_tara.setSizePolicy(sizePolicy5)
        self.pushButton_azzeramento_tara.setMinimumSize(QSize(0, 70))
        self.pushButton_azzeramento_tara.setFont(font1)
        self.pushButton_azzeramento_tara.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_azzeramento_tara.setStyleSheet(u"QWidget{\n"
"	background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0.965909, stop:0 rgba(255, 220, 129, 236), stop:1 rgba(255, 110, 110, 242)); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 20px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"QPushButton::pressed{\n"
"	border-width: 2px;\n"
"	background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0.965909, stop:0 rgba(255, 110, 110, 242), stop:1 rgba(255, 220, 129, 236)); \n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.gridLayout_9.addWidget(self.pushButton_azzeramento_tara, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_9, 3, 0, 1, 3)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.lineEdit_fondoscala = QLineEdit(self.gridWidget_3)
        self.lineEdit_fondoscala.setObjectName(u"lineEdit_fondoscala")
        sizePolicy2.setHeightForWidth(self.lineEdit_fondoscala.sizePolicy().hasHeightForWidth())
        self.lineEdit_fondoscala.setSizePolicy(sizePolicy2)
        self.lineEdit_fondoscala.setFont(font)
        self.lineEdit_fondoscala.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(255, 255, 255); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 20;\n"
"	color: rgb(0,0,0);\n"
"}")
        self.lineEdit_fondoscala.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.lineEdit_fondoscala, 0, 1, 1, 1)

        self.comboBox_fullscale = QComboBox(self.gridWidget_3)
        self.comboBox_fullscale.addItem("")
        self.comboBox_fullscale.addItem("")
        self.comboBox_fullscale.addItem("")
        self.comboBox_fullscale.setObjectName(u"comboBox_fullscale")
        sizePolicy3.setHeightForWidth(self.comboBox_fullscale.sizePolicy().hasHeightForWidth())
        self.comboBox_fullscale.setSizePolicy(sizePolicy3)
        self.comboBox_fullscale.setMinimumSize(QSize(100, 0))
        self.comboBox_fullscale.setMaximumSize(QSize(100, 16777215))
        self.comboBox_fullscale.setFont(font1)
        self.comboBox_fullscale.setStyleSheet(u"QComboBox {\n"
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

        self.gridLayout_6.addWidget(self.comboBox_fullscale, 0, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_6, 2, 1, 1, 2)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_fondoscala_setup = QLabel(self.gridWidget_3)
        self.label_fondoscala_setup.setObjectName(u"label_fondoscala_setup")
        sizePolicy4.setHeightForWidth(self.label_fondoscala_setup.sizePolicy().hasHeightForWidth())
        self.label_fondoscala_setup.setSizePolicy(sizePolicy4)
        self.label_fondoscala_setup.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 20px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.label_fondoscala_setup, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_3, 2, 0, 1, 1)


        self.gridLayout_7.addWidget(self.gridWidget_3, 1, 0, 1, 1)


        self.horizontalLayout.addWidget(self.widget)


        self.retranslateUi(Canale_Setup)

        self.comboBox_fullscale.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Canale_Setup)
    # setupUi

    def retranslateUi(self, Canale_Setup):
        Canale_Setup.setWindowTitle(QCoreApplication.translate("Canale_Setup", u"Dialog", None))
        self.label_setup_title.setText(QCoreApplication.translate("Canale_Setup", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:700; color:#00aa00;\">CANALE 1</span></p></body></html>", None))
        self.lineEdit_sensibilita.setText(QCoreApplication.translate("Canale_Setup", u"-", None))
        self.comboBox_sens.setItemText(0, QCoreApplication.translate("Canale_Setup", u"mV/V", None))

        self.label_sensib_setup.setText(QCoreApplication.translate("Canale_Setup", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">SENSIBILITA'</span></p></body></html>", None))
        self.pushButton_azzeramento_tara.setText(QCoreApplication.translate("Canale_Setup", u"AZZERAMENTO TARA", None))
        self.lineEdit_fondoscala.setText(QCoreApplication.translate("Canale_Setup", u"-", None))
        self.comboBox_fullscale.setItemText(0, QCoreApplication.translate("Canale_Setup", u"Kg", None))
        self.comboBox_fullscale.setItemText(1, QCoreApplication.translate("Canale_Setup", u"N", None))
        self.comboBox_fullscale.setItemText(2, QCoreApplication.translate("Canale_Setup", u"Nm", None))

        self.label_fondoscala_setup.setText(QCoreApplication.translate("Canale_Setup", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">FONDOSCALA</span></p></body></html>", None))
    # retranslateUi

