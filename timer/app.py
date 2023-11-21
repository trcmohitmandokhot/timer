import sys

from PyQt5 import QtWidgets

from ui.timer_ui import Ui_MainWindow


class MyMainWindow(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()
        pass


# class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)


app = QtWidgets.QApplication([])
window = MyMainWindow()
window.show()
app.exec_()
