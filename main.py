#-----------------------------Модули----------------------------
import pyaudio
import speech_recognition as sr
import os
import random
import webbrowser
import mouse
import time
import datetime
import configparser
from gtts import gTTS
from playsound import playsound
from text_to_speech import speak
import math
import numexpr as ne
import plyer

#----------------------------Сокращения-------------------------
r = sr.Recognizer()
config = configparser.ConfigParser()

#----------------------------Переменные-------------------------
ok_was = False
zametka = False
oko = True
speech = ''

#----------------------------Код-------------------------
plyer.notification.notify(message='Голосовой помощник запущен',app_name='Masha',app_icon='ICON.ico',title='СТАРТ!')
def tts_speech(text,lang):
    speak(text, lang, save=False)
config.read("config.ini", 'utf-8')
while True:
    with sr.Microphone(device_index=int(config["System"]["microphone_index"])) as source:
        print('Скажите шо нить плз)')
        #r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        speech = r.recognize_google(audio, language='ru_RU').lower()
    except:
        print('Вы ничего не сказали')
        pass
    print('Вы сказали: '+speech)

#----------------------------Будильник-----------------------------
    h = open(r'alarm/hour.txt')
    m = open(r'alarm/minute.txt')
    time_now = datetime.datetime.now()
    if str(h.read()) == str(time_now.hour) and str(m.read()) == str(time_now.minute):
        playsound("media/audio/alarm.mp3")
        h = open(r'alarm/hour.txt','w')
        m = open(r'alarm/minute.txt','w')

        h.write('')
        m.write('')

        h.close()
        m.close()
        plyer.notification.notify(message='Внимание! Будильник прозвенел!',app_name='Masha',app_icon='ICON.ico',title='Будильник!')
    h.close()
    m.close()

#-----------------------------Фразы-----------------------------
    if speech == "о'кей маша" and ok_was != True:
        tts_speech('Слушаю', 'ru')
        ok_was = True
    print(ok_was)
    if ok_was:
        if speech.startswith('открой сайт'):
            webbrowser.open_new('https://'+speech[12:])
            tts_speech('Открываю', 'ru')
            ok_was = False
            plyer.notification.notify(message='Открываю сайт '+speech[12:],app_name='Masha',app_icon='ICON.ico',title='Сайт')
        elif speech.startswith('посчитай '):
            speech = speech.replace("посчитай ","")
            speech = speech.replace("в степени ","**")
            speech = speech.replace("встепен ","**")
            speech = speech.replace("степен ","**")
            speech = speech.replace("х","*")
            speech = speech.replace(" ","")
            speech = speech.replace("и","")
            print(speech)
            solve = ne.evaluate(speech)
            print(solve)
            tts_speech(str(solve), 'ru')
            plyer.notification.notify(message=speech,app_name='Masha',app_icon='ICON.ico',title=str(solve))
        elif speech.startswith('поставь будильник на '):
            speech = speech.replace("поставь будильник на ","")
            speech = speech.replace("минута ","")
            speech = speech.replace("минуту ","")
            speech = speech.replace("минуты ","")
            speech = speech.replace(" минута ","")
            speech = speech.replace(" минуту ","")
            speech = speech.replace(" минуты ","")
            if speech[1] == ':':
                speech = '0' + speech
            hour = speech[:2]
            print(hour)
            speech = speech[3:]
            if speech[1] == ' ':
                speech = '0' + speech
            minutes = speech
            print(minutes)
            h = open(r'alarm/hour.txt','w')
            m = open(r'alarm/minute.txt','w')

            h.write(str(hour))
            m.write(str(minutes))

            h.close()
            m.close()

            tts_speech('Будильник разбудит вас в '+hour+':'+minutes, 'ru')
            plyer.notification.notify(message='Будильник поставлен на '+hour+':'+minutes,app_name='Masha',app_icon='ICON.ico',title='Будильник')
            ok_was = False
        elif speech.startswith('найди'):
            speech = speech.replace("мне ",'')
            speech = speech.replace("найди ",'')
            webbrowser.open_new('https://www.google.com/search?q='+speech)
            tts_speech('Ищу специально для вас', 'ru')
            ok_was = False
            plyer.notification.notify(message='Ищу '+speech,app_name='Masha',app_icon='ICON.ico',title='Ищу')
        time.sleep(0.1)
    speech = ''