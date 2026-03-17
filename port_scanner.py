############################################################
#Author: Logan Agunat
#Date created: 3/17/26
#Date last modified:
#Description: Port Scanner module. 
############################################################
import socket

def scan_port(ip_address: str, port: int) -> bool:
    try:
        # Create a TCP socket
        #sock ← CREATE socket
       with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)

        # Set timeout so it doesn't hang
        #SET sock timeout TO 1 second
        sock.settimeout(timeout=1)
        print(f"Connecting to {ip_address} and {port}...")

        # Try to connect to the IP and port
        #result ← CONNECT sock TO (ip_address, port)
        result = sock.connect(ip_address, port)
        print("Connected Succesfully!")
      
        if result == 0:
           return True
        else:
           return False
    except Exception:
        return False
    
def scan_ports(ip_address: str, port_range: list) -> list:
   #open_ports ← EMPTY LIST
    open_ports = []

    for port in port_range:
        result = scan_port(ip_address, port)
        if result == True:
           open_ports.append(port)
    return open_ports
