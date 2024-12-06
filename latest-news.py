import requests
from bs4 import BeautifulSoup

url = "https://news.google.com/news/rss"

response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, 'xml')
items = soup.find_all('item')

for item in items:
  print(item.title.text)
  print(item.link.text)
  print(item.pubDate.text)
  print("-" * 55)
