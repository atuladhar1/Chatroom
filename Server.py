import socket
import pickle
from _thread import *
import random

ip = "localhost"
port = 8235
client_list = {}
# Add a client to the client list and broadcast the message to every other client# incomplete


# convert the message to be sent into at tuple
def messager(message):
    tupl = ("Message",len(message),message)
    return tupl


# convert the client list to string
def listString():
    lost = list(client_list.keys())
    last=","
    lister = last.join(lost) 
    lest = "Currently online members: "+ lister
    return lest


def timely_broadcast(userName):
    ts = random.randint(1,50)
    if ts ==29 :
        print (messager(listString())[2])
        client_list[userName].send(pickle.dumps(messager(listString())))
    

def check_connection_status(client):
    if client is False:
        client.close()
        print('Fuck you kumar')
        


# Send message to all the clients other than the one who send the message
def sendMessage(connection,message):
        for client in client_list:
            if(client_list[client]!=connection):
                client_list[client].send(pickle.dumps(message))


# A singular thread function that will be used to multithread as required
def createThread(connection,address):
    connection.send(bytes("Welcome to the Server", "utf8"))
    # Take user name as unput
    userName = connection.recv(1024).decode()
    # Ask the Client for username that is not currently connected
    while userName in client_list:
        connection.send(bytes("username in use","utf8"))
        userName=connection.recv(1024).decode()
    connection.send(bytes("Welcome","utf8"))
    # send a list of users currently connected to the user
    client_list[userName]= connection
    for client in client_list:
        client_list[client].send(pickle.dumps(messager(listString())))


    # infinite loop receive a message and broadcast it to all the connected clients
    while (True):
        try:
        
            recv = connection.recv(1024).decode()
            if recv is None:
                print(f"connection closed to {username}")
            message = userName+":" + recv
            sendMessage(connection,messager(message))
            timely_broadcast(userName)
            print(message)
            check_connection_status(client)

        # except ConnectionResetError:
        #     print (f"Connection was lost to {userName}")
        #     exit()
        
        # except IOError:
        #     print (f"{userName} hates you")
        #     connection.close()        
        #     exit()
        
        except:
            continue
        

        




# Core program that will call thred function and multithread
# Values to be entered as required
# Open the server socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((ip, port))
    print(f"The server has been established at {ip} : {port}")
    server.listen(5)
    while True:
        connection, address = server.accept()
        start_new_thread(createThread,(connection,address))
