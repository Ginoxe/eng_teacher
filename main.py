import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import *
import time
import json

def dump_storage(storage):
    with open('vocabulary.json', 'w') as data:
        json.dump(storage, data)

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
        
        self.buttons = []
        self.dayLabel = QLabel()
        self.engLabel = QLabel()
        self.korLabel = QLabel()
        self.back_btn1 = QPushButton()
        self.back_btn2 = QPushButton()
        self.hideButtons = []

        with open('vocabulary.json', encoding="UTF-8") as data:
            self.storage = json.load(data)

        
    def start(self):
        self.mainWin.show()
        sys.exit(self.app.exec_())


    def main(self):
        self.clearAll()
        self.vocab_btn.show()
        self.tt_btn.show()
        self.mock_btn.show()


    def vocabulary(self):
        self.clearMain()
        self.clearDef()
        self.defLabel = QLabel('       Definition', parent = self.mainWin)
        self.defLabel.setFont(QFont('Arial font', 80))
        self.defLabel.setGeometry(0, 0, 960, 200)
        self.etk_btn = QPushButton('English to Korean', parent = self.mainWin)
        self.etk_btn.setFont(QFont('Arial font', 45))
        self.etk_btn.setGeometry(0, 200, 960, 440)
        self.etk_btn.clicked.connect(lambda: self.vocabETK())
        self.kte_btn = QPushButton('Korean to English', parent = self.mainWin)
        self.kte_btn.setFont(QFont('Arial font', 45))
        self.kte_btn.setGeometry(0, 640, 960, 440)

        self.exLabel = QLabel('  Example Sentence', parent = self.mainWin)
        self.exLabel.setFont(QFont('Arial font', 80))
        self.exLabel.setGeometry(960, 0, 960, 200)
        self.sen_btn1 = QPushButton('Level 1', parent = self.mainWin)
        self.sen_btn1.setFont(QFont('Arial font', 45))
        self.sen_btn1.setGeometry(960, 200, 960, 440)
        self.sen_btn2 = QPushButton('Level 2', parent = self.mainWin)
        self.sen_btn2.setFont(QFont('Arial font', 45))
        self.sen_btn2.setGeometry(960, 640, 960, 440)
        self.back_btn = QPushButton('Back', parent = self.mainWin)
        self.back_btn.setFont(QFont('Arial font', 30))
        self.back_btn.setGeometry(30, 900, 100, 100)
        self.back_btn.clicked.connect(lambda: self.main())
        self.defLabel.show()
        self.exLabel.show()
        self.etk_btn.show()
        self.kte_btn.show()
        self.sen_btn1.show()
        self.sen_btn2.show()
        self.back_btn.show()
        
    def vocabETK(self):
        self.clearAll()

        self.dayLabel = QLabel('    Select a Day', parent = self.mainWin)
        self.dayLabel.setFont(QFont('Arial font', 90))
        self.dayLabel.move(500, 0)
        self.day31_btn = QPushButton('31', parent = self.mainWin)
        self.day32_btn = QPushButton('32', parent = self.mainWin)
        self.day33_btn = QPushButton('33', parent = self.mainWin)
        self.day34_btn = QPushButton('34', parent = self.mainWin)
        self.day35_btn = QPushButton('35', parent = self.mainWin)
        self.day36_btn = QPushButton('36', parent = self.mainWin)
        self.day37_btn = QPushButton('37', parent = self.mainWin)
        self.day38_btn = QPushButton('38', parent = self.mainWin)
        self.day39_btn = QPushButton('39', parent = self.mainWin)
        self.day40_btn = QPushButton('40', parent = self.mainWin)
        self.day41_btn = QPushButton('41', parent = self.mainWin)
        self.day42_btn = QPushButton('42', parent = self.mainWin)
        self.day43_btn = QPushButton('43', parent = self.mainWin)
        self.day44_btn = QPushButton('44', parent = self.mainWin)
        self.day45_btn = QPushButton('45', parent = self.mainWin)
        # self.day31_btn.setGeometry(340, 250, 200, 200)
        # self.day32_btn.setGeometry(600, 250, 200 ,200)
        # self.day33_btn.setGeometry(860, 250, 200 ,200)
        # self.day34_btn.setGeometry(1120, 250, 200 ,200)
        # self.day35_btn.setGeometry(1380, 250, 200 ,200)
        # self.day36_btn.setGeometry(340, 510, 200 ,200)
        # self.day37_btn.setGeometry(600, 510, 200 ,200)
        # self.day38_btn.setGeometry(860, 510, 200 ,200)
        # self.day39_btn.setGeometry(1120, 510, 200 ,200)
        # self.day40_btn.setGeometry(1380, 510, 200 ,200)
        # self.day41_btn.setGeometry(340, 770, 200 ,200)
        # self.day42_btn.setGeometry(600, 770, 200 ,200)
        # self.day43_btn.setGeometry(860, 770, 200 ,200)
        # self.day44_btn.setGeometry(1120, 770, 200 ,200)
        # self.day45_btn.setGeometry(1380, 770, 200 ,200)
        # self.day31_btn.
    
        self.buttons = [self.day31_btn, self.day32_btn, self.day33_btn, self.day34_btn, self.day35_btn,
                   self.day36_btn, self.day37_btn, self.day38_btn, self.day39_btn, self.day40_btn,
                   self.day41_btn, self.day42_btn, self.day43_btn, self.day44_btn, self.day45_btn]
        j = 0
        x = 340
        for i in self.buttons:
            if j < 5:
                i.setGeometry(x + (260 * j), 250, 200, 200)
            elif 5 <= j < 10:
                i.setGeometry(x + (260 * (j - 5)), 510, 200, 200)
            else:
                i.setGeometry(x + (260 * (j - 10)), 770, 200, 200)
            i.setFont(QFont('Arial font', 40))
            i.show()
            j += 1

        self.dayLabel.show()

        self.day31_btn.clicked.connect(lambda: self.ETKstage(31))
        self.day32_btn.clicked.connect(lambda: self.ETKstage(32))
        self.day33_btn.clicked.connect(lambda: self.ETKstage(33))
        self.day34_btn.clicked.connect(lambda: self.ETKstage(34))
        self.day35_btn.clicked.connect(lambda: self.ETKstage(35))
        self.day36_btn.clicked.connect(lambda: self.ETKstage(36))
        self.day37_btn.clicked.connect(lambda: self.ETKstage(37))
        self.day38_btn.clicked.connect(lambda: self.ETKstage(38))
        self.day39_btn.clicked.connect(lambda: self.ETKstage(39))
        self.day40_btn.clicked.connect(lambda: self.ETKstage(40))
        self.day41_btn.clicked.connect(lambda: self.ETKstage(41))
        self.day42_btn.clicked.connect(lambda: self.ETKstage(42))
        self.day43_btn.clicked.connect(lambda: self.ETKstage(43))
        self.day44_btn.clicked.connect(lambda: self.ETKstage(44))
        self.day45_btn.clicked.connect(lambda: self.ETKstage(45))

        self.back_btn1 = QPushButton('Back', parent = self.mainWin)
        self.back_btn1.setFont(QFont('Arial font', 30))
        self.back_btn1.setGeometry(30, 900, 100, 100)
        self.back_btn1.clicked.connect(lambda: self.vocabulary())
        self.back_btn1.show()

    def ETKstage(self, day: int):
        for i in self.buttons:
            i.close()
        self.dayLabel.close()
        selected_day = self.storage['def'][f'day{day}']
        eng_words = list(selected_day.keys())
        labeltext = ''
        for i in eng_words:
            labeltext += i
            labeltext += '\n'
        self.engLabel = QLabel(labeltext, parent = self.mainWin)
        self.engLabel.move(740, 0)
        self.engLabel.setFont(QFont('Arial font', 20))
        self.engLabel.show()
        kor_words = list(selected_day.values())
        labeltext = ''
        for i in kor_words:
            labeltext += i
            labeltext += '\n'
        self.korLabel = QLabel(labeltext, parent = self.mainWin)
        self.korLabel.move(960, 0)
        self.korLabel.setFont(QFont('Arial font', 20))
        self.korLabel.show()
        
        self.back_btn2 = QPushButton('Back', parent = self.mainWin)
        self.back_btn2.setFont(QFont('Arial font', 30))
        self.back_btn2.setGeometry(30, 900, 100, 100)
        self.back_btn2.clicked.connect(lambda: self.vocabETK())
        self.back_btn2.show()

        self.hide1 = QPushButton('', parent = self.mainWin)
        self.hide1.clicked.connect(lambda: self.hide1.close())
        self.hide2 = QPushButton('', parent = self.mainWin)
        self.hide2.clicked.connect(lambda: self.hide2.close())
        self.hide3 = QPushButton('', parent = self.mainWin)
        self.hide3.clicked.connect(lambda: self.hide3.close())
        self.hide4 = QPushButton('', parent = self.mainWin)
        self.hide4.clicked.connect(lambda: self.hide4.close())
        self.hide5 = QPushButton('', parent = self.mainWin)
        self.hide5.clicked.connect(lambda: self.hide5.close())
        self.hide6 = QPushButton('', parent = self.mainWin)
        self.hide6.clicked.connect(lambda: self.hide6.close())
        self.hide7 = QPushButton('', parent = self.mainWin)
        self.hide7.clicked.connect(lambda: self.hide7.close())
        self.hide8 = QPushButton('', parent = self.mainWin)
        self.hide8.clicked.connect(lambda: self.hide8.close())
        self.hide9 = QPushButton('', parent = self.mainWin)
        self.hide9.clicked.connect(lambda: self.hide9.close())
        self.hide10 = QPushButton('', parent = self.mainWin)
        self.hide10.clicked.connect(lambda: self.hide10.close())
        self.hide11 = QPushButton('', parent = self.mainWin)
        self.hide11.clicked.connect(lambda: self.hide11.close())
        self.hide12 = QPushButton('', parent = self.mainWin)
        self.hide12.clicked.connect(lambda: self.hide12.close())
        self.hide13 = QPushButton('', parent = self.mainWin)
        self.hide13.clicked.connect(lambda: self.hide13.close())
        self.hide14 = QPushButton('', parent = self.mainWin)
        self.hide14.clicked.connect(lambda: self.hide14.close())
        self.hide15 = QPushButton('', parent = self.mainWin)
        self.hide15.clicked.connect(lambda: self.hide15.close())
        self.hide16 = QPushButton('', parent = self.mainWin)
        self.hide16.clicked.connect(lambda: self.hide16.close())
        self.hide17 = QPushButton('', parent = self.mainWin)
        self.hide17.clicked.connect(lambda: self.hide17.close())
        self.hide18 = QPushButton('', parent = self.mainWin)
        self.hide18.clicked.connect(lambda: self.hide18.close())
        self.hide19 = QPushButton('', parent = self.mainWin)
        self.hide19.clicked.connect(lambda: self.hide19.close())
        self.hide20 = QPushButton('', parent = self.mainWin)
        self.hide20.clicked.connect(lambda: self.hide20.close())
        self.hide21 = QPushButton('', parent = self.mainWin)
        self.hide21.clicked.connect(lambda: self.hide21.close())
        self.hide22 = QPushButton('', parent = self.mainWin)
        self.hide22.clicked.connect(lambda: self.hide22.close())
        self.hide23 = QPushButton('', parent = self.mainWin)
        self.hide23.clicked.connect(lambda: self.hide23.close())
        self.hide24 = QPushButton('', parent = self.mainWin)
        self.hide24.clicked.connect(lambda: self.hide24.close())
        self.hide25 = QPushButton('', parent = self.mainWin)
        self.hide25.clicked.connect(lambda: self.hide25.close())
        self.hide26 = QPushButton('', parent = self.mainWin)
        self.hide26.clicked.connect(lambda: self.hide26.close())
        self.hide27 = QPushButton('', parent = self.mainWin)
        self.hide27.clicked.connect(lambda: self.hide27.close())
        self.hide28 = QPushButton('', parent = self.mainWin)
        self.hide28.clicked.connect(lambda: self.hide28.close())
        self.hide29 = QPushButton('', parent = self.mainWin)
        self.hide29.clicked.connect(lambda: self.hide29.close())
        self.hide30 = QPushButton('', parent = self.mainWin)
        self.hide30.clicked.connect(lambda: self.hide30.close())
        self.hideButtons = [self.hide1, self.hide2, self.hide3, self.hide4, self.hide5, self.hide6, self.hide7, self.hide8, self.hide9, self.hide10,
                            self.hide11, self.hide12, self.hide13, self.hide14, self.hide15, self.hide16, self.hide17, self.hide18, self.hide19, self.hide20,
                            self.hide21, self.hide22, self.hide23, self.hide24, self.hide25, self.hide26, self.hide27, self.hide28, self.hide29, self.hide30]
        k = 0
        for i in self.hideButtons:
            i.setGeometry(960, k*33, 300, 34)
            i.show()
            k += 1
        
        


    def textbook(self):
        pass

    def mockexam(self):
        pass

    def clearMain(self):
        self.vocab_btn.close()
        self.tt_btn.close()
        self.mock_btn.close()

    def clearVocab(self):
        self.defLabel.close()
        self.exLabel.close()
        self.etk_btn.close()
        self.kte_btn.close()
        self.sen_btn1.close()
        self.sen_btn2.close()
        self.back_btn.close()

    def clearDef(self):
        self.dayLabel.close()
        for i in self.buttons:
            i.close()

    def clearAll(self):
        self.defLabel.close()
        self.exLabel.close()
        self.etk_btn.close()
        self.kte_btn.close()
        self.sen_btn1.close()
        self.sen_btn2.close()
        self.back_btn.close()
        self.back_btn1.close()
        self.back_btn2.close()
        self.dayLabel.close()
        for i in self.buttons:
            i.close()
        for i in self.hideButtons:
            i.close()
        self.engLabel.close()
        self.korLabel.close()
    

base = EnglishTeacher()
base.start()