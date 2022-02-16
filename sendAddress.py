import socket
from threading import local
from time import sleep




hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
ip_arr = local_ip.split('.')
ip_arr[3] = '255'
UDP_IP = '.'.join(ip_arr)
UDP_IP = "127.0.1.255"
UDP_PORT = 9001
print(hostname)
print(local_ip)
MESSAGE = local_ip.encode('UTF-8')

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: %s" % MESSAGE)
while(True):
    sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    print("sent")
    sleep(5)