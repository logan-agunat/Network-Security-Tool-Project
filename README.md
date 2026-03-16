Network-Security-Tool-Project
Date started: 3/13/25

Project Description:
  This is a python based network analysis/security tool, designed to explore security/networking concepts like port scanning,
  device discovery, and network traffic analysis.
  Project was created as a learning exercise to understand network security, build skills in python, etc.
  Drew conceptual inspiration from Nmap & Wireshark.

  Overview:
    Project aim:
      -Identify devices on a local network
      - Analyze network services exposed by those devices
      - Monitor network traffic patterns
      - Detect potentially suspicious behavior

    Project Phases:
      P1: Get it working on my machine
        - complete all util files, etc
        - test it end to end
        - fix bugs
      P2: Make it robust
        - Better error handling
        - Input validation
        - Logging instead of print errors
      P3: Cross platform?
        - Adding platform detection
        - Different code paths for each OS
      P4: Security Hardening?
        - Rate limiting to prevent flooding network
        - Permission checks before scans
        - IP range validation before scan
        - Add warning before any scans run
      P5: Extra features?
        - Export results to csv or json
        - Create simple UI

    Features/Planned modules:
      Device Discovery:
        Scans the local network to identify active devices
      Port Scanner:
        Identifies open ports/services running on discovered devices
      Packet Sniffer:
        Capture and analyzes live network packets
      Traffic Analyzer:
        Summarize captured traffic and identifies protocol usage
      Alert Engine:
        Detects potentially suspicious behavior such as:
          - port scanning, unusual traffic spikes, repeated connection attempts

    Architecture:
      Network Security Tool
        -> Device Discovery
        -> Port Scanner
        -> Packet Sniffer
        -> Traffic Analyzer
        -> Alert Engine

      Project Structure:
        main program
          modules
            - device discovery
            - port scanner
            - packet sniffer
            - traffic analyzer
            - alert engine
          utilities(util)
            - networking helper functions
            - packet parsing
            - logging
          logs
          documentation

      
      

  

