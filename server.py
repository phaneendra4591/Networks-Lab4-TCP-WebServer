
import socket             

s = socket.socket()
host = socket.gethostname()
port = 34567
s.bind(('', port))
s.listen(5)           
while True:
	c, addr = s.accept()
	print('Thank you for connecting')
	message=c.recv(1024)
	filename=message.decode().split()[1]
	# filename=c.recv(1024)
	# print('File content: ')
	# filename=filename.decode()
	f = open("/home/examuser/Desktop/"+filename)
	g = f.read(1024)
	c.send(g.encode())
	print("sent")
	f.close()
	c.close()
	
