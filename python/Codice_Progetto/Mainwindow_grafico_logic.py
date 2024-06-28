
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

        self.logger = banco_di_taratura.logger
        self.controller_TCP = banco_di_taratura.controller_tcp
        self.controller_MODBUS = banco_di_taratura.controller_modbus
        self.result_media_passato = 0

        
        # # segnale di refresh       
        self.timer = QTimer()
        self.timer.setInterval(20)
        # self.timer.timeout.connect(self.update_plot_CH2)
        self.timer.timeout.connect(self.update2)
        self.timer.start()

        # axis descriptions
        self.ui.graphWidget_solo_channel.setLabel('left', "<span style=\"color:red;font-size:10px\">Voltage (mV)</span>")
        self.ui.graphWidget_solo_channel.setLabel('bottom', "<span style=\"color:red;font-size:10px\">Samples (samples)</span>")
        
        
        
        # 2) Allow data to accumulate. In these examples, the array doubles in length
        #    whenever it is full. 
        pen2 = pg.mkPen(color=('g'), width=1, style=PySide6.QtCore.Qt.SolidLine)
        
        self.p4 = self.ui.graphWidget_solo_channel.plot( pen=pen2, name='Sensor 2')
        self.ui.graphWidget_solo_channel.setDownsampling(mode='peak')
        self.ui.graphWidget_solo_channel.setClipToView(True)
        self.ui.graphWidget_solo_channel.setLimits(xMin=-100)
        self.curve4 = self.ui.graphWidget_solo_channel.plot()
        self.data3 = [None] * 100
        self.ptr3 = 0


    def media_esponenziale(self):
       x=self.controller_TCP.DATA.LIST_Nm_VALUE[1]
       alpha=0.8
       result_media=alpha*x + (1-alpha)*self.result_media_passato
       self.result_media_passato = result_media
       return result_media 
        

    def update2(self):
        
        # Append new random value to data list
        self.data3[self.ptr3] = self.media_esponenziale()
        self.ptr3 += 1

        # Double the size of data list if ptr3 exceeds current size
        if self.ptr3 >= len(self.data3):
            self.data3.extend([None] * len(self.data3))
        
        # Update plot data
        self.curve4.setData(self.data3[:self.ptr3])  
        print(sys.getsizeof(self.data3))

            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = GraphWindow(banco_di_taratura=None)
    w.show()
    app.exec()