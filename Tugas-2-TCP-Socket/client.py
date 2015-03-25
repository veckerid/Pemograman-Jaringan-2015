#!/usr/bin/python

import socket, os
import curses

# Server IP addressnya
SERVER_IP = '127.0.0.1'
# Port number
PORT = 8888
# Inisialisasi object socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to server
s.connect((SERVER_IP, PORT))

print 'Cara penggunaan :'
print '\t 1. new (new nama_file \'isi_file\')'
print '\t 2. del (del nama_file)'
print '\t 3. read (read nama_file)'
print '\t 4. ketiakan exit untuk keluar!'
print '\t 5. ketikan clear untuk menghapus layar!'
print '\n'*2

while True:
	try:
		operation = raw_input("operation File [\"new\",\"del\",\"read\"] [space] [nama_file] : ")
		if operation=='exit':
			print '-'*50
			print '\t'*4,'koneksi di hentikan!'
			print '-'*50
			break
		elif operation=='clear':
			os.system(['clear','cls'][os.name == 'nt'])
			print 'Cara penggunaan :'
			print '\t 1. new (new nama_file \'isi_file\')'
			print '\t 2. del (del nama_file)'
			print '\t 3. read (read nama_file)'
			print '\t 4. ketiakan exit untuk keluar!'
			print '\t 5. ketikan clear untuk menghapus layar!'
			print '\n'*2
			operation = raw_input("operation File [\"new\",\"del\",\"read\"] [space] [nama_file] : ")
	except KeyboardInterrupt :
		print '-'*50
		print '\t'*4,'koneksi di hentikan!'
		print '-'*50
		break	
	# Kirim
	s.sendall(operation) #tidak perlu definisikan addressnya karena sudah di simpan s.connect
	# Baca kiriman balik dari Server
	data, address = s.recvfrom(4096)
	print
	print '-'*50
	print '\t',data
	print '-'*50
	print
s.close()
