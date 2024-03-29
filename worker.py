from PyQt6.QtCore import QThread, QObject, pyqtSignal as Signal, pyqtSlot as Slot
from PyQt6.QtGui import QTextCursor
import bot_library as bl
import datetime
from random import randint
import time


class Worker(QObject):
    flag = True
    log = Signal(str)
    success_counter_signal = Signal(str)
    try_counter_signal = Signal(str)



        
    def stopBot(self, flag):
        self.flag = flag
    
    def runBot(self):      
        util = bl.utility()
        d = bl.Data()
        unique = "testData"
        count = 1
        success_counter = 0
        self.log.emit("Çalışıyor...")
        kadi = d.load_data(index=0)
        ksifre = d.load_data(index=1)
        san = int(d.load_data(index=2))
        sayfa =  d.load_data(index=3)
        rstatus =  d.load_data(index=5)
        rcount = int( d.load_data(index=6))
        yorum =  d.load_data(index=4)
        rchoise = int( d.load_data(index=7))
        comment_number = int( d.load_data(index=8))

        util.choise = rchoise
        auto = bl.autoComment()
        auto.setChoise(rchoise, rcount)
        if(self.flag!=True):
            self.log.emit("Durduruldu...")
        self.try_counter_signal.emit(str(count))
        length = len(yorum.splitlines()) -1
        yorum_temp = yorum.splitlines()
        while(self.flag):
            rnd = randint(0,length)
            print("Length: ",length, rnd)
            yorum = yorum_temp[rnd]
            if(rstatus == "True"):
                yorum += " "+util.buildRand(rcount)
            an = datetime.datetime.now()
            saat = datetime.datetime.strftime(an, '%X') # Saat
            self.log.emit(f"\n{saat} >> Denetleme süresi: {san}")
            time.sleep(san)
            if(self.flag != True):
                break
            self.log.emit(f"\n{saat} >> Deneme sayısı: {count}")
            auto.setAccount(username=kadi, password=ksifre)
            auto.setPage(sayfa)
            print(yorum)
            auto.setComment(comment=yorum)
            auto.connect()
            if(self.flag != True):
                break
            auto.getMedia(comment_number)
            if(count < 2):
                unique = auto.tempCode
            count=count+1
            if(unique != auto.tempCode):
                auto.send(auto.tempCode)
                if(self.flag != True):
                    break
                self.log.emit(f"\n{saat} >> Yeni post paylaşıldı və comment yazıldı")
                unique = auto.tempCode
                success_counter+=1
            else:
                if(self.flag != True):
                    break
                self.log.emit(f"\n{saat} >> Yeni paylaşım bulunamadı")
                self.success_counter_signal.emit(str(success_counter))
                self.try_counter_signal.emit(str(count))
                continue
