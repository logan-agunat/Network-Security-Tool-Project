############################################################
#Author: Logan Agunat
#Date created: 3/17/26
#Date last modified:
#Description: Port Scanner module
############################################################
import socket

#put docstring

def scan_port(ip_address: str, port_range: int) -> bool:
    try:
       with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)

        #SET sock timeout TO 1 second
        sock.settimeout(timeout=1)
        print(f"Open ports on {ip_address}: {list(port_range)}")
        
        result = sock.connect(ip_address, port_range) #attempt connection to the IP and port
        print("Connected Succesfully!")
      
        if result == 0:
           return True
        else:
           return False
    except Exception:
        return False
    
def scan_ports(ip_address: str, port_range: list) -> list:
    open_ports = []

    for port in port_range:
        result = scan_port(ip_address, port)
        if result == True:
           open_ports.append(port)
    return open_ports
