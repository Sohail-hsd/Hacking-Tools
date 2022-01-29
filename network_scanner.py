#usr/bin/env python

import scapy.all as scapy

def scane(ip):
	arp_request = scapy.ARP(pdst=id)
	print(arp_request.summary())
	scapy.ls(arp_request)

scane("192.168.10.1")