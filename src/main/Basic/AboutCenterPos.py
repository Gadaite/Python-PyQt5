import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication


class AboutCenterPos(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.resize(1366, 768)
        self.center()

        self.setWindowTitle('Center')
        self.show()


    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = AboutCenterPos()
    sys.exit(app.exec_())