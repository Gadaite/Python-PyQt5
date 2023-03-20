import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
import MainPartner

app = QApplication(sys.argv)
mainWindow = QMainWindow()
ui = MainPartner.Ui_MainWindow()
ui.setupUi(mainWindow)
mainWindow.show()
sys.exit(app.exec_())