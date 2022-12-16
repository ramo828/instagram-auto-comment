from PyQt6.QtCore import QThread, QObject, pyqtSignal as Signal, pyqtSlot as Slot
from PyQt6.QtGui import QTextCursor
import bot_library as bl
import datetime
import time


class Worker(QObject):
    flag = True
    log = Signal(str)

        
    def stopBot(self, flag):
        self.flag = flag
    
    def runBot(self):      
        util = bl.utility()
        d = bl.Data()
        # util.randomize()
        unique = "testData"
        count = 1
        self.log.emit("Çalışıyor...")
        kadi = d.load_data(index=0)
        ksifre = d.load_data(index=1)
        san = int(d.load_data(index=2))
        sayfa =  d.load_data(index=3)
        rstatus =  d.load_data(index=5)
        rcount = int( d.load_data(index=6))
        yorum =  d.load_data(index=4)
        rchoise = int( d.load_data(index=7))
        util.choise = rchoise
        if(rstatus == "True"):
            yorum += util.buildRand(rcount)
        auto = bl.autoComment()
        if(self.flag!=True):
            self.log.emit("Durduruldu...")
        while(self.flag):
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
            auto.getMedia()
            if(count < 2):
                unique = auto.tempCode
            count=count+1
            if(unique != auto.tempCode):
                # print(auto.tempCode)
                auto.send(auto.tempCode)
                if(self.flag != True):
                    break
                self.log.emit(f"\n{saat} >> Yeni post paylaşıldı və comment yazıldı")
                unique = auto.tempCode
            else:
                if(self.flag != True):
                    break
                self.log.emit(f"\n{saat} >> Yeni paylaşım bulunamadı")
                
                continue
