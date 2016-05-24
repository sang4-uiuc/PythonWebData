import urllib
from bs4 import BeautifulSoup

url = raw_input("Enter - ")
if len(url)<1: url = "http://python-data.dr-chuck.net/comments_241887.html"
file = urllib.urlopen(url).read()

soup = BeautifulSoup(file)

tags = soup('span')
total = 0
for tag in tags:
	num = int(tag.contents[0])
	total += num

print total


