from json import load
from pprint import pprint

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from questions import Ui_MainWindow

main_base, main_form = uic.loadUiType('Board.ui')


def get(key):
    with open('question.json', 'r') as file:
        f = load(file)[key]
        return f


class MainWindow(main_base, main_form):
    def __init__(self):
        super(main_base, self).__init__()
        self.setupUi(self)

        self.category = [
            self.a_0, self.b_0, self.c_0, self.d_0, self.e_0, self.f_0
        ]

        for i, item in enumerate(self.category):
            item.setText(categories[i])

        self.btn = [
            [self.a_1, self.a_2, self.a_3, self.a_4, self.a_5],
            [self.b_1, self.b_2, self.b_3, self.b_4, self.b_5],
            [self.c_1, self.c_2, self.c_3, self.c_4, self.c_5],
            [self.d_1, self.d_2, self.d_3, self.d_4, self.d_5],
            [self.e_1, self.e_2, self.e_3, self.e_4, self.e_5],
            [self.f_1, self.f_2, self.f_3, self.f_4, self.f_5]]

        for i, _list in enumerate(self.btn):
            for j, btn in enumerate(_list):
                self.pressed(btn, i, j)

        self.scores = {"team 1": 0, "team 2": 0}
        self.pot = 0

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

        # team 1
        elif e.key() == Qt.Key_1:
            self.scores['team 1'] += self.pot
            self.pot = 0
            print(self.scores['team 1'])
        elif e.key() == Qt.Key_Exclam:
            try:
                x = int(input('Team 1 new score: '))
                self.scores['team 1'] = x
            except ValueError:
                print('Not an integer')
            finally:
                print(self.scores['team 1'])
        # team 2
        elif e.key() == Qt.Key_2:
            self.scores['team 2'] += self.pot
            self.pot = 0
            print(self.scores['team 2'])
        elif e.key() == Qt.Key_At:
            try:
                self.scores['team 2'] = int(input('Team 2 new score: '))
            except ValueError:
                print('Not an integer')
            finally:
                print(self.scores['team 2'])

        elif e.key() == Qt.Key_Return or e.key() == Qt.Key_Enter:
            print(self.scores)

    def pressed(self, button, i, j):
        button.clicked.connect(lambda: self.popup(button, i, j))

    def popup(self, button, i, j):
        if button.text():
            question = str(questions[i][j])
            answer = str(answers[i][j])
            self.pot = int((button.text()).strip('$ '))
            print(self.pot)
            button.setText('')
            self.open(question, answer)

    def open(self, text, answer):
        self.wn = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.wn, text=text, answer=answer)
        self.wn.showMaximized()
        # self.wn.showFullScreen()


if __name__ == '__main__':
    import sys

    questions = get('questions')
    answers = get('answers')
    categories = get('categories')

    app = QApplication(sys.argv)
    win = MainWindow()

    # win.showFullScreen()
    win.showMaximized()
    sys.exit(app.exec_())
