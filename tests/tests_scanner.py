############################################################
#Author: Logan Agunat
#Date created: 3/16/26
#Date last modified:
#Description: Test file for scanner.py   
############################################################
from unittest.mock import patch

from scapy.layers.inet import ICMP, IP

from utils import scanner

# === Test Functions: Local Fake Server (Non-live) ===

def test_probe_device_returns_response():
 fake = IP(src="192.168.1.1") / ICMP()
 with patch.object(scanner, "sr1", return_value = fake):
    assert scanner.probe_device("192.168.1.1") is fake

def test_prob_device_returns_none_when_no_reply():
    with patch.object(scanner, "sr1", return_value=None):
       assert scanner.probe_device("10.0.0.9") is None

def test_probe_device_returns_none_or_error():
    with patch.object(scanner, "sr1", side_effect=OSError):
       assert scanner.probe_device("10.0.0.9") is None

def test_run_discovery_scan_empty_range():
   assert scanner.run_discovery_scan([]) == []

def test_run_discovery_scan_keeps_only_responders():
    def fake_probe(ip):
       return object() if ip.endswith(".2") else None

    with patch.object(scanner, "probe_device", side_effect=fake_probe), \
        patch.object(scanner, "collect_device_data",
                    side_effect=lambda ip, response: {"ip": ip}):
        result = scanner.run_discovery_scan(["10.0.0.1", "10.0.0.2"])
    assert result == [{"ip": "10.0.0.2"}]

def test_run_discovery_scan_probes_each_ip_once():
    ips = ["10.0.0.1", "10.0.0.2", "10.0.0.3"]
    with patch.object(scanner, "probe_device", return_value=None) as probe:
       scanner.run_discovery_scan(ips)
    assert probe.call_count == len(ips)     


    
