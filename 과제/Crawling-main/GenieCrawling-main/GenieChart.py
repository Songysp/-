import requests
from bs4 import BeautifulSoup
import time

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
pages = ['&pg=1','&pg=2','&pg=3','&pg=4']
baseUrl = "https://www.genie.co.kr/chart/top200?ditc=D&ymd=20240521&hh=14&rtm=Y"
rank = 1

for i in pages:
    request = requests.get(baseUrl + i, headers=header)
    time.sleep(5)
    soup = BeautifulSoup(request.text)
    tbody = soup.find('tbody')
    titles = tbody.findAll('a', {'class':'title'})
    artists = tbody.findAll('a', {'class':'artist'})
    for y, (t, a) in enumerate(zip(titles, artists)):
        title = t.text.strip()
        artist = a.text.strip()
        print(f'{rank}위. {title} - {artist}')
        rank += 1
