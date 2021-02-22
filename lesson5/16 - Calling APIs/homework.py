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
# print(video_List)

# with open('video.txt', 'w', encoding='utf-8') as file:
#     for idx,video in enumerate(video_List,start=1):
#         file.write(f'#{idx} {video["snippet"]["channelTitle"]} \n{video["snippet"]["title"]}\nhttps://www.youtube.com/watch?v={video["id"]}\n')

path = 'output_data.txt'
with open(path, 'w', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['No', 'channelTitle', 'link'])
    for idx,video in enumerate(video_List,start=1):
        writer.writerow([idx, video["snippet"]["title"], f'https://www.youtube.com/watch?v={video["id"]}'])