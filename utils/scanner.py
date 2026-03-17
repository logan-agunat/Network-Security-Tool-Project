############################################################
#Author: Logan Agunat
#Date created: 3/13/26
#Date last modified:
#Description: Contains the neccessary helper functions.      
############################################################
from scapy.layers.inet import IP, ICMP
from scapy.sendrecv import sr1
from utils.device import collect_device_data

def probe_device(ip_address):
    try:
        # build the packet; 
        packet = IP(dst=ip_address) / ICMP()
        response = sr1(packet, timeout=1, verbose=0)

        if response is not None:
            return response
        else:
            return None
    except Exception:
        return None

    

def run_discovery_scan(scan_range: list) -> list:
    device_list = []
    failed_list = []

    for ip_address in scan_range:
        response = probe_device(ip_address)
        if response is not None:
            device_info = collect_device_data(ip_address, response)
            if device_info is not None:
                device_list.append(device_info)
            else:
                failed_list.append(ip_address)
    if failed_list:
        print(f"Failed to collect data for: {failed_list}")
    return device_list
