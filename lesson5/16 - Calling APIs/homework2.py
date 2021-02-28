# https://pypi.org/project/pyttsx3/
# 是一個文字到語音(text to speech)的 Python Library
import pyttsx3 #pip install pyttsx3
# https://pypi.org/project/SpeechRecognition/
# pip install speechRecognition
import speech_recognition as sr
import datetime
import urllib.request as request
import ssl #for Mac
import json #json格式
import csv
import wikipedia
from selenium import webdriver
import time
engine = pyttsx3.init()
voices = engine.getProperty('voices')

def speak(message):
    print(message)
    engine.say(message)
    engine.runAndWait()




def voiceRecognition():
    # 聽取使用者的聲音，回傳字串
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("聆聽中...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("辨識中...")    
        query = r.recognize_google(audio, language='zh-tw')
        print(f"辨識結果: {query}\n")

    except Exception as e:  
        print("請再說一次...")  
        return "None"
    return query

ssl._create_default_https_context = ssl._create_unverified_context #for Mmac
src = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=rdec-key-123-45678-011121314'

def callfun():
    words = voiceRecognition().lower()
    total=0
    method=''
    if '加' in words or '+' in words:
        method='加'
        arr=words.split('加')
        for i in arr:
            total=total+int(i)
    elif '減' in words or '-' in words:
        method='減'
        arr=words.split('減')
        total=int(arr[0])-int(arr[1])
    elif '乘' in words or '*' in words:
        method='乘'
        arr=words.split('乘')
        total=int(arr[0])*int(arr[1])
    elif '除' in words or '/' in words:
        method='除'
        arr=words.split('除')
        total=int(arr[0])/int(arr[1])
    else:
        callfun()
    speak(f'{arr[0]}{method}{arr[1]}等於{total}')

if __name__ == "__main__":
    # greet()
    while True:
        query = voiceRecognition().lower()
        print(query)
        if '天氣預報' in query:
            speak('查詢地點')
            location = voiceRecognition().lower()
            print(location)
            location=location.replace('台','臺')
            print(location)
            with request.urlopen(src) as response:
                data = json.load(response) 
                result= data['records']['location']
                for i in range(0,len(result)):
                    if result[i]['locationName'] == location:
                        speak(f"{location}今日天氣{result[i]['weatherElement'][0]['time'][0]['parameter']['parameterName']}")
                        speak(f"最低溫為：{result[i]['weatherElement'][2]['time'][0]['parameter']['parameterName']}度")
                        speak(f"最高溫為：{result[i]['weatherElement'][4]['time'][0]['parameter']['parameterName']}度")
                        speak(f"降雨機率為：{result[i]['weatherElement'][1]['time'][0]['parameter']['parameterName']}%")
        elif '維基百科' in query:
            speak('查詢文字')
            search = voiceRecognition().lower()
            wikipedia.set_lang("zh-tw")
            speak(wikipedia.summary(search))
        elif '搜尋' in query:
            speak('查詢文字')
            search = voiceRecognition().lower()
            driver = webdriver.Chrome('/Users/ianliao/Downloads/chromedriver-2')
            driver.get('http://www.google.com')
            driver.find_element_by_name('q').send_keys(search)
            driver.find_element_by_name('q').submit()
        elif '購物' in query:
            speak('商品')
            search = voiceRecognition().lower()
            driver = webdriver.Chrome('/Users/ianliao/Downloads/chromedriver-2')
            driver.get('https://shopee.tw/')
            driver.find_element_by_class_name('shopee-popup__close-btn').click()
            driver.find_element_by_class_name('shopee-searchbar-input__input').send_keys(search)
            driver.find_element_by_class_name('btn-solid-primary').click()
        elif '計算機' in query:
            words = voiceRecognition().lower()
            total=0
            method=''
            if '加' in words or '+' in words:
                method='加'
                arr=words.split('加')
                for i in arr:
                    total=total+int(i)
                speak(f'{arr[0]}{method}{arr[1]}等於{total}')
            elif '減' in words or '-' in words:
                method='減'
                arr=words.split('減')
                total=int(arr[0])-int(arr[1])
                speak(f'{arr[0]}{method}{arr[1]}等於{total}')
            elif '乘' in words or '*' in words:
                method='乘'
                arr=words.split('乘')
                total=int(arr[0])*int(arr[1])
                speak(f'{arr[0]}{method}{arr[1]}等於{total}')
            elif '除' in words or '/' in words:
                method='除'
                arr=words.split('除')
                total=int(arr[0])/int(arr[1])
                speak(f'{arr[0]}{method}{arr[1]}等於{total}')
            else:
                callfun()


            
            



    

            


        
    


