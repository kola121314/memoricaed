from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGroupBox,
                             QButtonGroup, QRadioButton, QLabel, QPushButton)

app = QApplication([])
window = QWidget()
window.setWindowTitle("Memory Card")
window.resize(700, 500)

lb_question = QLabel("Запитання")
radio_group_box = QGroupBox("Варіанти відповідей")
rbtn_1 = QRadioButton("1)")
rbtn_2 = QRadioButton("2)")
rbtn_3 = QRadioButton("3)")
rbtn_4 = QRadioButton("4)")
btn_ok = QPushButton("Відповідь")

radio_button_group = QButtonGroup()
radio_button_group.addButton(rbtn_1)
radio_button_group.addButton(rbtn_2)
radio_button_group.addButton(rbtn_3)
radio_button_group.addButton(rbtn_4)

layout_ans_1 = QHBoxLayout()
layout_ans_2 = QHBoxLayout()
layout_ans_main = QVBoxLayout()

layout_ans_1.addWidget(rbtn_1)
layout_ans_1.addWidget(rbtn_2)
layout_ans_2.addWidget(rbtn_3)
layout_ans_2.addWidget(rbtn_4)

layout_ans_main.addLayout(layout_ans_1)
layout_ans_main.addLayout(layout_ans_2)
radio_group_box.setLayout(layout_ans_main)

ans_group_box = QGroupBox("Результат ")
lb_result = QLabel("Правильно/Неправильно")
lb_correct = QLabel("Правильна відповідь")
lb_layout_result = QVBoxLayout()
lb_layout_result.addWidget(lb_result, alignment=(Qt.AlignLeft | Qt.AlignTop))
lb_layout_result.addWidget(lb_correct, alignment=Qt.AlignHCenter, stretch=2)
ans_group_box.setLayout(lb_layout_result)



layout_row_1 = QHBoxLayout()
layout_row_2 = QHBoxLayout()
layout_row_3 = QHBoxLayout()
layout_card = QVBoxLayout()

layout_row_1.addWidget(lb_question, alignment=Qt.AlignCenter)
layout_row_2.addWidget(radio_group_box)

layout_row_2.addWidget(ans_group_box)
ans_group_box.hide()

layout_row_3.addStretch(1)
layout_row_3.addWidget(btn_ok, stretch=2)
layout_row_3.addStretch(1)


layout_card.addLayout(layout_row_1, stretch=2)
layout_card.addLayout(layout_row_2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_row_3, stretch=1)
layout_card.addStretch(1)

layout_card.setSpacing(5)
window.setLayout(layout_card)

def show_result():
    radio_group_box.hide()
    ans_group_box.show()
    btn_ok.setText("Наступне питання")


def show_question():
    ans_group_box.hide()
    radio_group_box.show()
    btn_ok.setText("Відповідь")
    radio_button_group.setExclusive(False)
    rbtn_1.setChecked(False)    
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    radio_button_group.setExclusive(True)

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

from random import shuffle
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_question.setText(q.question)
    lb_correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct("Правильно!")
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct("Неправильно!")

def next_question():
    window.current_q += 1
    if window.current_q >= len(window.question_list):
        shuffle(window.question_list)
        window.current_q = 0
    ask(window.question_list[window.current_q])
def click_ok():
    if btn_ok.text() == "Відповідь":
        check_answer()
    else:
        next_question()



q1 = Question("Яка країна є найбільшою за площею?", "Росія", "Канада", "Китай", "США")


q2 = Question("Яка планета є найближчою до Сонця?", "Меркурій", "Венера", "Земля", "Марс")

q3 = Question("Яка річка є найдовшою у світі?", "Амазонка", "Амазонка", "Янцзи", "Міссісіпі")


q4 = Question("Яка країна є найбільшою за населенням?", "Китай", "Індія", "США", "Індонезія")


q5 = Question("Яка гора є найвищою у світі?", "Еверест", "К2", "Канченджанга", "Лхоцзе")


q6 = Question("скільки планет у Сонячній системі?", "8", "7", "9", "10")


q7 = Question("скільки континентів на Землі?", "7", "5", "6", "8")


window.question_list = [q1, q2, q3, q4, q5, q6, q7]
shuffle(window.question_list)
window.current_q = 0



btn_ok.clicked.connect(click_ok)
next_question()

window.show()
app.exec_() 