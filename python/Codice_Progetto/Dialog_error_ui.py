# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dialog_error.ui'
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
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_Dialog_Error(object):
    def setupUi(self, Dialog_Error):
        if not Dialog_Error.objectName():
            Dialog_Error.setObjectName(u"Dialog_Error")
        Dialog_Error.setWindowModality(Qt.WindowModal)
        Dialog_Error.resize(500, 160)
        Dialog_Error.setMinimumSize(QSize(400, 160))
        Dialog_Error.setBaseSize(QSize(0, 0))
        icon = QIcon(QIcon.fromTheme(u"dialog-error"))
        Dialog_Error.setWindowIcon(icon)
        Dialog_Error.setStyleSheet(u"QWidget {\n"
"	background-color:rgb(255, 255, 255); \n"
"	border-style: outset;\n"
"    border-width: 0px;\n"
"    border-color:rgb(202, 202, 202);\n"
"}")
        Dialog_Error.setSizeGripEnabled(False)
        Dialog_Error.setModal(True)
        self.gridLayout = QGridLayout(Dialog_Error)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(0, 8, 0, 0)
        self.label_Error = QLabel(Dialog_Error)
        self.label_Error.setObjectName(u"label_Error")
        self.label_Error.setMinimumSize(QSize(500, 100))
        font = QFont()
        font.setFamilies([u"Forgotten Futurist"])
        font.setPointSize(15)
        font.setBold(False)
        self.label_Error.setFont(font)
        self.label_Error.setStyleSheet(u"QLabel {\n"
"    border: 2px solid;\n"
"    border-radius: 0px;\n"
"	border-style: outset;\n"
"    border-width: 0px;\n"
"}\n"
"QLabel{\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_Error.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_Error, 0, 0, 1, 1)

        self.frame = QFrame(Dialog_Error)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(0, 50))
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setStyleSheet(u"QWidget {\n"
"	background-color:qlineargradient(spread:pad, x1:0.48339, y1:0, x2:0.493, y2:1, stop:0 rgba(239, 239, 239, 255), stop:1 rgba(202, 202, 202, 255));\n"
"	border-style: outset;\n"
"    border-width: 0px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(15, 8, 15, 8)
        self.pushButton_error = QPushButton(self.frame_3)
        self.pushButton_error.setObjectName(u"pushButton_error")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_error.sizePolicy().hasHeightForWidth())
        self.pushButton_error.setSizePolicy(sizePolicy1)
        self.pushButton_error.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_error.setStyleSheet(u"QPushButton {\n"
"	border-color: rgb(120, 120, 120);\n"
"	border-width: 1px;\n"
"	color: rgb(122, 122, 122);\n"
"}\n"
"QPushButton::pressed{\n"
"	border-width: 1px;\n"
"	border-color: rgb(120, 120, 120);\n"
"	color: rgb(122, 122, 122);\n"
"	background-color: qlineargradient(spread:pad, x1:0.48339, y1:0, x2:0.493, y2:1, stop:0 rgba(220, 220, 220, 255), stop:1 rgba(180, 180, 180, 255));\n"
"}")

        self.gridLayout_2.addWidget(self.pushButton_error, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.frame_3)


        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)


        self.retranslateUi(Dialog_Error)

        QMetaObject.connectSlotsByName(Dialog_Error)
    # setupUi

    def retranslateUi(self, Dialog_Error):
        Dialog_Error.setWindowTitle(QCoreApplication.translate("Dialog_Error", u"Dialog", None))
        self.label_Error.setText(QCoreApplication.translate("Dialog_Error", u"TextLabel", None))
        self.pushButton_error.setText(QCoreApplication.translate("Dialog_Error", u"OK", None))
    # retranslateUi

