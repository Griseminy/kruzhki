import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QLineEdit, QLCDNumber, QPlainTextEdit
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel
from pathlib import Path
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication
from random import randint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()

    def initUI(self):
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw_flag()
            self.qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self):
        self.qp.setPen(QColor(255, 255, 0))
        self.qp.setBrush(QColor(255, 255, 0))
        for i in range(randint(10, 30)):
            self.d = randint(0, 100)
            self.qp.drawEllipse(randint(0, 670), randint(0, 680), self.d, self.d)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())