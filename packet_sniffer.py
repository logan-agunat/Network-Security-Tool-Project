############################################################
#Author: Logan Agunat
#Date created: 3/17/26
#Date last modified:
#Description: Packet sniffer module.
############################################################

from scapy import SNIFF
from scapy.layers.inet import IP, TCP, UDP, ICMP

def process_packet(packet) -> None:
    if packet.haslayer(IP):
        
