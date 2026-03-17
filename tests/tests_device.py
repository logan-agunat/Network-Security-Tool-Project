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

def test_reverse_dns_lookup() -> None:
    # test with known local ip
    result1a  = reverse_dns_lookup("127.0.0.1")
    assert result1a is None
    assert isinstance(result1a, str)
    print("Hostname for 127.0.0.1" + result1a) 
    #test with invalid ip
    result1b = reverse_dns_lookup("0.0.0.0.")
    assert result1b == "unknown"
    print("test_reverse_dns_lookup test has passed!")

def test_parse_mac_from_response() -> None:
    result2a = parse_mac_from_response(None)
    assert result2a is None
    #test with a mock response that has no Ether layer
    result2b = parse_mac_from_response("invalid")
    assert result2b == "unknown"
    print*("test_parse_mac_from_response has passed!")


def test_calculate_response_time() -> None:
    result3a = calculate_response_time(None)
    assert result3a is None
    #trest with an invlaid response
    result3b = calculate_response_time("invalid")
    assert result3b == "unknown"
    print("test_calculate_response_time has passed!")
    
def test_collection_device_data() -> None:
    #test with a None response
    result4a = collect_device_data(None)
    assert result4a is None
    #test with an invalid response
    result4b = collect_device_data("invalid")
    assert result4b is not None
    assert isinstance(result4b, dict)
    assert "ip" in result4b
    assert "mac" in result4b
    assert "vendor" in result4b
    assert "hostname" in result4b
    assert "latency" in result4b
    assert "timestamp" in result4b
    assert result4b["ip"] == "192.168.1.1"
    print("test_collection_device_data has passed!")

if __name__ == "__main__":
    test_reverse_dns_lookup()
    test_parse_mac_from_response()
    test_calculate_response_time()
    test_collection_device_data()
    print("All device tests has passed!")
