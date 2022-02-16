import socket

localIP     = "127.0.0.1"
localPort   = 20001
bufferSize  = 1024

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
msgFromServer       = "Hello UDP Client"
bytesToSend2        = str.encode(local_ip)
bytesToSend         = str.encode(msgFromServer)

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")
# Listen for incoming datagrams
while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = "Message from Client:{}".format(message)
    clientIP  = "Client IP Address:{}".format(address)

    print(clientMsg)
    #print((len(clientMsg)- len("Message from Client:")))
    #if((len(clientMsg)- len("Message from Client:"))< 5):
    #    break
    if(message == b'done'):
        print("break")
        break
    # Sending a reply to client
    print("Sending ip address")
    UDPServerSocket.sendto(bytesToSend2, address)
print("IP transmitted and I am done")