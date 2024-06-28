
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
import time
import sys

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
        self.start_time = time.time()
        
        self.recent_values = []  # List to store recent values
        self.time_window = 1  # seconds for the moving average window

        self.logger = banco_di_taratura.logger
        self.controller_TCP = banco_di_taratura.controller_tcp
        self.controller_MODBUS = banco_di_taratura.controller_modbus
        self.result_media_passato = 1
        self.update_period = 5

        
        # # segnale di refresh       
        self.timer = QTimer()
        self.timer.setInterval(self.update_period)
        # self.timer.timeout.connect(self.update_plot_CH2)
        self.timer.timeout.connect(self.update2)
        self.timer.start()

        # axis descriptions
        self.ui.graphWidget_solo_channel.setLabel('left', "<span style=\"color:red;font-size:10px\">Voltage (mV)</span>")
        self.ui.graphWidget_solo_channel.setLabel('bottom', "<span style=\"color:red;font-size:10px\">Time (s)</span>")
        
        
        
        # 2) Allow data to accumulate. In these examples, the array doubles in length
        #    whenever it is full. 
        pen2 = pg.mkPen(color=('g'), width=1, style=PySide6.QtCore.Qt.SolidLine)
        
        self.ui.graphWidget_solo_channel.setRange()
        self.p4 = self.ui.graphWidget_solo_channel.plot( pen=pen2, name='Sensor 2')
        self.ui.graphWidget_solo_channel.setDownsampling(mode='peak')
        self.ui.graphWidget_solo_channel.setClipToView(True)
        self.ui.graphWidget_solo_channel.setLimits(xMin=-100)
        self.curve4 = self.ui.graphWidget_solo_channel.plot()
        self.dataY = [None] * 100
        self.dataX = [None] * 100
        self.ptr3 = 0


    def media_esponenziale(self):
        x=self.controller_TCP.DATA.LIST_Nm_VALUE[1]
        while x==0:
            x=self.controller_TCP.DATA.LIST_Nm_VALUE[1]
        alpha=0.10
        true_alpha = alpha*self.update_period
        result_media=true_alpha*x + (1-true_alpha)*self.result_media_passato
        self.result_media_passato = result_media
        return result_media 
   
    def media_temporale(self, data, recent_values):
        current_time = time.time()
        # Append new value and timestamp to recent_values
        recent_values.append((current_time, data))

        # Remove values older than the time window
        recent_values = [(t, val) for t, val in recent_values if current_time - t <= self.time_window]

        # Calculate the average of the remaining values
        if recent_values:
            return sum(val for t, val in recent_values) / len(recent_values)
        else:
            return 0
        

    def update2(self):
        
        # Append new random value to data list
        # self.dataY[self.ptr3] = self.media_temporale(data=self.controller_TCP.DATA.LIST_Nm_VALUE[1], recent_values=self.recent_values)
        self.dataY[self.ptr3] = self.media_esponenziale()
        self.dataX[self.ptr3] = time.time() - self.start_time
        self.ptr3 += 1

        # Double the size of data list if ptr3 exceeds current size
        if self.ptr3 >= len(self.dataY):
            self.dataY.extend([None] * len(self.dataY))
            self.dataX.extend([None] * len(self.dataX))
        
        # Update plot data
        self.curve4.setData(self.dataX[:self.ptr3], self.dataY[:self.ptr3])  
        print(sys.getsizeof(self.dataY))

            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = GraphWindow(banco_di_taratura=None)
    w.show()
    app.exec()