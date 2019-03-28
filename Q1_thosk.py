import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QPixmap("./dragonite.jpg")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 127, 0))
        p.drawPolygon([
            QPoint(60, 100), QPoint(10,100),
            QPoint(130,100), QPoint(100,150),
        ])

        p.setPen(QColor(255, 127, 0))
        p.setBrush(QColor(203,47,112))
        p.drawPie(50, 150, 100, 100,0 ,180 * 15)

        p.drawPolygon(
            [QPoint(100, 200), QPoint(150, 200), QPoint(100, 400)]
        )

        p.drawPixmap(QRect(200, 100, 320,320), self.rabbit)
        p.end()

def main():
    app = QApplication(sys.argv)

    w = Simple_drawing_window()
    w.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())