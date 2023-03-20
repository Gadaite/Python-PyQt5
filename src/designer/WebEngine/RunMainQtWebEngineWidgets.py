from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
from MainQtWebEngineWidgets import Ui_MainWindow
# todo :可能为该版本BUG，或者操作不当，不能从url生成页面代码
app = QApplication(sys.argv)
mainWindow = QMainWindow()
ui = Ui_MainWindow()
ui.load(QUrl("https://www.baidu.com/"))
ui.setupUi(mainWindow)
mainWindow.show()
sys.exit(app.exec_())