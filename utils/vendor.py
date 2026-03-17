############################################################
#Author: Logan Agunat
#Date created: 3/16/26
#Date last modified:
#Description: Has the neccessary helper functions
############################################################
"""vendor.py
Description:
    Looks up the manufacturer of a network device using its MAC address
    by querying the macvendors.com API.
Functions:
    lookup_mac_vendor(mac_address)  - Returns the vendor name for a given MAC address
Dependencies:
    requests
    """
import requests

def lookup_mac_vendor(mac_address: str) -> str:
    """Look up the vendor/manufacturer of a device using its MAC address.
    Parameters:
        mac_address (str): The MAC address to look up
    Returns:
        str: The vendor name
        str: "Unknown" if the lookup fails or the MAC address is invalid
    """
    if mac_address is None:
        return "Unknown"
    if mac_address == "Unknown":
        return "Unknown"
    try:
        #Build the API URL
        url = "https://api.macvendors.com" + mac_address
        response = requests.get(url)
        #Check if the request was successful
        if response .status_code == 200:
            return response.text
        else:
            return "Unknown"
    except Exception:
        return "Unknown"
    

