import socket
import re
import sys
import os
from thread import start_new_thread

# Port number
PORT = 8888
# Inisialisasi socket TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind Port
s.bind(('', PORT))
# Listen
s.listen(10) #berapa jumlah maksimal permintaan koneksi
hasil = ""
# 	# Accepting incoming connection
# conn, address = s.accept() #socket yang diterima ketika sudah di accept
# data, address = conn.recvfrom(4096)

def buatfile(nama_file, isi):
	try:
		file = open(nama_file,'w')   # Trying to create a new file or open one
		file.write(isi)
		file.close()
		hasil= 'OK file berhasil di buat!'
		conn.sendall(hasil)
	except:
		hasil = "File gagal dibuat!"
		conn.sendall(hasil)
		sys.exit(0) # quit Python

def dell_file(nama_file):
	try:
		os.remove(nama_file)
		hasil = "OK file telah terhapus!"
		conn.sendall(hasil)
	except:
		hasil = "file gagal dihapus!"
		conn.sendall(hasil)
		sys.exit(0) # quit Python

def readfile(nama):
	try:
		# file = open('contoh.txt','r+')
		# f= file.readlines()
		# hasil = "".join(f)
		# file.close()
		# conn.sendall(hasil)
		file = open(nama,'r+')
		f= file.readlines()
		hasil = "".join(f)
		file.close()
		conn.sendall(hasil)
	except:
		hasil = "file gagal diload atau file belum ada!"
		conn.sendall(hasil)
		
def dataThread(conn):
	while True:
		try:
			data, address = conn.recvfrom(4096)
			split = re.split(" ", data)
			operation = split[0]
			nama_file = split[1]
			
			
			if(operation =='new'):
				isi_raw = re.split("\'", data)
				isi_file = isi_raw[1]
				buatfile(nama_file, isi_file)
				
			elif(operation=='del'):
				dell_file(nama_file)
				

			elif(operation=='read'):
				readfile(nama_file)

			else:
				hasil = 'operation tidak dikenali'
				conn.sendall(hasil)

		except Exception, e:
			sys.exit(0)

		print 'Request',operation,nama_file,' from ', s.getsockname()
	conn.close()

while True:
	conn, address = s.accept() 
	start_new_thread(dataThread ,(conn,))
	
