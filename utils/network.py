############################################################
#Author: Logan Agunat
#Date created: 3/13/26
#Date last modified:
#Description: Contains the neccessary helper functions for
#               module device_discovery.py           
############################################################
import socket
import ipaddress
import psutil
import subprocess


def get_local_ip():
    try:
        #create a temporary socket to determine local ip
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            local_ip = s.getsockname()[0]
        return local_ip
    except OSError as e:
        print(f"Error retrieving local IP: {e}")
    
def get_subnet_mask(local_ip: str):
    """Return the IPv4 subnet mask that is associated with a given local IPv4 address.
        Function enumerates the network interfaces of the system using 'psutil.net_if_addrs()',
        collects their IPv4 addresses and masks, and will return the subnet mask for the first match of 'local_ip'
    Args:
        local_ip: str
            The IPv4 address for which to look up the subnet mask
    Returns:
        subnet_mask: the string which matches a address that is found
    Raises:
        None: all exceptions are handled interanlly and will result in 'None'
            when being returned
    Notes:
        -Only IPv4 addresses are considered
        -Relies on ptusil to query local interface information
    """
    # list of (ip, netmask) tuples
    interfaces_info = {}
    try:
        net_if_addrs = psutil.net_if_addrs()

        for interface_name, addresses in net_if_addrs.items():
            ip_mask_list = []
            for addr in addresses:
                # only consider IPv4 addresses
                if addr.family == socket.AF_INET:
                    # ensure that both fields exist before appending
                    ip_mask_list.append((addr.address, addr.netmask))
            if ip_mask_list:
                interfaces_info[interface_name] = ip_mask_list
    except Exception as e:
        print(f"Error in retrieving network interfaces: {e}")
    # find the subnet mask that corresponds to local_ip
    for interface_name, ip_mask_list in interfaces_info.items():
        for ip, subnet_mask in ip_mask_list:
            if ip == local_ip:
                return subnet_mask
    return None #No matches where found

def get_default_gateway():
    """Returns the systems default IPv4 gateway as a string, or None if it is not found.
        This function shells out to the OS routing command and will scan thhe output for defualt route line
        that targets '0.0.0.0'. Should expect a route table format
    """
    
    try:
        result = subprocess.run(
            command = ["route", "print", "0.0.0.0"],
            capture_output = True,
            text = True,
            check = False,
        )
        # iterate over each line of the command's output
        lines = result.stdout.splitlines()
        for line in lines:
            # Remove any whitespace before checks/split
            clean_line = line.strip()
            # default routing will include '0.0.0.0' (destination and netmask)
            if "0.0.0.0" in clean_line:
                # split whitespace to get columns: layout - (Dest, Mask, Gateway, Interface, Metric)
                find_gateway = clean_line.split()
                # return 'Gateway' portion
                return find_gateway[2]
    except Exception as e:
    
        print(f"Error retrieving default gateway: {e}")
    #no default gateway found, or an error occurred
    return None
               

        
    
  
def get_network_information(local_ip, subnet_mask, gateway_ip):
    pass

def calc_network_address(local_ip, subnet_mask):
    pass

def calc_host_count(subnet_mask):
    pass


