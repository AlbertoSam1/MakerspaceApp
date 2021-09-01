# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

import sys

from PySide2.QtCore import QCoreApplication, QEvent, Qt, QTimer, QUrl
from PySide2.QtGui import QKeyEvent
from PySide2.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile

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


class PyWebView(QWebEngineView):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.page().profile().cookieStore().deleteAllCookies()
        self.username = None
        self.password = None

    def set_url(self, url, *args):
        self.username = args[0][0]
        self.password = args[0][1]
        self.load(
            QUrl(url)
        )

        self.loadFinished.connect(self.handle_load_finished)

    def handle_load_finished(self, ok):
        if ok:
            QTimer.singleShot(100, self.write_email)
        else:
            print("Could not load page")

    def write_email(self, *args):
        self.page().runJavaScript(
            """let ap = document.querySelector('#user_email')
                ap.focus();""",
            0,
            self.callback_email,
        )

    def callback_email(self, *args):
        write_text(self, self.username)
        QTimer.singleShot(100, self.write_password)

    def write_password(self):
        self.page().runJavaScript(
            """let pa = document.querySelector('#user_password');
                pa.focus();""",
            0,
            self.callback_password,
        )

    def callback_password(self, *args):
        write_text(self, self.password)
        QTimer.singleShot(100, self.click)

    def click(self):
        self.page().runJavaScript(
            """let btn = document.getElementsByTagName('button')[0];
                btn.focus();
                btn.click();"""
        )

    def change_url(self, url):
        self.setUrl(QUrl(url))
