import datetime
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QThread, QObject, pyqtSignal as Signal, pyqtSlot as Slot
import threading as td
import sys
import Ui_basic
import time
import bot_library as bl



class Worker(QObject):
    flag = True
    log = Signal(str)
    def stopBot(self, flag):
        self.flag = flag
    
    def runBot(self):
        util = bl.utility()
        d = bl.Data()
        util.randomize()
        unique = "testData"
        terminal = ""
        count = 1
        self.log.emit("Çalışıyor...")
        kadi = util.commandSpliter(d.load_data(index=0))
        ksifre = util.commandSpliter(d.load_data(index=1))
        san = int(util.commandSpliter(d.load_data(index=2)))
        sayfa = util.commandSpliter(d.load_data(index=3))
        rstatus = util.commandSpliter(d.load_data(index=5))
        rcount = int(util.commandSpliter(d.load_data(index=6)))
        yorum = util.commandSpliter(d.load_data(index=4))
        if(rstatus == "True"):
            rand = util.buildRand(rcount)
        else:
            rand = ""
        auto = bl.autoComment()
        if(self.flag!=True):
            self.log.emit("Durduruldu...")
        while(self.flag):
            an = datetime.datetime.now()
            saat = datetime.datetime.strftime(an, '%X') # Saat
            terminal += (f"\n{saat} >> Denetleme süresi: {san}")
            time.sleep(san)
            if(self.flag != True):
                break
            terminal += (f"\n{saat} >> Deneme sayısı: {count}")
            auto.setAccount(username=kadi, password=ksifre)
            auto.setPage(sayfa)
            auto.setComment(comment=yorum+rand)
            auto.connect()
            if(self.flag != True):
                break
            auto.getMedia()
            if(count < 2):
                unique = auto.tempCode
            count=count+1
            if(unique != auto.tempCode):
                # print(auto.tempCode)
                auto.send(auto.tempCode)
                if(self.flag != True):
                    break
                terminal += (f"\n{saat} >> Yeni post paylaşıldı və comment yazıldı")
                unique = auto.tempCode
            else:
                if(self.flag != True):
                    break
                terminal += (f"\n{saat} >> Yeni paylaşım bulunamadı")
                print(terminal)
                self.log.emit(terminal)
                continue

class Pencere(QMainWindow, Ui_basic.Ui_instaBot):

    def __init__(self):
        super().__init__()
        self.work = Worker()
        self.flag = True
        self.setWindowTitle("Instagram")
        self.setupUi(self)
        self.loadSettingData()
        self.start.clicked.connect(self.click)
        # self.start.clicked.connect(self.save)
        self.save_settings.clicked.connect(self.save)
        self.work.log.connect(self.terminal.setPlainText)
    
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