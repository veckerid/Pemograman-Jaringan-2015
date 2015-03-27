import socket, sys, re
import select

# Port number
PORT = 6666

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind(('',PORT)) 
s.listen(10) 
input = [s,sys.stdin]
print 'Listening at', s.getsockname()

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
                data, address = conn.recvfrom(4096)
                # Check if receive data is not empty
                try :
                    if data :
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
                    else :
                        conn.close() 
                        input.remove(conn)
                        print "Connection closed by client"
                except socket.error, e :
                    conn.close() 
                    input.remove(conn)
                    print "Connection closed by client"
    except KeyboardInterrupt :
        break
s.close()
