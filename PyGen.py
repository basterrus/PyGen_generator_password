from PyQt5 import QtCore, QtGui, QtWidgets
from winform import *
import sys
import clipboard
import random

numbers = '1234567890'
lowcase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
char = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'


class Generator(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.gen = Ui_MainWindow()
        self.gen.setupUi(self)

        self.gen.pushButton.clicked.connect(self.generate)
        self.gen.pushButton_2.clicked.connect(self.clear)
        self.gen.pushButton_3.clicked.connect(self.cp_clipboard)
        self.gen.pushButton_4.clicked.connect(self.about)

    def generate(self):
        alphabet = ''

        if self.gen.checkBox.isChecked():
            alphabet = alphabet + numbers

        if self.gen.checkBox_2.isChecked():
            alphabet = alphabet + uppercase

        if self.gen.checkBox_3.isChecked():
            alphabet = alphabet + lowcase

        if self.gen.checkBox_4.isChecked():
            alphabet = alphabet + char

        for quantity in range(self.gen.spinBox_2.value()):
            password = ''
            for passwordsize in range(self.gen.spinBox.value()):
                password += random.choice(alphabet)
            self.gen.plainTextEdit.appendPlainText(password)

    def cp_clipboard(self):
        password = self.gen.plainTextEdit.toPlainText()
        if password == '':
            QtWidgets.QMessageBox.warning(self, 'Ошибка', 'Нет текста!')
        else:
            clipboard.copy(password)
            QtWidgets.QMessageBox.information(self, 'Выполнено', 'Пароль скопирован в буфер!')

    def clear(self):
        self.gen.checkBox.setChecked(True)
        self.gen.checkBox_2.setChecked(True)
        self.gen.checkBox_3.setChecked(True)
        self.gen.checkBox_4.setChecked(False)
        self.gen.plainTextEdit.clear()
        self.gen.spinBox.setValue(6)
        self.gen.spinBox_2.setValue(1)
        QtWidgets.QMessageBox.information(self, 'Выполнено', 'Поля очищены!')

    def about(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setWindowTitle('О программе')
        msg.setInformativeText('Подробности ShowDetails')
        msg.setDetailedText('Author : Pavel Nedoshivin\n'
                            'NameProg: PyGen\n'
                            'Use Lib: PyQt5, clipboard, random\n'
                            'GitHub: https://github.com/basterrus')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        item = msg.exec_()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gen = Generator()
    gen.show()
    sys.exit(app.exec_())
