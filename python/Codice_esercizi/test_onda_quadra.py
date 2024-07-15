import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtWidgets
from scipy import signal

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Crea un widget grafico
        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        # Genera dati per l'onda quadra
        t = np.linspace(0, 1, 500, endpoint=False)
        square_wave = signal.square(2 * np.pi * 5 * t)  # frequenza di 5 Hz

        # Imposta i dati nel grafico
        self.graphWidget.plot(t, square_wave, pen=pg.mkPen(color='r', width=2))

        # Aggiungi etichette agli assi
        self.graphWidget.setLabel('left', 'Amplitude', units='V')
        self.graphWidget.setLabel('bottom', 'Time', units='s')

        # Aggiungi un titolo
        self.graphWidget.setTitle('Square Wave')

# Avvia l'applicazione
app = QtWidgets.QApplication([])
window = MainWindow()
window.show()
app.exec()