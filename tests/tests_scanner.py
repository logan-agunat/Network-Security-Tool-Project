############################################################
#Author: Logan Agunat
#Date created: 3/16/26
#Date last modified:
#Description: Test file for scanner.py   
############################################################
from utils.scanner import(
    probe_device,
    run_discovery_scan
)

# === Test Functions ===

def test_probe_device() -> None:
    #testing with local host (should always respond)
    result1a = probe_device("127.0.0.1")
    print("Pobe localhost: " + str(result1a))
    assert result1a is not None

    #testing with invali ip - returns None
    result1b = probe_device("0.0.0.0")
    assert result1b is None
    print("test_probe_device has passed!")

def test_run_discovery_scan() -> None:
    #testing with small range containing localhost
    result2a = run_discovery_scan(["127.0.0.1"])
    print("Discovery scan result: " + str(result2a))
    assert result2a is not None
    assert isinstance(result2a, list)

    #test with empty list
    result2b = run_discovery_scan([])
    assert result2b == []
    print("test_run_discovery_scan has passed!")

if __name__ == "__main__":
    test_probe_device()
    test_run_discovery_scan()
