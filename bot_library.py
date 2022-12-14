from instagrapi import Client
import random as rd


class Data:
    def __init__(self):
        pass

    def load_data(self,index = 0):
        setting_data = open("settings.txt","r")
        data = setting_data.read()
        return data.split("\n")[index]

    def save_data(self,*args):
        setting_data = open("settings.txt","w")
        for split_data in args:
            setting_data.write(f" : {split_data}\n")


class utility:
    def __init__(self, choise = 0):
        self.choise = choise
    
    def randomize(self):
        char = ""
        alpha = "abcdefghjklmnopqrstuvxyzw"
        numeric = "0123456789"
        symbol = "~!@#$%^&*()_+:'"
        if(self.choise == 0):
            rand = rd.randint(0, len(alpha)-1)
            char = alpha[rand]
        elif (self.choise == 1):
            rand = rd.randint(0, len(numeric)-1)
            char = numeric[rand]
        elif (self.choise == 2):
            rand = rd.randint(0, len(symbol)-1)
            char = symbol[rand]
        return char

    def buildRand(self, length):
        ch =""
        for i in range(length):
            ch = ch + self.randomize()
        return ch
    
    def commandSpliter(self, data):
        index = data.find(":")
        return data[index+2:len(data)]





class autoComment:

    def __init__(self, url="https://www.instagram.com/p/", temp_code=""):
        self.url = url
        self.tempCode = temp_code
        self.medias = []
        self.user_id = ""
        self.cl = Client()
        # call instapi client
       

    def setAccount(self, username, password):
        self.username = username
        self.password = password
        # Login ve sifre
    def connect(self):
        self.cl.login(self.username, self.password)
        self.user_id = self.cl.user_id_from_username(self.page)
        # instagram page
       

    def getMedia(self):
        self.medias = self.cl.user_medias(self.user_id, 5)
        # page media (max=5)
        latest_post = self.medias[0].code
        # latest post code
        self.tempCode = latest_post
        # tamper code
        self.url = self.url
        # instagram post link

    def setPage(self, page):
        self.page = page

    def setComment(self, comment):
        self.comment = comment

    def send(self, code):
        media_id = self.cl.media_id(self.cl.media_pk_from_url(self.url+code))
        # latest post id
        comment = self.cl.media_comment(media_id, self.comment)
        # comment   