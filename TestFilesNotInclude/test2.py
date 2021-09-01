from PySide2.QtCore import QUrl
from PySide2.QtWidgets import QMainWindow, QApplication
from PySide2.QtWebEngineWidgets import QWebEngineView

import os
import sys


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://miu2021.monday.com/auth/login_monday/email_password"))
        self.setCentralWidget(self.browser)

        self.browser.loadFinished.connect(self.handle_load_finished)

    def handle_load_finished(self, ok):
        if ok:
            print("Page loaded successfully")
            self.browser.page().runJavaScript("let ap = document.querySelector('#user_email');"
                                              "ap.value = 'email@email.com';"
                                              "let pa = document.querySelector('#user_password');"
                                              "pa.value = 'password';"
                                              "let btn = document.getElementsByTagName('button')[0];"
                                              "btn.click();")
        else:
            print("Could not load page")


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()
