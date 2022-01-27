import sys
import random

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
lst = []
count = 0


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_star(qp)
            qp.end()

    def paint(self):
        global count
        self.do_paint = True
        self.repaint()
        count += 1

    def draw_star(self, qp):
        global count
        global lst
        x = random.randint(0, 800)
        y = random.randint(0, 600)
        wh = random.randint(0, 500)
        lst.append([x, y, wh])
        lst = lst[:count + 1]
        pen = QPen(Qt.yellow, 5)
        qp.setPen(pen)
        for i in lst:
            qp.drawArc(i[0], i[1], i[2], i[2], 0, 5760)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())