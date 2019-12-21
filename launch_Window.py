import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
import test


class InventorySystem(QDialog,test.Ui_MainWindow):

    def __init__(self):
        super(InventorySystem, self).__init__()
        loadUi('Test.ui')
        self.pushButton.clicked.connect(self.box_Set_LCD)

    def box_Set_LCD(self):
        inventory_Count = self.plainTExtEdit.toPlainText()
        self.lcdNumber.setText(inventory_Count)

    # def open_window():
app = QApplication(sys.argv)
widget = InventorySystem()
widget.show()
sys.exit(app.exec())
    #       app = QtWidgets.QApplication(sys.argv)
    #     w = QtWidgets.QWidget()
    #     window.setupUi()
    #     sys.exit(app.exec())

# open_window()