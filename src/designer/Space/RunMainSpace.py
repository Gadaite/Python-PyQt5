import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
import MainSpace

app = QApplication(sys.argv)
mainWindow = QMainWindow()
ui = MainSpace.Ui_MainWindow()
ui.setupUi(mainWindow)
mainWindow.show()
sys.exit(app.exec_())