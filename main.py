from GoogleTranslateUI import *
from PyQt5.QtWidgets import *


def main():
    app = QApplication([])
    window = GoogleTranslateUI()
    app.exec_()


if __name__ == "__main__":

    main()
