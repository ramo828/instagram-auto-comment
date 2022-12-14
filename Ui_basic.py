# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_instaBot(object):
    def setupUi(self, instaBot):
        instaBot.setObjectName("instaBot")
        instaBot.resize(604, 410)
        self.homePage = QtWidgets.QWidget(instaBot)
        self.homePage.setObjectName("homePage")
        self.login = QtWidgets.QLineEdit(self.homePage)
        self.login.setGeometry(QtCore.QRect(20, 20, 161, 26))
        self.login.setObjectName("login")
        self.password = QtWidgets.QLineEdit(self.homePage)
        self.password.setGeometry(QtCore.QRect(20, 60, 161, 26))
        self.password.setObjectName("password")
        self.page_name = QtWidgets.QLineEdit(self.homePage)
        self.page_name.setGeometry(QtCore.QRect(20, 100, 201, 26))
        self.page_name.setObjectName("page_name")
        self.comment = QtWidgets.QPlainTextEdit(self.homePage)
        self.comment.setGeometry(QtCore.QRect(20, 210, 201, 71))
        self.comment.setAccessibleDescription("")
        self.comment.setAutoFillBackground(False)
        self.comment.setTabChangesFocus(False)
        self.comment.setBackgroundVisible(False)
        self.comment.setCenterOnScroll(False)
        self.comment.setObjectName("comment")
        self.d_label = QtWidgets.QLabel(self.homePage)
        self.d_label.setGeometry(QtCore.QRect(20, 143, 141, 18))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.d_label.setFont(font)
        self.d_label.setObjectName("d_label")
        self.k_label = QtWidgets.QLabel(self.homePage)
        self.k_label.setGeometry(QtCore.QRect(20, 181, 121, 18))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.k_label.setFont(font)
        self.k_label.setObjectName("k_label")
        self.san = QtWidgets.QSpinBox(self.homePage)
        self.san.setGeometry(QtCore.QRect(180, 140, 45, 27))
        self.san.setObjectName("san")
        self.char_number = QtWidgets.QSpinBox(self.homePage)
        self.char_number.setGeometry(QtCore.QRect(180, 180, 45, 27))
        self.char_number.setObjectName("char_number")
        self.set_char = QtWidgets.QGroupBox(self.homePage)
        self.set_char.setGeometry(QtCore.QRect(390, 20, 161, 121))
        self.set_char.setObjectName("set_char")
        self.alpha = QtWidgets.QRadioButton(self.set_char)
        self.alpha.setGeometry(QtCore.QRect(10, 30, 109, 24))
        self.alpha.setObjectName("alpha")
        self.number = QtWidgets.QRadioButton(self.set_char)
        self.number.setGeometry(QtCore.QRect(10, 60, 109, 24))
        self.number.setObjectName("number")
        self.symbol = QtWidgets.QRadioButton(self.set_char)
        self.symbol.setGeometry(QtCore.QRect(10, 90, 109, 24))
        self.symbol.setObjectName("symbol")
        self.anti_spam = QtWidgets.QCheckBox(self.homePage)
        self.anti_spam.setGeometry(QtCore.QRect(260, 100, 151, 24))
        self.anti_spam.setObjectName("anti_spam")
        self.save_settings = QtWidgets.QPushButton(self.homePage)
        self.save_settings.setGeometry(QtCore.QRect(20, 310, 201, 26))
        self.save_settings.setObjectName("save_settings")
        self.start = QtWidgets.QPushButton(self.homePage)
        self.start.setGeometry(QtCore.QRect(430, 310, 121, 26))
        self.start.setObjectName("start")
        self.terminal = QtWidgets.QTextEdit(self.homePage)
        self.terminal.setGeometry(QtCore.QRect(260, 160, 291, 121))
        self.terminal.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"color: rgb(52, 233, 41);\n"
"selection-color: rgb(153, 193, 241);")
        self.terminal.setReadOnly(True)
        self.terminal.setObjectName("terminal")
        instaBot.setCentralWidget(self.homePage)
        self.menubar = QtWidgets.QMenuBar(instaBot)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 604, 23))
        self.menubar.setObjectName("menubar")
        self.menuTema = QtWidgets.QMenu(self.menubar)
        self.menuTema.setObjectName("menuTema")
        instaBot.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(instaBot)
        self.statusbar.setObjectName("statusbar")
        instaBot.setStatusBar(self.statusbar)
        self.actionSiyah = QtGui.QAction(instaBot)
        self.actionSiyah.setObjectName("actionSiyah")
        self.actionKirmizi = QtGui.QAction(instaBot)
        self.actionKirmizi.setObjectName("actionKirmizi")
        self.actionBeyaz = QtGui.QAction(instaBot)
        self.actionBeyaz.setObjectName("actionBeyaz")
        self.actionSiyah_2 = QtGui.QAction(instaBot)
        self.actionSiyah_2.setObjectName("actionSiyah_2")
        self.actionBeyaz_2 = QtGui.QAction(instaBot)
        self.actionBeyaz_2.setCheckable(False)
        self.actionBeyaz_2.setObjectName("actionBeyaz_2")
        self.actionYesil = QtGui.QAction(instaBot)
        self.actionYesil.setObjectName("actionYesil")
        self.menuTema.addAction(self.actionSiyah_2)
        self.menuTema.addAction(self.actionBeyaz_2)
        self.menuTema.addAction(self.actionYesil)
        self.menubar.addAction(self.menuTema.menuAction())

        self.retranslateUi(instaBot)
        QtCore.QMetaObject.connectSlotsByName(instaBot)

    def retranslateUi(self, instaBot):
        _translate = QtCore.QCoreApplication.translate
        instaBot.setWindowTitle(_translate("instaBot", "MainWindow"))
        self.login.setPlaceholderText(_translate("instaBot", "Kullanıcı adı"))
        self.password.setPlaceholderText(_translate("instaBot", "Şifre"))
        self.page_name.setPlaceholderText(_translate("instaBot", "Yorum yapılacak sayfa"))
        self.comment.setPlaceholderText(_translate("instaBot", "Yazılacak yorum"))
        self.d_label.setText(_translate("instaBot", "Denetleme süresi:"))
        self.k_label.setText(_translate("instaBot", "Karakter sayısı: "))
        self.set_char.setTitle(_translate("instaBot", "Rastgele Karakter"))
        self.alpha.setText(_translate("instaBot", "Harfler"))
        self.number.setText(_translate("instaBot", "Numaralar"))
        self.symbol.setText(_translate("instaBot", "Semboller"))
        self.anti_spam.setText(_translate("instaBot", "Anti Spam"))
        self.save_settings.setText(_translate("instaBot", "Ayarları kaydet"))
        self.start.setText(_translate("instaBot", "Başla"))
        self.terminal.setHtml(_translate("instaBot", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.menuTema.setTitle(_translate("instaBot", "Tema"))
        self.actionSiyah.setText(_translate("instaBot", "Siyah"))
        self.actionKirmizi.setText(_translate("instaBot", "Kirmizi"))
        self.actionBeyaz.setText(_translate("instaBot", "Beyaz"))
        self.actionSiyah_2.setText(_translate("instaBot", "Siyah"))
        self.actionBeyaz_2.setText(_translate("instaBot", "Beyaz"))
        self.actionYesil.setText(_translate("instaBot", "Yeşil"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    instaBot = QtWidgets.QMainWindow()
    ui = Ui_instaBot()
    ui.setupUi(instaBot)
    instaBot.show()
    sys.exit(app.exec())
