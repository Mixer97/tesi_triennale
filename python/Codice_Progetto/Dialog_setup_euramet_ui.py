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
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_Dialog_Euramet_setup(object):
    def setupUi(self, Dialog_Euramet_setup):
        if not Dialog_Euramet_setup.objectName():
            Dialog_Euramet_setup.setObjectName(u"Dialog_Euramet_setup")
        Dialog_Euramet_setup.resize(1003, 612)
        Dialog_Euramet_setup.setStyleSheet(u"background-color: rgb(48, 199, 40);")
        self.gridLayout = QGridLayout(Dialog_Euramet_setup)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(0)
        self.frame = QFrame(Dialog_Euramet_setup)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(238, 255, 239);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame_8 = QFrame(self.frame)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_8)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_euramet = QStackedWidget(self.frame_8)
        self.stackedWidget_euramet.setObjectName(u"stackedWidget_euramet")
        self.stackedWidget_euramet.setStyleSheet(u"border-color: rgb(0, 85, 0);\n"
"border-width: 3px;")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_5 = QGridLayout(self.page)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(5)
        self.gridLayout_5.setContentsMargins(5, 5, 5, 5)
        self.frame_25 = QFrame(self.page)
        self.frame_25.setObjectName(u"frame_25")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_25.sizePolicy().hasHeightForWidth())
        self.frame_25.setSizePolicy(sizePolicy1)
        self.frame_25.setMaximumSize(QSize(16777215, 100))
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_25)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_26 = QFrame(self.frame_25)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_38 = QLabel(self.frame_26)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_38.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_38)

        self.label_step_1_1 = QLabel(self.frame_26)
        self.label_step_1_1.setObjectName(u"label_step_1_1")
        self.label_step_1_1.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 255, 255); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_step_1_1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_step_1_1)


        self.verticalLayout_6.addWidget(self.frame_26)


        self.gridLayout_5.addWidget(self.frame_25, 0, 0, 1, 1)

        self.stackedWidget_euramet.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_6 = QGridLayout(self.page_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(5)
        self.gridLayout_6.setContentsMargins(5, 5, 5, 5)
        self.frame_22 = QFrame(self.page_2)
        self.frame_22.setObjectName(u"frame_22")
        sizePolicy1.setHeightForWidth(self.frame_22.sizePolicy().hasHeightForWidth())
        self.frame_22.setSizePolicy(sizePolicy1)
        self.frame_22.setMinimumSize(QSize(0, 200))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_22)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_23 = QFrame(self.frame_22)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_37 = QLabel(self.frame_23)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_37.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_37)

        self.label_step_1_2 = QLabel(self.frame_23)
        self.label_step_1_2.setObjectName(u"label_step_1_2")
        self.label_step_1_2.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 255, 255); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_step_1_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_step_1_2)


        self.verticalLayout_5.addWidget(self.frame_23)

        self.frame_24 = QFrame(self.frame_22)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.frame_24)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_15)

        self.label_step_2_2 = QLabel(self.frame_24)
        self.label_step_2_2.setObjectName(u"label_step_2_2")
        self.label_step_2_2.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 255, 255); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_step_2_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_step_2_2)


        self.verticalLayout_5.addWidget(self.frame_24)


        self.gridLayout_6.addWidget(self.frame_22, 0, 0, 1, 1)

        self.stackedWidget_euramet.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_7 = QGridLayout(self.page_3)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(5)
        self.gridLayout_7.setContentsMargins(5, 5, 5, 5)
        self.frame_18 = QFrame(self.page_3)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy1.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy1)
        self.frame_18.setMinimumSize(QSize(0, 300))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_18)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_19 = QFrame(self.frame_18)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_36 = QLabel(self.frame_19)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_36.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_36)

        self.label_step_1_3 = QLabel(self.frame_19)
        self.label_step_1_3.setObjectName(u"label_step_1_3")
        self.label_step_1_3.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 255, 255); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_step_1_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_step_1_3)


        self.verticalLayout_4.addWidget(self.frame_19)

        self.frame_20 = QFrame(self.frame_18)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.frame_20)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_13)

        self.label_step_2_3 = QLabel(self.frame_20)
        self.label_step_2_3.setObjectName(u"label_step_2_3")
        self.label_step_2_3.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 255, 255); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_step_2_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_step_2_3)


        self.verticalLayout_4.addWidget(self.frame_20)

        self.frame_21 = QFrame(self.frame_18)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.frame_21)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_14)

        self.label_step_3_3 = QLabel(self.frame_21)
        self.label_step_3_3.setObjectName(u"label_step_3_3")
        self.label_step_3_3.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 255, 255); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_step_3_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_step_3_3)


        self.verticalLayout_4.addWidget(self.frame_21)


        self.gridLayout_7.addWidget(self.frame_18, 0, 0, 1, 1)

        self.stackedWidget_euramet.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.gridLayout_8 = QGridLayout(self.page_4)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setHorizontalSpacing(5)
        self.gridLayout_8.setContentsMargins(5, 5, 5, 5)
        self.frame_13 = QFrame(self.page_4)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy1.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy1)
        self.frame_13.setMaximumSize(QSize(16777215, 400))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_13)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_35 = QLabel(self.frame_14)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_35.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_35)

        self.label_step_1_4 = QLabel(self.frame_14)
        self.label_step_1_4.setObjectName(u"label_step_1_4")
        self.label_step_1_4.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 255, 255); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_step_1_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_step_1_4)


        self.verticalLayout_3.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.frame_13)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_15)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_7)

        self.label_step_2_4 = QLabel(self.frame_15)
        self.label_step_2_4.setObjectName(u"label_step_2_4")
        self.label_step_2_4.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 255, 255); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_step_2_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_step_2_4)


        self.verticalLayout_3.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.frame_13)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.frame_16)
        self.label_9.setObjectName(u"label_9")
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

        self.horizontalLayout_10.addWidget(self.label_9)

        self.label_step_3_4 = QLabel(self.frame_16)
        self.label_step_3_4.setObjectName(u"label_step_3_4")
        self.label_step_3_4.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 255, 255); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_step_3_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_step_3_4)


        self.verticalLayout_3.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.frame_13)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.frame_17)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_11)

        self.label_step_4_4 = QLabel(self.frame_17)
        self.label_step_4_4.setObjectName(u"label_step_4_4")
        self.label_step_4_4.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 255, 255); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_step_4_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_step_4_4)


        self.verticalLayout_3.addWidget(self.frame_17)


        self.gridLayout_8.addWidget(self.frame_13, 0, 0, 1, 1)

        self.stackedWidget_euramet.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.gridLayout_9 = QGridLayout(self.page_5)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setHorizontalSpacing(5)
        self.gridLayout_9.setContentsMargins(5, 5, 5, 5)
        self.frame_7 = QFrame(self.page_5)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy1.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy1)
        self.frame_7.setMaximumSize(QSize(16777215, 500))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_7)
        self.verticalLayout_2.setSpacing(7)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_7)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_34 = QLabel(self.frame_6)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_34.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_34)

        self.label_step_1_5 = QLabel(self.frame_6)
        self.label_step_1_5.setObjectName(u"label_step_1_5")
        self.label_step_1_5.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 255, 255); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_step_1_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_step_1_5)


        self.verticalLayout_2.addWidget(self.frame_6)

        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_9)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_6)

        self.label_step_2_5 = QLabel(self.frame_9)
        self.label_step_2_5.setObjectName(u"label_step_2_5")
        self.label_step_2_5.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 255, 255); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_step_2_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_step_2_5)


        self.verticalLayout_2.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_7)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.frame_10)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_8)

        self.label_step_3_5 = QLabel(self.frame_10)
        self.label_step_3_5.setObjectName(u"label_step_3_5")
        self.label_step_3_5.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 255, 255); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_step_3_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_step_3_5)


        self.verticalLayout_2.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_7)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.frame_11)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_10)

        self.label_step_4_5 = QLabel(self.frame_11)
        self.label_step_4_5.setObjectName(u"label_step_4_5")
        self.label_step_4_5.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 255, 255); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_step_4_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_step_4_5)


        self.verticalLayout_2.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_7)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.frame_12)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_12)

        self.label_step_5_5 = QLabel(self.frame_12)
        self.label_step_5_5.setObjectName(u"label_step_5_5")
        self.label_step_5_5.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 255, 255); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_step_5_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_step_5_5)


        self.verticalLayout_2.addWidget(self.frame_12)


        self.gridLayout_9.addWidget(self.frame_7, 0, 0, 1, 1)

        self.stackedWidget_euramet.addWidget(self.page_5)

        self.gridLayout_3.addWidget(self.stackedWidget_euramet, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_8, 1, 0, 2, 1)

        self.frame_28 = QFrame(self.frame)
        self.frame_28.setObjectName(u"frame_28")
        sizePolicy1.setHeightForWidth(self.frame_28.sizePolicy().hasHeightForWidth())
        self.frame_28.setSizePolicy(sizePolicy1)
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.frame_2 = QFrame(self.frame_28)
        self.frame_2.setObjectName(u"frame_2")
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


        self.horizontalLayout_18.addWidget(self.frame_2)

        self.checkBox_salita_1 = QCheckBox(self.frame_28)
        self.checkBox_salita_1.setObjectName(u"checkBox_salita_1")
        sizePolicy1.setHeightForWidth(self.checkBox_salita_1.sizePolicy().hasHeightForWidth())
        self.checkBox_salita_1.setSizePolicy(sizePolicy1)
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
"")

        self.horizontalLayout_18.addWidget(self.checkBox_salita_1)

        self.checkBox_discesa_1 = QCheckBox(self.frame_28)
        self.checkBox_discesa_1.setObjectName(u"checkBox_discesa_1")
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

        self.horizontalLayout_18.addWidget(self.checkBox_discesa_1)

        self.checkBox_salita_2 = QCheckBox(self.frame_28)
        self.checkBox_salita_2.setObjectName(u"checkBox_salita_2")
        self.checkBox_salita_2.setEnabled(False)
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
        self.checkBox_salita_2.setCheckable(True)
        self.checkBox_salita_2.setChecked(True)

        self.horizontalLayout_18.addWidget(self.checkBox_salita_2)

        self.checkBox_altezza = QCheckBox(self.frame_28)
        self.checkBox_altezza.setObjectName(u"checkBox_altezza")
        sizePolicy1.setHeightForWidth(self.checkBox_altezza.sizePolicy().hasHeightForWidth())
        self.checkBox_altezza.setSizePolicy(sizePolicy1)
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

        self.horizontalLayout_18.addWidget(self.checkBox_altezza)

        self.comboBox_step = QComboBox(self.frame_28)
        self.comboBox_step.addItem("")
        self.comboBox_step.addItem("")
        self.comboBox_step.addItem("")
        self.comboBox_step.addItem("")
        self.comboBox_step.addItem("")
        self.comboBox_step.setObjectName(u"comboBox_step")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.comboBox_step.sizePolicy().hasHeightForWidth())
        self.comboBox_step.setSizePolicy(sizePolicy2)
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

        self.horizontalLayout_18.addWidget(self.comboBox_step)


        self.gridLayout_4.addWidget(self.frame_28, 0, 0, 1, 2)

        self.frame_29 = QFrame(self.frame)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMaximumSize(QSize(200, 16777215))
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_29)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_27 = QFrame(self.frame_29)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_27)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_quadrante_iniziale = QLabel(self.frame_27)
        self.label_quadrante_iniziale.setObjectName(u"label_quadrante_iniziale")
        self.label_quadrante_iniziale.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")

        self.verticalLayout_7.addWidget(self.label_quadrante_iniziale)

        self.comboBox_quadrante = QComboBox(self.frame_27)
        self.comboBox_quadrante.addItem("")
        self.comboBox_quadrante.addItem("")
        self.comboBox_quadrante.setObjectName(u"comboBox_quadrante")
        self.comboBox_quadrante.setStyleSheet(u"QComboBox {\n"
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

        self.verticalLayout_7.addWidget(self.comboBox_quadrante)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)


        self.verticalLayout_8.addWidget(self.frame_27)


        self.gridLayout_4.addWidget(self.frame_29, 1, 1, 2, 1)


        self.gridLayout.addWidget(self.frame, 1, 1, 1, 1)

        self.frame_navigation = QFrame(Dialog_Euramet_setup)
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
        self.horizontalLayout_19 = QHBoxLayout(self.frame_navigation)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.pushButton_concludi_setup = QPushButton(self.frame_navigation)
        self.pushButton_concludi_setup.setObjectName(u"pushButton_concludi_setup")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_concludi_setup.sizePolicy().hasHeightForWidth())
        self.pushButton_concludi_setup.setSizePolicy(sizePolicy3)
        self.pushButton_concludi_setup.setMaximumSize(QSize(200, 16777215))
        font1 = QFont()
        font1.setPointSize(14)
        self.pushButton_concludi_setup.setFont(font1)
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

        self.horizontalLayout_19.addWidget(self.pushButton_concludi_setup)

        self.pushButton_impostazioni_csv = QPushButton(self.frame_navigation)
        self.pushButton_impostazioni_csv.setObjectName(u"pushButton_impostazioni_csv")
        sizePolicy3.setHeightForWidth(self.pushButton_impostazioni_csv.sizePolicy().hasHeightForWidth())
        self.pushButton_impostazioni_csv.setSizePolicy(sizePolicy3)
        self.pushButton_impostazioni_csv.setMaximumSize(QSize(200, 16777215))
        self.pushButton_impostazioni_csv.setFont(font1)
        self.pushButton_impostazioni_csv.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_impostazioni_csv.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_19.addWidget(self.pushButton_impostazioni_csv)

        self.frame_30 = QFrame(self.frame_navigation)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_19.addWidget(self.frame_30)


        self.gridLayout.addWidget(self.frame_navigation, 0, 1, 1, 1)


        self.retranslateUi(Dialog_Euramet_setup)

        self.stackedWidget_euramet.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Dialog_Euramet_setup)
    # setupUi

    def retranslateUi(self, Dialog_Euramet_setup):
        Dialog_Euramet_setup.setWindowTitle(QCoreApplication.translate("Dialog_Euramet_setup", u"Dialog", None))
        self.label_38.setText(QCoreApplication.translate("Dialog_Euramet_setup", u"STEP 1", None))
        self.label_step_1_1.setText(QCoreApplication.translate("Dialog_Euramet_setup", u"-", None))
        self.label_37.setText(QCoreApplication.translate("Dialog_Euramet_setup", u"STEP 1", None))
        self.label_step_1_2.setText(QCoreApplication.translate("Dialog_Euramet_setup", u"-", None))
        self.label_15.setText(QCoreApplication.translate("Dialog_Euramet_setup", u"STEP 2", None))
        self.label_step_2_2.setText(QCoreApplication.translate("Dialog_Euramet_setup", u"-", None))
        self.label_36.setText(QCoreApplication.translate("Dialog_Euramet_setup", u"STEP 1", None))
        self.label_step_1_3.setText(QCoreApplication.translate("Dialog_Euramet_setup", u"-", None))
        self.label_13.setText(QCoreApplication.translate("Dialog_Euramet_setup", u"STEP 2", None))
        self.label_step_2_3.setText(QCoreApplication.translate("Dialog_Euramet_setup", u"-", None))
        self.label_14.setText(QCoreApplication.translate("Dialog_Euramet_setup", u"STEP 3", None))
        self.label_step_3_3.setText(QCoreApplication.translate("Dialog_Euramet_setup", u"-", None))
        self.label_35.setText(QCoreApplication.translate("Dialog_Euramet_setup", u"STEP 1", None))
        self.label_step_1_4.setText(QCoreApplication.translate("Dialog_Euramet_setup", u"-", None))
        self.label_7.setText(QCoreApplication.translate("Dialog_Euramet_setup", u"STEP 2", None))
        self.label_step_2_4.setText(QCoreApplication.translate("Dialog_Euramet_setup", u"-", None))
        self.label_9.setText(QCoreApplication.translate("Dialog_Euramet_setup", u"STEP 3", None))
        self.label_step_3_4.setText(QCoreApplication.translate("Dialog_Euramet_setup", u"-", None))
        self.label_11.setText(QCoreApplication.translate("Dialog_Euramet_setup", u"STEP 4", None))
        self.label_step_4_4.setText(QCoreApplication.translate("Dialog_Euramet_setup", u"-", None))
        self.label_34.setText(QCoreApplication.translate("Dialog_Euramet_setup", u"STEP 1", None))
        self.label_step_1_5.setText(QCoreApplication.translate("Dialog_Euramet_setup", u"-", None))
        self.label_6.setText(QCoreApplication.translate("Dialog_Euramet_setup", u"STEP 2", None))
        self.label_step_2_5.setText(QCoreApplication.translate("Dialog_Euramet_setup", u"-", None))
        self.label_8.setText(QCoreApplication.translate("Dialog_Euramet_setup", u"STEP 3", None))
        self.label_step_3_5.setText(QCoreApplication.translate("Dialog_Euramet_setup", u"-", None))
        self.label_10.setText(QCoreApplication.translate("Dialog_Euramet_setup", u"STEP 4", None))
        self.label_step_4_5.setText(QCoreApplication.translate("Dialog_Euramet_setup", u"-", None))
        self.label_12.setText(QCoreApplication.translate("Dialog_Euramet_setup", u"STEP 5", None))
        self.label_step_5_5.setText(QCoreApplication.translate("Dialog_Euramet_setup", u"-", None))
        self.label.setText(QCoreApplication.translate("Dialog_Euramet_setup", u"EURAMET", None))
        self.checkBox_salita_1.setText(QCoreApplication.translate("Dialog_Euramet_setup", u"SALITA 1", None))
        self.checkBox_discesa_1.setText(QCoreApplication.translate("Dialog_Euramet_setup", u"DISCESA 1", None))
        self.checkBox_salita_2.setText(QCoreApplication.translate("Dialog_Euramet_setup", u"SALITA 2", None))
        self.checkBox_altezza.setText(QCoreApplication.translate("Dialog_Euramet_setup", u"ALTEZZA", None))
        self.comboBox_step.setItemText(0, QCoreApplication.translate("Dialog_Euramet_setup", u"1 Step", None))
        self.comboBox_step.setItemText(1, QCoreApplication.translate("Dialog_Euramet_setup", u"2 Step", None))
        self.comboBox_step.setItemText(2, QCoreApplication.translate("Dialog_Euramet_setup", u"3 Step", None))
        self.comboBox_step.setItemText(3, QCoreApplication.translate("Dialog_Euramet_setup", u"4 Step", None))
        self.comboBox_step.setItemText(4, QCoreApplication.translate("Dialog_Euramet_setup", u"5 Step", None))

        self.label_quadrante_iniziale.setText(QCoreApplication.translate("Dialog_Euramet_setup", u"Quadrante iniziale", None))
        self.comboBox_quadrante.setItemText(0, QCoreApplication.translate("Dialog_Euramet_setup", u"Q1", None))
        self.comboBox_quadrante.setItemText(1, QCoreApplication.translate("Dialog_Euramet_setup", u"Q3", None))

        self.pushButton_concludi_setup.setText(QCoreApplication.translate("Dialog_Euramet_setup", u"CONCLUDI SETUP", None))
        self.pushButton_impostazioni_csv.setText(QCoreApplication.translate("Dialog_Euramet_setup", u"IMPOSTAZIONI", None))
    # retranslateUi

