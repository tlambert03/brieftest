"""
My first application
"""
import sys
from PySide2 import QtWidgets


class HelloWorld(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('helloworld')
        self.show()

def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = HelloWorld()
    sys.exit(app.exec_())