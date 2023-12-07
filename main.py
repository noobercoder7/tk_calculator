from PyQt5.QtWidgets import (QMainWindow, QApplication)
from PyQt5 import uic


class myCalc(QMainWindow):

    def __init__(self):
        super(myCalc, self).__init__()
        uic.loadUi("my_calc.ui", self)
        self.text = ''
        self.show()

        self.btn_0.clicked.connect(lambda: self.num_btn("0"))
        self.btn_1.clicked.connect(lambda: self.num_btn("1"))
        self.btn_2.clicked.connect(lambda: self.num_btn("2"))
        self.btn_3.clicked.connect(lambda: self.num_btn("3"))
        self.btn_4.clicked.connect(lambda: self.num_btn("4"))
        self.btn_5.clicked.connect(lambda: self.num_btn("5"))
        self.btn_6.clicked.connect(lambda: self.num_btn("6"))
        self.btn_7.clicked.connect(lambda: self.num_btn("7"))
        self.btn_8.clicked.connect(lambda: self.num_btn("8"))
        self.btn_9.clicked.connect(lambda: self.num_btn("9"))
        self.btn_add.clicked.connect(lambda: self.num_btn("+"))
        self.btn_sub.clicked.connect(lambda: self.num_btn("-"))
        self.btn_mul.clicked.connect(lambda: self.num_btn("*"))
        self.btn_div.clicked.connect(lambda: self.num_btn("/"))
        self.btn_dot.clicked.connect(lambda: self.num_btn("."))
        self.btn_del.clicked.connect(self.opr_btn_del)
        self.btn_clr.clicked.connect(self.opr_btn_clr)
        self.btn_equal.clicked.connect(self.result)

    def num_btn(self, btn_pressed):
        self.text += btn_pressed
        self.out_label.setText(self.text)

    def opr_btn_del(self):
        self.text = (self.text[:-1])
        self.out_label.setText(self.text)
        if self.text == '':
            self.out_label.setText("0")

    def opr_btn_clr(self):
        self.text = ''
        self.out_label.setText("0")

    def result(self):
        try:
            out_sum = eval(self.text)
            self.text = str(out_sum)
            self.out_label.setText(self.text)

        except:
            self.out_label.setText("error")
            self.text = ''


app = QApplication([])
window = myCalc()
app.exec_()
