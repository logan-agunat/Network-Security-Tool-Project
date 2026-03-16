############################################################
#Author: Logan Agunat
#Date created: 3/13/26
#Date last modified:
#Description: Contains the neccessary helper functions.        
############################################################
"""
network.py

Description:
    Helper module for retrieving and calculating local network information.
    Provides functions to get the local IP, subnet mask, default gateway,
    and generate a full IP range for network scanning.

Functions:
    get_local_ip()                            - Returns the local IP address
    get_subnet_mask(local_ip)                 - Returns the subnet mask
    get_default_gateway()                     - Returns the default gateway
    get_network_information()                 - Returns all network info bundled
    calc_network_address(local_ip, subnet_mask) - Returns the network address
    calculate_host_count(subnet_mask)         - Returns the number of usable hosts
    generate_ip_range(network_info)           - Returns list of all IPs to scan

Dependencies:
    socket, ipaddress, psutil, subprocess
"""
import socket
import ipaddress
import psutil
import subprocess


def get_local_ip() -> str | None:
    """Retrieves the local IP address of the machine
    Returns:
        str: the local IP address
        None: If the Ip address could not be retrieved"""
    try:
        #create a temporary socket to determine local ip
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            local_ip = s.getsockname()[0]
        return local_ip
    except OSError as e:
        print(f"Error retrieving local IP: {e}")
    
def get_subnet_mask(local_ip: str) -> str | None:
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

def get_default_gateway() -> str | None:
    """Returns the systems default IPv4 gateway as a string, or None if it is not found from the system routing table.
    Returns:
        str: The gateway IP address
        None: If the gateway could not be retrieved
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
               

def get_network_information() -> dict | None:
    """Retrieves all local network information.
    Returns:
        dict: Contains 'local_ip', 'subnet_mask', and 'gateway'
        None: If any value could not be retrieved
    """
        
    local_ip = get_local_ip()
    subnet_mask = get_subnet_mask(local_ip)
    gateway = get_default_gateway()

    # Validate all values are retrieved
    #Local IP check
    if local_ip is None:
        print("Error: Could not retrieve local IP.")
        return None
    if subnet_mask is None:
        print("Error: Could not retrieve subnet mask.")
        return None
    if gateway is None:
        print("Error: Could not retrieve gateway.")
        return None

    # Bundle them together and return all network information

    network_information = {
        "local_ip"  : local_ip,
        "subnet_mask"   : subnet_mask,
        "gateway"   : gateway
    }
    return network_information


def calc_network_address(local_ip: str, subnet_mask: str) -> str:
    """Calculate the network address from an IP and subnet mask.
    Parameters:
        local_ip (str): The local IP address
        subnet_mask (str): The subnet mask
    Returns:
        str: The network address
    """
    # Convert local_ip and subnet_mask strings into network objects
    #ip_object   ← CONVERT local_ip TO IPv4Address object via ipaddress module
    # mask_object ← CONVERT subnet_mask TO IPv4Address object via ipaddress module
    # network_address ← ip_object AND mask_object
    network = ipaddress.IPv4Network(local_ip + "/" + subnet_mask, strict=False)
    result = str(network.network_address)
    return result

def calc_host_count(subnet_mask: str) -> int:
    """Calculates the number of usable hosts in a subnet.
    Parameters:
        subnet_mask (str): The subnet mask
    Returns:
        int: The number of usable host addresses
    """

    # Convert subnet_mask string into a network object
    network = ipaddress.IPv4Network(subnet_mask)
    #network ← CREATE IPv4Network object from subnet_mask
    # Get the total number of hosts/addresses in the network
    total_hosts = network.num_addresses
    # Subtract 2 to exclude:
    # - the network address (e.g. 192.168.1.0)
    # - the broadcast address (e.g. 192.168.1.255)
    #host_count ← total_addresses - 2
    host_count = total_hosts - 2
    return host_count

def generate_ip_range(network_information: dict) -> list:
    """Generates a list of all scannable IP addresses in the local network.
    Paramaters:
        network_information (dict): A dictionary containing
            -'local_ip' (str): The local IP addresses
            - 'subnet_mask' (str): The subnet mask
    Returns:
        list: A list of IP addresses strings to scan, excluding local machines IP address
    """
    local_ip = network_information["local_ip"]
    subnet_mask = network_information["subnet_mask"]

    network_address = calc_network_address(local_ip, subnet_mask)
    host_count = calc_host_count(subnet_mask)

    ip_list = []
    for i in range(1, host_count + 1):
        ip = str(ipaddress.IPv4Address(network_address) + i)
        ip_list.append(ip)
    if local_ip in ip_list:
        ip_list.remove(local_ip)
    return ip_list
       

