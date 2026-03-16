############################################################
#Author: Logan Agunat
#Date created: 3/16/26
#Date last modified:
#Description: Test file for network.py     
############################################################

from utils.network import (
     get_local_ip,
    get_subnet_mask,
    get_default_gateway,
    get_network_information,
    calc_network_address,
    calc_host_count,
    generate_ip_range
)

# ==== Test Functions ====
def test_get_local_ip() -> None:
    result = get_local_ip()
    print("Local IP: " + result)
    #check if function returned a value and does not fail
    assert result is not None
    #check that value returned is correct data type
    assert isinstance(result, str)

def test_get_subnet_mask() -> None:
    local_ip = get_local_ip()
    result2  = get_subnet_mask(local_ip)
    print("Subnet Mask: " + result2)
    assert result2 is not None
    assert isinstance(result2, str)

def test_get_default_gateway() -> None:
    result3 = get_default_gateway()
    print("Default Gateway: " + result3)
    assert result3 is not None
    assert isinstance(result3, str)

def test_get_network_information() -> None:
    result4 = get_network_information()
    print("Network Information: " + result4)
    assert result4 is not None
    assert isinstance(result4, dict)
    assert "local_ip" in result4
    assert "subnet_mask" in result4
    assert "gateway" in result4

def test_calc_network_address() -> None:
    local_ip = get_local_ip
    subnet_mask = get_subnet_mask(local_ip)
    result5 = calc_network_address(local_ip, subnet_mask)
    print("Network Address: " + result5)
    assert result5 is not None
    assert isinstance(result5, str)

def test_calc_host_count() -> None:
    local_ip = get_local_ip()
    subnet_mask = get_subnet_mask(local_ip)
    result6 = calc_host_count(subnet_mask)
    print("Host Count: " + result6)
    assert result6 is not None
    assert isinstance(result6, int)

def test_generate_ip_range() -> None:
    network_info = get_network_information()
    result7 = generate_ip_range(network_info)
    print("IP Range Count: " + len(result7))
    assert result7 is not None
    assert  isinstance(result7, list)
    assert len(result7) > 0

# ==== Run All Test Functions ====
if __name__ == "__main__":
    test_get_local_ip() 
    test_get_subnet_mask()
    test_get_default_gateway()
    test_get_network_information()
    test_calc_network_address()
    test_calc_host_count()
    test_generate_ip_range()
    print("All Tests have passed!")
