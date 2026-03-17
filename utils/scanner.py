############################################################
#Author: Logan Agunat
#Date created: 3/13/26
#Date last modified:
#Description: Contains the neccessary helper functions.      
############################################################
"""scanner.py
Description:
    Handles network scanning by sending ICMP probes to target IP addresses
    and collecting response from active devices.
Functions:
    probe_device(ip_address)        - Sends ICMP ping and will return a response
    run_discovery_scan(scan_range)  - Scansa list of IPs and returns active devices
Dependencies:
    scapy, utils.device
"""
from scapy.layers.inet import IP, ICMP
from scapy.sendrecv import sr1
from utils.device import collect_device_data

def probe_device(ip_address):
    """Sends an ICMP ping to a target IP and waits for a response.
    Parameters:
        object: The scapy packet response if device is active
        None: If no response received or an error occured
    """
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
    """Scans a list of IP addresses and returns all active devices.
    Parameters:
        scan_range (list): A list of IP address strings to scan
    Returns:
        list: A list of device dictionaries containing de vice information
    """
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
