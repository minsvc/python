#! /usr/bin/python

import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = '172.16.1.121'
port = 515
while True:
	for data in range(1,1000000):
		if (data%1000==0):
			time.sleep(2)
			print ("------sleep 1 second-------")
		s.sendto(str(data),(ip, port))
		print data
	#print s.recv(1024)
s.close()
test
