import socket, re
# from thread import start_new_thread
import thread

# Port number
PORT = 6666
# Inisialisasi socket TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind Port
s.bind(('', PORT))
# Listen
s.listen(10) #berapa jumlah maksimal permintaan koneksi
hasil = 0
# 	# Accepting incoming connection
# conn, address = s.accept() #socket yang diterima ketika sudah di accept
# data, address = conn.recvfrom(4096)
def Thread_connection(conn):
	try:
		while True:
			data, address = conn.recvfrom(4096)
			# Kirim balik ke client
			split = re.split("_", data)
			angka1 = split[1]
			operation = split[0]
			angka2 = split[2]
			if(operation =='*'):
				hasil = int(angka1)*int(angka2)
				conn.sendall(str(hasil))
			elif(operation=='/'):
				hasil = int(angka1)/int(angka2)
				conn.sendall(str(hasil))
			elif(operation=='+'):
				hasil = int(angka1)+int(angka2)
				conn.sendall(str(hasil))
			elif(operation=='-'):
				hasil = int(angka1)-int(angka2)
				conn.sendall(str(hasil))
			else:
				hasil = 'operation tidak dikenali'
				conn.sendall(str(hasil))
		conn.close()
	except :
		sys.exit(0)

while True:
	# Accepting incoming connection
	conn, address = s.accept() #socket yang diterima ketika sudah di accept
	# Baca pesan dari client
	thread.start_new_thread(Thread_connection ,(conn,))
