############################################################
#Author: Logan Agunat
#Date created: 3/16/26
#Date last modified:
#Description: Test file for scanner.py   
############################################################
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.vendor import (lookup_mac_vendor)

def test_lookup_mac_vendor() -> None:
    #test with None
    result1 = lookup_mac_vendor(None)
    assert result1 == "Unknown"
    print("None test has passed!")

    #test with Unknown
    result2 = lookup_mac_vendor("Unknown") 
    assert result2 == "Unknown"
    print("Unknown test has passed!")
 

    #test with a known MAC address
    result3 = lookup_mac_vendor("00:1A:2B:3C:4D:5E") 
    print("Vendor lookup result: "+ result3)
    assert result3 is not None
    assert isinstance(result3, str)

    print("test_lookup_mac_vendor has passed!")

if __name__ == "__main__":
    test_lookup_mac_vendor()
    print("All vendor tests have passed!")