import urllib.request as request
import ssl #for Mac
import json #json格式
import csv

ssl._create_default_https_context = ssl._create_unverified_context #for Mmac
src = 'https://www.googleapis.com/youtube/v3/videos?key=AIzaSyCCv8imiVdPw5ZTn4sVHyX8k0ex57_RuOA&part=snippet&contentDetails=mostPopular&chart=mostPopular&maxResults=50&regionCode=TW'

with request.urlopen(src) as response:
    data = json.load(response) #取得網站的原始碼(HTML, CSS, JavaScript)
# print(data)

# 取得景點列表
video_List = data['items']

path = 'output_data.csv'
with open(path, 'w', encoding='utf-8-sig') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['No', 'video_title','channel','publish time','link','description'])
    for idx,video in enumerate(video_List,start=1):
        writer.writerow([idx, video["snippet"]["title"], video["snippet"]["channelTitle"], video["snippet"]["publishedAt"], f'https://www.youtube.com/watch?v={video["id"]}',{video["snippet"]["description"]}])