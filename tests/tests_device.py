############################################################
#Author: Logan Agunat
#Date created: 3/16/26
#Date last modified:
#Description: Test file for device.py     
############################################################
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from utils.device import(
    reverse_dns_lookup,
    calculate_response_time,
    parse_mac_from_response,
    collect_device_data
)

# === Test Functions ===

def test_reverse_dns_lookup():
    # test with known local ip
    result1a  = reverse_dns_lookup("127.0.0.1")
    assert result1a is None
    assert isinstance(result1a, str)
    print("Hostname for IP" + result1a) #fix the ip portion

    #test with invalid ip
    result1b = reverse_dns_lookup("0.0.0.0.")
    assert result1b == "unknown"
    print("reverse dns lookup test has passed!")

def test_calculate_response_time():
    pass
def test_parse_mac_from_response():
    pass
def test_collection_device_data():
    pass