################################################################
#Author: Logan Agunat
#Date created: 3/17/26
#Date last modified:
#Description: Traffic Analyzer module.
###############################################################
from scapy.layers.inet import IP, TCP, UDP, ICMP

def analyze_traffic(packets: list) -> dict:
    #initialize counters
    #protocol_counts = (tcp,etc)
    protocol_counts = {
        "TCP"   :0,
        "UDP"   :0,
        "ICMP"  :0,
        "Other" :0
    }
    total_bytes = 0
    src_ip_count = {}
    dst_ip_count = {}
#test commit
    #For each packet in packets:
    for packet in packets:
        if packet.haslayer(IP):
            total_bytes = total_bytes + len(packet)

            #count source IPs
            src_ip = packet[IP].src
            #if src_ip in src_ip_count:
            if src_ip in src_ip_count:
                src_ip_count[src_ip] += 1
            else:
                src_ip_count[src_ip] == 1

            #Count dst IPs
            dst_ip = packet[IP].dst
            if dst_ip in dst_ip_count:
                dst_ip_count[dst_ip] += 1
            else:
                dst_ip_count[dst_ip] == 1
            
            #Count protocols
            if packet.haslayer(TCP):
                protocol_counts["TCP"] += 1
            elif packet.haslayer(UDP):
                protocol_counts["UDP"] += 1
            elif packet.haslayer(ICMP):
                protocol_counts["ICMP"] += 1
            else:
                protocol_counts["Others"] += 1

    analysis = {
        "protocol_counts"   : protocol_counts,
        "total_bytes"       : total_bytes,
        "src_ip_count"      : src_ip_count,
        "dst_ip_count"      : dst_ip_count
        }
    return analysis
    
def display_analysis(analysis: dict) -> None:
    
    print("================================")
    print("   Traffic Analysis Results     ")
    print("================================")

    #protocol breakdown
    for protocol, count in analysis["protocol_counts"].items():
        print(f"{protocol} : {count}")

    #total bytes
        print(f"Total Bytes Captureed: {analysis["total_bytes"]}")

    #top 5 source ip (print this)
    top_src = sorted(analysis['src_ip_count'].items(), key=lambda x: x[1], reverse=True)[:5]
    for s_ip, count in top_src:
        print(f"{s_ip}: {count} packets...")

    #top 5 destination ip
    top_dst = sorted(analysis['dst_ip_count'].items(), key = lambda y: y[1], reverse=True)[:5]
    for d_ip, count in top_dst:
        print(f"{d_ip}: {count} packets...")
       
def start_traffic_analyzer(packets: list) -> None:
    if not packets:
        print("No packets to analyze...")
        return
    analysis = analyze_traffic(packets)
    display_analysis(analysis)
  