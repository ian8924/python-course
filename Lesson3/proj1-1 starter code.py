# 是一個文字到語音(text to speech)的 Python Library
# 如果import pyttsx3遇到錯誤另外需要 pip install pypiwin32
# pip3 install pyttsx3
import pyttsx3 
import datetime
import os

# Lesson 3 設定
# pyaudio
# install code to path

# step 1: 必須要呼叫init()來得到 pyttsx3 的engine物件
# https://pypi.org/project/pyttsx3/

engine = pyttsx3.init()

# engine.say('hello')
# engine.runAndWait()
# step 2: 如何選擇AI助理說的語言呢
# https://pyttsx3.readthedocs.io/en/latest/engine.html#module-pyttsx3.voice
# Mac: 25
# Window: 0
# index=0
# for voice in voices:
#     print("Voice: %s" % voice.name)
#     print(" - ID: %s" % voice.id)
#     print(" - Languages: %s" % voice.languages)
#     print(" - Gender: %s" % voice.gender)
#     print(" - Age: %s" % voice.age)
#     print(" - index: %s" % index)
#     index = index + 1
#     print("\n")
# step 3: 設定語音助理的語言為中文
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[25].id)
# step 4: 找出現在時間
# https://docs.python.org/3/library/datetime.html
# current_date=datetime.date.day
time = datetime.datetime.now().hour
print(time)
if time>=0 and time<12:
    engine.say('早安')
elif time>=12 and time<18:
    engine.say('午安')
else:
    engine.say('晚安')
engine.runAndWait()
# Assignment 
# step 5: 讓語音助理依照時間不同作出回應
# 1. hour 介在0和12之間 -> 說出早安
# 2. hour 介在12和18之間 -> 說出午安
# 3. hour 在18之後 -> 說出晚安