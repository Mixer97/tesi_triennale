
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
import time
import sys

if TYPE_CHECKING:
    from Banco_Taratura import BANCO_DI_TARATURA


class Graph:
    def __init__(self, GraphWindow:GraphWindow, graph, channel, title):
        
        self.channel = channel
        self.graph = graph
        self.title = title
        self.recent_values = []  # List to store recent values
        # self.time_window = 1  # seconds for the moving average window
        self.result_media_passato = 1
        self.update_period = 15
        self.GraphWindow = GraphWindow
        self.time_window = 5  # In secondi
        self.alpha = 0.02
        
        # segnale di refresh       
        self.timer = QTimer()
        self.timer.setInterval(self.update_period)
        self.timer.timeout.connect(self.update_someData)
        self.timer.start()
        
        self.GraphWindow.ui.lineEdit_time_window.editingFinished.connect(self.change_time_window)

        # axis descriptions
        self.graph.setContentsMargins(10, 10, 10, 10)
        self.axisX_desc = "Voltage (mV)"
        self.axisY_desc = "Time (s)"
        self.graph.setLabel('right', self.axisX_desc)
        self.graph.setLabel('bottom', self.axisY_desc)
        
        # Impostazione del grafico
        self.pen1 = pg.mkPen(color=('g'), width=1, style=PySide6.QtCore.Qt.SolidLine)
        self.graph.setDownsampling(mode='peak')
        self.graph.setClipToView(True)
        self.graph.setLimits(xMin=-100)
        self.graph.setLimits(yMin=-1000)
        self.graph.setLimits(yMax=1000)
        self.curve4 = self.graph.plot(pen=self.pen1)
        self.dataY = []
        self.dataX = []
        self.ptr3 = 0
        self.counter = 0
        self.graph.setRange(yRange=(-5,5), padding=0.2)
        self.graph.setTitle(self.title)
    
    def change_time_window(self):
        time_inserted = int(self.GraphWindow.ui.lineEdit_time_window.text())
        self.time_window = time_inserted
        self.graph.setRange(xRange=(-self.time_window/2, +self.time_window/2))

    def media_esponenziale(self):
        x=self.get_data()
        true_alpha = self.alpha*self.update_period
        result_media=true_alpha*x + (1-true_alpha)*self.result_media_passato
        self.result_media_passato = result_media
        return result_media 
    
    def get_data(self):
        if self.channel == 'ch1':
            data = self.elaborate_data_ch1()
        elif self.channel == 'ch2':
            data = self.elaborate_data_ch2()
        elif self.channel == 'ch3':
            data = self.elaborate_data_ch3()
        elif self.channel == 'ch4':
            data = self.elaborate_data_ch4()
        elif self.channel == 'main':
            data = self.elaborate_data_main()
        elif self.channel == 'temp':    
            data = self.GraphWindow.banco_di_taratura.controller_modbus.DATA.canale_temperatura_mV
        else:
            data = None
        return data

    def elaborate_data_ch1(self):
        if self.GraphWindow.banco_di_taratura.logger.DATA.text_lcd[0] == 'mV':
            data = self.GraphWindow.banco_di_taratura.controller_tcp.DATA.LIST_mV_VALUE[0]
        elif self.GraphWindow.banco_di_taratura.logger.DATA.text_lcd[0] == 'Kg':
            data = self.GraphWindow.banco_di_taratura.controller_tcp.DATA.LIST_Kg_VALUE[0]
        elif self.GraphWindow.banco_di_taratura.logger.DATA.text_lcd[0] == 'N':
            data = self.GraphWindow.banco_di_taratura.controller_tcp.DATA.LIST_N_VALUE[0]
        elif self.GraphWindow.banco_di_taratura.logger.DATA.text_lcd[0] == 'Nm':
            data = self.GraphWindow.banco_di_taratura.controller_tcp.DATA.LIST_Nm_VALUE[0]
        else:
            data = None
        return data

    def elaborate_data_ch2(self):
        if self.GraphWindow.banco_di_taratura.logger.DATA.text_lcd[1] == 'mV':
            data = self.GraphWindow.banco_di_taratura.controller_tcp.DATA.LIST_mV_VALUE[1]
        elif self.GraphWindow.banco_di_taratura.logger.DATA.text_lcd[1] == 'Kg':
            data = self.GraphWindow.banco_di_taratura.controller_tcp.DATA.LIST_Kg_VALUE[1]
        elif self.GraphWindow.banco_di_taratura.logger.DATA.text_lcd[1] == 'N':
            data = self.GraphWindow.banco_di_taratura.controller_tcp.DATA.LIST_N_VALUE[1]
        elif self.GraphWindow.banco_di_taratura.logger.DATA.text_lcd[1] == 'Nm':
            data = self.GraphWindow.banco_di_taratura.controller_tcp.DATA.LIST_Nm_VALUE[1]
        else:
            data = None
        return data

    def elaborate_data_ch3(self):
        if self.GraphWindow.banco_di_taratura.logger.DATA.text_lcd[2] == 'mV':
            data = self.GraphWindow.banco_di_taratura.controller_tcp.DATA.LIST_mV_VALUE[2]
        elif self.GraphWindow.banco_di_taratura.logger.DATA.text_lcd[2] == 'Kg':
            data = self.GraphWindow.banco_di_taratura.controller_tcp.DATA.LIST_Kg_VALUE[2]
        elif self.GraphWindow.banco_di_taratura.logger.DATA.text_lcd[2] == 'N':
            data = self.GraphWindow.banco_di_taratura.controller_tcp.DATA.LIST_N_VALUE[2]
        elif self.GraphWindow.banco_di_taratura.logger.DATA.text_lcd[2] == 'Nm':
            data = self.GraphWindow.banco_di_taratura.controller_tcp.DATA.LIST_Nm_VALUE[2]
        else:
            data = None
        return data

    def elaborate_data_ch4(self):
        if self.GraphWindow.banco_di_taratura.logger.DATA.text_lcd[3] == 'mV':
            data = self.GraphWindow.banco_di_taratura.controller_tcp.DATA.LIST_mV_VALUE[3]
        elif self.GraphWindow.banco_di_taratura.logger.DATA.text_lcd[3] == 'Kg':
            data = self.GraphWindow.banco_di_taratura.controller_tcp.DATA.LIST_Kg_VALUE[3]
        elif self.GraphWindow.banco_di_taratura.logger.DATA.text_lcd[3] == 'N':
            data = self.GraphWindow.banco_di_taratura.controller_tcp.DATA.LIST_N_VALUE[3]
        elif self.GraphWindow.banco_di_taratura.logger.DATA.text_lcd[3] == 'Nm':
            data = self.GraphWindow.banco_di_taratura.controller_tcp.DATA.LIST_Nm_VALUE[3]
        else:
            data = None
        return data

    def elaborate_data_main(self):
        if self.GraphWindow.banco_di_taratura.logger.DATA.text_lcd_SG600_main_temp[0] == 'mV':
            data = self.GraphWindow.banco_di_taratura.controller_modbus.DATA.canale_principale_mV
        elif self.GraphWindow.banco_di_taratura.logger.DATA.text_lcd_SG600_main_temp[0] == 'Kg':
            data = self.GraphWindow.banco_di_taratura.controller_modbus.DATA.canale_principale_Kg
        elif self.GraphWindow.banco_di_taratura.logger.DATA.text_lcd_SG600_main_temp[0] == 'N':
            data = self.GraphWindow.banco_di_taratura.controller_modbus.DATA.canale_principale_N
        elif self.GraphWindow.banco_di_taratura.logger.DATA.text_lcd_SG600_main_temp[0] == 'Nm':
            data = self.GraphWindow.banco_di_taratura.controller_modbus.DATA.canale_principale_Nm
        else:
            data = None
        return data

    def update_fullData(self):
        
        # Append new random value to data list
        # self.dataY[self.ptr3] = self.media_temporale(data=self.controller_TCP.DATA.LIST_Nm_VALUE[1], recent_values=self.recent_values)
        self.dataY[self.ptr3] = self.media_esponenziale()
        self.dataX[self.ptr3] = time.time() - self.GraphWindow.start_time
        self.ptr3 += 1

        # Double the size of data list if ptr3 exceeds current size
        if self.ptr3 >= len(self.dataY):
            self.dataY.extend([None] * len(self.dataY))
            self.dataX.extend([None] * len(self.dataX))
        
        # Update plot data
        self.curve4.setData(self.dataX[:self.ptr3], self.dataY[:self.ptr3])  
        print(sys.getsizeof(self.dataY))

    def update_someData(self):
        
        # Append new random value to data list
        self.dataY.append(self.media_esponenziale())
        actual_time = time.time()
        difference = actual_time - self.GraphWindow.start_time
        self.dataX.append(difference)

        # Update pointer
        self.counter = self.counter + 1
        if difference > self.time_window:
            self.dataX.pop(0)
            self.dataY.pop(0)
            self.counter = self.counter - 1 # pointer back to max range

        # Update plot data
        self.curve4.setData(self.dataX, self.dataY)
        
        


class GraphWindow(QMainWindow):
    def __init__(self, banco_di_taratura:BANCO_DI_TARATURA):
        super().__init__()
        self.banco_di_taratura = banco_di_taratura
        # Create an instance of the generated UI class
        self.ui = Ui_GraphWindow()
        # Setup the user interface
        self.ui.setupUi(self)
        self.start_time = time.time()
        
        # grafici disponibili
        graph_main = self.ui.graphWidget_SG600_main
        graph_temp = self.ui.graphWidget_SG600_temp
        graph_soloTemp = self.ui.graphWidget_SG600_solo_temp
        graph_soloMain = self.ui.graphWidget_SG600_solo_main
        graph_ch1 = self.ui.graphWidget_solo_channel_1
        graph_ch2 = self.ui.graphWidget_solo_channel_2
        graph_ch3 = self.ui.graphWidget_solo_channel_3
        graph_ch4 = self.ui.graphWidget_solo_channel_4
        
        # data dispolibili
        channel_ch1 = 'ch1'
        channel_ch2 = 'ch2'
        channel_ch3 = 'ch3'
        channel_ch4 = 'ch4'
        channel_main_ch = 'main'
        channel_temp_ch = 'temp'

        self.logger = banco_di_taratura.logger
        self.controller_TCP = banco_di_taratura.controller_tcp
        self.controller_MODBUS = banco_di_taratura.controller_modbus
        
        self.graph_main = Graph(self, graph=graph_main, channel=channel_main_ch, title='Main')
        self.graph_soloMain = Graph(self, graph=graph_soloMain, channel=channel_main_ch, title='Main')
        self.graph_temp = Graph(self, graph=graph_temp, channel=channel_temp_ch, title='Temp')
        self.graph_soloTemp = Graph(self, graph=graph_soloTemp, channel=channel_temp_ch, title='Temp')
        
        self.graph_ch1 = Graph(self, graph=graph_ch1, channel=channel_ch1, title='CH1')
        self.graph_ch2 = Graph(self, graph=graph_ch2, channel=channel_ch2, title='CH2')
        self.graph_ch3 = Graph(self, graph=graph_ch3, channel=channel_ch3, title='CH3')
        self.graph_ch4 = Graph(self, graph=graph_ch4, channel=channel_ch4, title='CH4')
        
        # Setup segnali
        self.ui.comboBox_Main_Temp.activated.connect(self.ui.stackedWidget_SG600.setCurrentIndex)
        self.ui.comboBox_Ch_1234.activated.connect(self.ui.stackedWidget_Laumas.setCurrentIndex)
        
        self.ui.pushButton_autorange_ch1.clicked.connect(self.ui.graphWidget_solo_channel_1.getPlotItem().getViewBox().autoRange)
            
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = GraphWindow(banco_di_taratura=None)
    w.show()
    app.exec()