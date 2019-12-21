# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TableView2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QPushButton
from Save_Backup_Files import *
from timer_Backup_File import *
from parse_Inventory_File import *

# Setup Variable Methods
grab = document_Parse()
row_1_Col_1 = "Text"
row_1_Col_2 = "Second Texta"
class Ui_Form(object):
    save = create_Backup_Files()
    grab = document_Parse()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(597, 578)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(210, 150, 281, 201))
        # self.tableWidget.setRowCount(3)
        # self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(360, 400, 56, 17))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(180, 400, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.getInventoryStats()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "PushButton"))
        self.setup_Table(row = 3, column = 2)
        # self.pushButton.clicked.connect(self.update_Table("This"))
        # QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL('clicked()'),self.update_Table("This"))
        # self.connect(self.pushButton, SIGNAL("clicked()"), self.update_Table("This"))

    def setup_Table(self, row, column):

        self.tableWidget.setRowCount(row)
        self.tableWidget.setColumnCount(column)
        self.tableWidget.setItem(0, 0, QTableWidgetItem(row_1_Col_1))
        self.tableWidget.setItem(1, 0, QTableWidgetItem(row_1_Col_2))
        self.tableWidget.setItem(2, 0, QTableWidgetItem(grab.Row_and_Column(2, 0)))
        self.tableWidget.setItem(3, 0, QTableWidgetItem(grab.Row_and_Column(3, 0)))
        self.tableWidget.setItem(0, 1, QTableWidgetItem(grab.Row_and_Column(0, 1)))
        self.tableWidget.setItem(1, 1, QTableWidgetItem(grab.Row_and_Column(1, 1)))
        self.tableWidget.setItem(2, 1, QTableWidgetItem(grab.Row_and_Column(2, 1)))

    def update_Table(self, itemNumber):
        print("Updating Table")
        return "Clicked"

    def save_file_on_Exit(self):
        save = create_Backup_Files
        app = QtWidgets.QApplication(sys.argv)
        app.exec()
        print("Application Close")
        save.save_File(self, "AppleCrack")

    def getInventoryStats(self):
        row_1_Col_1 = grab.Row_and_Column(0, 0)
        row_1_Col_2 = grab.Row_and_Column(1, 0)
        # row_2_Col_1
        # row_2_Col_2




if __name__ == "__main__":
    import sys
    run = Ui_Form()
    timer = start_Timer()
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    timer.timer_Kicked()
    # sys.exit(app.exec_())
    sys.exit(ui.save_file_on_Exit())

