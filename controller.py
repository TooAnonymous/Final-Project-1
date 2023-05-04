from PyQt5.QtWidgets import *
from gui import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow,Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.setupUi(self)

        self.lineEdit.hide()
        self.lineEdit_2.hide()
        self.submit_button.hide()
        self.total_label.hide()
        self.clear_button.hide()
        self.submit_button.clicked.connect(lambda: self.submit())
        self.clear_button.clicked.connect(lambda: self.clear())


    def add(self):
        self.lineEdit.show()
        self.lineEdit_2.show()
        self.math_label.setText('+')
        self.submit_button.show()
        self.clear_button.show()

    def subtract(self):
        self.lineEdit.show()
        self.lineEdit_2.show()
        self.math_label.setText('-')
        self.submit_button.show()
        self.clear_button.show()

    def multiply(self):
        self.lineEdit.show()
        self.lineEdit_2.show()
        self.math_label.setText('*')
        self.submit_button.show()
        self.clear_button.show()

    def divide(self):
        self.lineEdit.show()
        self.lineEdit_2.show()
        self.math_label.setText('/')
        self.submit_button.show()
        self.clear_button.show()

    def clear(self):
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        self.total_label.setText('')

    def submit(self):
        self.total_label.show()
        num_1= float(self.lineEdit.text())
        num_2= float(self.lineEdit_2.text())
        if self.math_label.text() == '+':
            self.total_label.setText(f'Total: {num_1+num_2:.2f}')
        elif self.math_label.text() == '-':
            self.total_label.setText(f'Total: {num_1-num_2:.2f}')
        elif self.math_label.text() == "*":
            self.total_label.setText(f'Total: {num_1*num_2:.2f}')
        elif self.math_label.text() == "/":
            if self.lineEdit_2.text() == '0':
                self.total_label.setText("Can not divide by Zero")
            else:
                self.total_label.setText(f'Total: {num_1/num_2:.2f}')
