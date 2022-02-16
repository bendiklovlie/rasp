import socket


hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
serverAddressPort = ("127.0.0.1", 20001)
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

msgFromClient = "Please give me your ip address"
msgFromServer = "123"
while(True):
    bytesToSend = str.encode(msgFromClient)

    # Create a UDP socket at client side
    
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    if(msgFromClient == 'done'):
        break
    msgFromServer = UDPClientSocket.recvfrom(1024)
    msg = "Message from Server {}".format(msgFromServer[0])
    print(msg)
    msgFromClient = input("What do you want to send to raspberry? ")
print("raspberry pi ip address is: ")
print(msgFromServer[0])