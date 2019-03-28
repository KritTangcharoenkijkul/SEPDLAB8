import sys
from PySide2.QtWidgets import QApplication
from Q1Code import Simple_drawing_window
from Q1_Krit import  Simple_drawing_window2
from Q1_thosk import Simple_drawing_window1

def main():
    app = QApplication(sys.argv)

    w = Simple_drawing_window()
    w1 = Simple_drawing_window1()
    w2 = Simple_drawing_window2()
    w.show()
    w1.show()
    w2.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())