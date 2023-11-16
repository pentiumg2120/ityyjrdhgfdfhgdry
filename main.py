import random
import sys
from file import Ui_MainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = None
        self.circle_button.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_flag(self, qp):
        # Задаем кисть
        qp.setBrush(QColor(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))
        x = random.randrange(1, 700)
        y = random.randrange(1, 500)
        diametr = random.randrange(25, 500)
        qp.drawEllipse(x, y, diametr, diametr)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
