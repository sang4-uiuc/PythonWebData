import socket
import urllib


fh = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
print fh.read()
#while True:
#    data = fh.read()
#    if ( len(data) < 1 ) :
#        break
#    print data;


