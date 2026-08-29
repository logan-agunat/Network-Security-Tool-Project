## Technologies Used:
    Python (core language)
    socket (network communication)
    subprocess (system interaction)
    ipaddress (IP range handling)


## Overview:
      -Device discovery on local networks
      -Port scanning for open services
      -Packet sniffing and traffic analysis
      -Detection of basic suspicious behavior

### Device Discovery Module
    Responsible for identifying active devices on the local network.
    Uses IP range iteration and network probing to detect live hosts.

### Port Scanner Module
    Scans the discovered devices for open ports.
    Determines which services may be running.

### Packet Sniffer Module
    Captures live network traffic for analysis.
    Processes packet-level data for inspection.

### Traffic Analyzer Module
    Analyzes captured traffic to identify usage patterns and anomalies.

### Alert Engine Module
    Evaluates network behavior and flags suspicious activity such as:
        -Port scanning
        -Unusual traffic spikes
        -Repeated connection attempts
