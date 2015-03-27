import socket, sys, re, os
import select

# Port number
PORT = 6666

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind(('',PORT)) 
s.listen(10) 
input = [s,sys.stdin]
print 'Listening at', s.getsockname()

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

while True:
    try :
        inputready,outputready,exceptready = select.select(input,[],[]) 

        for conn in inputready: 
            # Handle the server socket
            if conn == s:             
                conn, address = s.accept() 
                input.append(conn) 
            # Handle standard input
            elif conn == sys.stdin:             
                junk = sys.stdin.readline() 
                running = 0 
            # Handle client socket
            else:             
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

                    else :
                        conn.close() 
                        input.remove(conn)
                        print "Connection closed by client"

                    print 'Request',operation,nama_file,' from ', s.getsockname()

                except socket.error, e :
                    conn.close() 
                    input.remove(conn)
                    print "Connection closed by client"

    except KeyboardInterrupt :
        break
s.close()
