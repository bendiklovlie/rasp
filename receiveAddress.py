import socket


hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
ip_arr = local_ip.split('.')
ip_arr[3] = '255'
UDP_IP = '.'.join(ip_arr)
UDP_IP = "127.0.0.1"
UDP_PORT = 9001

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print("received message: %s" % data)