from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QThread, QObject, pyqtSignal as Signal, pyqtSlot as Slot
import threading as td
import sys
import Ui_basic
import bot_library as bl
from worker import Worker


class Pencere(QMainWindow, Ui_basic.Ui_instaBot):

    def __init__(self):
        super().__init__()
        self.work = Worker()
        self.flag = True
        self.setWindowTitle("Instagram")
        self.setupUi(self)
        self.loadSettingData()
        self.start.clicked.connect(self.click)
        self.save_settings.clicked.connect(self.save)
        self.work.log.connect(self.terminal.setPlainText)
        self.actionSiyah_3.triggered.connect(self.themeBlack)
        self.actionMavi.triggered.connect(self.themeBlue)
        self.actionKirmizi_2.triggered.connect(self.themeRed)
        self.actionSari.triggered.connect(self.themeYellow)



        # diqqet
    
    def black(self):
        self.homePage.setStyleSheet("""
        background-color: rgb(119, 118, 123);
        color: rgb(192, 191, 188);
        """)
       
    def themeBlack(self):
        self.black()
        self.terminal.setStyleSheet("""
        color: rgb(222, 221, 218);
        background-color: rgb(61, 56, 70);
        """)

    def blue(self):
        self.homePage.setStyleSheet("""
        background-color: rgb(53, 132, 228);
        color: rgb(153, 193, 241);
        """)
       
    def themeBlue(self):
        self.blue()
        self.terminal.setStyleSheet("""
        color: rgb(4, 54, 241);
        background-color: rgb(80, 96, 191);
        """)
    def red(self):
        self.homePage.setStyleSheet("""
        background-color: rgb(224, 27, 36);
        color: rgb(220, 138, 221);
        """)
       
    def themeRed(self):
        self.red()
        self.terminal.setStyleSheet("""
        background-color: rgb(246, 97, 81);
        color: rgb(80, 96, 191);
        """)

    def yellow(self):
        self.homePage.setStyleSheet("""
        background-color:  rgb(249, 240, 107);
        color: rgb(255, 120, 0)
        """)
       
    def themeYellow(self):
        self.yellow()
        self.terminal.setStyleSheet("""
        color: rgb(247, 244, 178)
        background-color: rgb(229, 165, 10)
        """)
    

    def click(self):
        if self.flag == True:
            self.start.setText("Durdur")
            self.flag = False
        else:
            self.start.setText("Başla")
            self.flag = True

        self.thread = td.Thread(target=self.work.runBot, daemon=True)
        if(self.flag):
            print("Durdu")
            # self.thread.start()
            self.work.stopBot(False)
        else:
            print("Calisdi")
            self.terminal.clear()
            self.work.stopBot(True)
            self.thread.start()


    def save(self):
        d = bl.Data()
        selected_spam = 0
        login = self.login.text()
        password = self.password.text()
        san = self.san.text()
        page_name = self.page_name.text()
        comment = self.comment.toPlainText()
        a_spam = str(self.anti_spam.isChecked())
        random_char = str(self.char_number.text())
        if(self.alpha.isChecked()):
            selected_spam = 0
        elif(self.number.isChecked()):
            selected_spam = 1
        elif(self.symbol.isChecked()):
            selected_spam = 2
        d.save_data(
         login,
         password, 
         san, 
         page_name,
         comment,
         a_spam,
         random_char,
        str(selected_spam),
        "False",
        )
    
    def loadSettingData(self):
        util = bl.utility()
        d = bl.Data()
        test = open("settings.txt","r")
        t = test.read()
        util.randomize()
        kadi = util.commandSpliter(d.load_data(index=0))
        ksifre = util.commandSpliter(d.load_data(index=1))
        san = int(util.commandSpliter(d.load_data(index=2)))
        sayfa = util.commandSpliter(d.load_data(index=3))
        rstatus = util.commandSpliter(d.load_data(index=5))
        rcount = int(util.commandSpliter(d.load_data(index=6)))
        rchoise = int(util.commandSpliter(d.load_data(index=7)))
        # icstatus = util.commandSpliter(d.load_data(index=8))
        yorum = util.commandSpliter(d.load_data(index=4))
        self.comment.setPlainText(yorum)
        self.page_name.setText(sayfa)
        self.san.setValue(san)
        self.char_number.setValue(rcount)
        self.password.setText(ksifre)
        self.login.setText(kadi)
        if(rchoise == 0):
            self.alpha.setChecked(True)
        elif(rchoise == 1):
            self.number.setChecked(True)
        elif(rchoise == 2):
            self.number.setChecked(True)

        if(rstatus == "True"):
            self.anti_spam.setChecked(True)
        else:
            self.anti_spam.setChecked(False)            

    
            

app = QApplication(sys.argv)
pencere = Pencere()
pencere.show()
sys.exit(app.exec())