############################################################
#Author: Logan Agunat
#Date created: 3/17/26
#Date last modified:
#Description: alert_engine.py
############################################################
from scapy.layers.inet import IP, TCP, UDP, ICMP
from scapy.sendrecv import sniff
import datetime


def check_port_scan(packet, connection_tracker: dict, port_scan_threshold: int) -> None:
    if packet.haslayer(IP) and packet.haslayer(TCP):
        src_ip = packet[IP].src
        dst_port = packet[TCP].dport

        if src_ip not in connection_tracker:
            connection_tracker[src_ip] = () #set to empty set
            connection_tracker[src_ip].append(dst_port)
        ports_scanned = len(connection_tracker[src_ip])
        if ports_scanned > port_scan_threshold:
            process_alert(
                "Port Scan detected",
                src_ip,
                f"Scanned: {ports_scanned} ports"
            )
            #reset  for this IP to avoid repeated alerts
            connection_tracker[src_ip] = ()

def check_suspicious_ip(packet, black_list):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
    if src_ip in black_list:
            process_alert("Suspicious IP", src_ip, "source ip is blacklisted..." )
    if dst_ip in black_list:
        process_alert("Suspicious IP", dst_ip, "source ip is blacklisted..." )
   
def check_large_packet(packet, pkt_threshold: int) -> None:

    if packet.haslayer(IP):
        src_ip = packet[IP].src
        pkt_size = len(packet)
        if pkt_size > pkt_threshold:
            process_alert("Large packet detecrted", {src_ip}, 
                          f"Packetsize: {pkt_size} bytes exceed threshold: {pkt_threshold}")

def process_alert(alert_type: str, src_ip: str, details: str) -> None:

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"ALERT: {alert_type}")
    print(f"ALERT: {alert_type}")
    print(f"Timestamp: {current_time}") 
    print(f"Source: {src_ip}")
    print(f"Details: {details}")
    print("=====================================")

def analyze_packet(packet, black_list: list, pkt_threshold: int, port_scan_threshold: int, connection_tracker: dict) -> None:
    #call check_sus, check large pkt, check port scan
    check_suspicious_ip(packet, black_list)
    check_large_packet(packet, pkt_threshold)
    check_port_scan(packet, connection_tracker, port_scan_threshold)

def start_alert_engine(interface: str, count: int) -> None:
    black_list = [] #add malicious ip here later
    pkt_threshold = 1500 #pack threshold
    port_scan_threshold = 10
    connection_tracker = {}
    print(f"Starting alert engine on interface: {interface}")
    print("================================")
    packets = sniff(
        iface = interface,
        count = count,
        prn = lambda packet: analyze_packet(packet, black_list, pkt_threshold, port_scan_threshold, connection_tracker)
    )
    
