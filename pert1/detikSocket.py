#!/usr/bin/env python

import socket,re

content = ''
sock = socket.socket()
sock.connect(('detik.feedsportal.com', 80))
sock.sendall(
	'GET http://detik.feedsportal.com/c/33613/f/656082/index.rss HTTP/1.1\r\n'
	'Host: sindikasi.okezone.com:80\r\n'
	'User-Agent: socket.py\r\n'
	'Connection: close\r\n'
	'\r\n')
# Read all received message
while True:
    buf = sock.recv(1000) #1000 brapa jumlah buffernya
    if not buf:
        break
    content += buf
# print content
mylist = re.split("<item>", content)
count = len(mylist)
for x in xrange(1,count):
	title = re.split("</title>", mylist[x])
	judul = re.split("<title>",title[0])
	link = re.split("</link>",title[1])
	alamat = re.split("<link>", link[0])
	print x,'.',judul[1],' -> ',alamat[1]
	print ""
sock.close()

