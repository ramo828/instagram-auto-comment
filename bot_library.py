from instagrapi import Client
import random as rd
import sqlite3 as sql
from os.path import exists
from random import randint

class Data:
    def __init__(self):
        self.codec = "utf-8"
        file_exists = exists("base.sqlite")
        self.sql = sql.connect("base.sqlite")
        self.cursor = self.sql.cursor()
        self.cursor.execute("""
        CREATE TABLE if NOT EXISTS settings (
        login TEXT,
        password TEXT, 
        try_time INT, 
        page TEXT, 
        comment TEXT,
        antiban TEXT,
        random_length INT,
        random_choise INT,
        comment_number INT)
        """)
        if(file_exists):
            self.default_data("","",5,"","","True",0,0,0)

    def default_data(self, *args):
        addValue = "INSERT INTO settings VALUES('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}')".format(args[0],args[1],args[2],args[3],args[4],args[5],args[6],args[7],args[8])
        self.cursor.execute(addValue)
        self.sql.commit()

    def load_data(self,index = 0):
        sql = "SELECT * FROM settings"
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data[0][index]

    def save_data(self,*args):
        
        addValue = "UPDATE settings SET login = '{0}',password = '{1}', try_time = '{2}', page = '{3}', comment = '{4}',antiban = '{5}',random_length = '{6}',random_choise = '{7}',comment_number = '{8}'".format(args[0],args[1],args[2],args[3],args[4],args[5],args[6],args[7],args[8])
        self.cursor.execute(addValue)
        self.sql.commit()


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
    
    # def commandSpliter(self, data):
    #     index = data.find(":")
    #     return data[index+2:len(data)]





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
    def setChoise(self, ch, len):
        self.ch = ch
        self.len  = len

    def getMedia(self, commentNo):
        self.medias = self.cl.user_medias(int(self.user_id), 2+commentNo)
        # page media (max=5)
        latest_post = self.medias[commentNo].code
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
        media_pk = self.cl.media_pk_from_url(self.url+code)
        media_id = self.cl.media_id(media_pk=media_pk)
        print(self.cl.media_info(media_pk=media_pk))
        print(media_id)
        # latest post id
        comment = self.cl.media_comment(media_id, self.comment)
        # comment   