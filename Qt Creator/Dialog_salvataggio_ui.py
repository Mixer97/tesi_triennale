# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dialog_salvataggio.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(679, 268)
        Dialog.setBaseSize(QSize(600, 300))
        Dialog.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        Dialog.setModal(False)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(Dialog)
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
        self.label_salvataggio_title = QLabel(self.widget)
        self.label_salvataggio_title.setObjectName(u"label_salvataggio_title")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_salvataggio_title.sizePolicy().hasHeightForWidth())
        self.label_salvataggio_title.setSizePolicy(sizePolicy)
        self.label_salvataggio_title.setMinimumSize(QSize(0, 70))
        self.label_salvataggio_title.setStyleSheet(u"QLabel {\n"
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

        self.gridLayout_4.addWidget(self.label_salvataggio_title, 0, 0, 1, 1)


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
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.pushButton_salvataggio = QPushButton(self.gridWidget_3)
        self.pushButton_salvataggio.setObjectName(u"pushButton_salvataggio")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_salvataggio.sizePolicy().hasHeightForWidth())
        self.pushButton_salvataggio.setSizePolicy(sizePolicy1)
        self.pushButton_salvataggio.setMinimumSize(QSize(0, 70))
        font = QFont()
        font.setPointSize(15)
        self.pushButton_salvataggio.setFont(font)
        self.pushButton_salvataggio.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_salvataggio.setStyleSheet(u"QWidget{\n"
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

        self.gridLayout_9.addWidget(self.pushButton_salvataggio, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_9, 2, 0, 1, 2)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.lineEdit_nome_file = QLineEdit(self.gridWidget_3)
        self.lineEdit_nome_file.setObjectName(u"lineEdit_nome_file")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit_nome_file.sizePolicy().hasHeightForWidth())
        self.lineEdit_nome_file.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setPointSize(16)
        font1.setItalic(True)
        self.lineEdit_nome_file.setFont(font1)
        self.lineEdit_nome_file.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(255, 255, 255); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}")
        self.lineEdit_nome_file.setMaxLength(100)
        self.lineEdit_nome_file.setCursorPosition(7)
        self.lineEdit_nome_file.setAlignment(Qt.AlignCenter)
        self.lineEdit_nome_file.setClearButtonEnabled(True)

        self.gridLayout_5.addWidget(self.lineEdit_nome_file, 0, 1, 1, 1)

        self.label_nome_file = QLabel(self.gridWidget_3)
        self.label_nome_file.setObjectName(u"label_nome_file")
        self.label_nome_file.setStyleSheet(u"QWidget {\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"}\n"
"QLabel{\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")

        self.gridLayout_5.addWidget(self.label_nome_file, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_5, 0, 0, 1, 2)


        self.gridLayout_7.addWidget(self.gridWidget_3, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_salvataggio_title.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#292fa3;\">SALVATAGGIO FILE SETUP</span></p></body></html>", None))
        self.pushButton_salvataggio.setText(QCoreApplication.translate("Dialog", u"CONCLUDI", None))
        self.lineEdit_nome_file.setText(QCoreApplication.translate("Dialog", u"Default", None))
        self.lineEdit_nome_file.setPlaceholderText("")
        self.label_nome_file.setText(QCoreApplication.translate("Dialog", u"NOME FILE", None))
    # retranslateUi

