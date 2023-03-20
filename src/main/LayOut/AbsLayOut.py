import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget


class AbsLayOut(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lable1 = QLabel("labelName1", self)
        lable2 = QLabel("labelName2", self)
        lable3 = QLabel("labelName3", self)
        lable1.move(10, 20)
        lable2.move(20, 40)
        lable3.move(30, 60)
        self.setWindowTitle("ABS LayOut")
        # self.resize(400,500)
        # self.center()
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    absLayout = AbsLayOut()
    sys.exit(app.exec_())
