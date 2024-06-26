
from __future__ import annotations
from typing import TYPE_CHECKING
from PySide6.QtWidgets import QMainWindow, QGraphicsView, QGraphicsScene, QGraphicsItem, QApplication
from PySide6.QtCore import QTimer
import  PySide6.QtCore
from Mainwindow_grafico_ui import Ui_GraphWindow
import pyqtgraph as pg
import sys
from time import sleep
from random import randint

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
        
        hour2 = [2,4,6,8,10,12,14,16,18,20]
        hour = [1,2,3,4,5,6,7,8,9,10]
        temperature2 = [80,81,87,83,85,86,89,91,92,90]
        temperature = [30,32,34,32,33,31,29,32,35,45]
        self.x = list(range(50))  # 100 time points
        self.y = [randint(0,50) for _ in range(50)]  # 100 data points
        self.ui.graphWidget.setBackground('k')
        
        pen = pg.mkPen(color=(255, 0, 0), width=1, style=PySide6.QtCore.Qt.SolidLine)
        self.ui.graphWidget.setTitle("Graph 1", color="b", size="30pt")
        
        self.my_line = self.ui.graphWidget.plot(self.x, self.y, pen=pen)
        # self.ui.graphWidget.plot(hour2, temperature2, pen=pen)
        
        self.timer = QTimer()
        self.timer.setInterval(30)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()
        
        # styles = {'color':'r', 'font-size':'20px'}
        self.ui.graphWidget.setLabel('left', 'Temperature (°C)')
        self.ui.graphWidget.setLabel('bottom', 'Hour (H)')
        
        
    def update_plot_data(self):
        self.x = self.x[1:]  # Remove the first y element.
        self.x.append(self.x[-1] + 1)  # Add a new value 1 higher than the last.
        self.y = self.y[1:]  # Remove the first
        self.y.append( randint(0,50))  # Add a new random value.
        self.my_line.setData(self.x, self.y)  # Update the data.
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = GraphWindow(banco_di_taratura=0)
    w.show()
    app.exec()