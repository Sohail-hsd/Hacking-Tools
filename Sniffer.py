#!/usr/bin/evn python

import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniff_packet)

def process_sniff_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        print(packet)


interface = "wlan0"

sniff(interface)

