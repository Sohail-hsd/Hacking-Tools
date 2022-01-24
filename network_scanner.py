#usr/bin/env python

import scapy.all as scapy

def scan(ip):
	arp_request = scapy.ARP(pdst=ip)

scan(192.168.10.1/24)