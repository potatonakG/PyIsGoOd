import requests
from bs4 import BeautifulSoup as bsoup
import re

player = input("Enter scoresaber user code > ")

baseurl = 'https://scoresaber.com/u/' + player
ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
req = requests.get(baseurl, headers={'User-Agent': ua})
html = req.text
soup = bsoup(html, 'html.parser')
playername = soup.select_one('body > div > div > div > div:nth-child(1) > div > div:nth-child(2) > h5 > a')
titles = str(soup.select('body div div div div:nth-child(1) div div:nth-child(2) ul li:nth-child(1)'))
titles=re.sub('<.+?>', '', titles, 0).strip()

def cleanText(readData):
    text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', readData)
    return text
number = re.findall("\d+", cleanText(titles))

print(playername.text.strip())
print("world : " + number[0] + " country : " + number[1])