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
    items_To_Display = "Medium"
    item_To_Display = "Large"

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 450)
        # self.tableWidget = QtWidgets.QTableWidget(Form)
        # self.tableWidget.setGeometry(QtCore.QRect(20, 50, 240, 135))
        # self.tableWidget.setObjectName("First Table")
        # self.tableWidget.setWindowTitle("Hello First Table")
        # self.tableWidget2 = QtWidgets.QTableWidget(Form)
        # self.tableWidget2.setGeometry(QtCore.QRect(260, 50, 240, 135))
        # self.tableWidget2.setObjectName("Second Table")
        # self.tableWidget3 = QtWidgets.QTableWidget(Form)
        # self.tableWidget3.setGeometry(QtCore.QRect(20, 200, 240, 135))
        # self.tableWidget3.setObjectName("Third Table")
        self.tableWidget4 = QtWidgets.QTableWidget(Form)
        self.tableWidget4.setGeometry(QtCore.QRect(40, 40, 540, 295))
        self.tableWidget4.setColumnWidth(0, 1110)
        self.tableWidget4.setObjectName("Fourth Table")

        # Create the Drop Down list of Items
        self.dropdown = QtWidgets.QComboBox(Form)
        self.dropdown.setGeometry(QtCore.QRect(620, 70, 213, 20))
        self.dropdown.setObjectName("Drop_Down")
        self.dropdown.addItems(self.set_drop_Down_List())

        # Push Button to Add Inventory
        pushButton = QtWidgets.QPushButton(Form)
        pushButton.setGeometry(QtCore.QRect(620, 180, 50, 20))
        pushButton.setObjectName("add_Inventory")
        pushButton.setText("Add")

        # Push Button to Remove Inventory
        pushButton2 = QtWidgets.QPushButton(Form)
        pushButton2.setGeometry(QtCore.QRect(700, 180, 50, 20))
        pushButton2.setObjectName("remove_Inventory")
        pushButton2.setText("Remove")
        # pushButton3 = QtWidgets.QPushButton(Form)
        # pushButton3.setGeometry(QtCore.QRect(780, 180, 50, 20))
        # pushButton3.setObjectName("count_Inventory")
        # pushButton3.setText("Count")
        # self.lineEdit = QtWidgets.QLineEdit(Form)
        # self.lineEdit.setGeometry(QtCore.QRect(620, 70, 213, 20))
        # self.lineEdit.setObjectName("lineEdit")
        self.lineEdit2 = QtWidgets.QLineEdit(Form)
        self.lineEdit2.setGeometry(QtCore.QRect(620, 100,213, 20))
        self.lineEdit2.setObjectName("lineEdit")
        # self.getInventoryStats()
        pushButton.clicked.connect(self.update_Table_Add)
        pushButton2.clicked.connect(self.update_Table_Remove)
        # pushButton3.clicked.connect(self.update_Table_Count)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        # self.pushButton.setText(_translate("Form", "PushButton"))
        self.setup_Table(row = 9, column = 3)
        # self.pushButton.clicked.connect(self.update_Table("This"))
        # QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL('clicked()'),self.update_Table("This"))
        # self.connect(self.pushButton, SIGNAL("clicked()"), self.update_Table("This"))

    def setup_Table(self, row, column):

        # self.tableWidget.setRowCount(row)
        # self.tableWidget.setColumnCount(column)
        # self.tableWidget.setItem(0, 0, QTableWidgetItem(grab.Row_and_Column(0, 0)))
        # self.tableWidget2.setRowCount(row)
        # self.tableWidget2.setColumnCount(column)
        # self.tableWidget2.setItem(0, 0, QTableWidgetItem(grab.Row_and_Column(0, 0)))
        # self.tableWidget2.setItem(1, 0, QTableWidgetItem(grab.Row_and_Column(1, 0)))
        # self.tableWidget2.setItem(2, 0, QTableWidgetItem(grab.Row_and_Column(3, 0)))
        # self.tableWidget2.setItem(3, 0, QTableWidgetItem(grab.Row_and_Column(2, 0)))
        # self.tableWidget2.setItem(0, 1, QTableWidgetItem(grab.Row_and_Column(1, 1)))
        # self.tableWidget2.setItem(1, 1, QTableWidgetItem(grab.Row_and_Column(0, 1)))
        # self.tableWidget2.setItem(2, 1, QTableWidgetItem(grab.Row_and_Column(2, 1)))
        # self.tableWidget3.setRowCount(row)
        # self.tableWidget3.setColumnCount(column)
        # self.tableWidget3.setItem(0, 0, QTableWidgetItem(grab.Row_and_Column(0, 0)))
        # self.tableWidget3.setItem(1, 0, QTableWidgetItem(grab.Row_and_Column(1, 0)))
        # self.tableWidget3.setItem(2, 0, QTableWidgetItem(grab.Row_and_Column(2, 1)))
        # self.tableWidget3.setItem(3, 0, QTableWidgetItem(grab.Row_and_Column(0, 1)))
        # self.tableWidget3.setItem(0, 1, QTableWidgetItem(grab.Row_and_Column(1, 1)))
        # self.tableWidget3.setItem(1, 1, QTableWidgetItem(grab.Row_and_Column(2, 0)))
        # self.tableWidget3.setItem(2, 1, QTableWidgetItem(grab.Row_and_Column(3, 0)))
        # Table Widget for Table 4
        self.tableWidget4.setRowCount(row)
        self.tableWidget4.setColumnCount(column)
        # Set item names in Columns of Table 4
        self.tableWidget4.setItem(0, 0, QTableWidgetItem(self.set_Table_Item(0)))
        self.tableWidget4.setItem(1, 0, QTableWidgetItem(self.set_Table_Item(1)))
        self.tableWidget4.setItem(2, 0, QTableWidgetItem(self.set_Table_Item(2)))
        self.tableWidget4.setItem(3, 0, QTableWidgetItem(self.set_Table_Item(3)))
        self.tableWidget4.setItem(4, 0, QTableWidgetItem(self.set_Table_Item(4)))
        self.tableWidget4.setItem(5, 0, QTableWidgetItem(self.set_Table_Item(5)))
        self.tableWidget4.setItem(6, 0, QTableWidgetItem(self.set_Table_Item(6)))
        self.tableWidget4.setItem(7, 0, QTableWidgetItem(self.set_Table_Item(7)))
        self.tableWidget4.setItem(8, 0, QTableWidgetItem(self.set_Table_Item(8)))
        self.tableWidget4.setItem(9, 0, QTableWidgetItem(self.set_Table_Item(9)))
        # self.tableWidget4.setItem(10, 0, QTableWidgetItem(self.set_Table_Item(10)))
        # Set Quantity in Columns
        self.tableWidget4.setItem(0, 1, QTableWidgetItem(self.set_Table_Quantity(0)))
        self.tableWidget4.setItem(1, 1, QTableWidgetItem(self.set_Table_Quantity(1)))
        self.tableWidget4.setItem(2, 1, QTableWidgetItem(self.set_Table_Quantity(2)))
        self.tableWidget4.setItem(3, 1, QTableWidgetItem(self.set_Table_Quantity(3)))
        self.tableWidget4.setItem(4, 1, QTableWidgetItem(self.set_Table_Quantity(4)))
        self.tableWidget4.setItem(5, 1, QTableWidgetItem(self.set_Table_Quantity(5)))
        self.tableWidget4.setItem(6, 1, QTableWidgetItem(self.set_Table_Quantity(6)))
        self.tableWidget4.setItem(7, 1, QTableWidgetItem(self.set_Table_Quantity(7)))
        self.tableWidget4.setItem(8, 1, QTableWidgetItem(self.set_Table_Quantity(8)))
        self.tableWidget4.setItem(9, 1, QTableWidgetItem(self.set_Table_Quantity(9)))
        # self.tableWidget4.setItem(10, 1, QTableWidgetItem(self.set_Table_Quantity(10)))
        # Set Description in Columns
        self.tableWidget4.setItem(0, 2, QTableWidgetItem(self.set_Table_Descrtiption(0)))
        self.tableWidget4.setItem(1, 2, QTableWidgetItem(self.set_Table_Descrtiption(1)))
        self.tableWidget4.setItem(2, 2, QTableWidgetItem(self.set_Table_Descrtiption(2)))
        self.tableWidget4.setItem(3, 2, QTableWidgetItem(self.set_Table_Descrtiption(3)))
        self.tableWidget4.setItem(4, 2, QTableWidgetItem(self.set_Table_Descrtiption(4)))
        self.tableWidget4.setItem(5, 2, QTableWidgetItem(self.set_Table_Descrtiption(5)))
        self.tableWidget4.setItem(6, 2, QTableWidgetItem(self.set_Table_Descrtiption(6)))
        self.tableWidget4.setItem(7, 2, QTableWidgetItem(self.set_Table_Descrtiption(7)))
        self.tableWidget4.setItem(8, 2, QTableWidgetItem(self.set_Table_Descrtiption(8)))
        self.tableWidget4.setItem(9, 2, QTableWidgetItem(self.set_Table_Descrtiption(9)))

    def update_Table_Add(self):
        # adding_Target = int(grab.Row_and_Column(2, 1))
        added_Target_Name = self.dropdown.currentText()
        print(added_Target_Name)
        amount_To_Add = int(self.lineEdit2.text())
        print(amount_To_Add)
        current_Amount = int(grab.get_item_return_quantity(added_Target_Name))
        new_Target = current_Amount + amount_To_Add
        # self.tableWidget.setItem(2, 1, QTableWidgetItem(str(new_Target)))
        print("Updating Table")
        grab.replace_Quantity_In_File(str(current_Amount), str(new_Target), added_Target_Name)
        self.retranslateUi(Form)
        return

    def update_Table_Remove(self):
        try:
            # removing_Target = int(grab.Row_and_Column(2, 1))
            remove_Target = self.lineEdit.text()
            remove_Amount = self.lineEdit2.text()
            new_amount = grab.get_item_return_quantity(remove_Target)
            new_Target = new_amount - remove_Amount

            print(new_amount)

            # self.tableWidget.setItem(2, 1, QTableWidgetItem(str(new_Target)))
            print("Updating Table")
            return
        except:
            print("Exception Thrownw")


    # Get Table Item from line return from file
    def set_Table_Item(self, Row):
        get_Items_From_File = grab.Row_and_Column(Row)
        item_From_Line = grab.find_Item_Name(get_Items_From_File)
        return item_From_Line

    # Get Table Quantity from line return from file
    def set_Table_Quantity(self, Row):
        get_Items_From_File = grab.Row_and_Column(Row)
        quantity_From_Line = grab.find_Item_Quantity(get_Items_From_File)
        return quantity_From_Line

    # Get Table Desctiption from line return from file
    def set_Table_Descrtiption(self, Row):
        get_Items_From_File = grab.Row_and_Column(Row)
        quantity_From_Line = grab.find_Item_Description(get_Items_From_File)
        return quantity_From_Line

    def save_file_on_Exit(self):
        save = create_Backup_Files
        app = QtWidgets.QApplication(sys.argv)
        app.exec()
        print("Application Close")
        save.save_File(self, "AppleCrack")

    # def getInventoryStats(self):
    #     row_1_Col_1 = grab.Row_and_Column(0, 0)
    #     row_1_Col_2 = grab.Row_and_Column(1, 0)
        # row_2_Col_1
        # row_2_Col_2
    def set_drop_Down_List(self):
        count_In_Inventory = grab.how_many_lines()
        list_items = []
        i = 0
        while i < count_In_Inventory:
            get_Items_From_File = grab.Row_and_Column(i)
            item_From_Line = grab.find_Item_Name(get_Items_From_File)
            list_items += [item_From_Line]
            i += 1
        return list_items




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
    # sys.exit()
    sys.exit(app.exec_())
    # sys.exit(ui.save_file_on_Exit())

