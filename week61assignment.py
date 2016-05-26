import json
import urllib

while True:
	url = raw_input("Enter location: ")
	if len(url)<1 : url = "http://python-data.dr-chuck.net/comments_241888.json"
	print "Retrieving ", url
#urlopen is needed to urls
	fh = urllib.urlopen(url).read()
	print "Retrieved ", len(fh), "characters"
#how jason takes the strings and returns a dictionary
	info = json.loads(fh)

#in case the json file is bad
	try: js = json.loads(str(fh))
	except:
#sorta useless in this case
		print "Failure to Retrieve!"
		continue

	total = 0
	count = 0
#goes through the comments for the list
	for num in js["comments"]:
		count += 1
#converts the strings into ints
		num1 = int(num["count"])
		total += num1
	print "Count: ", count
	print "Sum: ", total
	break
