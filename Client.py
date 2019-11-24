import socket
import pickle
from threading import Thread

# TODO send a tuple through the socket
# set up an exit Function
# IP and port addresses to connect to the server
ip = "localhost"
port = 8234
# userName=("userName",len(uname),uname)
# initialize the socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip, port))
recv = client.recv(1024).decode()
print(recv)

# send Username to server and wait for the acknowledgement
userName= input("Enter the userName: ")
client.send(bytes(userName,"utf8"))
recv = client.recv(1024).decode()
while (recv !=("Welcome")):
    print(recv)
    userName= input ("Please enter a new userName: ")
    client.send(bytes(userName,"utf8"))
    recv=client.recv(1024).decode()

# recieve the current client list from server
recv=client.recv(1024)
client_list=pickle.loads(recv)
print(client_list[2])
# functions to send message from user. Used as a concurrent thre`ad
def sendMessage():
    while True:
        message= input()
        client.send(bytes(message,"utf8"))
# function to recieve message from user. Used as a concurrent thread.
def recieveMessage():
    while True:
        recv= client.recv(2048)
        message= pickle.loads(recv)
        print(message[2])
# run the threads to recieve and send messages simultaneously
Thread(target=sendMessage).start()
Thread(target=recieveMessage).start()