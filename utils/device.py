############################################################
#Author: Logan Agunat
#Date created: 3/13/26
#Date last modified:
#Description: Contains the neccessary helper functions.      
############################################################

from scapy.layers.12 import Ether
import socket
from datetime import datetime



def reverse_dns_lookup(ip_address: str) -> str:
    #Extract the MAC address from the probe response
    #Return it as a formatted string
    pass

def calculate_response_time(response: object) -> float | None:
    #Calculate howe long device took to respond
    #Return it in milliseconds
    pass

def parse_mac_from_response(response: object) -> str | None:
    #Try to resolve the IP to a hostname
    #Return the hostname or "Unknown" if it fails
    if response is None:
        return None
    if Ether in response:
        mac_address = response[Ether].src
        return mac_address
    else:
        return "Unnknown"

def collect_device_data(ip_address: str, response: object) -> dict | None:
    # calls the functions above
    #bundles everything into a dictionary
    #Returns a complete device record with IP, MAC, vendor, hostname, latency, and timestamp
    pass
