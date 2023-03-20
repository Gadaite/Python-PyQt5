import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
import MainWinContainer

app = QApplication(sys.argv)
mainWindow = QMainWindow()
ui = MainWinContainer.Ui_MainWindow()
ui.setupUi(mainWindow)
mainWindow.show()
sys.exit(app.exec_())