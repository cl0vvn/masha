from PyQt5 import QtCore, QtGui, QtWidgets
from ui import Ui_Masha
import sys
import os
import configparser
import webbrowser
config = configparser.ConfigParser()
config.read("config.ini", 'utf-8')


app = QtWidgets.QApplication(sys.argv)

Masha = QtWidgets.QWidget()
ui = Ui_Masha()
ui.setupUi(Masha)
Masha.show()

def startAssistant():
    os.system('start main.py')
def indexnfo():
    os.system('start get_microphone.py')
def setindex():
    print(ui.lineEdit.text())
    config['System']['microphone_index'] = ui.lineEdit.text()
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
def info():
    webbrowser.open_new('https://github.com/cl0vvn/masha/wiki/Индекс-микрофона')

ui.startbtn.clicked.connect(startAssistant)
ui.indexknow.clicked.connect(indexnfo)
ui.lineEdit.textChanged.connect(setindex)
ui.infoindex.clicked.connect(info)

sys.exit(app.exec_())
