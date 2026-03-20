############################################################
#Author: Logan Agunat
#Date created: 3/13/26
#Date last modified:
#Description: Main drive of the program
############################################################
from modules.device_discovery import start_discovery
from modules.port_scanner import scan_ports
from modules.packet_sniffer import start_sniffer, sniff_packets
from modules.traffic_analyzer import start_traffic_analyzer
from modules.alert_engine import start_alert_engine

def get_user_choice() -> str:
    user_input = input("Enter your choice: ")
    return user_input

def main() -> None:
    print("================================")
    print("     NETWORK SECURITY TOOL      ")
    print("================================")
    #Menu
    print("1. Device Discovery")
    print("2. Port Scanner")
    print("3. Packet Sniffer")
    print("4. Traffic Analyzer")    
    print("5. Alert Engine")
    print("6. Exit")
    print("================================")
    
    while True:
        choice = get_user_choice()
        # Device Discovery
        if choice == "1": 
            start_discovery()
        #Port Scanner
        elif choice == "2":
            ip_address = (input("Enter target IP Address: "))
            start_port = int(input("Enter start port: "))
            end_port = int(input("Enter end port: "))
            port_range = range(start_port, end_port + 1)
            scan_ports(ip_address, port_range)
            print(f"Open ports on {ip_address}: {list(port_range)}")
        #Packet Sniffer
        elif choice == "3":
            interface = input("Enter network in interface(e.g: eth0, Wi-Fi): ")
            pkt_count = int(input("Enter number of packets to capture: "))
            start_sniffer(interface, pkt_count)
        #Traffic Analyzer
        elif choice == "4":
            interface = input("Enter network interface: ")
            count = int(input("Enter number of packets to capture: "))
            packets = sniff_packets(interface, count)
            start_traffic_analyzer(packets)
        #Alert Engine
        elif choice == "5":
            interface = input("Enter network interface: ")
            count = int(input("Enter number of packets to capture: "))
            start_alert_engine(interface, count)
        elif choice == "6":
            print("Exiting program.......")
            exit()
            
            
if __name__ == "__main__":
    main()

