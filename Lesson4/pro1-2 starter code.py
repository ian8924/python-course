# https://pypi.org/project/pyttsx3/
# 是一個文字到語音(text to speech)的 Python Library
import pyttsx3 #pip install pyttsx3
# https://pypi.org/project/SpeechRecognition/
# pip install speechRecognition
# import speech_recognition as sr
import datetime
# https://pypi.org/project/wikipedia/
# import wikipedia #pip install wikipedia
# https://docs.python.org/2/library/webbrowser.html
# import webbrowser
# import os, sys, subprocess
# import smtplib
# import googletrans
# from googletrans import Translator

# step 1: 必須要呼叫init()來得到pyttsx3的engine物件
engine = pyttsx3.init()
engine.say('hello')
engine.runAndWait()
# step 2: 如何選擇AI助理說的語言呢
# https://pyttsx3.readthedocs.io/en/latest/engine.html#module-pyttsx3.voice
voices = engine.getProperty('voices')
# index = 0
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
engine.setProperty('voice', voices[25].id)
engine.say('哈囉朋友們')
engine.runAndWait()

# step 4: 找出現在時間
# https://docs.python.org/3/library/datetime.html
full_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
print(full_date)
hour = int(datetime.datetime.now().hour)
print(hour)
engine.say("現在時間是" + str(full_date))   
engine.runAndWait()

# step 5: 讓語音助理依照時間不同作出回應
if hour>=0 and hour<12:
    engine.say('早安')
    engine.runAndWait()

elif hour>=12 and hour<18:
    engine.say('午安')   
    engine.runAndWait()

else:
    engine.say('晚安')  
    engine.runAndWait()

engine.say('我是你的語音小幫手，有什麼我可以幫忙的嗎')  
engine.runAndWait()

# step 6: 將你的名字存成變數
# step 7: 寫出你的AI方程式
# def speak():

# def greet():

# def voiceRecognition():
    # 聽取使用者的聲音，回傳字串
    # r = sr.Recognizer()
    # with sr.Microphone() as source:
    #     print("聆聽中...")
    #     r.pause_threshold = 1
    #     audio = r.listen(source)

    # try:
    #     print("辨識中...")    
    #     query = r.recognize_google(audio, language='en-US')
    #     print(f"辨識結果: {query}\n")

    # except Exception as e:  
    #     print("請再說一次...")  
    #     return "None"
    # return query

# step 9 打開瀏覽器
# def openUrl(): 
# MacOS
# chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
# Windows
# chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

# step 8
# if __name__ == "__main__":
#     greet()
#     while True:
#         query = voiceRecognition().lower()
#         if 'wikipedia' in query: