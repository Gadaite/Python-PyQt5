import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QHBoxLayout

class HorizontalLayOut(QWidget):

    def __init__(self):
        super(HorizontalLayOut, self).__init__()
        self.InitUI();
    def InitUI(self):
        okBtn = QPushButton("ok")
        cancelBtn = QPushButton("cancel")
        hBox = QHBoxLayout()
        hBox.addStretch(1)
        hBox.addWidget(okBtn)
        hBox.addWidget(cancelBtn)
        self.setGeometry(300,300,300,150)
        self.setLayout(hBox)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    hlayout = HorizontalLayOut()
    sys.exit(app.exec_())