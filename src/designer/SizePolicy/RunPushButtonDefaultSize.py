import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
import PushButtonDefaultSize

app = QApplication(sys.argv)
mainWindow = QMainWindow()
ui = PushButtonDefaultSize.Ui_MainWindow()
ui.setupUi(mainWindow)
mainWindow.show()
sys.exit(app.exec_())