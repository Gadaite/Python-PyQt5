from PyQt5.QtWidgets import QApplication,QLabel,QWidget
import sys
app = QApplication(sys.argv)
mainWindow = QWidget()
mainWindow.setWindowTitle("quickStart")
mainWindow.resize(1366,768)
lable = QLabel(mainWindow)
lable.setText("welcome pyqt5!")
# lable.resize(500,500)
lable.move(0,0)
mainWindow.show()
sys.exit(app.exec_())