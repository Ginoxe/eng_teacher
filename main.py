import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import *
import time

class EnglishTeacher():
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.mainWin = QWidget()
        self.mainWin.setWindowTitle("English Teacher")
        self.mainWin.setGeometry(0, 0, 1920, 1080)
        #self.mainWin.showMaximized()

        self.vocab_btn = QPushButton('Vocabulary', parent = self.mainWin)
        self.vocab_btn.setFont(QFont('Arial font', 90))
        self.vocab_btn.clicked.connect(lambda: self.vocabulary())
        self.vocab_btn.setGeometry(0, 0, 960, 540)
        
        self.tt_btn = QPushButton('Text Book', parent = self.mainWin)
        self.tt_btn.setFont(QFont('Arial font', 90))
        self.tt_btn.clicked.connect(lambda: self.textbook())
        self.tt_btn.setGeometry(960, 0, 960, 540)

        self.mock_btn = QPushButton('Mock Exam', parent = self.mainWin)
        self.mock_btn.setFont(QFont('Arial font', 90))
        self.mock_btn.clicked.connect(lambda: self.textbook())
        self.mock_btn.setGeometry(0, 540, 960, 540)

        

    def main(self):
        self.mainWin.show()
        sys.exit(self.app.exec_())

    def vocabulary(self):
        pass

    def textbook(self):
        pass

    def mockexam(self):
        pass
    

base = EnglishTeacher()
base.main()