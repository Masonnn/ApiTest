import requests
from bs4 import BeautifulSoup as bs


myUrl = 'https://movie.douban.com/top250'

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'

header = {'user-agent': user_agent}


response = requests.get(myUrl, headers = header)

bs_res = bs(response.text, 'html.parser')



for tags in bs_res.find_all('div', attrs={'class':'hd'}):
    for atag in tags.find_all('a'):
        print(atag.get('href'))
        print(atag.find('span').text)

# print(response.text)
print(f'返回的状态码是：{response.status_code}')

