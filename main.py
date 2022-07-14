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
        self.buttons2 = []
        self.buttons3 = []
        self.dayLabel = QLabel()
        self.engLabel = QLabel()
        self.korLabel = QLabel()
        self.back_btn1 = QPushButton()
        self.back_btn2 = QPushButton()
        self.hideButtons = []
        self.wordboxes = []
        self.memory = {}
        for i in range(30):
            self.memory[i] = False

        markLabel1 = QLabel('', parent = self.mainWin)
        markLabel2 = QLabel('', parent = self.mainWin)
        markLabel3 = QLabel('', parent = self.mainWin)
        markLabel4 = QLabel('', parent = self.mainWin)
        markLabel5 = QLabel('', parent = self.mainWin)
        markLabel6 = QLabel('', parent = self.mainWin)
        markLabel7 = QLabel('', parent = self.mainWin)
        markLabel8 = QLabel('', parent = self.mainWin)
        markLabel9 = QLabel('', parent = self.mainWin)
        markLabel10 = QLabel('', parent = self.mainWin)
        markLabel11 = QLabel('', parent = self.mainWin)
        markLabel12 = QLabel('', parent = self.mainWin)
        markLabel13 = QLabel('', parent = self.mainWin)
        markLabel14 = QLabel('', parent = self.mainWin)
        markLabel15 = QLabel('', parent = self.mainWin)
        markLabel16 = QLabel('', parent = self.mainWin)
        markLabel17 = QLabel('', parent = self.mainWin)
        markLabel18 = QLabel('', parent = self.mainWin)
        markLabel19 = QLabel('', parent = self.mainWin)
        markLabel20 = QLabel('', parent = self.mainWin)
        markLabel21 = QLabel('', parent = self.mainWin)
        markLabel22 = QLabel('', parent = self.mainWin)
        markLabel23 = QLabel('', parent = self.mainWin)
        markLabel24 = QLabel('', parent = self.mainWin)
        markLabel25 = QLabel('', parent = self.mainWin)
        markLabel26 = QLabel('', parent = self.mainWin)
        markLabel27 = QLabel('', parent = self.mainWin)
        markLabel28 = QLabel('', parent = self.mainWin)
        markLabel29 = QLabel('', parent = self.mainWin)
        markLabel30 = QLabel('', parent = self.mainWin)
        self.markLabels = [markLabel1, markLabel2, markLabel3, markLabel4, markLabel5, markLabel6, markLabel7, markLabel8, markLabel9, markLabel10,
                           markLabel11, markLabel12, markLabel13, markLabel14, markLabel15, markLabel16, markLabel17, markLabel18, markLabel19, markLabel20,
                           markLabel21, markLabel22, markLabel23, markLabel24, markLabel25, markLabel26, markLabel27, markLabel28, markLabel29, markLabel30]

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
        self.defLabel.setFont(QFont('Arial font', 60))
        self.defLabel.setGeometry(0, 0, 960, 200)
        self.etk_btn = QPushButton('English to Korean', parent = self.mainWin)
        self.etk_btn.setFont(QFont('Arial font', 45))
        self.etk_btn.setGeometry(0, 200, 960, 440)
        self.etk_btn.clicked.connect(lambda: self.vocabETK())
        self.kte_btn = QPushButton('Korean to English', parent = self.mainWin)
        self.kte_btn.setFont(QFont('Arial font', 45))
        self.kte_btn.setGeometry(0, 640, 960, 440)
        self.kte_btn.clicked.connect(lambda: self.vocabKTE())

        self.exLabel = QLabel('  Example Sentence', parent = self.mainWin)
        self.exLabel.setFont(QFont('Arial font', 60))
        self.exLabel.setGeometry(960, 0, 960, 200)
        self.sen_btn1 = QPushButton('Level 1', parent = self.mainWin)
        self.sen_btn1.setFont(QFont('Arial font', 45))
        self.sen_btn1.setGeometry(960, 200, 960, 440)
        self.sen_btn1.clicked.connect(lambda: self.exlvl1())
        self.sen_btn2 = QPushButton('Level 2', parent = self.mainWin)
        self.sen_btn2.setFont(QFont('Arial font', 45))
        self.sen_btn2.setGeometry(960, 640, 960, 440)
        self.back_btn = QPushButton('Back', parent = self.mainWin)
        self.back_btn.setFont(QFont('Arial font', 15))
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

        self.dayLabel = QLabel(' Select a Day', parent = self.mainWin)
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
        self.back_btn1.setFont(QFont('Arial font', 15))
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
        self.engLabel.setFont(QFont('Arial font', 17))
        self.engLabel.show()
        kor_words = list(selected_day.values())
        labeltext = ''
        for i in kor_words:
            labeltext += i
            labeltext += '\n'
        self.korLabel = QLabel(labeltext, parent = self.mainWin)
        self.korLabel.move(960, 0)
        self.korLabel.setFont(QFont('Arial font', 17))
        self.korLabel.show()
        
        self.back_btn2 = QPushButton('Back', parent = self.mainWin)
        self.back_btn2.setFont(QFont('Arial font', 15))
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
            i.setGeometry(960, k*32, 400, 34)
            i.show()
            k += 1
        
    def vocabKTE(self):
        self.clearAll()

        self.dayLabel = QLabel(' Select a Day', parent = self.mainWin)
        self.dayLabel.setFont(QFont('Arial font', 90))
        self.dayLabel.move(500, 0)
        
        self.day31_btn2 = QPushButton('31', parent = self.mainWin)
        self.day32_btn2 = QPushButton('32', parent = self.mainWin)
        self.day33_btn2 = QPushButton('33', parent = self.mainWin)
        self.day34_btn2 = QPushButton('34', parent = self.mainWin)
        self.day35_btn2 = QPushButton('35', parent = self.mainWin)
        self.day36_btn2 = QPushButton('36', parent = self.mainWin)
        self.day37_btn2 = QPushButton('37', parent = self.mainWin)
        self.day38_btn2 = QPushButton('38', parent = self.mainWin)
        self.day39_btn2 = QPushButton('39', parent = self.mainWin)
        self.day40_btn2 = QPushButton('40', parent = self.mainWin)
        self.day41_btn2 = QPushButton('41', parent = self.mainWin)
        self.day42_btn2 = QPushButton('42', parent = self.mainWin)
        self.day43_btn2 = QPushButton('43', parent = self.mainWin)
        self.day44_btn2 = QPushButton('44', parent = self.mainWin)
        self.day45_btn2 = QPushButton('45', parent = self.mainWin)

        self.buttons2 = [self.day31_btn2, self.day32_btn2, self.day33_btn2, self.day34_btn2, self.day35_btn2,
                         self.day36_btn2, self.day37_btn2, self.day38_btn2, self.day39_btn2, self.day40_btn2,
                         self.day41_btn2, self.day42_btn2, self.day43_btn2, self.day44_btn2, self.day45_btn2]

        j = 0
        x = 340
        for i in self.buttons2:
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

        self.day31_btn2.clicked.connect(lambda: self.KTEstage(31))
        self.day32_btn2.clicked.connect(lambda: self.KTEstage(32))
        self.day33_btn2.clicked.connect(lambda: self.KTEstage(33))
        self.day34_btn2.clicked.connect(lambda: self.KTEstage(34))
        self.day35_btn2.clicked.connect(lambda: self.KTEstage(35))
        self.day36_btn2.clicked.connect(lambda: self.KTEstage(36))
        self.day37_btn2.clicked.connect(lambda: self.KTEstage(37))
        self.day38_btn2.clicked.connect(lambda: self.KTEstage(38))
        self.day39_btn2.clicked.connect(lambda: self.KTEstage(39))
        self.day40_btn2.clicked.connect(lambda: self.KTEstage(40))
        self.day41_btn2.clicked.connect(lambda: self.KTEstage(41))
        self.day42_btn2.clicked.connect(lambda: self.KTEstage(42))
        self.day43_btn2.clicked.connect(lambda: self.KTEstage(43))
        self.day44_btn2.clicked.connect(lambda: self.KTEstage(44))
        self.day45_btn2.clicked.connect(lambda: self.KTEstage(45))

        self.back_btn1 = QPushButton('Back', parent = self.mainWin)
        self.back_btn1.setFont(QFont('Arial font', 15))
        self.back_btn1.setGeometry(30, 900, 100, 100)
        self.back_btn1.clicked.connect(lambda: self.vocabulary())
        self.back_btn1.show()

    def KTEstage(self, day):
        self.clearAll()

        for i in self.buttons2:
            i.close()
        self.dayLabel.close()
        selected_day = self.storage['def'][f'day{day}']
        kor_words = list(selected_day.values())
        eng_words = list(selected_day.keys())

        labeltext = ''
        for i in eng_words:
            labeltext += i
            labeltext += '\n'
        self.engLabel = QLabel(labeltext, parent = self.mainWin)
        self.engLabel.move(1000, 0)
        self.engLabel.setFont(QFont('Arial font', 17))
        self.engLabel.show()
        labeltext = ''
        for i in kor_words:
            labeltext += i
            labeltext += '\n'
        self.korLabel = QLabel(labeltext, parent = self.mainWin)
        self.korLabel.move(700, 0)
        self.korLabel.setFont(QFont('Arial font', 17))
        self.korLabel.show()
        
        self.back_btn2 = QPushButton('Back', parent = self.mainWin)
        self.back_btn2.setFont(QFont('Arial font', 15))
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
            i.setGeometry(995, k*32, 200, 34)
            i.show()
            k += 1


    def exlvl1(self):
        self.clearAll()

        self.dayLabel = QLabel(' Select a Day', parent = self.mainWin)
        self.dayLabel.setFont(QFont('Arial font', 90))
        self.dayLabel.move(500, 0)
        self.day31_btn3 = QPushButton('31', parent = self.mainWin)
        self.day32_btn3 = QPushButton('32', parent = self.mainWin)
        self.day33_btn3 = QPushButton('33', parent = self.mainWin)
        self.day34_btn3 = QPushButton('34', parent = self.mainWin)
        self.day35_btn3 = QPushButton('35', parent = self.mainWin)
        self.day36_btn3 = QPushButton('36', parent = self.mainWin)
        self.day37_btn3 = QPushButton('37', parent = self.mainWin)
        self.day38_btn3 = QPushButton('38', parent = self.mainWin)
        self.day39_btn3 = QPushButton('39', parent = self.mainWin)
        self.day40_btn3 = QPushButton('40', parent = self.mainWin)
        self.day41_btn3 = QPushButton('41', parent = self.mainWin)
        self.day42_btn3 = QPushButton('42', parent = self.mainWin)
        self.day43_btn3 = QPushButton('43', parent = self.mainWin)
        self.day44_btn3 = QPushButton('44', parent = self.mainWin)
        self.day45_btn3 = QPushButton('45', parent = self.mainWin)

        self.buttons3 = [self.day31_btn3, self.day32_btn3, self.day33_btn3, self.day34_btn3, self.day35_btn3,
                         self.day36_btn3, self.day37_btn3, self.day38_btn3, self.day39_btn3, self.day40_btn3,
                         self.day41_btn3, self.day42_btn3, self.day43_btn3, self.day44_btn3, self.day45_btn3]

        j = 0
        x = 340
        for i in self.buttons3:
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

        self.day31_btn3.clicked.connect(lambda: self.exlvl1stage(31))
        self.day32_btn3.clicked.connect(lambda: self.exlvl1stage(32))
        self.day33_btn3.clicked.connect(lambda: self.exlvl1stage(33))
        self.day34_btn3.clicked.connect(lambda: self.exlvl1stage(34))
        self.day35_btn3.clicked.connect(lambda: self.exlvl1stage(35))
        self.day36_btn3.clicked.connect(lambda: self.exlvl1stage(36))
        self.day37_btn3.clicked.connect(lambda: self.exlvl1stage(37))
        self.day38_btn3.clicked.connect(lambda: self.exlvl1stage(38))
        self.day39_btn3.clicked.connect(lambda: self.exlvl1stage(39))
        self.day40_btn3.clicked.connect(lambda: self.exlvl1stage(40))
        self.day41_btn3.clicked.connect(lambda: self.exlvl1stage(41))
        self.day42_btn3.clicked.connect(lambda: self.exlvl1stage(42))
        self.day43_btn3.clicked.connect(lambda: self.exlvl1stage(43))
        self.day44_btn3.clicked.connect(lambda: self.exlvl1stage(44))
        self.day45_btn3.clicked.connect(lambda: self.exlvl1stage(45))

        self.back_btn1 = QPushButton('Back', parent = self.mainWin)
        self.back_btn1.setFont(QFont('Arial font', 15))
        self.back_btn1.setGeometry(30, 900, 100, 100)
        self.back_btn1.clicked.connect(lambda: self.vocabulary())
        self.back_btn1.show()

    def exlvl1stage(self, day):
        self.clearAll()

        for i in self.buttons3:
            i.close()
        self.dayLabel.close()

        selected_day = self.storage['ex'][f'day{day}']
        sentences = list(selected_day.values())
        labeltext = ''
        for i in sentences:
            labeltext += i[0] + ' (' + i[1] + ')\n'
            senLabel = QLabel(labeltext, parent = self.mainWin)
        senLabel.setFont(QFont('Arial font', 17))
        senLabel.show()

        wordbox1 = QLineEdit('', parent = self.mainWin)
        wordbox1.returnPressed.connect(lambda: self.checkKeyword(day, 0, wordbox1.text()))
        wordbox2 = QLineEdit('', parent = self.mainWin)
        wordbox2.returnPressed.connect(lambda: self.checkKeyword(day, 1, wordbox2.text()))
        wordbox3 = QLineEdit('', parent = self.mainWin)
        wordbox3.returnPressed.connect(lambda: self.checkKeyword(day, 2, wordbox3.text()))
        wordbox4 = QLineEdit('', parent = self.mainWin)
        wordbox4.returnPressed.connect(lambda: self.checkKeyword(day, 3, wordbox4.text()))
        wordbox5 = QLineEdit('', parent = self.mainWin)
        wordbox5.returnPressed.connect(lambda: self.checkKeyword(day, 4, wordbox5.text()))
        wordbox6 = QLineEdit('', parent = self.mainWin)
        wordbox6.returnPressed.connect(lambda: self.checkKeyword(day, 5, wordbox6.text()))
        wordbox7 = QLineEdit('', parent = self.mainWin)
        wordbox7.returnPressed.connect(lambda: self.checkKeyword(day, 6, wordbox7.text()))
        wordbox8 = QLineEdit('', parent = self.mainWin)
        wordbox8.returnPressed.connect(lambda: self.checkKeyword(day, 7, wordbox8.text()))
        wordbox9 = QLineEdit('', parent = self.mainWin)
        wordbox9.returnPressed.connect(lambda: self.checkKeyword(day, 8, wordbox9.text()))
        wordbox10 = QLineEdit('', parent = self.mainWin)
        wordbox10.returnPressed.connect(lambda: self.checkKeyword(day, 9, wordbox10.text()))
        wordbox11 = QLineEdit('', parent = self.mainWin)
        wordbox11.returnPressed.connect(lambda: self.checkKeyword(day, 10, wordbox11.text()))
        wordbox12 = QLineEdit('', parent = self.mainWin)
        wordbox12.returnPressed.connect(lambda: self.checkKeyword(day, 11, wordbox12.text()))
        wordbox13 = QLineEdit('', parent = self.mainWin)
        wordbox13.returnPressed.connect(lambda: self.checkKeyword(day, 12, wordbox13.text()))
        wordbox14 = QLineEdit('', parent = self.mainWin)
        wordbox14.returnPressed.connect(lambda: self.checkKeyword(day, 13, wordbox14.text()))
        wordbox15 = QLineEdit('', parent = self.mainWin)
        wordbox15.returnPressed.connect(lambda: self.checkKeyword(day, 14, wordbox15.text()))
        wordbox16 = QLineEdit('', parent = self.mainWin)
        wordbox16.returnPressed.connect(lambda: self.checkKeyword(day, 15, wordbox16.text()))
        wordbox17 = QLineEdit('', parent = self.mainWin)
        wordbox17.returnPressed.connect(lambda: self.checkKeyword(day, 16, wordbox17.text()))
        wordbox18 = QLineEdit('', parent = self.mainWin)
        wordbox18.returnPressed.connect(lambda: self.checkKeyword(day, 17, wordbox18.text()))
        wordbox19 = QLineEdit('', parent = self.mainWin)
        wordbox19.returnPressed.connect(lambda: self.checkKeyword(day, 18, wordbox19.text()))
        wordbox20 = QLineEdit('', parent = self.mainWin)
        wordbox20.returnPressed.connect(lambda: self.checkKeyword(day, 19, wordbox20.text()))
        wordbox21 = QLineEdit('', parent = self.mainWin)
        wordbox21.returnPressed.connect(lambda: self.checkKeyword(day, 20, wordbox21.text()))
        wordbox22 = QLineEdit('', parent = self.mainWin)
        wordbox22.returnPressed.connect(lambda: self.checkKeyword(day, 21, wordbox22.text()))
        wordbox23 = QLineEdit('', parent = self.mainWin)
        wordbox23.returnPressed.connect(lambda: self.checkKeyword(day, 22, wordbox23.text()))
        wordbox24 = QLineEdit('', parent = self.mainWin)
        wordbox24.returnPressed.connect(lambda: self.checkKeyword(day, 23, wordbox24.text()))
        wordbox25 = QLineEdit('', parent = self.mainWin)
        wordbox25.returnPressed.connect(lambda: self.checkKeyword(day, 24, wordbox25.text()))
        wordbox26 = QLineEdit('', parent = self.mainWin)
        wordbox26.returnPressed.connect(lambda: self.checkKeyword(day, 25, wordbox26.text()))
        wordbox27 = QLineEdit('', parent = self.mainWin)
        wordbox27.returnPressed.connect(lambda: self.checkKeyword(day, 26, wordbox27.text()))
        wordbox28 = QLineEdit('', parent = self.mainWin)
        wordbox28.returnPressed.connect(lambda: self.checkKeyword(day, 27, wordbox28.text()))
        wordbox29 = QLineEdit('', parent = self.mainWin)
        wordbox29.returnPressed.connect(lambda: self.checkKeyword(day, 28, wordbox29.text()))
        wordbox30 = QLineEdit('', parent = self.mainWin)
        wordbox30.returnPressed.connect(lambda: self.checkKeyword(day, 29, wordbox30.text()))
        self.wordboxes = [wordbox1, wordbox2, wordbox3, wordbox4, wordbox5, wordbox6, wordbox7, wordbox8, wordbox9, wordbox10,
                          wordbox11, wordbox12, wordbox13, wordbox14, wordbox15, wordbox16, wordbox17, wordbox18, wordbox19, wordbox20,
                          wordbox21, wordbox22, wordbox23, wordbox24, wordbox25, wordbox26, wordbox27, wordbox28, wordbox29, wordbox30]

        k = 0
        for i in self.wordboxes:
            i.setGeometry(1720, k*32, 200, 34)
            i.setFont(QFont('Arial font', 17))
            i.show()
            k += 1

    def checkKeyword(self, day, wordNum, text):
        if self.markLabels[wordNum].text():
            self.markLabels[wordNum].close()

        selected_day = self.storage['ex'][f'day{day}']
        words = list(selected_day.keys())


        if words[wordNum] == text:
            correct = '○'
        else:
            correct = 'X'
        self.markLabels[wordNum] = QLabel(correct, parent = self.mainWin)
        self.markLabels[wordNum].setFont(QFont('Arial font', 17))
        if correct == '○':
            self.markLabels[wordNum].move(1690, 34 * wordNum)
        else:
            self.markLabels[wordNum].move(1695, 34 * wordNum)
        self.markLabels[wordNum].show()

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
        for i in self.buttons2:
            i.close()
        for i in self.buttons3:
            i.close()
        for i in self.wordboxes:
            i.close()
        self.engLabel.close()
        self.korLabel.close()
    

base = EnglishTeacher()
base.start()