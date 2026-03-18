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
## Project Phases:
      P1: Get it working on my machine(Windows) # current phase
        - complete all util files and test files
        - Complete/test/run all modules
        - test it end to end
        - fix bugs

      P2: Make it robust
        - Improve error handling
        - Add input validation
        - Replace print statements with logging

      P3: Cross platform?
        - Detect operating system
        - Implement OS-specific logic

      P4: Security Hardening?
        - Add rate limiting
        - Validate IP ranges
        - Require permission checks
        
      P5: Extra features?
        - Export results to csv or json
        - Build simple UI
## Architecture:

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
