# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dialog_xlxs_euramet.ui'
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
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog_csv_euramet(object):
    def setupUi(self, Dialog_csv_euramet):
        if not Dialog_csv_euramet.objectName():
            Dialog_csv_euramet.setObjectName(u"Dialog_csv_euramet")
        Dialog_csv_euramet.resize(986, 621)
        Dialog_csv_euramet.setStyleSheet(u"background-color: rgb(48, 199, 40);")
        self.gridLayout = QGridLayout(Dialog_csv_euramet)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(0)
        self.frame = QFrame(Dialog_csv_euramet)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(238, 255, 239);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.frame_9 = QFrame(self.frame_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_data = QLabel(self.frame_9)
        self.label_data.setObjectName(u"label_data")
        self.label_data.setMinimumSize(QSize(205, 0))
        self.label_data.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_data.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_data)

        self.lineEdit_data = QLineEdit(self.frame_9)
        self.lineEdit_data.setObjectName(u"lineEdit_data")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_data.sizePolicy().hasHeightForWidth())
        self.lineEdit_data.setSizePolicy(sizePolicy)
        self.lineEdit_data.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(255, 255, 255); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}")
        self.lineEdit_data.setAlignment(Qt.AlignCenter)
        self.lineEdit_data.setClearButtonEnabled(True)

        self.horizontalLayout_7.addWidget(self.lineEdit_data)


        self.verticalLayout_2.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_3)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_rif_interno_attivita = QLabel(self.frame_10)
        self.label_rif_interno_attivita.setObjectName(u"label_rif_interno_attivita")
        self.label_rif_interno_attivita.setMinimumSize(QSize(205, 0))
        self.label_rif_interno_attivita.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_rif_interno_attivita.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_rif_interno_attivita)

        self.lineEdit_rif_interno_attivita = QLineEdit(self.frame_10)
        self.lineEdit_rif_interno_attivita.setObjectName(u"lineEdit_rif_interno_attivita")
        sizePolicy.setHeightForWidth(self.lineEdit_rif_interno_attivita.sizePolicy().hasHeightForWidth())
        self.lineEdit_rif_interno_attivita.setSizePolicy(sizePolicy)
        self.lineEdit_rif_interno_attivita.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(255, 255, 255); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}")
        self.lineEdit_rif_interno_attivita.setAlignment(Qt.AlignCenter)
        self.lineEdit_rif_interno_attivita.setClearButtonEnabled(True)

        self.horizontalLayout_8.addWidget(self.lineEdit_rif_interno_attivita)


        self.verticalLayout_2.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_3)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_cliente = QLabel(self.frame_11)
        self.label_cliente.setObjectName(u"label_cliente")
        self.label_cliente.setMinimumSize(QSize(205, 0))
        self.label_cliente.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_cliente.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_cliente)

        self.lineEdit_cliente = QLineEdit(self.frame_11)
        self.lineEdit_cliente.setObjectName(u"lineEdit_cliente")
        sizePolicy.setHeightForWidth(self.lineEdit_cliente.sizePolicy().hasHeightForWidth())
        self.lineEdit_cliente.setSizePolicy(sizePolicy)
        self.lineEdit_cliente.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(255, 255, 255); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}")
        self.lineEdit_cliente.setAlignment(Qt.AlignCenter)
        self.lineEdit_cliente.setClearButtonEnabled(True)

        self.horizontalLayout_9.addWidget(self.lineEdit_cliente)


        self.verticalLayout_2.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_3)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_SN_TX = QLabel(self.frame_12)
        self.label_SN_TX.setObjectName(u"label_SN_TX")
        self.label_SN_TX.setMinimumSize(QSize(205, 0))
        self.label_SN_TX.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_SN_TX.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_SN_TX)

        self.lineEdit_SN_TX = QLineEdit(self.frame_12)
        self.lineEdit_SN_TX.setObjectName(u"lineEdit_SN_TX")
        sizePolicy.setHeightForWidth(self.lineEdit_SN_TX.sizePolicy().hasHeightForWidth())
        self.lineEdit_SN_TX.setSizePolicy(sizePolicy)
        self.lineEdit_SN_TX.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(255, 255, 255); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}")
        self.lineEdit_SN_TX.setAlignment(Qt.AlignCenter)
        self.lineEdit_SN_TX.setClearButtonEnabled(True)

        self.horizontalLayout_10.addWidget(self.lineEdit_SN_TX)


        self.verticalLayout_2.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_3)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_descrizione_UUT = QLabel(self.frame_13)
        self.label_descrizione_UUT.setObjectName(u"label_descrizione_UUT")
        self.label_descrizione_UUT.setMinimumSize(QSize(205, 0))
        self.label_descrizione_UUT.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_descrizione_UUT.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_descrizione_UUT)

        self.lineEdit_descrizione_UUT = QLineEdit(self.frame_13)
        self.lineEdit_descrizione_UUT.setObjectName(u"lineEdit_descrizione_UUT")
        sizePolicy.setHeightForWidth(self.lineEdit_descrizione_UUT.sizePolicy().hasHeightForWidth())
        self.lineEdit_descrizione_UUT.setSizePolicy(sizePolicy)
        self.lineEdit_descrizione_UUT.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(255, 255, 255); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}")
        self.lineEdit_descrizione_UUT.setAlignment(Qt.AlignCenter)
        self.lineEdit_descrizione_UUT.setClearButtonEnabled(True)

        self.horizontalLayout_11.addWidget(self.lineEdit_descrizione_UUT)


        self.verticalLayout_2.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_3)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_progetto_UUT = QLabel(self.frame_14)
        self.label_progetto_UUT.setObjectName(u"label_progetto_UUT")
        self.label_progetto_UUT.setMinimumSize(QSize(205, 0))
        self.label_progetto_UUT.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_progetto_UUT.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_progetto_UUT)

        self.lineEdit_progetto_UUT = QLineEdit(self.frame_14)
        self.lineEdit_progetto_UUT.setObjectName(u"lineEdit_progetto_UUT")
        sizePolicy.setHeightForWidth(self.lineEdit_progetto_UUT.sizePolicy().hasHeightForWidth())
        self.lineEdit_progetto_UUT.setSizePolicy(sizePolicy)
        self.lineEdit_progetto_UUT.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(255, 255, 255); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}")
        self.lineEdit_progetto_UUT.setAlignment(Qt.AlignCenter)
        self.lineEdit_progetto_UUT.setClearButtonEnabled(True)

        self.horizontalLayout_12.addWidget(self.lineEdit_progetto_UUT)


        self.verticalLayout_2.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.frame_3)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_SN_UUT = QLabel(self.frame_15)
        self.label_SN_UUT.setObjectName(u"label_SN_UUT")
        self.label_SN_UUT.setMinimumSize(QSize(205, 0))
        self.label_SN_UUT.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_SN_UUT.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_SN_UUT)

        self.lineEdit_SN_UUT = QLineEdit(self.frame_15)
        self.lineEdit_SN_UUT.setObjectName(u"lineEdit_SN_UUT")
        sizePolicy.setHeightForWidth(self.lineEdit_SN_UUT.sizePolicy().hasHeightForWidth())
        self.lineEdit_SN_UUT.setSizePolicy(sizePolicy)
        self.lineEdit_SN_UUT.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(255, 255, 255); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}")
        self.lineEdit_SN_UUT.setAlignment(Qt.AlignCenter)
        self.lineEdit_SN_UUT.setClearButtonEnabled(True)

        self.horizontalLayout_13.addWidget(self.lineEdit_SN_UUT)


        self.verticalLayout_2.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.frame_3)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_report_calibrazione_TX = QLabel(self.frame_16)
        self.label_report_calibrazione_TX.setObjectName(u"label_report_calibrazione_TX")
        self.label_report_calibrazione_TX.setMinimumSize(QSize(205, 0))
        self.label_report_calibrazione_TX.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_report_calibrazione_TX.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_report_calibrazione_TX)

        self.lineEdit_report_calibrazione_TX = QLineEdit(self.frame_16)
        self.lineEdit_report_calibrazione_TX.setObjectName(u"lineEdit_report_calibrazione_TX")
        sizePolicy.setHeightForWidth(self.lineEdit_report_calibrazione_TX.sizePolicy().hasHeightForWidth())
        self.lineEdit_report_calibrazione_TX.setSizePolicy(sizePolicy)
        self.lineEdit_report_calibrazione_TX.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(255, 255, 255); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}")
        self.lineEdit_report_calibrazione_TX.setAlignment(Qt.AlignCenter)
        self.lineEdit_report_calibrazione_TX.setClearButtonEnabled(True)

        self.horizontalLayout_14.addWidget(self.lineEdit_report_calibrazione_TX)


        self.verticalLayout_2.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.frame_3)
        self.frame_17.setObjectName(u"frame_17")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy1)
        self.frame_17.setMinimumSize(QSize(0, 200))
        self.frame_17.setStyleSheet(u"border-width: 0px;")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_17)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_20 = QFrame(self.frame_17)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_title_cella_start_Q3_2 = QLabel(self.frame_20)
        self.label_title_cella_start_Q3_2.setObjectName(u"label_title_cella_start_Q3_2")
        self.label_title_cella_start_Q3_2.setMinimumSize(QSize(0, 0))
        self.label_title_cella_start_Q3_2.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_title_cella_start_Q3_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_title_cella_start_Q3_2)

        self.label_colonna_start_Q3 = QLineEdit(self.frame_20)
        self.label_colonna_start_Q3.setObjectName(u"label_colonna_start_Q3")
        sizePolicy1.setHeightForWidth(self.label_colonna_start_Q3.sizePolicy().hasHeightForWidth())
        self.label_colonna_start_Q3.setSizePolicy(sizePolicy1)
        self.label_colonna_start_Q3.setMinimumSize(QSize(80, 0))
        self.label_colonna_start_Q3.setMaximumSize(QSize(80, 16777215))
        self.label_colonna_start_Q3.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(255, 255, 255); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}")
        self.label_colonna_start_Q3.setAlignment(Qt.AlignCenter)
        self.label_colonna_start_Q3.setClearButtonEnabled(True)

        self.horizontalLayout_17.addWidget(self.label_colonna_start_Q3)


        self.gridLayout_3.addWidget(self.frame_20, 1, 0, 1, 1)

        self.frame_18 = QFrame(self.frame_17)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_title_riga_start_Q3 = QLabel(self.frame_18)
        self.label_title_riga_start_Q3.setObjectName(u"label_title_riga_start_Q3")
        self.label_title_riga_start_Q3.setMinimumSize(QSize(0, 0))
        self.label_title_riga_start_Q3.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_title_riga_start_Q3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_title_riga_start_Q3)

        self.label_riga_start_Q3 = QLineEdit(self.frame_18)
        self.label_riga_start_Q3.setObjectName(u"label_riga_start_Q3")
        sizePolicy.setHeightForWidth(self.label_riga_start_Q3.sizePolicy().hasHeightForWidth())
        self.label_riga_start_Q3.setSizePolicy(sizePolicy)
        self.label_riga_start_Q3.setMinimumSize(QSize(80, 0))
        self.label_riga_start_Q3.setMaximumSize(QSize(80, 16777215))
        self.label_riga_start_Q3.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(255, 255, 255); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}")
        self.label_riga_start_Q3.setAlignment(Qt.AlignCenter)
        self.label_riga_start_Q3.setClearButtonEnabled(True)

        self.horizontalLayout_15.addWidget(self.label_riga_start_Q3)


        self.gridLayout_3.addWidget(self.frame_18, 1, 1, 1, 1)

        self.frame_21 = QFrame(self.frame_17)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_title_cella_start_Q3_3 = QLabel(self.frame_21)
        self.label_title_cella_start_Q3_3.setObjectName(u"label_title_cella_start_Q3_3")
        self.label_title_cella_start_Q3_3.setMinimumSize(QSize(0, 0))
        self.label_title_cella_start_Q3_3.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_title_cella_start_Q3_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.label_title_cella_start_Q3_3)

        self.label_colonna_start_Q1 = QLineEdit(self.frame_21)
        self.label_colonna_start_Q1.setObjectName(u"label_colonna_start_Q1")
        sizePolicy.setHeightForWidth(self.label_colonna_start_Q1.sizePolicy().hasHeightForWidth())
        self.label_colonna_start_Q1.setSizePolicy(sizePolicy)
        self.label_colonna_start_Q1.setMinimumSize(QSize(80, 0))
        self.label_colonna_start_Q1.setMaximumSize(QSize(80, 16777215))
        self.label_colonna_start_Q1.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(255, 255, 255); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}")
        self.label_colonna_start_Q1.setAlignment(Qt.AlignCenter)
        self.label_colonna_start_Q1.setClearButtonEnabled(True)

        self.horizontalLayout_18.addWidget(self.label_colonna_start_Q1)


        self.gridLayout_3.addWidget(self.frame_21, 2, 0, 1, 1)

        self.frame_19 = QFrame(self.frame_17)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_title_cella_start_Q1 = QLabel(self.frame_19)
        self.label_title_cella_start_Q1.setObjectName(u"label_title_cella_start_Q1")
        self.label_title_cella_start_Q1.setMinimumSize(QSize(0, 0))
        self.label_title_cella_start_Q1.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_title_cella_start_Q1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_title_cella_start_Q1)

        self.label_riga_start_Q1 = QLineEdit(self.frame_19)
        self.label_riga_start_Q1.setObjectName(u"label_riga_start_Q1")
        sizePolicy.setHeightForWidth(self.label_riga_start_Q1.sizePolicy().hasHeightForWidth())
        self.label_riga_start_Q1.setSizePolicy(sizePolicy)
        self.label_riga_start_Q1.setMinimumSize(QSize(80, 0))
        self.label_riga_start_Q1.setMaximumSize(QSize(80, 16777215))
        self.label_riga_start_Q1.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(255, 255, 255); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}")
        self.label_riga_start_Q1.setAlignment(Qt.AlignCenter)
        self.label_riga_start_Q1.setClearButtonEnabled(True)

        self.horizontalLayout_16.addWidget(self.label_riga_start_Q1)


        self.gridLayout_3.addWidget(self.frame_19, 2, 1, 1, 1)

        self.frame_22 = QFrame(self.frame_17)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_title_cella_start_Q1_2 = QLabel(self.frame_22)
        self.label_title_cella_start_Q1_2.setObjectName(u"label_title_cella_start_Q1_2")
        self.label_title_cella_start_Q1_2.setMinimumSize(QSize(0, 0))
        self.label_title_cella_start_Q1_2.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 153, 119); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color:rgb(255, 140, 100);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_title_cella_start_Q1_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.label_title_cella_start_Q1_2)

        self.label_nome_excell = QLineEdit(self.frame_22)
        self.label_nome_excell.setObjectName(u"label_nome_excell")
        sizePolicy.setHeightForWidth(self.label_nome_excell.sizePolicy().hasHeightForWidth())
        self.label_nome_excell.setSizePolicy(sizePolicy)
        self.label_nome_excell.setMinimumSize(QSize(150, 0))
        self.label_nome_excell.setMaximumSize(QSize(80, 16777215))
        self.label_nome_excell.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(255, 255, 255); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}")
        self.label_nome_excell.setAlignment(Qt.AlignCenter)
        self.label_nome_excell.setClearButtonEnabled(True)

        self.horizontalLayout_19.addWidget(self.label_nome_excell)


        self.gridLayout_3.addWidget(self.frame_22, 3, 0, 1, 1)

        self.frame_23 = QFrame(self.frame_17)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_title_cella_start_Q1_3 = QLabel(self.frame_23)
        self.label_title_cella_start_Q1_3.setObjectName(u"label_title_cella_start_Q1_3")
        self.label_title_cella_start_Q1_3.setMinimumSize(QSize(0, 0))
        self.label_title_cella_start_Q1_3.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_title_cella_start_Q1_3.setAlignment(Qt.AlignCenter)
        self.label_title_cella_start_Q1_3.setMargin(2)

        self.horizontalLayout_20.addWidget(self.label_title_cella_start_Q1_3)

        self.label_nome_foglio_dati = QLineEdit(self.frame_23)
        self.label_nome_foglio_dati.setObjectName(u"label_nome_foglio_dati")
        sizePolicy.setHeightForWidth(self.label_nome_foglio_dati.sizePolicy().hasHeightForWidth())
        self.label_nome_foglio_dati.setSizePolicy(sizePolicy)
        self.label_nome_foglio_dati.setMinimumSize(QSize(150, 0))
        self.label_nome_foglio_dati.setMaximumSize(QSize(80, 16777215))
        self.label_nome_foglio_dati.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(255, 255, 255); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}")
        self.label_nome_foglio_dati.setAlignment(Qt.AlignCenter)
        self.label_nome_foglio_dati.setClearButtonEnabled(True)

        self.horizontalLayout_20.addWidget(self.label_nome_foglio_dati)


        self.gridLayout_3.addWidget(self.frame_23, 3, 1, 1, 1)

        self.label_3 = QLabel(self.frame_17)
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

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 2)


        self.verticalLayout_2.addWidget(self.frame_17)


        self.gridLayout_2.addWidget(self.frame_3, 1, 1, 1, 1)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
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

        self.verticalLayout.addWidget(self.label)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_unita_ingegneristica_di_misura = QLabel(self.frame_4)
        self.label_unita_ingegneristica_di_misura.setObjectName(u"label_unita_ingegneristica_di_misura")
        self.label_unita_ingegneristica_di_misura.setMinimumSize(QSize(205, 0))
        self.label_unita_ingegneristica_di_misura.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_unita_ingegneristica_di_misura.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_unita_ingegneristica_di_misura)

        self.lineEdit_unita_ingegneristica_di_misura = QLineEdit(self.frame_4)
        self.lineEdit_unita_ingegneristica_di_misura.setObjectName(u"lineEdit_unita_ingegneristica_di_misura")
        sizePolicy.setHeightForWidth(self.lineEdit_unita_ingegneristica_di_misura.sizePolicy().hasHeightForWidth())
        self.lineEdit_unita_ingegneristica_di_misura.setSizePolicy(sizePolicy)
        self.lineEdit_unita_ingegneristica_di_misura.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(255, 255, 255); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}")
        self.lineEdit_unita_ingegneristica_di_misura.setAlignment(Qt.AlignCenter)
        self.lineEdit_unita_ingegneristica_di_misura.setClearButtonEnabled(True)

        self.horizontalLayout_2.addWidget(self.lineEdit_unita_ingegneristica_di_misura)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_unita_ingegneristica_UUT = QLabel(self.frame_5)
        self.label_unita_ingegneristica_UUT.setObjectName(u"label_unita_ingegneristica_UUT")
        self.label_unita_ingegneristica_UUT.setMinimumSize(QSize(205, 0))
        self.label_unita_ingegneristica_UUT.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_unita_ingegneristica_UUT.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_unita_ingegneristica_UUT)

        self.lineEdit_unita_ingegneristica_UUT = QLineEdit(self.frame_5)
        self.lineEdit_unita_ingegneristica_UUT.setObjectName(u"lineEdit_unita_ingegneristica_UUT")
        sizePolicy.setHeightForWidth(self.lineEdit_unita_ingegneristica_UUT.sizePolicy().hasHeightForWidth())
        self.lineEdit_unita_ingegneristica_UUT.setSizePolicy(sizePolicy)
        self.lineEdit_unita_ingegneristica_UUT.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(255, 255, 255); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}")
        self.lineEdit_unita_ingegneristica_UUT.setAlignment(Qt.AlignCenter)
        self.lineEdit_unita_ingegneristica_UUT.setClearButtonEnabled(True)

        self.horizontalLayout_3.addWidget(self.lineEdit_unita_ingegneristica_UUT)


        self.verticalLayout.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_scale = QLabel(self.frame_6)
        self.label_scale.setObjectName(u"label_scale")
        self.label_scale.setMinimumSize(QSize(205, 0))
        self.label_scale.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_scale.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_scale)

        self.lineEdit_scale = QLineEdit(self.frame_6)
        self.lineEdit_scale.setObjectName(u"lineEdit_scale")
        sizePolicy.setHeightForWidth(self.lineEdit_scale.sizePolicy().hasHeightForWidth())
        self.lineEdit_scale.setSizePolicy(sizePolicy)
        self.lineEdit_scale.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(255, 255, 255); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}")
        self.lineEdit_scale.setAlignment(Qt.AlignCenter)
        self.lineEdit_scale.setClearButtonEnabled(True)

        self.horizontalLayout_4.addWidget(self.lineEdit_scale)


        self.verticalLayout.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_offset = QLabel(self.frame_7)
        self.label_offset.setObjectName(u"label_offset")
        self.label_offset.setMinimumSize(QSize(205, 0))
        self.label_offset.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_offset.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_offset)

        self.lineEdit_offset = QLineEdit(self.frame_7)
        self.lineEdit_offset.setObjectName(u"lineEdit_offset")
        sizePolicy.setHeightForWidth(self.lineEdit_offset.sizePolicy().hasHeightForWidth())
        self.lineEdit_offset.setSizePolicy(sizePolicy)
        self.lineEdit_offset.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(255, 255, 255); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}")
        self.lineEdit_offset.setAlignment(Qt.AlignCenter)
        self.lineEdit_offset.setClearButtonEnabled(True)

        self.horizontalLayout_5.addWidget(self.lineEdit_offset)


        self.verticalLayout.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_coppia_taratura_max = QLabel(self.frame_8)
        self.label_coppia_taratura_max.setObjectName(u"label_coppia_taratura_max")
        self.label_coppia_taratura_max.setMinimumSize(QSize(205, 0))
        self.label_coppia_taratura_max.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_coppia_taratura_max.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_coppia_taratura_max)

        self.lineEdit_coppia_taratura_max = QLineEdit(self.frame_8)
        self.lineEdit_coppia_taratura_max.setObjectName(u"lineEdit_coppia_taratura_max")
        sizePolicy.setHeightForWidth(self.lineEdit_coppia_taratura_max.sizePolicy().hasHeightForWidth())
        self.lineEdit_coppia_taratura_max.setSizePolicy(sizePolicy)
        self.lineEdit_coppia_taratura_max.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(255, 255, 255); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}")
        self.lineEdit_coppia_taratura_max.setAlignment(Qt.AlignCenter)
        self.lineEdit_coppia_taratura_max.setClearButtonEnabled(True)

        self.horizontalLayout_6.addWidget(self.lineEdit_coppia_taratura_max)


        self.verticalLayout.addWidget(self.frame_8)

        self.pushButton_save_and_back = QPushButton(self.frame_2)
        self.pushButton_save_and_back.setObjectName(u"pushButton_save_and_back")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_save_and_back.sizePolicy().hasHeightForWidth())
        self.pushButton_save_and_back.setSizePolicy(sizePolicy2)
        self.pushButton_save_and_back.setMaximumSize(QSize(16777215, 200))
        font = QFont()
        font.setPointSize(14)
        self.pushButton_save_and_back.setFont(font)
        self.pushButton_save_and_back.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_save_and_back.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout.addWidget(self.pushButton_save_and_back)


        self.gridLayout_2.addWidget(self.frame_2, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 1, 1, 1, 1)

        self.frame_navigation = QFrame(Dialog_csv_euramet)
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
        self.horizontalLayout_21 = QHBoxLayout(self.frame_navigation)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.pushButton_save_euramet_setup = QPushButton(self.frame_navigation)
        self.pushButton_save_euramet_setup.setObjectName(u"pushButton_save_euramet_setup")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_save_euramet_setup.sizePolicy().hasHeightForWidth())
        self.pushButton_save_euramet_setup.setSizePolicy(sizePolicy3)
        self.pushButton_save_euramet_setup.setMaximumSize(QSize(200, 16777215))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setStrikeOut(False)
        self.pushButton_save_euramet_setup.setFont(font1)
        self.pushButton_save_euramet_setup.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_save_euramet_setup.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_21.addWidget(self.pushButton_save_euramet_setup)

        self.pushButton_load_euramet_setup = QPushButton(self.frame_navigation)
        self.pushButton_load_euramet_setup.setObjectName(u"pushButton_load_euramet_setup")
        sizePolicy3.setHeightForWidth(self.pushButton_load_euramet_setup.sizePolicy().hasHeightForWidth())
        self.pushButton_load_euramet_setup.setSizePolicy(sizePolicy3)
        self.pushButton_load_euramet_setup.setMaximumSize(QSize(200, 16777215))
        self.pushButton_load_euramet_setup.setFont(font1)
        self.pushButton_load_euramet_setup.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_load_euramet_setup.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_21.addWidget(self.pushButton_load_euramet_setup)

        self.frame_24 = QFrame(self.frame_navigation)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_24)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(0)
        self.gridLayout_4.setContentsMargins(-1, 2, -1, 2)
        self.label_title_cella_start_Q3_4 = QLabel(self.frame_24)
        self.label_title_cella_start_Q3_4.setObjectName(u"label_title_cella_start_Q3_4")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_title_cella_start_Q3_4.sizePolicy().hasHeightForWidth())
        self.label_title_cella_start_Q3_4.setSizePolicy(sizePolicy4)
        self.label_title_cella_start_Q3_4.setMinimumSize(QSize(0, 0))
        self.label_title_cella_start_Q3_4.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(255, 207, 84); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}\n"
"")
        self.label_title_cella_start_Q3_4.setAlignment(Qt.AlignCenter)
        self.label_title_cella_start_Q3_4.setMargin(5)

        self.gridLayout_4.addWidget(self.label_title_cella_start_Q3_4, 0, 0, 1, 1)

        self.label_euramet_attuale = QLabel(self.frame_24)
        self.label_euramet_attuale.setObjectName(u"label_euramet_attuale")
        font2 = QFont()
        font2.setPointSize(8)
        self.label_euramet_attuale.setFont(font2)
        self.label_euramet_attuale.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(255, 255, 255); \n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 106, 0);\n"
"	border-radius: 0px;\n"
"	color: rgb(0,0,0);\n"
"}")
        self.label_euramet_attuale.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_euramet_attuale, 0, 1, 1, 1)


        self.horizontalLayout_21.addWidget(self.frame_24)


        self.gridLayout.addWidget(self.frame_navigation, 0, 1, 1, 1)


        self.retranslateUi(Dialog_csv_euramet)

        QMetaObject.connectSlotsByName(Dialog_csv_euramet)
    # setupUi

    def retranslateUi(self, Dialog_csv_euramet):
        Dialog_csv_euramet.setWindowTitle(QCoreApplication.translate("Dialog_csv_euramet", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Dialog_csv_euramet", u"Variabili report di taratura", None))
        self.label_data.setText(QCoreApplication.translate("Dialog_csv_euramet", u"Data", None))
        self.lineEdit_data.setText(QCoreApplication.translate("Dialog_csv_euramet", u"-", None))
        self.label_rif_interno_attivita.setText(QCoreApplication.translate("Dialog_csv_euramet", u"Rif interno attivita", None))
        self.lineEdit_rif_interno_attivita.setText(QCoreApplication.translate("Dialog_csv_euramet", u"-", None))
        self.label_cliente.setText(QCoreApplication.translate("Dialog_csv_euramet", u"Cliente", None))
        self.lineEdit_cliente.setText(QCoreApplication.translate("Dialog_csv_euramet", u"-", None))
        self.label_SN_TX.setText(QCoreApplication.translate("Dialog_csv_euramet", u"SN TX", None))
        self.lineEdit_SN_TX.setText(QCoreApplication.translate("Dialog_csv_euramet", u"-", None))
        self.label_descrizione_UUT.setText(QCoreApplication.translate("Dialog_csv_euramet", u"Descrizione UUT", None))
        self.lineEdit_descrizione_UUT.setText(QCoreApplication.translate("Dialog_csv_euramet", u"-", None))
        self.label_progetto_UUT.setText(QCoreApplication.translate("Dialog_csv_euramet", u"Progetto UUT", None))
        self.lineEdit_progetto_UUT.setText(QCoreApplication.translate("Dialog_csv_euramet", u"-", None))
        self.label_SN_UUT.setText(QCoreApplication.translate("Dialog_csv_euramet", u"SN UUT", None))
        self.lineEdit_SN_UUT.setText(QCoreApplication.translate("Dialog_csv_euramet", u"-", None))
        self.label_report_calibrazione_TX.setText(QCoreApplication.translate("Dialog_csv_euramet", u"Report di calibrazione TX", None))
        self.lineEdit_report_calibrazione_TX.setText(QCoreApplication.translate("Dialog_csv_euramet", u"-", None))
        self.label_title_cella_start_Q3_2.setText(QCoreApplication.translate("Dialog_csv_euramet", u"colonna primo dato Q3 ", None))
        self.label_colonna_start_Q3.setText(QCoreApplication.translate("Dialog_csv_euramet", u"D", None))
        self.label_title_riga_start_Q3.setText(QCoreApplication.translate("Dialog_csv_euramet", u"riga primo dato Q3 ", None))
        self.label_riga_start_Q3.setText(QCoreApplication.translate("Dialog_csv_euramet", u"7", None))
        self.label_title_cella_start_Q3_3.setText(QCoreApplication.translate("Dialog_csv_euramet", u"colonna primo dato Q1 ", None))
        self.label_colonna_start_Q1.setText(QCoreApplication.translate("Dialog_csv_euramet", u"D", None))
        self.label_title_cella_start_Q1.setText(QCoreApplication.translate("Dialog_csv_euramet", u"riga primo dato Q1", None))
        self.label_riga_start_Q1.setText(QCoreApplication.translate("Dialog_csv_euramet", u"29", None))
        self.label_title_cella_start_Q1_2.setText(QCoreApplication.translate("Dialog_csv_euramet", u"nome_excell", None))
        self.label_nome_excell.setText(QCoreApplication.translate("Dialog_csv_euramet", u"Default", None))
        self.label_title_cella_start_Q1_3.setText(QCoreApplication.translate("Dialog_csv_euramet", u"foglio_dati", None))
        self.label_nome_foglio_dati.setText(QCoreApplication.translate("Dialog_csv_euramet", u"Euramet", None))
        self.label_3.setText(QCoreApplication.translate("Dialog_csv_euramet", u"Riferimento per inserimento dati", None))
        self.label.setText(QCoreApplication.translate("Dialog_csv_euramet", u"Parametri di acquisizione", None))
        self.label_unita_ingegneristica_di_misura.setText(QCoreApplication.translate("Dialog_csv_euramet", u"Unit\u00e0 ingegneristica di misura", None))
        self.lineEdit_unita_ingegneristica_di_misura.setText(QCoreApplication.translate("Dialog_csv_euramet", u"Nm", None))
        self.label_unita_ingegneristica_UUT.setText(QCoreApplication.translate("Dialog_csv_euramet", u"Unit\u00e0 ingegneristica UUT", None))
        self.lineEdit_unita_ingegneristica_UUT.setText(QCoreApplication.translate("Dialog_csv_euramet", u"Nm", None))
        self.label_scale.setText(QCoreApplication.translate("Dialog_csv_euramet", u"Scale [Nm/V]", None))
        self.lineEdit_scale.setText(QCoreApplication.translate("Dialog_csv_euramet", u"1", None))
        self.label_offset.setText(QCoreApplication.translate("Dialog_csv_euramet", u"Offset [V]", None))
        self.lineEdit_offset.setText(QCoreApplication.translate("Dialog_csv_euramet", u"2.5", None))
        self.label_coppia_taratura_max.setText(QCoreApplication.translate("Dialog_csv_euramet", u"Coppia taratura MAX [Nm]", None))
        self.lineEdit_coppia_taratura_max.setText(QCoreApplication.translate("Dialog_csv_euramet", u"2000", None))
        self.pushButton_save_and_back.setText(QCoreApplication.translate("Dialog_csv_euramet", u"SALVA E CREA EXCELL EURAMET", None))
        self.pushButton_save_euramet_setup.setText(QCoreApplication.translate("Dialog_csv_euramet", u"SALVA SETUP", None))
        self.pushButton_load_euramet_setup.setText(QCoreApplication.translate("Dialog_csv_euramet", u"CARICA SETUP", None))
        self.label_title_cella_start_Q3_4.setText(QCoreApplication.translate("Dialog_csv_euramet", u"setup attuale", None))
        self.label_euramet_attuale.setText(QCoreApplication.translate("Dialog_csv_euramet", u"-----", None))
    # retranslateUi

