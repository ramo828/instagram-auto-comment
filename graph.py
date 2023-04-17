from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit
from PyQt6.QtCore import QThread, QObject, pyqtSignal as Signal, pyqtSlot as Slot
from PyQt6.QtGui import QTextCursor

import threading as td
import sys
import Ui_basic
import bot_library as bl
from worker import Worker


class Pencere(QMainWindow, Ui_basic.Ui_instaBot):

    def __init__(self):
        super().__init__()
        bl.Data()
        self.work = Worker()
        self.flag = True
        self.pinflag = False
        self.show_password_flag = False
        self.setWindowTitle("Instagram")
        self.setupUi(self)
        self.loadSettingData()
        self.start.clicked.connect(self.click)
        self.save_settings.clicked.connect(self.save)
        self.work.log.connect(self.writeEnd)
        self.actionSiyah.triggered.connect(self.themeBlack)
        self.actionMavi.triggered.connect(self.themeBlue)
        self.actionKirmizi.triggered.connect(self.themeRed)
        self.actionSari.triggered.connect(self.themeYellow)
        self.show_passord.clicked.connect(self.show_password)
        self.pin_bypass.clicked.connect(self.enablePinSkip)
        self.work.success_counter_signal.connect(self.success_counter.setText)
        self.work.try_counter_signal.connect(self.try_counter.setText)
        self.comment_skip_number.setReadOnly(True)
        self.comment_skip_number.setPlaceholderText("0")

        # diqqet
    
    def enablePinSkip(self,ch):
        if(ch):
            if(len(self.comment_skip_number.text()) == 0):
                self.comment_skip_number.setText("0")
            self.pinFlag = True
            self.comment_skip_number.setStyleSheet("""
            color: rgb(0,0,0);
            background-color: rgb(255, 255, 255);
            """)
            self.comment_skip_number.setReadOnly(False)
            self.pin_bypass.setText("Pasiv")
        else:
            self.pinFlag = False
            self.pin_bypass.setText("0")
            self.comment_skip_number.clear()
            self.comment_skip_number.setStyleSheet("""
            color: rgb(222, 221, 218);
            background-color: rgb(222, 221, 218);
            """)
            self.pin_bypass.setText("Aktiv")
            self.comment_skip_number.setReadOnly(True)




    def writeEnd(self,message):
            cursor1 = QTextCursor(self.terminal.textCursor())
            cursor1.movePosition(cursor1.MoveOperation.Down)
            self.terminal.setTextCursor(cursor1)
            self.terminal.insertPlainText(message)

    def show_password(self):
        if(self.show_password_flag):
            self.password.setEchoMode(self.password.echoMode().Password)
            self.show_passord.setText("Şifreyi göster")
            self.show_password_flag = False
        else:
            self.password.setEchoMode(self.password.echoMode().Normal)
            self.show_passord.setText("Şifreyi gizle")
            self.show_password_flag = True



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
        color: rgb(249, 240, 107);
        """)
       
    def themeRed(self):
        self.red()
        self.try_counter.setStyleSheet(
            """
                    color: rgb(249, 240, 107);
            
            """
        )
        self.success_counter.setStyleSheet(
            """
                    color: rgb(249, 240, 107);
            
            """
        )
        self.terminal.setStyleSheet("""
        background-color: rgb(246, 97, 81);
        color: rgb(80, 96, 191);
        """)

    def yellow(self):
        self.homePage.setStyleSheet("""
        background-color:  rgb(249, 240, 107);
        color: rgb(67, 105, 141);
        """)
       
    def themeYellow(self):
        self.yellow()
        self.terminal.setStyleSheet("""
        color: rgb(0, 0, 128);
        background-color: rgb(75,104,184);
        """)
    

    def click(self):
        if self.flag == True:
            self.start.setText("Durdur")
            self.flag = False
        else:
            self.start.setText("Başla")
            self.flag = True
        self.thread1 = td.Thread(target=self.work.runBot, daemon=True)
        if(self.flag):
            print("Durdu")
            # self.thread.start()
            self.work.stopBot(False)
        else:
            print("Calisdi")
            self.terminal.clear()
            self.work.stopBot(True)
            self.thread1.start()


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
        comment_number = self.comment_skip_number.text()
        if(len(comment_number) > 0 and comment_number.isdigit() and self.pin_bypass.isChecked()):
            comment_number = int(comment_number)
        else:
            comment_number = 0
            self.comment_skip_number.setText("0")
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
        comment_number
                )
    
    def loadSettingData(self):
        util = bl.utility()
        d = bl.Data()
        util.randomize()
        kadi =d.load_data(index=0)
        ksifre = d.load_data(index=1)
        san = int(d.load_data(index=2))
        sayfa =d.load_data(index=3)
        rstatus = d.load_data(index=5)
        rcount = int(d.load_data(index=6))
        rchoise = int(d.load_data(index=7))
        comment_number = int(d.load_data(index=8))
        yorum = d.load_data(index=4)
        self.comment.setPlainText(yorum)
        self.page_name.setText(sayfa)
        self.san.setValue(san)
        self.char_number.setValue(rcount)
        self.password.setText(ksifre)
        self.login.setText(kadi)
        self.comment_skip_number.setText(str(comment_number))
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