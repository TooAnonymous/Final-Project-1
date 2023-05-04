# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        MainWindow.setMinimumSize(QtCore.QSize(400, 300))
        MainWindow.setMaximumSize(QtCore.QSize(400, 300))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 381, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_button = QtWidgets.QPushButton(self.horizontalLayoutWidget, clicked= lambda: self.add())
        self.add_button.setObjectName("add_button")
        self.horizontalLayout.addWidget(self.add_button)
        self.subtract_button = QtWidgets.QPushButton(self.horizontalLayoutWidget, clicked= lambda: self.subtract())
        self.subtract_button.setObjectName("subtract_button")
        self.horizontalLayout.addWidget(self.subtract_button)
        self.multiply_button = QtWidgets.QPushButton(self.horizontalLayoutWidget, clicked= lambda: self.multiply())
        self.multiply_button.setObjectName("multiply_button")
        self.horizontalLayout.addWidget(self.multiply_button)
        self.divide_button = QtWidgets.QPushButton(self.horizontalLayoutWidget, clicked= lambda: self.divide())
        self.divide_button.setObjectName("divide_button")
        self.horizontalLayout.addWidget(self.divide_button)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(5, 60, 391, 91))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.math_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.math_label.setEnabled(True)
        self.math_label.setMinimumSize(QtCore.QSize(10, 10))
        self.math_label.setMaximumSize(QtCore.QSize(10, 10))
        self.math_label.setText("")
        self.math_label.setObjectName("math_label")
        self.horizontalLayout_2.addWidget(self.math_label)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.submit_button = QtWidgets.QPushButton(self.centralwidget)
        self.submit_button.setGeometry(QtCore.QRect(40, 160, 130, 40))
        self.submit_button.setObjectName("submit_button")
        self.total_label = QtWidgets.QLabel(self.centralwidget)
        self.total_label.setGeometry(QtCore.QRect(20, 230, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.total_label.setFont(font)
        self.total_label.setObjectName("total_label")
        self.clear_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_button.setGeometry(QtCore.QRect(230, 160, 130, 40))
        self.clear_button.setMinimumSize(QtCore.QSize(130, 40))
        self.clear_button.setMaximumSize(QtCore.QSize(130, 40))
        self.clear_button.setObjectName("clear_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Final Project"))
        self.add_button.setText(_translate("MainWindow", "Add"))
        self.subtract_button.setText(_translate("MainWindow", "Subtract"))
        self.multiply_button.setText(_translate("MainWindow", "Multipy"))
        self.divide_button.setText(_translate("MainWindow", "Divide"))
        self.submit_button.setText(_translate("MainWindow", "Submit"))
        self.total_label.setText(_translate("MainWindow", "Total:  "))
        self.clear_button.setText(_translate("MainWindow", "Clear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
