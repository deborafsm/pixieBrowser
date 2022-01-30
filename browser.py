import sys
from turtle import back
from PyQt5.QtCore import *
from PyQt5.QtWidgets import * 
from PyQt5.QtWebEngineWidgets import * 



class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://duckduckgo.com/'))
        self.setCentralWidget(self.browser)
        self.showMaximized()


        # NavBar
        navbar = QToolBar()
        self.addToolBar(navbar)
        # back button, back in the ini page.
        back_button = QAction('Back', self)
        back_button.triggered.connect(self.browser.back)
        navbar.addAction(back_button)

app = QApplication(sys.argv)
QApplication.setApplicationName('Pixie Browser')
window = MainWindow()

app.exec_()