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
        self.gridWidget.setStyleSheet(u"background-color: rgb(251, 255, 246);\n"
"border-width: 1px")
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
        self.gridLayout_4.setContentsMargins(2, 2, 2, 2)
        self.frame_11 = QFrame(self.page_temp_main)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy3)
        self.frame_11.setMaximumSize(QSize(50, 16777215))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_11)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.frame_11)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy4)

        self.verticalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.frame_11)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy4.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy4)

        self.verticalLayout_2.addWidget(self.pushButton_2)


        self.gridLayout_4.addWidget(self.frame_11, 0, 1, 4, 1)

        self.graphWidget_main = PlotWidget(self.page_temp_main)
        self.graphWidget_main.setObjectName(u"graphWidget_main")
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

        self.stackedWidget_SG600.addWidget(self.page_temp_main)
        self.page_temp = QWidget()
        self.page_temp.setObjectName(u"page_temp")
        self.gridLayout_7 = QGridLayout(self.page_temp)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(2, 2, 2, 2)
        self.graphWidget_SG600_solo_temp = PlotWidget(self.page_temp)
        self.graphWidget_SG600_solo_temp.setObjectName(u"graphWidget_SG600_solo_temp")
        sizePolicy3.setHeightForWidth(self.graphWidget_SG600_solo_temp.sizePolicy().hasHeightForWidth())
        self.graphWidget_SG600_solo_temp.setSizePolicy(sizePolicy3)
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
        self.pushButton_4 = QPushButton(self.frame_17)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy3.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy3)

        self.verticalLayout_3.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame_17)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy3.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy3)

        self.verticalLayout_3.addWidget(self.pushButton_5)


        self.gridLayout_7.addWidget(self.frame_17, 0, 1, 3, 1)

        self.stackedWidget_SG600.addWidget(self.page_temp)
        self.page_main = QWidget()
        self.page_main.setObjectName(u"page_main")
        self.gridLayout_5 = QGridLayout(self.page_main)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(2, 2, 2, 2)
        self.frame_14 = QFrame(self.page_main)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMaximumSize(QSize(50, 16777215))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_14)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton_7 = QPushButton(self.frame_14)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy3.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy3)

        self.verticalLayout_4.addWidget(self.pushButton_7)

        self.pushButton_6 = QPushButton(self.frame_14)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy3.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy3)

        self.verticalLayout_4.addWidget(self.pushButton_6)


        self.gridLayout_5.addWidget(self.frame_14, 0, 1, 3, 1)

        self.graphWidget_solo_main = PlotWidget(self.page_main)
        self.graphWidget_solo_main.setObjectName(u"graphWidget_solo_main")
        sizePolicy3.setHeightForWidth(self.graphWidget_solo_main.sizePolicy().hasHeightForWidth())
        self.graphWidget_solo_main.setSizePolicy(sizePolicy3)
        self.graphWidget_solo_main.setStyleSheet(u"background-color: rgb(26, 49, 255);")

        self.gridLayout_5.addWidget(self.graphWidget_solo_main, 1, 0, 1, 1)

        self.stackedWidget_SG600.addWidget(self.page_main)

        self.verticalLayout.addWidget(self.stackedWidget_SG600)

        self.stackedWidget_Laumas = QStackedWidget(self.frame_5)
        self.stackedWidget_Laumas.setObjectName(u"stackedWidget_Laumas")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.stackedWidget_Laumas.sizePolicy().hasHeightForWidth())
        self.stackedWidget_Laumas.setSizePolicy(sizePolicy5)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        sizePolicy2.setHeightForWidth(self.page_7.sizePolicy().hasHeightForWidth())
        self.page_7.setSizePolicy(sizePolicy2)
        self.gridLayout_3 = QGridLayout(self.page_7)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(2, 2, 2, 2)
        self.frame_12 = QFrame(self.page_7)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(50, 16777215))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame_12)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy3.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy3)

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.gridLayout_3.addWidget(self.frame_12, 0, 1, 5, 1)

        self.graphWidget_solo_channel = PlotWidget(self.page_7)
        self.graphWidget_solo_channel.setObjectName(u"graphWidget_solo_channel")
        sizePolicy3.setHeightForWidth(self.graphWidget_solo_channel.sizePolicy().hasHeightForWidth())
        self.graphWidget_solo_channel.setSizePolicy(sizePolicy3)
        self.graphWidget_solo_channel.setStyleSheet(u"background-color: rgb(26, 49, 255);")

        self.gridLayout_3.addWidget(self.graphWidget_solo_channel, 3, 0, 1, 1)

        self.stackedWidget_Laumas.addWidget(self.page_7)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_9 = QGridLayout(self.page)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(2, 2, 2, 2)
        self.graphWidget_solo_channel_4 = PlotWidget(self.page)
        self.graphWidget_solo_channel_4.setObjectName(u"graphWidget_solo_channel_4")
        sizePolicy3.setHeightForWidth(self.graphWidget_solo_channel_4.sizePolicy().hasHeightForWidth())
        self.graphWidget_solo_channel_4.setSizePolicy(sizePolicy3)
        self.graphWidget_solo_channel_4.setStyleSheet(u"background-color: rgb(26, 49, 255);")

        self.gridLayout_9.addWidget(self.graphWidget_solo_channel_4, 0, 0, 1, 1)

        self.frame_16 = QFrame(self.page)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMaximumSize(QSize(50, 16777215))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pushButton_10 = QPushButton(self.frame_16)
        self.pushButton_10.setObjectName(u"pushButton_10")
        sizePolicy3.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy3)

        self.horizontalLayout_5.addWidget(self.pushButton_10)


        self.gridLayout_9.addWidget(self.frame_16, 0, 1, 1, 1)

        self.stackedWidget_Laumas.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_8 = QGridLayout(self.page_2)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(2, 2, 2, 2)
        self.graphWidget_solo_channel_3 = PlotWidget(self.page_2)
        self.graphWidget_solo_channel_3.setObjectName(u"graphWidget_solo_channel_3")
        sizePolicy3.setHeightForWidth(self.graphWidget_solo_channel_3.sizePolicy().hasHeightForWidth())
        self.graphWidget_solo_channel_3.setSizePolicy(sizePolicy3)
        self.graphWidget_solo_channel_3.setStyleSheet(u"background-color: rgb(26, 49, 255);")

        self.gridLayout_8.addWidget(self.graphWidget_solo_channel_3, 0, 0, 1, 1)

        self.frame_15 = QFrame(self.page_2)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(50, 16777215))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton_9 = QPushButton(self.frame_15)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy3.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy3)

        self.horizontalLayout_4.addWidget(self.pushButton_9)


        self.gridLayout_8.addWidget(self.frame_15, 0, 1, 1, 1)

        self.stackedWidget_Laumas.addWidget(self.page_2)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.gridLayout_6 = QGridLayout(self.page_8)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(2, 2, 2, 2)
        self.graphWidget_solo_channel_2 = PlotWidget(self.page_8)
        self.graphWidget_solo_channel_2.setObjectName(u"graphWidget_solo_channel_2")
        sizePolicy3.setHeightForWidth(self.graphWidget_solo_channel_2.sizePolicy().hasHeightForWidth())
        self.graphWidget_solo_channel_2.setSizePolicy(sizePolicy3)
        self.graphWidget_solo_channel_2.setStyleSheet(u"background-color: rgb(26, 49, 255);")

        self.gridLayout_6.addWidget(self.graphWidget_solo_channel_2, 0, 0, 1, 1)

        self.frame_13 = QFrame(self.page_8)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(50, 16777215))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton_8 = QPushButton(self.frame_13)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy3.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy3)

        self.horizontalLayout_3.addWidget(self.pushButton_8)


        self.gridLayout_6.addWidget(self.frame_13, 0, 1, 1, 1)

        self.stackedWidget_Laumas.addWidget(self.page_8)

        self.verticalLayout.addWidget(self.stackedWidget_Laumas)


        self.gridLayout.addWidget(self.frame_5, 1, 0, 1, 1)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy6)
        self.frame_4.setMinimumSize(QSize(0, 50))
        self.frame_4.setMaximumSize(QSize(16777215, 16777215))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_4, 2, 0, 1, 1)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy6.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy6)
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

        self.horizontalLayout.addWidget(self.frame_2)


        self.gridLayout_2.addWidget(self.gridWidget, 0, 0, 1, 1)

        GraphWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(GraphWindow)

        QMetaObject.connectSlotsByName(GraphWindow)
    # setupUi

    def retranslateUi(self, GraphWindow):
        GraphWindow.setWindowTitle(QCoreApplication.translate("GraphWindow", u"MainWindow", None))
        self.pushButton_3.setText(QCoreApplication.translate("GraphWindow", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("GraphWindow", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("GraphWindow", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("GraphWindow", u"PushButton", None))
        self.pushButton_7.setText(QCoreApplication.translate("GraphWindow", u"PushButton", None))
        self.pushButton_6.setText(QCoreApplication.translate("GraphWindow", u"PushButton", None))
        self.pushButton.setText(QCoreApplication.translate("GraphWindow", u"PushButton", None))
        self.pushButton_10.setText(QCoreApplication.translate("GraphWindow", u"PushButton", None))
        self.pushButton_9.setText(QCoreApplication.translate("GraphWindow", u"PushButton", None))
        self.pushButton_8.setText(QCoreApplication.translate("GraphWindow", u"PushButton", None))
    # retranslateUi

