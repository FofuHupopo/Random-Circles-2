import sys
import random
import time

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QPen, QColor
from PyQt5.QtCore import Qt
from PyQt5 import uic

from ui import Ui_MainWindow


class OCWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        
        self.pushButton.clicked.connect(self.btn_clicked)
        self.draw_circle = False
        
    def btn_clicked(self):
        self.draw_circle = True
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)

        if self.draw_circle:
            for i in range(random.randint(5, 20)):
                painter.setPen(QPen(QColor(
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255),
                    ), 3, Qt.SolidLine
                ))

                radius = random.randint(10, 100)
                x_coords = random.randint(0, 600)
                y_coords = random.randint(0, 400)

                painter.drawEllipse(x_coords, y_coords, radius, radius)

            self.draw_circle = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = OCWindow()
    ex.show()
    sys.exit(app.exec_())
