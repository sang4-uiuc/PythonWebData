import re


fh = raw_input("Enter filename: ")
#returns regex_sum_241882.txt as default when nothing is entered
if len(fh)<1 : fh = "regex_sum_241882.txt"
file = open(fh)
sums = list()
#goes through each line in the file
for line in file:
	#finds the numbers in each line and puts them in a list
	nums = re.findall('[0-9]+',line)
	#adds the numbers to an existing list
	for num in nums:
		
		sums.append(int(num))
#sums the list
print sum(sums)
