############################################################
#Author: Logan Agunat
#Date created: 3/13/26
#Date last modified:
#Description: Device Discovery module. Purpose is to
#              identify active devices on the local network
############################################################
from utils.network import get_network_information, generate_ip_range
from utils.scanner import run_discovery_scan

#START DeviceDiscovery

   

    # ── STEP 6: Display Results ───────────────────────────────
def display_results(discovered_devices: list) -> None:

        #IF discovered_devices IS EMPTY THEN
            #DISPLAY "No active devices found."
            #EXIT
        #END IF
        if discovered_devices == []: 
             print("No active devices found")
             return

        #SORT discovered_devices BY ip ASC
        discovered_devices.sort(key=lambda device: device["ip"]) #lambda will loop through each device in the list 
                                                                  # and sort by ip address value

        print("Active Devices Found: " + {len(discovered_devices)})
        print("==================================================")
        for  device in discovered_devices:
           print ("IP:" + device["ip"])
           print("MAC: " + device["mac"])
           print("Vendor:   " + device["vendor"])
           print("Hostname: " + device["hostname"])
           print("Latency:  " + device["latency"] + "ms")
           print("Timestamp:    " + device["timestamp"])
           print("==================================================")

        # Optional: export
        #IF export_enabled THEN
            #SAVE discovered_devices TO "scan_results.csv"
        #END IF

def start_discovery() -> None:
    network_info = get_network_information
    if network_info is None:
        print("Error: Could not deterkmine network information.")
        return
    #generate ip range
    scan_range = generate_ip_range(network_info)
    print("Scanning" + {len(scan_range)} + "IP addresses...." )

    # run discovery scan
    discovered_devices = run_discovery_scan(scan_range)

    #display results
    display_results(discovered_devices)