	
import sys
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget

class TimerExample(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.time_elapsed = 0  # Tempo trascorso in secondi

    def initUI(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateTime)

        self.label = QLabel("Time elapsed: 0 seconds", self)

        self.start_btn = QPushButton("Start Timer", self)
        self.start_btn.clicked.connect(self.startTimer)

        self.stop_btn = QPushButton("Stop Timer", self)
        self.stop_btn.clicked.connect(self.stopTimer)

        self.reset_btn = QPushButton("Reset Timer", self)
        self.reset_btn.clicked.connect(self.resetTimer)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.start_btn)
        layout.addWidget(self.stop_btn)
        layout.addWidget(self.reset_btn)

        self.setLayout(layout)

        self.setWindowTitle('QTimer Example')
        self.show()

    def startTimer(self):
        self.timer.start(1000)  # Timer ticks every second

    def stopTimer(self):
        self.timer.stop()

    def resetTimer(self):
        self.stopTimer()
        self.time_elapsed = 0  # Reset del contatore del tempo trascorso
        self.label.setText("Time elapsed: 0 seconds")

    def updateTime(self):
        self.time_elapsed += 1
        self.label.setText(f"Time elapsed: {self.time_elapsed} seconds")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TimerExample()
    sys.exit(app.exec_())
