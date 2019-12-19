import requests
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/board/review/list.nhn'

req = requests.get(url).text

soup = BeautifulSoup(req, 'html.parser')
movie = soup.select_one('#old_content > table > tbody > tr:nth-child(1) > td.title > a')
print(movie.text)
