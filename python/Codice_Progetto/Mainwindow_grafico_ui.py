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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QSizePolicy, QWidget)

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
        self.gridLayout_6 = QGridLayout(self.gridWidget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.graphWidget = PlotWidget(self.gridWidget)
        self.graphWidget.setObjectName(u"graphWidget")

        self.gridLayout_3.addWidget(self.graphWidget, 0, 0, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_3, 0, 0, 1, 2)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")

        self.gridLayout_6.addLayout(self.gridLayout_5, 1, 1, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label = QLabel(self.gridWidget)
        self.label.setObjectName(u"label")

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1, Qt.AlignHCenter)


        self.gridLayout_6.addLayout(self.gridLayout_4, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.gridWidget, 0, 0, 1, 1)

        GraphWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(GraphWindow)

        QMetaObject.connectSlotsByName(GraphWindow)
    # setupUi

    def retranslateUi(self, GraphWindow):
        GraphWindow.setWindowTitle(QCoreApplication.translate("GraphWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("GraphWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">TextLabel</span></p></body></html>", None))
    # retranslateUi

