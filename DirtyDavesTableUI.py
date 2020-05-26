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
from email_results import sending_email


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
        self.item_dropdown = QtWidgets.QComboBox(Form)
        self.item_dropdown.setGeometry(QtCore.QRect(620, 70, 213, 20))
        self.item_dropdown.setObjectName("item_Drop_Down")
        self.item_dropdown.addItems(self.set_drop_Down_List())

        # Create Drop down for packages
        self.package_dropdown = QtWidgets.QComboBox(Form)
        self.package_dropdown.setGeometry(QtCore.QRect(620, 230, 213, 20))
        self.package_dropdown.setObjectName("Package_Drop_Down")
        self.package_dropdown.addItems(self.set_Packages())

        # Push Button for Adding Packages
        add_package_pushButton = QtWidgets.QPushButton(Form)
        add_package_pushButton.setGeometry(QtCore.QRect(620, 260, 100, 20))
        add_package_pushButton.setObjectName("add_packages")
        add_package_pushButton.setText("Add Pacakges")

        # Push Button to Removing Packages
        remove_package_pushButton = QtWidgets.QPushButton(Form)
        remove_package_pushButton.setGeometry(QtCore.QRect(730, 260, 100, 20))
        remove_package_pushButton.setObjectName("remove_packages")
        remove_package_pushButton.setText("Remove Packages")

        # Push Button to Add Inventory
        pushButton = QtWidgets.QPushButton(Form)
        pushButton.setGeometry(QtCore.QRect(620, 150, 50, 20))
        pushButton.setObjectName("add_Inventory")
        pushButton.setText("Add")

        # Push Button to Remove Inventory
        pushButton2 = QtWidgets.QPushButton(Form)
        pushButton2.setGeometry(QtCore.QRect(700, 150, 50, 20))
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
        add_package_pushButton.clicked.connect(self.update_package_add)
        remove_package_pushButton.clicked.connect(self.update_package_remove)
        # pushButton3.clicked.connect(self.update_Table_Count)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        # self.pushButton.setText(_translate("Form", "PushButton"))
        self.setup_Table(row = grab.how_many_lines(), column = 3)
        # self.pushButton.clicked.connect(self.update_Table("This"))
        # QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL('clicked()'),self.update_Table("This"))
        # self.connect(self.pushButton, SIGNAL("clicked()"), self.update_Table("This"))

    def setup_Table(self, row, column):
        print(row)
        print(column)

        # Table Widget for Table 4
        self.tableWidget4.setRowCount(row)
        self.tableWidget4.setColumnCount(column)
        r = 0
        c = 0
        while r < row:
            self.tableWidget4.setItem(r, c, QTableWidgetItem(self.set_Table_Item(r)))
            r += 1
        c +=1
        r = 0
        while r < row:
            self.tableWidget4.setItem(r, c, QTableWidgetItem(self.set_Table_Quantity(r)))
            r += 1
        c += 1
        r = 0
        while r < row:
            self.tableWidget4.setItem(r, c, QTableWidgetItem(self.set_Table_Descrtiption(r)))
            r += 1

    def update_Table_Add(self):
        try:
            # adding_Target = int(grab.Row_and_Column(2, 1))
            added_Target_Name = self.item_dropdown.currentText()
            print(added_Target_Name)
            amount_To_Add = int(self.lineEdit2.text())
            print(amount_To_Add)
            current_Amount = int(grab.get_item_return_quantity(added_Target_Name))
            new_Target = current_Amount + amount_To_Add
            # self.tableWidget.setItem(2, 1, QTableWidgetItem(str(new_Target)))
            print("Updating Table")
            grab.replace_Quantity_In_File(str(current_Amount), str(new_Target), added_Target_Name)
            self.retranslateUi(Form)
        except Exception as ex:
            print(ex)

    def update_Table_Remove(self):
        try:
            # adding_Target = int(grab.Row_and_Column(2, 1))
            added_Target_Name = self.item_dropdown.currentText()
            print(added_Target_Name)
            amount_To_Add = int(self.lineEdit2.text())
            print(amount_To_Add)
            current_Amount = int(grab.get_item_return_quantity(added_Target_Name))
            print(current_Amount)
            new_Target = current_Amount - amount_To_Add
            # self.tableWidget.setItem(2, 1, QTableWidgetItem(str(new_Target)))
            print("Updating Table")
            # new_text_amount = str(added_Target_Name) + "," + str(new_Target)
            # old_text_amount = str(added_Target_Name) + "," + str(current_Amount)
            grab.replace_Quantity_In_File(str(current_Amount), str(new_Target), added_Target_Name)
            # grab.replace_Quantity_In_File(old_text_amount, new_text_amount, added_Target_Name)
            self.retranslateUi(Form)
            # return
        except Exception as x:
            print(x)


    # Get Table Item from line return from file
    def set_Table_Item(self, Row):
        get_Items_From_File = grab.Row_and_Column(Row)
        item_From_Line = grab.find_Item_Name(get_Items_From_File)
        return item_From_Line

    # Get Table Quantity from line return from file
    def set_Table_Quantity(self, Row):
        get_Items_From_File = grab.Row_and_Column(Row)
        quantity_From_Line = grab.find_Item_Quantity(get_Items_From_File)
        if int(quantity_From_Line) == 1:
            print("Inventory Low")
        return quantity_From_Line

    # Get Table Desctiption from line return from file
    def set_Table_Descrtiption(self, Row):
        get_Items_From_File = grab.Row_and_Column(Row)
        quantity_From_Line = grab.find_Item_Description(get_Items_From_File)
        return quantity_From_Line

    # Get Table Desctiption from line return from file
    def set_Packages(self):
        packages = ["Package 1", "Package 2"]
        return packages

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
    def prep_Inventory_List_Email(self):
        with open("InventoryFiles/Inventory.txt", "r") as inventory_File:
            email_Body = inventory_File.readlines()
            sending_email.send_email(email_Body)

    def update_package_remove(self):
        print("Remove Packages")

    def update_package_add(self):
        print("Add Packages")




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

