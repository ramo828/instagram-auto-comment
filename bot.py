"""
    ###############################
    Created by Mammadli Ramiz
    email: illegalism666@gmail.com
    phone: +994558302766
    ###############################
"""
import bot_library as bl
import time

# print(test.buildRand(20))

if(__name__ == "__main__"):
    rand = ""
    util = bl.utility()
    util.randomize()
    setting = open("settings.txt","r")
    data = setting.read()
    rstatus = util.commandSpliter(data.split("\n")[5])
    rcount = int(util.commandSpliter(data.split("\n")[6]))
    rchoise = int(util.commandSpliter(data.split("\n")[7]))
    util.choise = rchoise
    if(rstatus == "True"):
        rand = util.buildRand(rcount)
    else:
        rand = ""
    kadi = util.commandSpliter(data.split("\n")[0])
    ksifre = util.commandSpliter(data.split("\n")[1])
    san = int(util.commandSpliter(data.split("\n")[2]))
    sayfa = util.commandSpliter(data.split("\n")[3])
    yorum = util.commandSpliter(data.split("\n")[4]+rand)

    auto = bl.autoComment()
    unique = "testData"
    count = 1
    while(True):
        print(f"\nDenetleme süresi: {san}")
        time.sleep(san)
        print(f"\nDeneme sayısı: {count}")
        auto.setAccount(username=kadi, password=ksifre)
        auto.setPage(sayfa)
        auto.setComment(comment=yorum)
        auto.connect()
        auto.getMedia()
        if(count < 2):
            unique = auto.tempCode
        count=count+1
        if(unique != auto.tempCode):
            # print(auto.tempCode)
            auto.send(auto.tempCode)
            print("\nYeni post paylaşıldı və comment yazıldı")
            unique = auto.tempCode
        else:
            print("Yeni paylaşım bulunamadı")
            continue
    