import socket, sys, re, thread

# Port number
PORT = 6666
# Inisialisasi socket TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind Port
s.bind(('', PORT))
# Listen
s.listen(10) #berapa jumlah maksimal permintaan koneksi
connection = []

def menerima_notifikasi(conn):
    try:
    	while True:
    		data= conn.recv(4096)
    		if data=='group_pemadam':
    			connection.append(conn)

    		elif data=='diterima':
    			print "Pemadam berangkat ke TKP! "

    		else :
    			conn.sendall("laporan anda telah diterima!")
    			for client in connection:
    				client.sendall(data)

        conn.close()

    except :
        sys.exit(0)
        print sys.exc_info()


while True:
	# Accepting incoming connection
	# Accepting incoming connection
	conn, address = s.accept() #socket yang diterima ketika sudah di accept
	# Baca pesan dari client
	thread.start_new_thread(menerima_notifikasi ,(conn,))
	# thread.start_new_thread(mengirim_notifikasi, (data_kebakaran,))
