from PyQt5.QtWidgets import QWidget
from key_reader import KeyReader


class GUI(QWidget):
        
        def __init__(self):
            super().__init__()
            self.key_reader = KeyReader()
            self.init_ui()
            
        def init_ui(self):
            self.setGeometry(100, 100, 200, 200)
            self.setWindowTitle("Shortcut Manager")
            self.show()

GUI().init_ui()  