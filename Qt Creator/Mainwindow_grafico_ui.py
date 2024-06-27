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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QMainWindow, QPushButton, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)

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
"    border-width: 2px;\n"
"    border-color: black;\n"
"}\n"
"")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridWidget = QWidget(self.centralwidget)
        self.gridWidget.setObjectName(u"gridWidget")
        self.gridWidget.setStyleSheet(u"background-color: rgb(251, 255, 246);")
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
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

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
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy1)
        self.frame_5.setMinimumSize(QSize(0, 400))
        self.frame_5.setMaximumSize(QSize(16777215, 16777215))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_5)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_SG600 = QStackedWidget(self.frame_5)
        self.stackedWidget_SG600.setObjectName(u"stackedWidget_SG600")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.stackedWidget_SG600.sizePolicy().hasHeightForWidth())
        self.stackedWidget_SG600.setSizePolicy(sizePolicy2)
        self.page_temp_main = QWidget()
        self.page_temp_main.setObjectName(u"page_temp_main")
        self.gridLayout_4 = QGridLayout(self.page_temp_main)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.page_temp_main)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.frame_7, 0, 0, 1, 1)

        self.frame_11 = QFrame(self.page_temp_main)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(50, 16777215))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.frame_11, 0, 1, 4, 1)

        self.graphWidget_main = PlotWidget(self.page_temp_main)
        self.graphWidget_main.setObjectName(u"graphWidget_main")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.graphWidget_main.sizePolicy().hasHeightForWidth())
        self.graphWidget_main.setSizePolicy(sizePolicy3)
        self.graphWidget_main.setStyleSheet(u"background-color: rgb(26, 49, 255);")

        self.gridLayout_4.addWidget(self.graphWidget_main, 1, 0, 1, 1)

        self.graphWidget_temp = PlotWidget(self.page_temp_main)
        self.graphWidget_temp.setObjectName(u"graphWidget_temp")
        sizePolicy3.setHeightForWidth(self.graphWidget_temp.sizePolicy().hasHeightForWidth())
        self.graphWidget_temp.setSizePolicy(sizePolicy3)
        self.graphWidget_temp.setStyleSheet(u"background-color: rgb(26, 49, 255);")

        self.gridLayout_4.addWidget(self.graphWidget_temp, 2, 0, 1, 1)

        self.frame_10 = QFrame(self.page_temp_main)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.frame_10, 3, 0, 1, 1)

        self.stackedWidget_SG600.addWidget(self.page_temp_main)
        self.page_temp = QWidget()
        self.page_temp.setObjectName(u"page_temp")
        self.gridLayout_7 = QGridLayout(self.page_temp)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.page_temp)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 10))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)

        self.gridLayout_7.addWidget(self.frame_16, 0, 0, 1, 1)

        self.graphWidget_SG600_solo_temp = PlotWidget(self.page_temp)
        self.graphWidget_SG600_solo_temp.setObjectName(u"graphWidget_SG600_solo_temp")
        sizePolicy3.setHeightForWidth(self.graphWidget_SG600_solo_temp.sizePolicy().hasHeightForWidth())
        self.graphWidget_SG600_solo_temp.setSizePolicy(sizePolicy3)
        self.graphWidget_SG600_solo_temp.setStyleSheet(u"background-color: rgb(26, 49, 255);")

        self.gridLayout_7.addWidget(self.graphWidget_SG600_solo_temp, 1, 0, 1, 1)

        self.frame_18 = QFrame(self.page_temp)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 10))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)

        self.gridLayout_7.addWidget(self.frame_18, 2, 0, 1, 1)

        self.frame_17 = QFrame(self.page_temp)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(50, 16777215))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)

        self.gridLayout_7.addWidget(self.frame_17, 0, 1, 3, 1)

        self.stackedWidget_SG600.addWidget(self.page_temp)
        self.page_main = QWidget()
        self.page_main.setObjectName(u"page_main")
        self.gridLayout_5 = QGridLayout(self.page_main)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.page_main)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)

        self.gridLayout_5.addWidget(self.frame_13, 0, 0, 1, 1)

        self.frame_14 = QFrame(self.page_main)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMaximumSize(QSize(50, 16777215))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)

        self.gridLayout_5.addWidget(self.frame_14, 0, 1, 3, 1)

        self.graphWidget_solo_main = PlotWidget(self.page_main)
        self.graphWidget_solo_main.setObjectName(u"graphWidget_solo_main")
        sizePolicy3.setHeightForWidth(self.graphWidget_solo_main.sizePolicy().hasHeightForWidth())
        self.graphWidget_solo_main.setSizePolicy(sizePolicy3)
        self.graphWidget_solo_main.setStyleSheet(u"background-color: rgb(26, 49, 255);")

        self.gridLayout_5.addWidget(self.graphWidget_solo_main, 1, 0, 1, 1)

        self.frame_15 = QFrame(self.page_main)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)

        self.gridLayout_5.addWidget(self.frame_15, 2, 0, 1, 1)

        self.stackedWidget_SG600.addWidget(self.page_main)

        self.verticalLayout.addWidget(self.stackedWidget_SG600)

        self.stackedWidget_Laumas = QStackedWidget(self.frame_5)
        self.stackedWidget_Laumas.setObjectName(u"stackedWidget_Laumas")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.stackedWidget_Laumas.sizePolicy().hasHeightForWidth())
        self.stackedWidget_Laumas.setSizePolicy(sizePolicy4)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        sizePolicy2.setHeightForWidth(self.page_7.sizePolicy().hasHeightForWidth())
        self.page_7.setSizePolicy(sizePolicy2)
        self.gridLayout_3 = QGridLayout(self.page_7)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.page_7)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(50, 16777215))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.frame_12, 0, 1, 5, 1)

        self.frame_8 = QFrame(self.page_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.frame_8, 0, 0, 1, 1)

        self.frame_9 = QFrame(self.page_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.frame_9, 4, 0, 1, 1)

        self.graphWidget_4 = PlotWidget(self.page_7)
        self.graphWidget_4.setObjectName(u"graphWidget_4")
        sizePolicy3.setHeightForWidth(self.graphWidget_4.sizePolicy().hasHeightForWidth())
        self.graphWidget_4.setSizePolicy(sizePolicy3)
        self.graphWidget_4.setStyleSheet(u"background-color: rgb(26, 49, 255);")

        self.gridLayout_3.addWidget(self.graphWidget_4, 3, 0, 1, 1)

        self.stackedWidget_Laumas.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.stackedWidget_Laumas.addWidget(self.page_8)

        self.verticalLayout.addWidget(self.stackedWidget_Laumas)


        self.gridLayout.addWidget(self.frame_5, 1, 0, 1, 1)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy5)
        self.frame_4.setMinimumSize(QSize(0, 50))
        self.frame_4.setMaximumSize(QSize(16777215, 16777215))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_4, 2, 0, 1, 1)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy5.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy5)
        self.frame_6.setMinimumSize(QSize(0, 25))
        self.frame_6.setMaximumSize(QSize(16777215, 25))
        self.frame_6.setBaseSize(QSize(0, 0))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_6, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.gridWidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QSize(200, 0))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(70, 50, 83, 29))

        self.horizontalLayout.addWidget(self.frame_2)


        self.gridLayout_2.addWidget(self.gridWidget, 0, 0, 1, 1)

        GraphWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(GraphWindow)

        QMetaObject.connectSlotsByName(GraphWindow)
    # setupUi

    def retranslateUi(self, GraphWindow):
        GraphWindow.setWindowTitle(QCoreApplication.translate("GraphWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("GraphWindow", u"PushButton", None))
    # retranslateUi

