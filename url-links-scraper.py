import requests
from bs4 import BeautifulSoup

url = input("Enter URL target to scan for links: ")

r = requests.get(url)
content = r.text
soup = BeautifulSoup(content, 'html.parser')

for link in soup.find_all('a'):
    print(link.get('href'))
