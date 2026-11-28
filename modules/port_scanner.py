############################################################
#Author: Logan Agunat
#Date created: 3/17/26
#Date last modified: 6/2/26 
#Description: Port Scanner module
############################################################
import socket

#put docstring

def scan_port(ip_address: str, port: int, timeout: float = 1.0) -> bool:
   "Return True if a TCP connection to ip_address:port succeeds"
   try:
      with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
         sock.settimeout(timeout)
         return sock.connect_ex((ip_address, port)) == 0
   except OSError:
      return False

def scan_ports(ip_adress: str, port_range: range | list[int]) -> list[int]:
   return [port for port in port_range if scan_port(ip_adress, port)]

   