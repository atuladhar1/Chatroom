import socket
import pickle
from threading import Thread

# TODO send a tuple through the socket
# set up an exit Function
# IP and port addresses to connect to the server
ip = input('Please input IP to connect :')
port = int(input('Please enter the port to connect :').strip())
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip,port))
print(f'Connected to {ip} at port {port}')
# userName=("userName",len(uname),uname)
# initialize the socket
recv = client.recv(4096).decode()
print(recv)

# send Username to server and wait for the acknowledgement
userName= input("Enter the userName: ")
client.send(bytes(userName,"utf8"))
recv = client.recv(4096).decode()
while (recv !=("Welcome")):
    print(recv)
    userName= input ("Please enter a new userName: ")
    client.send(bytes(userName,"utf8"))
    recv=client.recv(4096).decode()

# recieve the current client list from server
recv=client.recv(4096)
client_list=pickle.loads(recv)
print(client_list[2])
# functions to send message from user. Used as a concurrent thread
def sendMessage():
    while True:
        message= input()
        client.send(bytes(message,"utf8"))
# function to recieve message from user. Used as a concurrent thread.
def recieveMessage():
    while True:
        recv= client.recv(4096)
        message= pickle.loads(recv)
        print(message[2])
# run the threads to recieve and send messages simultaneously
Thread(target=sendMessage).start()
Thread(target=recieveMessage).start()