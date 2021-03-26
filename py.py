import socket

my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_sock.connect(('6.tcp.ngrok.io', 14344))
my_sock.send('x0x100x001x0102x102x010x12010x01x010x201020'.encode())