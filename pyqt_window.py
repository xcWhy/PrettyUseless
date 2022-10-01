from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QTextEdit, QPushButton
import pdf_reader
#from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap


class addition(QMainWindow):

    def __init__(self):

        super(addition, self).__init__()
        #loadUi("D:\QtDesigner\some designs\NASA_app.ui", self)

        self.setWindowTitle("PyQt Addition Application")

        self.resize(800, 400)

        self.lbl1 = QLabel('File name', self)
        self.lbl1.setGeometry(100, 50, 80, 50)

        self.textbox1 = QTextEdit(self)
        self.textbox1.setGeometry(100, 100, 270, 80)

        self.lbl2 = QLabel('PDF location', self)
        self.lbl2.setGeometry(400, 50, 80, 50)

        self.textbox2 = QTextEdit(self)
        self.textbox2.setGeometry(400, 100, 270, 80)

        self.submit = QPushButton('Do it', self)
        self.submit.setGeometry(290, 200, 190, 30)

        self.lblResult = QLabel('', self)
        self.lblResult.setGeometry(360, 250, 200, 50)

        self.submit.clicked.connect(self.onClicked)

        self.show()

    def onClicked(self):
        location_for_file = str(self.textbox1.toPlainText())
        location_for_pdf = str(self.textbox2.toPlainText())

        pdf_reader.create_txt(location_for_new_file= location_for_file, location_of_pdf= location_for_pdf)

        #result = num1 + num2
        output = "Done!"
        self.lblResult.setText(output)


app = QApplication([])
# Start the event loop for executing the application
window = addition()

app.exec()

