import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from Q1Code import Simple_drawing_window

class Simple_drawing_window1(Simple_drawing_window):
    def __init__(self):
        QWidget.__init__(self, None)
        self.rabbit = QPixmap("./dragonite.jpg")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 127, 0))
        p.drawPolygon([
            QPoint(60, 100), QPoint(80,150),
            QPoint(130,100), QPoint(100,150),
        ])

        p.setPen(QColor(255, 127, 0))
        p.setBrush(QColor(203,47,112))
        p.drawPie(50, 150, 100, 100,0 ,180 * 15)

        p.drawPolygon(
            [QPoint(100, 200), QPoint(150, 200), QPoint(100, 200)]
        )

        p.drawPixmap(QRect(200, 100, 320,320), self.rabbit)
        p.end()

def main():
    app = QApplication(sys.argv)

    w = Simple_drawing_window1()
    w.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())