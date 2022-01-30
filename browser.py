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

        #home button
        home_button = QAction('Home', self)
        # navigate in chosen page by pressing enter
        home_button.triggered.connect(self.navigate_home)
        navbar.addAction(home_button)

        #URL bar
        self.url_bar = QLineEdit() 
        self.url_bar.returnPressed.connect(self.navigate_url)
        navbar.addWidget(self.url_bar) 


    def navigate_home(self):
        self.browser.setUrl(QUrl('https://github.com/deborafsm'))
    def navigate_url(self):
        url = self.url_bar.text()   
        self.browser.setUrl(QUrl(url))



app = QApplication(sys.argv)
QApplication.setApplicationName('Pixie Browser')
window = MainWindow()

app.exec_()