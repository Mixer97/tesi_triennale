
from __future__ import annotations
from typing import TYPE_CHECKING
from PySide6.QtWidgets import QMainWindow, QGraphicsView, QGraphicsScene, QGraphicsItem, QApplication
from PySide6.QtCore import QTimer
import  PySide6.QtCore
from Mainwindow_grafico_ui import Ui_GraphWindow
import pyqtgraph as pg
import sys
from time import sleep
from random import randint, random
import math

if TYPE_CHECKING:
    from Banco_Taratura import BANCO_DI_TARATURA



class GraphWindow(QMainWindow):
    def __init__(self, banco_di_taratura:BANCO_DI_TARATURA):
        super().__init__()
        self.banco_di_taratura = banco_di_taratura
        # Create an instance of the generated UI class
        self.ui = Ui_GraphWindow()
        # Setup the user interface
        self.ui.setupUi(self)

        self.x1 = [0]
        self.y1 = [0]
        self.x2 = [0]
        self.y2 = [0]
        self.y3 = [0]
        self.x3 = [0]
        self.x4 = [0]
        self.y4 = [0]
        
        self.ui.graphWidget_4.setBackground('k')
        
        pen1 = pg.mkPen(color=(255, 0, 0), width=1, style=PySide6.QtCore.Qt.SolidLine)
        pen2 = pg.mkPen(color=(0, 0, 255), width=1, style=PySide6.QtCore.Qt.SolidLine)
        pen3 = pg.mkPen(color=(255, 0, 0), width=1, style=PySide6.QtCore.Qt.SolidLine)
        pen4 = pg.mkPen(color=(0, 0, 255), width=1, style=PySide6.QtCore.Qt.SolidLine)

        # self.ui.graphWidget_4.setTitle("Graph 1", color="b", size="30pt")
        
        self.my_line = self.ui.graphWidget_4.plot(self.x1, self.y1, pen=pen1, name='Sensor 1')
        self.my_line_2 = self.ui.graphWidget_4.plot(self.x2, self.y2, pen=pen2, name='Sensor 2')
        self.my_line_3 = self.ui.graphWidget_main.plot(self.x3, self.y3, pen=pen3, name='Sensor 3')
        self.my_line_4 = self.ui.graphWidget_main.plot(self.x4, self.y4, pen=pen4, name='Sensor 4')
        
        # segnale di refresh       
        self.timer = QTimer()
        self.timer.setInterval(20)
        self.timer.timeout.connect(self.update_plot_data_MY_LINE)
        self.timer.timeout.connect(self.update_plot_data_MY_LINE_2)
        self.timer.timeout.connect(self.update_plot_data_MY_LINE_3)
        self.timer.timeout.connect(self.update_plot_data_MY_LINE_4)
        self.timer.start()
        
        # axis descriptions
        self.ui.graphWidget_4.setLabel('left', "<span style=\"color:red;font-size:10px\">Temperature (°C)</span>")
        self.ui.graphWidget_4.setLabel('bottom', "<span style=\"color:red;font-size:10px\">Hour (H)</span>")
        
        self.ui.graphWidget_4.addLegend()
        
        # Locking axis
        # self.ui.graphWidget_4.setXRange(5, 20, padding=0)
        # self.ui.graphWidget_4.setYRange(30, 40, padding=0)
        self.ui.graphWidget_4.enableAutoRange()
        self.ui.graphWidget_main.enableAutoRange()
        self.ui.graphWidget_temp.enableAutoRange()
        
        
        
    def update_plot_data_MY_LINE(self):
        self.x1.append(self.x1[-1] + 1)  # Add a new value 1 higher than the last.
        self.y1.append(40*math.sin(0.05*self.x1[-1]))  # Add a new random value.
        self.my_line.setData(self.x1, self.y1)  # Update the data.
        
    def update_plot_data_MY_LINE_2(self):
        self.x2.append(self.x2[-1] + 1)  # Add a new value 1 higher than the last.
        self.y2.append(100*math.sin(0.20*self.x2[-1]))  # Add a new random value.
        self.my_line_2.setData(self.x2, self.y2)  # Update the data.     

    def update_plot_data_MY_LINE_3(self):
        self.x3.append(self.x1[-1])  # Add a new value 1 higher than the last.
        self.y3.append(self.y1[-1])  # Add a new random value.
        self.my_line_3.setData(self.x3, self.y3)  # Update the data.
        
    def update_plot_data_MY_LINE_4(self):
        self.x4.append(self.x2[-1])  # Add a new value 1 higher than the last.
        self.y4.append(self.y2[-1])  # Add a new random value.
        self.my_line_4.setData(self.x4, self.y4)  # Update the data.
              
    def plot_graphWidget_4(self, x, y, plotname, color):
        pen = pg.mkPen(color=color)
        self.ui.graphWidget_4.plot(x, y, name=plotname, pen=pen, symbol='+', symbolSize=30, symbolBrush=(color))
        
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = GraphWindow(banco_di_taratura=None)
    w.show()
    app.exec()