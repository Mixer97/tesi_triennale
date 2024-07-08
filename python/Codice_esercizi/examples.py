from PySide6 import QtCore,QtGui
from PySide6.QtWidgets import QApplication,QFileDialog,QPushButton

def do_file():
    fname = QFileDialog.getOpenFileName()
    print(fname)

app = QApplication([])

button = QPushButton("Test File")
button.clicked.connect(do_file)
button.show()

app.exec_()

# con questo metodo posso fare cio che mi serve nella ricerca di un file 