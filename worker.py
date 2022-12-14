from PyQt6.QtCore import QThread, QObject, pyqtSignal as Signal, pyqtSlot as Slot
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
