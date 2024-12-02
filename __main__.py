import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *


class Window1(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 400, 350, 165)
        self.setWindowTitle('Процессы')

        self.slide = QSlider(self)
        self.slide.setMinimum(0)
        self.slide.setMaximum(100)
        self.slide.move(10, 60)

        self.slide = QSlider(self)
        self.slide.setMinimum(0)
        self.slide.setMaximum(100)
        self.slide.move(40, 60)

        self.slide = QSlider(self)
        self.slide.setMinimum(0)
        self.slide.setMaximum(100)
        self.slide.move(70, 60)

        label = QLabel("Процесс завершения", self)
        label.move(5, 5)
        label.resize(150, 27)

        label = QLabel("Домашние дела", self)
        label.move(220, 5)
        label.resize(150, 27)

        label = QLabel("Прогулка", self)
        label.move(260, 55)
        label.resize(150, 27)

        label = QLabel("Побочные дела", self)
        label.move(220, 30)
        label.resize(150, 27)

        label = QLabel("Завтрак", self)
        label.move(265, 80)
        label.resize(150, 27)

        label = QLabel("Обед", self)
        label.move(285, 105)
        label.resize(150, 27)

        label = QLabel("Ужин", self)
        label.move(285, 130)
        label.resize(150, 27)

        box = QCheckBox(self)
        box.move(325, 10)

        box = QCheckBox(self)
        box.move(325, 35)

        box = QCheckBox(self)
        box.move(325, 60)

        box = QCheckBox(self)
        box.move(325, 85)

        box = QCheckBox(self)
        box.move(325, 110)

        box = QCheckBox(self)
        box.move(325, 135)


class Notes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 650, 320)
        self.setWindowTitle('Заметки')

        self.label_edit = QLabel("Новая Заметка:", self)
        self.label_edit.move(18, 4)
        self.label_edit.resize(125, 27)

        self.filename_edit = QLineEdit(self)
        self.filename_edit.move(5, 30)
        self.filename_edit.resize(125, 27)

        self.win_button = QPushButton("Процессы", self)
        self.win_button.move(5, 65)
        self.win_button.resize(125, 27)
        self.win_button.clicked.connect(self.open_window_func)

        self.new_button = QPushButton(self)
        self.new_button.setStyleSheet("border-image : url(plus.png);")
        self.new_button.move(135, 31)
        self.new_button.resize(25, 25)
        self.new_button.clicked.connect(self.new_btn_func)

        self.button0 = QPushButton(self)
        self.button0.setStyleSheet("border-image : url(trash0.png);")
        self.button0.move(293, 125)
        self.button0.resize(45, 25)
        self.button0.clicked.connect(self.del_func)

        self.button1 = QPushButton(self)
        self.button1.setStyleSheet("border-image : url(Disk.png);")
        self.button1.move(295, 65)
        self.button1.resize(45, 25)
        self.button1.clicked.connect(self.save_btn_func)

        self.button2 = QPushButton(self)
        self.button2.setStyleSheet("border-image : url(Zametka.png);")
        self.button2.move(305, 35)
        self.button2.resize(25, 25)
        self.button2.clicked.connect(self.open_btn_func)

        self.button3 = QPushButton(self)
        self.button3.setStyleSheet("border-image : url(Stars.png);")
        self.button3.move(300, 90)
        self.button3.resize(35, 35)
        self.button3.clicked.connect(self.favourit_func)

        self.button4 = QPushButton(self)
        self.button4.setStyleSheet("border-image : url(Zametka.png);")
        self.button4.move(305, 215)
        self.button4.resize(25, 25)
        self.button4.clicked.connect(self.open_fav_btn_func)

        self.button5 = QPushButton(self)
        self.button5.setStyleSheet("border-image : url(Disk.png);")
        self.button5.move(295, 245)
        self.button5.resize(45, 25)
        self.button5.clicked.connect(self.save_fav_btn_func)

        self.button6 = QPushButton(self)
        self.button6.setStyleSheet("border-image : url(Zapret.png);")
        self.button6.move(305, 275)
        self.button6.resize(25, 25)
        self.button6.clicked.connect(self.del_favourit_func)

        self.save_button = QPushButton("Сохранить", self)
        self.save_button.move(175, 65)
        self.save_button.resize(125, 27)
        self.save_button.clicked.connect(self.save_btn_func)

        self.open_button = QPushButton("Открыть", self)
        self.open_button.move(175, 35)
        self.open_button.resize(125, 27)
        self.open_button.clicked.connect(self.open_btn_func)

        self.favourit = QPushButton("В Избранное", self)
        self.favourit.move(175, 95)
        self.favourit.resize(125, 27)
        self.favourit.clicked.connect(self.favourit_func)

        self.favourit_text = QLabel("Избранное:", self)
        self.favourit_text.move(175, 155)
        self.favourit_text.resize(150, 27)

        self.del_fail = QPushButton("Удалить", self)
        self.del_fail.move(175, 125)
        self.del_fail.resize(125, 27)
        self.del_fail.clicked.connect(self.del_func)

        self.fav_save_button = QPushButton("Сохранить", self)
        self.fav_save_button.move(175, 245)
        self.fav_save_button.resize(125, 27)
        self.fav_save_button.clicked.connect(self.save_fav_btn_func)

        self.fav_open_button = QPushButton("Открыть", self)
        self.fav_open_button.move(175, 215)
        self.fav_open_button.resize(125, 27)
        self.fav_open_button.clicked.connect(self.open_fav_btn_func)

        self.del_favourit = QPushButton("Убрать", self)
        self.del_favourit.move(175, 275)
        self.del_favourit.resize(125, 27)
        self.del_favourit.clicked.connect(self.del_favourit_func)

        self.text_edit = QPlainTextEdit(self)
        self.text_edit.move(350, 5)
        self.text_edit.resize(280, 300)

        self.combo_box = QComboBox(self)
        self.combo_box.move(170, 5)
        self.combo_box.resize(150, 27)
        self.combo_box.addItem("Первая заметка")

        self.favourit_box = QComboBox(self)
        self.favourit_box.move(170, 185)
        self.favourit_box.resize(150, 27)


    def new_btn_func(self):
        if self.filename_edit.text() != '':
            self.combo_box.addItem(self.filename_edit.text())
            with open(self.filename_edit.text(), "w", encoding="utf-8") as file:
                file.write("")
            self.filename_edit.setText("")
        else:
            pass

    def save_btn_func(self):
        with open(self.combo_box.currentText(), "w", encoding="utf-8") as file:
            plain_text = self.text_edit.toPlainText()
            file.write(plain_text)

    def open_btn_func(self):
        try:
            with open(self.combo_box.currentText(), "r", encoding="utf-8") as file:
                data = file.read()
                if data == "":
                    self.text_edit.setPlainText("")
                else:
                    self.text_edit.setPlainText(data)
        except FileNotFoundError:
            pass

    def favourit_func(self):
        self.favourit_box.addItem(self.combo_box.currentText())

    def del_func(self):
        favourit = self.combo_box.currentIndex()
        self.combo_box.removeItem(favourit)

    def save_fav_btn_func(self):
        with open(self.favourit_box.currentText(), "w", encoding="utf-8") as file:
            plain_text = self.text_edit.toPlainText()
            file.write(plain_text)

    def open_fav_btn_func(self):
        try:
            with open(self.favourit_box.currentText(), "r", encoding="utf-8") as file:
                data = file.read()
                if data == "":
                    self.text_edit.setPlainText("")
                else:
                    self.text_edit.setPlainText(data)
        except FileNotFoundError:
            pass

    def del_favourit_func(self):
        favourit = self.favourit_box.currentIndex()
        self.favourit_box.removeItem(favourit)

    def open_window_func(self):
        self.w1 = Window1()
        self.w1.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Notes()
    window.show()
    sys.exit(app.exec())