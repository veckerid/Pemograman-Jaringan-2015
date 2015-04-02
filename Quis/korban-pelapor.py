import socket, sys

# Server IP address
SERVER_IP = '127.0.0.1'
# Port number used by server
PORT = 6666
def main(argv):
	# Initialize socket object with TCP/Stream type
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# Initiate a CONNECTION
	s.connect((SERVER_IP, PORT))
	input = ''
	while True :
		input = raw_input("Alamat Kebakaran : ")
		# Send the message
		s.sendall(input)
		# Read message stream from server 
		data, address = s.recvfrom(4096)
		print data
	s.close()

if __name__ == "__main__":
	main(sys.argv)
