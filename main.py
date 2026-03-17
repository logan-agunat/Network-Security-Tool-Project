############################################################
#Author: Logan Agunat
#Date created: 3/13/26
#Date last modified:
#Description: Main drive of the program
############################################################
from device_discovery import start_discovery
from port_scanner import scan_ports


# Header
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

def get_user_choice() -> str:
    user_input = input("Enter your choice: ")
    return user_input

def main() -> None:
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
        #Packet Sniffer
        elif choice == "3":
            

       # ELSE IF choice EQUALS "3" THEN
            #PRINT "Exiting..."
            #EXIT

       # ELSE
            #PRINT "Invalid choice. Please try again."
        #END IF
    #END WHILE
 

