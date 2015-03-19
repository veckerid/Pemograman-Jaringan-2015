import httplib,sys,re

connection = httplib.HTTPConnection('detik.feedsportal.com')
connection.request('GET', 'http://detik.feedsportal.com/c/33613/f/656082/index.rss')
content = connection.getresponse().read()
mylist = re.split("<item>", content)
count = len(mylist)
#print content
for x in xrange(1,count):
	title = re.split("</title>", mylist[x])
	judul = re.split("<title>",title[0])
	link = re.split("</link>",title[1])
	alamat = re.split("<link>", link[0])
	print x,'.',judul[1],' -> ',alamat[1]
	print ""
