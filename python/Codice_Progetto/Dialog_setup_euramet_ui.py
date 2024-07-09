# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dialog_setup_euramet.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_Dialog_Euramet_setup(object):
    def setupUi(self, Dialog_Euramet_setup):
        if not Dialog_Euramet_setup.objectName():
            Dialog_Euramet_setup.setObjectName(u"Dialog_Euramet_setup")
        Dialog_Euramet_setup.resize(1003, 612)
        Dialog_Euramet_setup.setStyleSheet(u"background-color: rgb(48, 199, 40);")
        self.gridLayout = QGridLayout(Dialog_Euramet_setup)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(Dialog_Euramet_setup)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(238, 255, 239);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 10, 137, 61))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.comboBox_step = QComboBox(self.frame)
        self.comboBox_step.addItem("")
        self.comboBox_step.addItem("")
        self.comboBox_step.addItem("")
        self.comboBox_step.addItem("")
        self.comboBox_step.addItem("")
        self.comboBox_step.setObjectName(u"comboBox_step")
        self.comboBox_step.setGeometry(QRect(830, 10, 137, 61))
        self.comboBox_step.setStyleSheet(u"QComboBox {\n"
"    border: 3px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 1px 1px 10px;\n"
"    min-width: 6em;\n"
"    color: rgb(0, 0, 0); /* Colore del testo del QComboBox */\n"
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
"    selection-color:rgb(106, 112, 113); /* Colore del testo dell'elemento selezionato */\n"
"    bord"
                        "er: 3px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"    color: rgb(0, 0, 0); /* Colore del testo del QComboBox */\n"
"}")
        self.checkBox_discesa_1 = QCheckBox(self.frame)
        self.checkBox_discesa_1.setObjectName(u"checkBox_discesa_1")
        self.checkBox_discesa_1.setGeometry(QRect(320, 10, 161, 61))
        self.checkBox_discesa_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.checkBox_discesa_1.setStyleSheet(u"QCheckBox {\n"
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
"	Background-color: red;\n"
"	border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    border-style: outset;\n"
"}\n"
"\n"
"\n"
"")
        self.checkBox_salita_1 = QCheckBox(self.frame)
        self.checkBox_salita_1.setObjectName(u"checkBox_salita_1")
        self.checkBox_salita_1.setGeometry(QRect(160, 10, 151, 61))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_salita_1.sizePolicy().hasHeightForWidth())
        self.checkBox_salita_1.setSizePolicy(sizePolicy)
        self.checkBox_salita_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.checkBox_salita_1.setStyleSheet(u"QCheckBox {\n"
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
"	Background-color: red;\n"
"	border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    border-style: outset;\n"
"}\n"
"\n"
"\n"
"")
        self.checkBox_salita_2 = QCheckBox(self.frame)
        self.checkBox_salita_2.setObjectName(u"checkBox_salita_2")
        self.checkBox_salita_2.setGeometry(QRect(490, 10, 151, 61))
        self.checkBox_salita_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.checkBox_salita_2.setStyleSheet(u"QCheckBox {\n"
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
"	Background-color: red;\n"
"	border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    border-style: outset;\n"
"}\n"
"\n"
"\n"
"")
        self.checkBox_altezza = QCheckBox(self.frame)
        self.checkBox_altezza.setObjectName(u"checkBox_altezza")
        self.checkBox_altezza.setGeometry(QRect(650, 10, 151, 61))
        sizePolicy.setHeightForWidth(self.checkBox_altezza.sizePolicy().hasHeightForWidth())
        self.checkBox_altezza.setSizePolicy(sizePolicy)
        self.checkBox_altezza.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.checkBox_altezza.setStyleSheet(u"QCheckBox {\n"
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
"	Background-color: red;\n"
"	border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    border-style: outset;\n"
"}\n"
"\n"
"\n"
"")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(800, 90, 161, 162))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_correzione_lineare = QLabel(self.frame_3)
        self.label_correzione_lineare.setObjectName(u"label_correzione_lineare")
        self.label_correzione_lineare.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 20px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_correzione_lineare.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_correzione_lineare)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(30, 0))
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

        self.horizontalLayout_2.addWidget(self.label_3)

        self.lineEdit_m = QLineEdit(self.frame_4)
        self.lineEdit_m.setObjectName(u"lineEdit_m")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_m.sizePolicy().hasHeightForWidth())
        self.lineEdit_m.setSizePolicy(sizePolicy1)
        self.lineEdit_m.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(255, 255, 255); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}")
        self.lineEdit_m.setAlignment(Qt.AlignCenter)
        self.lineEdit_m.setClearButtonEnabled(True)

        self.horizontalLayout_2.addWidget(self.lineEdit_m)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_5)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(30, 0))
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

        self.horizontalLayout.addWidget(self.label_4)

        self.lineEdit_q = QLineEdit(self.frame_5)
        self.lineEdit_q.setObjectName(u"lineEdit_q")
        sizePolicy1.setHeightForWidth(self.lineEdit_q.sizePolicy().hasHeightForWidth())
        self.lineEdit_q.setSizePolicy(sizePolicy1)
        self.lineEdit_q.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(255, 255, 255); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}")
        self.lineEdit_q.setAlignment(Qt.AlignCenter)
        self.lineEdit_q.setClearButtonEnabled(True)

        self.horizontalLayout.addWidget(self.lineEdit_q)


        self.verticalLayout.addWidget(self.frame_5)

        self.stackedWidget_euramet = QStackedWidget(self.frame)
        self.stackedWidget_euramet.setObjectName(u"stackedWidget_euramet")
        self.stackedWidget_euramet.setGeometry(QRect(19, 109, 751, 451))
        self.stackedWidget_euramet.setStyleSheet(u"border-color: rgb(0, 85, 0);\n"
"border-width: 3px;")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget_euramet.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget_euramet.addWidget(self.page_2)
        self.pushButton_impostazion_csv = QPushButton(self.frame)
        self.pushButton_impostazion_csv.setObjectName(u"pushButton_impostazion_csv")
        self.pushButton_impostazion_csv.setGeometry(QRect(810, 280, 141, 121))
        self.pushButton_impostazion_csv.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_impostazion_csv.setStyleSheet(u"QPushButton{\n"
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
        self.pushButton_concludi_setup = QPushButton(self.frame)
        self.pushButton_concludi_setup.setObjectName(u"pushButton_concludi_setup")
        self.pushButton_concludi_setup.setGeometry(QRect(810, 420, 141, 131))
        self.pushButton_concludi_setup.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_concludi_setup.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)


        self.retranslateUi(Dialog_Euramet_setup)

        QMetaObject.connectSlotsByName(Dialog_Euramet_setup)
    # setupUi

    def retranslateUi(self, Dialog_Euramet_setup):
        Dialog_Euramet_setup.setWindowTitle(QCoreApplication.translate("Dialog_Euramet_setup", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog_Euramet_setup", u"EURAMET", None))
        self.comboBox_step.setItemText(0, QCoreApplication.translate("Dialog_Euramet_setup", u"1 Step", None))
        self.comboBox_step.setItemText(1, QCoreApplication.translate("Dialog_Euramet_setup", u"2 Step", None))
        self.comboBox_step.setItemText(2, QCoreApplication.translate("Dialog_Euramet_setup", u"3 Step", None))
        self.comboBox_step.setItemText(3, QCoreApplication.translate("Dialog_Euramet_setup", u"4 Step", None))
        self.comboBox_step.setItemText(4, QCoreApplication.translate("Dialog_Euramet_setup", u"5 Step", None))

        self.checkBox_discesa_1.setText(QCoreApplication.translate("Dialog_Euramet_setup", u"DISCESA 1", None))
        self.checkBox_salita_1.setText(QCoreApplication.translate("Dialog_Euramet_setup", u"SALITA 1", None))
        self.checkBox_salita_2.setText(QCoreApplication.translate("Dialog_Euramet_setup", u"SALITA 2", None))
        self.checkBox_altezza.setText(QCoreApplication.translate("Dialog_Euramet_setup", u"ALTEZZA", None))
        self.label_correzione_lineare.setText(QCoreApplication.translate("Dialog_Euramet_setup", u"correzione lineare", None))
        self.label_3.setText(QCoreApplication.translate("Dialog_Euramet_setup", u"m", None))
        self.lineEdit_m.setText(QCoreApplication.translate("Dialog_Euramet_setup", u"-", None))
        self.label_4.setText(QCoreApplication.translate("Dialog_Euramet_setup", u"q", None))
        self.lineEdit_q.setText(QCoreApplication.translate("Dialog_Euramet_setup", u"-", None))
        self.pushButton_impostazion_csv.setText(QCoreApplication.translate("Dialog_Euramet_setup", u"impostazione csv", None))
        self.pushButton_concludi_setup.setText(QCoreApplication.translate("Dialog_Euramet_setup", u"concludi setup", None))
    # retranslateUi

