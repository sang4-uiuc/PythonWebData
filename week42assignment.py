import urllib
from bs4 import BeautifulSoup

url = raw_input("Enter URL: ")
if len(url)<1 : url = "http://python-data.dr-chuck.net/known_by_Lawrence.html"
count = int(raw_input("Enter count: "))
position = int(raw_input("Enter position: "))

#setting the how many times it's gonna loop
for i in range(0, count + 1):
	#opens and soups up the url
	html = urllib.urlopen(url)
	soup = BeautifulSoup(html, "lxml")
	#prints the url at hand
	print "Retrieving: ", url
	tags = soup('a')
	#goes through the a tags
	pos = 0
	for tag in tags:
		#gets the url at the specified position
		if pos == position - 1:
			#changes the url to the new one
			url = str(tag.get('href', None))
			#nigga we out
			break
		pos += 1
