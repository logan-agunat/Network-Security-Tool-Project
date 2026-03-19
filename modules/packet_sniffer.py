############################################################
#Author: Logan Agunat
#Date created: 3/17/26
#Date last modified:
#Description: Packet sniffer module.
############################################################

from scapy.all import sniff 
from scapy.layers.inet import IP, TCP, UDP, ICMP

def process_packet(packet) -> None:
    if packet.haslayer(IP):
        #src_ip   ← EXTRACT source IP FROM packet
        src_ip = packet[IP].src
        #dst_ip   ← EXTRACT destination IP FROM packet
        dst_ip = packet[IP].dst
        #size     ← EXTRACT packet size FROM packet
        size = len(packet)

        if packet.haslayer(TCP):
            #protocol ← "TCP"
            protocol = "TCP"
            #src_port ← EXTRACT source port FROM packet TCP layer
            src_port = packet[TCP].sport
            #dst_port ← EXTRACT destination port FROM packet TCP layer
            dst_port = packet[TCP].dport

        elif packet.haslayer(UDP):
            #protocol ← "UDP"
            protocol = "UDP"
            #src_port ← EXTRACT source port FROM packet UDP layer
            src_port = packet[UDP].sport
            #dst_port ← EXTRACT destination port FROM packet UDP layer
            dst_port = packet[UDP].dport
        elif packet.haslayer(ICMP):
            protocol = "ICMP"
            src_port = "N/A"
            dst_port = "N/A"
        else:
            protocol = "Unknown"
            src_port = "N/A"
            dst_port = "N/A"
    
        #PRINT src_ip, dst_ip, protocol, src_port, dst_port, size
        print(f"{src_ip} | {dst_ip} | {protocol} | {src_port} | {dst_port} | {size} ")
   
def sniff_packets(interface: str, pkt_count: int) -> list:
    try:
        #packets - sniff on interface
        packets = sniff(iface = interface, count = pkt_count, prn = process_packet) #prn tells scapy to call that 
                                                                                    # process_packet for each packet
        return packets
            #then process each packet with process_packet
        #return packets

    except Exception:
        print("Error sniffing packets: " + Exception)
        return []

def start_sniffer(interface: str, pkt_count: int) -> list:
    #status updates
    print("STARTING packet capture on interface: " + interface)
    print(f"Capturing +{pkt_count}  packets.......")
    print("==================================================")
    packets = sniff_packets(interface, pkt_count)
    print("==================================================")
    print(f"CAPTURED  {len(packets)} packets....")