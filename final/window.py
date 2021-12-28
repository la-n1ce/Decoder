import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

from all_windows import *

from all_decoders import *


def WriteFile(name, text):
    new_file = open(name, "w+")
    new_file.write(text)
    new_file.close()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Decoder")
        self.setWindowIcon(QIcon('icon.png'))

        self.ascii.clicked.connect(self.Asci)
        self.sibir.clicked.connect(self.Sib)
        self.xeming.clicked.connect(self.Xem)
        self.CC.clicked.connect(self.C)
        self.elias.clicked.connect(self.El)
        self.text_format.clicked.connect(self.form)

    def Asci(self):
        self.asci_window = AsciiWindow()
        self.asci_window.setWindowTitle("ASCII-1251")
        self.asci_window.show()

    def Sib(self):
        self.sibir_window = SibirskyWindow()
        self.sibir_window.setWindowTitle("Sibirski")
        self.sibir_window.show()

    def Xem(self):
        self.xeming_window = XemingWindow()
        self.xeming_window.setWindowTitle("Xeming")
        self.xeming_window.show()

    def C(self):
        self.cc_window = CCWindow()
        self.cc_window.setWindowTitle("cc")
        self.cc_window.show()

    def El(self):
        self.elias_window = EliasWindow()
        self.elias_window.setWindowTitle("Elias")
        self.elias_window.show()

    def form(self):
        self.form_window = FormatWindow()
        self.form_window.setWindowTitle("Text set form")
        self.form_window.show()


class AsciiWindow(QMainWindow, Ui_second_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.run.clicked.connect(self.do)

    def do(self):
        text = self.code.toPlainText()
        text = text.replace('\n', ' ').replace('\t', ' ')
        encode = ascii_decode(text.split())
        if encode == "error":
            self.error = Errorwindow("245 255 236\nВ десятичной системе!")
            self.error.show()
        else:
            self.decode.setText(encode[:-1])
            WriteFile("output.txt", str(encode[:-1]))


class SibirskyWindow(QMainWindow, Ui_second_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.run.clicked.connect(self.do)

    def do(self):
        text = self.code.toPlainText()
        encode = sibirsky(text)
        if encode == "error":
            self.error = Errorwindow("я нюпм!о =)\nЛюбые символы!")
            self.error.show()
        else:
            self.decode.setText(encode[:-1])
            WriteFile("output.txt", str(encode[:-1]))


class XemingWindow(QMainWindow, Ui_second_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.run.clicked.connect(self.do)

    def do(self):
        text = self.code.toPlainText()
        text = text.replace('\n', ' ').replace('\t', ' ')
        encode = xeming_decoder(list(text.split()))
        if encode == "error":
            self.error = Errorwindow("111111101111000 111111101111000\nВ двочной системе!")
            self.error.show()
        else:
            self.decode.setText(encode)
            WriteFile("output.txt", str(encode))


class CCWindow(QMainWindow, Ui_CC_Window):
        def __init__(self):
            super().__init__()
            self.setupUi(self)
            self.run.clicked.connect(self.do)
            self.set.clicked.connect(self.set_text)

        def set_text(self):
            self.cc2.setText('')
            self.cc8.setText('')
            self.cc10.setText('')
            self.cc16.setText('')

        def do(self):
            numbers16 = []
            numbers10 = []
            numbers8 = []
            numbers2 = []

            try:
                if self.cc2.toPlainText() != '':
                    for num in list(self.cc2.toPlainText().split()):
                        numbers16.append(hex(int(num, 2))[2:])
                        numbers10.append(str(int(num, 2)))
                        numbers8.append(oct(int(num, 2))[2:])
                        numbers2.append(bin(int(num, 2))[2:])

                elif self.cc8.toPlainText() != '':
                    for num in list(self.cc8.toPlainText().split()):
                        numbers16.append(hex(int(num, 8))[2:])
                        numbers10.append(str(int(num, 8)))
                        numbers8.append(oct(int(num, 8))[2:])
                        numbers2.append(bin(int(num, 8))[2:])

                elif self.cc10.toPlainText() != '':
                    for num in list(self.cc10.toPlainText().split()):
                        numbers16.append(hex(int(num))[2:])
                        numbers10.append(str(int(num)))
                        numbers8.append(oct(int(num))[2:])
                        numbers2.append(bin(int(num))[2:])

                elif self.cc16.toPlainText() != '':
                    for num in list(self.cc16.toPlainText().split()):
                        numbers16.append(hex(int(num, 16))[2:])
                        numbers10.append(str(int(num, 16)))
                        numbers8.append(oct(int(num, 16))[2:])
                        numbers2.append(bin(int(num, 16))[2:])

                self.cc16.setText(' '.join(numbers16))
                self.cc10.setText(' '.join(numbers10))
                self.cc8.setText(' '.join(numbers8))
                self.cc2.setText(' '.join(numbers2))

            except Exception:
                self.error = Errorwindow("101101101\nВведи в правильной системе счисления!")
                self.error.show()


class EliasWindow(QMainWindow, Ui_second_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.run.clicked.connect(self.do)

    def do(self):
        text = self.code.toPlainText()
        text = text.replace('\n', '').replace('\t', '').replace(' ', '')
        encode = elias_decoder(text)
        if encode == "error":
            self.error = Errorwindow("101101101\nВ двоичной системе!")
            self.error.show()
        else:
            self.decode.setText(encode)
            WriteFile("output.txt", str(encode))


class Errorwindow(QMainWindow, Ui_Error):
    def __init__(self, error_text):
        super().__init__()
        self.setupUi(self)
        self.format_input.setText(error_text)
        self.button_ok.clicked.connect(self.do)

    def do(self):
        self.close()


class FormatWindow(QMainWindow, Ui_Format_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.to_8.clicked.connect(self.format_to_8)
        self.to_14.clicked.connect(self.format_to_14)
        self.set_zero.clicked.connect(self.delite_zero)

    def format_to_8(self):
        text = self.pole_input.toPlainText()
        text = text.replace('\n', '').replace('\t', '').replace(' ', '')
        tmp = []
        if len(text) != len(text) // 8 * 8:
            for i in range(len(text) // 8 + 1):
                tmp.append(text[:8])
                text = text[8:]
        else:
            for i in range(len(text) // 8):
                tmp.append(text[:8])
                text = text[8:]
        self.pole_output.setText(' '.join(tmp))

    def format_to_14(self):
        text = self.pole_input.toPlainText()
        text = text.replace('\n', '').replace('\t', '').replace(' ', '')
        tmp = []
        if len(text) != len(text) // 15 * 15:
            for i in range(len(text) // 15 + 1):
                tmp.append(text[:15])
                text = text[15:]
        else:
            for i in range(len(text) // 15):
                tmp.append(text[:15])
                text = text[15:]

        self.pole_output.setText(' '.join(tmp))

    def delite_zero(self):
        text = self.pole_input.toPlainText()
        text = text.replace('\n', '').replace('\t', '').replace(' ', '')
        simbols = list(text)
        kol = 0
        while simbols[0] != '1':
            simbols = simbols[1:]
            kol += 1

        self.pole_output.setText(text[kol:])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())