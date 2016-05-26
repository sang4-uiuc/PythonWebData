import urllib
import xml.etree.ElementTree as ET

fh = raw_input("Enter location: ")
#autoenters the correct address since i'm too lazy to type it out
if len(fh)<1: fh = "http://python-data.dr-chuck.net/comments_241884.xml"
print "Retrieving", fh
#have to use urllib to open url
url = urllib.urlopen(fh)
#put all this stuff in a string
data = url.read()
print "Retrieved", len(data), "characters"

#parses xml from a string directly into an element, root element of the parsed tree
stuff = ET.fromstring(data)
#finds all the count tags
counts = stuff.findall('.//count')
print "Count:", len(counts)
sum = 0
#retrieves the text content and converts it into int type
for num in counts:
	num = int(num.text)
#sums shit up
	sum += num

print sum
