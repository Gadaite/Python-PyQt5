import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QIcon
class AboutIcon(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(0,0,700,700)
        self.setWindowTitle("change Icon")
        self.setWindowIcon(QIcon())
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    obj = AboutIcon()
    sys.exit(app.exec_())