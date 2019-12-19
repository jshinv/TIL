import requests
from bs4 import BeautifulSoup

url = 'https://www.naver.com/'

req = requests.get(url).text

data = BeautifulSoup(req, 'html.parser')
sel = data.select('div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul >li > a')


title = sel.find('span')

print(title)

# for item in data:
#     print(item)

# li class="ah_item">
# <a class="ah_a" data-clk="lve.keyword" href="#">
# <span class="ah_r">16</span>
# <span class="ah_k">서울교통공사 채용</span>
# </a>
# </li>,