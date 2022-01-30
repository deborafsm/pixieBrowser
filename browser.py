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

        # back button, back one page in back 
        back_button = QAction('Back', self)
        back_button.triggered.connect(self.browser.back)
        navbar.addAction(back_button)


        # Forward button forward one page in forward
        forward_button = QAction('Forward', self)
        forward_button.triggered.connect(self.browser.forward)
        navbar.addAction(forward_button)

        # Reaload the page
        reload_page = QAction('Reload', self)
        reload_page.triggered.connect(self.browser.reload)
        navbar.addAction(reload_page)

    
app = QApplication(sys.argv)
QApplication.setApplicationName('Pixie Browser')
window = MainWindow()

app.exec_()