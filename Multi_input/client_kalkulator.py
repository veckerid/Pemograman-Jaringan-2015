import socket

# Server IP address
SERVER_IP = '127.0.0.1'
# Port number
PORT = 6666
# Inisialisasi object socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to server
s.connect((SERVER_IP, PORT))
kondisi = True
while kondisi:
	angka1 = raw_input("Masukan angka1: ")
	operation = raw_input("operation [*,/,+,-]:")
	angka2 = raw_input("Masukan angka2: ")
	input_user =  operation+'_'+angka1+'_'+angka2
	# Kirim
	s.sendall(input_user) #tidak perlu definisikan addressnya karena sudah di simpan s.connect
	# Baca kiriman balik dari Server
	data, address = s.recvfrom(4096)
	print 'Hasilnya : ', data
	lanjut = raw_input('untuk mengakhiri ketikan (bye): ')
	if lanjut=='bye':
		kondisi = False
	else :
		kondisi = True
		
s.close()
