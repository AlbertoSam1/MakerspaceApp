import sys

from PySide2.QtCore import QCoreApplication, QEvent, Qt, QTimer, QUrl
from PySide2.QtGui import QKeyEvent
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtWebEngineWidgets import QWebEngineView

KEYMAP = {
    "a": Qt.Key_A,
    "b": Qt.Key_B,
    "c": Qt.Key_C,
    "d": Qt.Key_D,
    "e": Qt.Key_E,
    "f": Qt.Key_F,
    "g": Qt.Key_G,
    "h": Qt.Key_H,
    "i": Qt.Key_I,
    "j": Qt.Key_J,
    "k": Qt.Key_K,
    "l": Qt.Key_L,
    "m": Qt.Key_M,
    "n": Qt.Key_N,
    "o": Qt.Key_O,
    "p": Qt.Key_P,
    "q": Qt.Key_Q,
    "r": Qt.Key_R,
    "s": Qt.Key_S,
    "t": Qt.Key_T,
    "u": Qt.Key_U,
    "v": Qt.Key_V,
    "w": Qt.Key_W,
    "x": Qt.Key_X,
    "y": Qt.Key_Y,
    "z": Qt.Key_Z,
    "1": Qt.Key_1,
    "2": Qt.Key_2,
    "3": Qt.Key_3,
    "4": Qt.Key_4,
    "5": Qt.Key_5,
    "6": Qt.Key_6,
    "7": Qt.Key_7,
    "8": Qt.Key_8,
    "9": Qt.Key_9,
    "0": Qt.Key_0,
    ".": Qt.Key_Period,
    "'": Qt.Key_Apostrophe,
}


def write_text(widget, text):
    for letter in text:
        key = KEYMAP.get(letter.lower(), Qt.Key_unknown)
        event = QKeyEvent(QEvent.KeyPress, key, Qt.NoModifier, letter)
        QCoreApplication.postEvent(widget.focusProxy(), event)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.browser = QWebEngineView()
        self.browser.load(
            QUrl("https://miu2021.monday.com/auth/login_monday/email_password")
        )
        self.setCentralWidget(self.browser)

        self.browser.loadFinished.connect(self.handle_load_finished)

    def handle_load_finished(self, ok):
        if ok:
            QTimer.singleShot(100, self.write_email)
        else:
            print("Could not load page")

    def write_email(self, *args):
        self.browser.page().runJavaScript(
            """let ap = document.querySelector('#user_email')
                ap.focus();""",
            0,
            self.callback_email,
        )

    def callback_email(self, *args):
        write_text(self.browser, "xts229@my.utsa.edu")
        QTimer.singleShot(100, self.write_password)

    def write_password(self):
        self.browser.page().runJavaScript(
            """let pa = document.querySelector('#user_password');
                pa.focus();""",
            0,
            self.callback_password,
        )

    def callback_password(self, *args):
        write_text(self.browser, "Hc8w&@8pa")
        QTimer.singleShot(100, self.click)

    def click(self):
        self.browser.page().runJavaScript(
            """let btn = document.getElementsByTagName('button')[0];
                btn.focus();
                btn.click();"""
        )


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()