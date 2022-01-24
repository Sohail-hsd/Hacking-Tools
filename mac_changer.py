#usr/bin/evn python

import subprocess
import optparse
import re
def get_args():
	parse = optparse.OptionParser()
	parse.add_option('-i','--interface',dest='interface',help="Interface to change its mac")
	parse.add_option('-m','--mac',dest='new_mac',help='New Mac Address')
	(option,args) = parse.parse_args()
	if not option.interface and not option.new_mac:
		parse.error("[*] Please Enter interface and MAC, For more info type --help command")
	if not option.interface:
		parse.error("[*] Please Enter interface, For more info type --help command")
	if not option.new_mac:
		parse.error("[*] Please Enter valid MAC Address")
	return option

def change_mac(interface,new_mac):
	print(f"[-] Mac changed successfully for {interface} to {new_mac}")
	subprocess.call(['ifconfig',interface,'down'])
	subprocess.call(['ifconfig',interface,'hw','ether',new_mac])
	subprocess.call(['ifconfig',interface,'down'])

def current_mac(interface):
	ifconfig_re = subprocess.check_output(['ifconfig',interface])
	check_mac = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w\:\w\w\',ifconfig_re)
	if check_mac:
		return chage_mac.group(0)
	else:
		print(f"[*] The Mac Address for {interface} is not exist")

option = get_args()
get_current_mac = current_mac(option.interface) # Actual Mac
print(f"current_mac : {str(current_mac)}") 
change_mac(option.interface,option.new_mac)
get_current_mac = current_mac(option.interface) # Changed Mac

if get_current_mac == option.new_mac:
	print(f'Mac Address was changed successfully to : {str(get_current_mac)}')
else:
	print("[*] The mac Address did not change")



