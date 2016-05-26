import requests

url = raw_input("Enter json URL: ")
if len(url)<1: url= "http://python-data.dr-chuck.net/comments_241888.json"
counts = []

file = requests.get(url)
data = file.json()
comments = data["comments"]

for comment in comments:
    counts.append(comment['count'])

print "Count: {0}".format(len(counts))
print "Sum: {0}".format(sum(counts))
