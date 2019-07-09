import requests
from bs4 import BeautifulSoup

response = requests.get("https://finance.naver.com/marketindex/exchangeDetail.nhn?marketindexCd=FX_EURKRW").text
soup = BeautifulSoup(response,'html.parser')
exchange = soup.select_one("#content > div.spot > div.today > p.no_today")
print(exchange.text)
 
