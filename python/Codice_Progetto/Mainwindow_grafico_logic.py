
from __future__ import annotations
from typing import TYPE_CHECKING
from PySide6.QtWidgets import QMainWindow, QGraphicsView, QGraphicsScene, QGraphicsItem, QApplication
from PySide6.QtCore import QSize
from PySide6.QtCore import QTimer
import  PySide6.QtCore
from Mainwindow_grafico_ui import Ui_GraphWindow
import pyqtgraph as pg
from pyqtgraph import PlotWidget
import sys
from time import sleep
from random import randint, random
import time
import sys

if TYPE_CHECKING:
    from Banco_Taratura import BANCO_DI_TARATURA
    from View_QT_HomePage_logic import MainWindow


class Graph:
    def __init__(self, GraphWindow:GraphWindow, graph:PlotWidget, channel, title, start_time):
        
        self.channel = channel
        self.graph = graph
        self.title = title
        self.start_time = start_time    # Inizio tempo del grafico 
        self.recent_values = []  # List to store recent values
        # self.time_window = 1  # seconds for the moving average window
        self.result_media_passato = 1
        self.update_period = 15    # ogni quanti ms prende un campione per il grafico
        self.GraphWindow = GraphWindow
        self.time_window = 5  # In secondi (tempo sull asse delle y)
        self.media_window = 0.5 # In secondi (tempo sul quale fa la media mobile)
        self.alpha = 0.005 # coefficiente per media esponenziale
        self.autorange_status = False  # status del grafico riguardante autorange
        self.buffer = [0]
        
        # segnale di refresh       
        self.timer = QTimer()
        self.timer.setInterval(self.update_period)
        self.timer.timeout.connect(self.update_someData)
        self.timer.timeout.connect(self.autorange)
        self.timer.start()
        
        # Segnale di update dell'asse x
        self.GraphWindow.ui.lineEdit_time_window.editingFinished.connect(self.change_time_window)

        # axis descriptions
        # self.graph.setContentsMargins(100, 100, 100, 100)
        self.axisX_desc = "Voltage (mV)"
        self.axisY_desc = "Time (s)"
        self.graph.setLabel('right', self.axisX_desc)
        self.graph.setLabel('bottom', self.axisY_desc)
        
        # Impostazione del grafico
        self.pen1 = pg.mkPen(color=('r'), width=1, style=PySide6.QtCore.Qt.SolidLine)
        self.graph.setDownsampling(mode='peak')
        self.graph.setClipToView(True)
        self.graph.setLimits(xMin=-100)
        self.graph.setLimits(yMin=-10000)
        self.graph.setLimits(yMax=10000)
        self.curve4 = self.graph.plot(pen=self.pen1)
        self.dataY = []
        self.dataX = []
        self.ptr3 = 0
        self.counter = 0
        self.graph.setRange(yRange=(-5,5), padding=0.2)
        self.graph.setTitle(self.title) 
                
        
    def reset_grafico(self): 
        
        # reset del timer
        self.start_time = time.time()
        
        # Impostazione del grafico
        self.dataY = []
        self.dataX = []
        self.ptr3 = 0
        self.counter = 0 
    
    def autorange(self):
        if self.autorange_status:
            self.graph.getPlotItem().getViewBox().autoRange()
    
    def change_status_autorange(self):
        self.autorange_status = not(self.autorange_status)
    
    def change_time_window(self):
        time_inserted = int(self.GraphWindow.ui.lineEdit_time_window.text())
        if time_inserted>0 or time_inserted<1000:
            self.time_window = time_inserted
        else:
            self.time_window = 10
        self.graph.setRange(xRange=(self.dataX[0], self.dataX[0]+self.time_window))


    def media_esponenziale(self):
        x=self.get_data()
        true_alpha = self.alpha*self.update_period
        result_media = true_alpha*x + (1-true_alpha)*self.result_media_passato
        self.result_media_passato = result_media
        return result_media 
    
    def media_mobile(self):
        x=self.get_data()
        self.buffer.append(x)
        update_period_seconds = self.update_period / 1000
        numero_di_campioni_nel_buffer = self.media_window / update_period_seconds
        while len(self.buffer) > numero_di_campioni_nel_buffer:
            self.buffer.pop(0)
        value = 0
        for i in self.buffer:
            value = value + i
        media_value = value/len(self.buffer)
        return media_value
            
        
    
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
            self.axisX_desc = "Voltage (mV)"
            self.graph.setLabel('right', self.axisX_desc)
        elif self.GraphWindow.banco_di_taratura.logger.DATA.text_lcd[0] == 'Kg':
            data = self.GraphWindow.banco_di_taratura.controller_tcp.DATA.LIST_Kg_VALUE[0]
            self.axisX_desc = "Kilogrammi (Kg)"
            self.graph.setLabel('right', self.axisX_desc)
        elif self.GraphWindow.banco_di_taratura.logger.DATA.text_lcd[0] == 'N':
            data = self.GraphWindow.banco_di_taratura.controller_tcp.DATA.LIST_N_VALUE[0]
            self.axisX_desc = "Newton (N)"
            self.graph.setLabel('right', self.axisX_desc)
        elif self.GraphWindow.banco_di_taratura.logger.DATA.text_lcd[0] == 'Nm':
            data = self.GraphWindow.banco_di_taratura.controller_tcp.DATA.LIST_Nm_VALUE[0]
            self.axisX_desc = "Newton metri (Nm)"
            self.graph.setLabel('right', self.axisX_desc)
        else:
            data = None
        return data

    def elaborate_data_ch2(self):
        if self.GraphWindow.banco_di_taratura.logger.DATA.text_lcd[1] == 'mV':
            data = self.GraphWindow.banco_di_taratura.controller_tcp.DATA.LIST_mV_VALUE[1]
            self.axisX_desc = "Voltage (mV)"
            self.graph.setLabel('right', self.axisX_desc)
        elif self.GraphWindow.banco_di_taratura.logger.DATA.text_lcd[1] == 'Kg':
            data = self.GraphWindow.banco_di_taratura.controller_tcp.DATA.LIST_Kg_VALUE[1]
            self.axisX_desc = "Kilogrammi (Kg)"
            self.graph.setLabel('right', self.axisX_desc)
        elif self.GraphWindow.banco_di_taratura.logger.DATA.text_lcd[1] == 'N':
            data = self.GraphWindow.banco_di_taratura.controller_tcp.DATA.LIST_N_VALUE[1]
            self.axisX_desc = "Newton (N)"
            self.graph.setLabel('right', self.axisX_desc)
        elif self.GraphWindow.banco_di_taratura.logger.DATA.text_lcd[1] == 'Nm':
            data = self.GraphWindow.banco_di_taratura.controller_tcp.DATA.LIST_Nm_VALUE[1]
            self.axisX_desc = "Newton metri (Nm)"
            self.graph.setLabel('right', self.axisX_desc)
        else:
            data = None
        return data

    def elaborate_data_ch3(self):
        if self.GraphWindow.banco_di_taratura.logger.DATA.text_lcd[2] == 'mV':
            data = self.GraphWindow.banco_di_taratura.controller_tcp.DATA.LIST_mV_VALUE[2]
            self.axisX_desc = "Voltage (mV)"
            self.graph.setLabel('right', self.axisX_desc)
        elif self.GraphWindow.banco_di_taratura.logger.DATA.text_lcd[2] == 'Kg':
            data = self.GraphWindow.banco_di_taratura.controller_tcp.DATA.LIST_Kg_VALUE[2]
            self.axisX_desc = "Kilogrammi (Kg)"
            self.graph.setLabel('right', self.axisX_desc)
        elif self.GraphWindow.banco_di_taratura.logger.DATA.text_lcd[2] == 'N':
            data = self.GraphWindow.banco_di_taratura.controller_tcp.DATA.LIST_N_VALUE[2]
            self.axisX_desc = "Newton (N)"
            self.graph.setLabel('right', self.axisX_desc)
        elif self.GraphWindow.banco_di_taratura.logger.DATA.text_lcd[2] == 'Nm':
            data = self.GraphWindow.banco_di_taratura.controller_tcp.DATA.LIST_Nm_VALUE[2]
            self.axisX_desc = "Newton metri (Nm)"
            self.graph.setLabel('right', self.axisX_desc)
        else:
            data = None
        return data

    def elaborate_data_ch4(self):
        if self.GraphWindow.banco_di_taratura.logger.DATA.text_lcd[3] == 'mV':
            data = self.GraphWindow.banco_di_taratura.controller_tcp.DATA.LIST_mV_VALUE[3]
            self.axisX_desc = "Voltage (mV)"
            self.graph.setLabel('right', self.axisX_desc)
        elif self.GraphWindow.banco_di_taratura.logger.DATA.text_lcd[3] == 'Kg':
            data = self.GraphWindow.banco_di_taratura.controller_tcp.DATA.LIST_Kg_VALUE[3]
            self.axisX_desc = "Kilogrammi (Kg)"
            self.graph.setLabel('right', self.axisX_desc)
        elif self.GraphWindow.banco_di_taratura.logger.DATA.text_lcd[3] == 'N':
            data = self.GraphWindow.banco_di_taratura.controller_tcp.DATA.LIST_N_VALUE[3]
            self.axisX_desc = "Newton (N)"
            self.graph.setLabel('right', self.axisX_desc)
        elif self.GraphWindow.banco_di_taratura.logger.DATA.text_lcd[3] == 'Nm':
            data = self.GraphWindow.banco_di_taratura.controller_tcp.DATA.LIST_Nm_VALUE[3]
            self.axisX_desc = "Newton metri (Nm)"
            self.graph.setLabel('right', self.axisX_desc)
        else:
            data = None
        return data

    def elaborate_data_main(self):
        if self.GraphWindow.banco_di_taratura.logger.DATA.text_lcd_SG600_main_temp[0] == 'mV':
            data = self.GraphWindow.banco_di_taratura.controller_modbus.DATA.canale_principale_mV
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
        # self.dataY.append(self.media_esponenziale())
        self.dataY.append(self.media_mobile())
        actual_time = time.time()
        difference = actual_time - self.start_time
        self.dataX.append(difference)

        # Update pointer
        self.counter = self.counter + 1
        while self.dataX[0] < difference - self.time_window:
            self.dataX.pop(0)
            self.dataY.pop(0)
            self.counter = self.counter - 1 # pointer back to max range

        # Update plot data
        self.curve4.setData(self.dataX, self.dataY)
        


class GraphWindow(QMainWindow):
    def __init__(self, banco_di_taratura:BANCO_DI_TARATURA, homepage:MainWindow):
        super().__init__()
        self.banco_di_taratura = banco_di_taratura
        # Create an instance of the generated UI class
        self.ui = Ui_GraphWindow()
        # Setup the user interface
        self.ui.setupUi(self)
        self.start_time = time.time()
        self.homepage = homepage
        
        # grafici disponibili
        graph_main_and_channel = self.ui.graphWidget_SG600_main_and_channel
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
        
        self.graph_main_and_channel = Graph(self, graph=graph_main_and_channel, channel=channel_main_ch, title='Main + channel', start_time=self.start_time)
        self.graph_soloMain = Graph(self, graph=graph_soloMain, channel=channel_main_ch, title='Main', start_time=self.start_time)
        self.graph_soloTemp = Graph(self, graph=graph_soloTemp, channel=channel_temp_ch, title='Temp', start_time=self.start_time)
        
        self.graph_ch1 = Graph(self, graph=graph_ch1, channel=channel_ch1, title='CH1', start_time=self.start_time)
        self.graph_ch2 = Graph(self, graph=graph_ch2, channel=channel_ch2, title='CH2', start_time=self.start_time)
        self.graph_ch3 = Graph(self, graph=graph_ch3, channel=channel_ch3, title='CH3', start_time=self.start_time)
        self.graph_ch4 = Graph(self, graph=graph_ch4, channel=channel_ch4, title='CH4', start_time=self.start_time)
        
        self.graph_vector = [self.graph_main_and_channel,
                             self.graph_soloMain,
                             self.graph_soloTemp, 
                             self.graph_ch1,
                             self.graph_ch2,
                             self.graph_ch3,
                             self.graph_ch4]
        
        # Setup segnali
        self.ui.comboBox_Main_Temp.activated.connect(self.ui.stackedWidget_SG600.setCurrentIndex)
        self.ui.comboBox_Ch_1234.activated.connect(self.ui.stackedWidget_Laumas.setCurrentIndex)
    
        self.ui.pushButton_autorange_ch1.clicked.connect(self.graph_ch1.change_status_autorange)
        self.ui.pushButton_autorange_ch2.clicked.connect(self.graph_ch2.change_status_autorange)
        self.ui.pushButton_autorange_ch3.clicked.connect(self.graph_ch3.change_status_autorange)
        self.ui.pushButton_autorange_ch4.clicked.connect(self.graph_ch4.change_status_autorange)
        self.ui.pushButton_autorange_solo_temp.clicked.connect(self.graph_soloTemp.change_status_autorange)
        self.ui.pushButton_autorange_main_and_channel.clicked.connect(self.graph_main_and_channel.change_status_autorange)
        self.ui.pushButton_autorange_solo_main.clicked.connect(self.graph_soloMain.change_status_autorange)
        
        self.ui.pushButton_reset_ch1.clicked.connect(self,self.graph_ch1.reset_grafico)
        self.ui.pushButton_reset_ch2.clicked.connect(self.graph_ch2.reset_grafico)
        self.ui.pushButton_reset_ch3.clicked.connect(self.graph_ch3.reset_grafico)
        self.ui.pushButton_reset_ch4.clicked.connect(self.graph_ch4.reset_grafico)
        self.ui.pushButton_reset_solo_temp.clicked.connect(self.graph_soloTemp.reset_grafico)
        self.ui.pushButton_reset_main_and_channel.clicked.connect(self.graph_main_and_channel.reset_grafico)
        self.ui.pushButton_reset_solo_main.clicked.connect(self.graph_soloMain.reset_grafico)
        
        # Segnale per torare a home page
        self.ui.pushButton_home.clicked.connect(self.show_home_window)
        
    def show_home_window(self):
        self.homepage.show()
        self.close()
        

        
        
            
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = GraphWindow(banco_di_taratura=None)
    w.show()
    app.exec()