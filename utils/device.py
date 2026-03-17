############################################################
#Author: Logan Agunat
#Date created: 3/13/26
#Date last modified:
#Description: Contains the neccessary helper functions.      
############################################################

from scapy.layers.l2 import Ether
import socket
from datetime import datetime



def reverse_dns_lookup(ip_address: str) -> str:
    """Resolves an IP address to a hostname using reverse dns lookup.
    Parameters:
        ip_address (str): The IP address to resolve
    Returns:
        str: The resolved hostname
        str: 'Unknown' if the lookup fails
    """
    #Extract the MAC address from the probe response
    #Return it as a formatted string
    try:
        host_info = socket.gethostbyaddr(ip_address)[0]
        print(f"Host Info: {host_info}")
        return host_info
    except Exception:
        return "unknown"


def calculate_response_time(response: object) -> float | None:
    """Calculates the round trip response time from a scapy packet.
    Paramters:
        response (object): A scapy packet response from a probe
    Returns:
        float: The response time in milliseconds
        None: If response is None or time cannot be calculated
    """
    #Calculate howe long device took to respond
    #Return it in milliseconds
    if response is None:
        return None
    #get response time from response
    #convert response time to milliseconds
    try:
        response_time = (response[1].time - response[0].time) * 1000
        return response_time
    except Exception:
        return None

def parse_mac_from_response(response: object) -> str | None:
    """Extracts the MAC address from a scapy packet response.
    Parameters:
        response (object): A scapy packet from a probe
        
    Returns:
        str: The MAC address
        str: 'Unknown' if no Ethernet layer is found
        None: If response is None
    """
    #Try to resolve the IP to a hostname
    #Return the hostname or "Unknown" if it fails
    if response is None:
        return None
    try:
        if response.haslayer(Ether):
            mac_address = response[Ether].src
            return mac_address
        else:
            return "Unnknown"
    except Exception:
        return "Unknown"

def collect_device_data(ip_address: str, response: object) -> dict | None:
    """Collects and bundles all data for a discovered device.
    Parameters:
        ip_address (str): The IP address of the device
        response (object): A scapy packet response from a probe
    Returns:
        device (dict): A dictionary containing:
            - 'ip' (str): The device IP address
            - 'mac' (str): The device MAC address
            - 'vendor' (str): The device vendor (default 'Unknown')
            - 'hostname' (str): The device hostname
            - 'latency' (float): The response time in milliseconds
            - 'timestamp' (str): The time the device was discovered
        None: If response is None
     """
    # calls the functions above
    #bundles everything into a dictionary
    #Returns a complete device record with IP, MAC, vendor, hostname, latency, and timestamp
    if response is None:
        return None
    
    mac = parse_mac_from_response(response)
    latency = calculate_response_time(response)
    hostname = reverse_dns_lookup(ip_address)

    device = {
        "ip"    : ip_address,
        "mac" : mac,
        "vendor"    : "unknown", #with vendor.py
        "hostname"  : hostname,
        "latency"   : latency,
        "timestamp"    : datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return device

