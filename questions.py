from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QSound


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, text, answer):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 576)
        MainWindow.setStyleSheet("QLabel {\n    color: rgb(255, 255, 255);\n    font: 75 30pt \"ITC "
                                 "Korinna\";\n}\nQWidget {\n    background-color: rgb(6, 12, 233);}\nQPushButton {\n "
                                 "   color: white;}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.question = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("ITC Korinna")
        font.setPointSize(30)
        self.question.setFont(font)
        self.question.setAlignment(QtCore.Qt.AlignCenter)
        self.question.setWordWrap(True)
        self.question.setObjectName("question")
        self.verticalLayout.addWidget(self.question)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(-1, 5, 3, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(700, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.btn_music = QtWidgets.QPushButton(self.frame)
        self.btn_music.setObjectName("btn_music")
        self.horizontalLayout_2.addWidget(self.btn_music)
        self.btn_question = QtWidgets.QPushButton(self.frame)
        self.btn_question.setObjectName("btn_question")
        self.horizontalLayout_2.addWidget(self.btn_question)
        self.btn_answer = QtWidgets.QPushButton(self.frame)
        self.btn_answer.setObjectName("btn_answer")
        self.horizontalLayout_2.addWidget(self.btn_answer)
        self.btn_done = QtWidgets.QPushButton(self.frame)
        self.btn_answer.setObjectName("btn_done")
        self.horizontalLayout_2.addWidget(self.btn_done)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow, text, answer)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow, text, answer):
        translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(translate("MainWindow", "Question"))
        self.question.setText(translate("MainWindow", text))
        self.btn_music.setText(translate("MainWindow", "Music"))
        self.btn_question.setText(translate("MainWindow", "Question"))
        self.btn_answer.setText(translate("MainWindow", "Answer"))
        self.btn_done.setText(translate("MainWindow", "Done"))

        self.sounds = {'Theme': QSound('theme.wav')}
        self.play()
        self.btn_music.pressed.connect(self.play)
        self.btn_answer.pressed.connect(lambda: self.answer(answer))
        self.btn_question.pressed.connect(lambda: self.question.setText(text))
        self.btn_done.pressed.connect(lambda: self.destroy(MainWindow))

    def play(self):
        self.sounds['Theme'].play()

    def answer(self, answer):
        self.question.setText(answer)
        self.sounds['Theme'].stop()

    def destroy(self, MainWindow):
        try:
            for _ in range(10):
                self.sounds['Theme'].stop()
        finally:
            MainWindow.destroy()
