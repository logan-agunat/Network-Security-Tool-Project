############################################################
#Author: Logan Agunat
#Date created: 3/13/26
#Date last modified:
#Description: Device Discovery module. Purpose is to
#              identify active devices on the local network
############################################################

#START DeviceDiscovery

    # ── STEP 1: Get Network Info ──────────────────────────────
    #network_info ← GET_NETWORK_INFORMATION()
        #local_ip     ← GET_LOCAL_IP()
        #gateway      ← GET_DEFAULT_GATEWAY()

        #IF local_ip IS null THEN
            #DISPLAY "Error: Could not determine local IP"
            #EXIT
        #END IF

    #RETURN { local_ip, subnet_mask, gateway }

    # ── STEP 2: Generate IP Range ─────────────────────────────
    #scan_range ← GENERATE_IP_RANGE(network_info)
        #network_base ← CALCULATE_NETWORK_ADDRESS(local_ip, subnet_mask)
        #total_hosts  ← CALCULATE_HOST_COUNT(subnet_mask)

        #ip_list ← EMPTY_LIST
        #FOR i FROM 1 TO total_hosts
            #ADD network_base + i TO ip_list
        #END FOR

        #EXCLUDE local_ip FROM ip_list   # don't scan yourself

    #RETURN ip_list

    # ── STEP 3: Run Discovery Scan ────────────────────────────
    #discovered_devices ← RUN_DISCOVERY_SCAN(scan_range)
        #device_list  ← EMPTY_LIST
        #failed_list  ← EMPTY_LIST

        #FOR each ip IN scan_range (run in parallel threads)

            #response ← PROBE_DEVICE(ip)

            #IF response EXISTS THEN
                #device_info ← COLLECT_DEVICE_DATA(ip, response)

                #IF device_info IS VALID THEN
                    #ADD device_info TO device_list
                #ELSE
                    #ADD ip TO failed_list
                #END IF
            #END IF

       #END FOR (wait for all threads)

        #IF failed_list IS NOT EMPTY THEN
            #LOG "Failed to collect data for: " + failed_list
        #END IF

    #RETURN device_list

    # ── STEP 4: Probe Device ──────────────────────────────────
    #FUNCTION PROBE_DEVICE(ip_address)
        #max_retries ← 3
        #timeout     ← 1000ms

        #FOR attempt FROM 1 TO max_retries

            #SEND ICMP_PING TO ip_address
            #WAIT for reply UNTIL timeout

            #IF reply_received THEN
                #RETURN reply
            #ELSE
                #IF attempt < max_retries THEN
                    #WAIT 500ms  # backoff before retry
                #END IF
            #END IF

        #END FOR

        #RETURN null  # no response after all retries

    #END FUNCTION

    # ── STEP 5: Collect Device Data ───────────────────────────
    #FUNCTION COLLECT_DEVICE_DATA(ip_address, response)
        #device ← NEW_DEVICE

        #device.ip      ← ip_address
        #device.mac     ← PARSE_MAC_FROM_RESPONSE(response)
        #device.latency ← CALCULATE_RESPONSE_TIME(response)
        #device.status  ← "active"
        #device.timestamp ← GET_CURRENT_TIME()

        #IF device.mac IS NOT null THEN
            #device.vendor ← LOOKUP_MAC_VENDOR(device.mac)
        #ELSE
            #device.vendor ← "Unknown"
        #END IF

        # Optional: try to resolve hostname
        #device.hostname ← REVERSE_DNS_LOOKUP(ip_address)
        #IF hostname FAILS THEN
            #device.hostname ← "Unknown"
        #END IF

    #RETURN device

    #END FUNCTION

    # ── STEP 6: Display Results ───────────────────────────────
    #DISPLAY_RESULTS(discovered_devices)

        #IF discovered_devices IS EMPTY THEN
            #DISPLAY "No active devices found."
            #EXIT
        #END IF

        #SORT discovered_devices BY ip ASC

        #DISPLAY "Active Devices Found: " + COUNT(discovered_devices)
        #DISPLAY separator line

        #FOR each device IN discovered_devices
           #PRINT device.ip
           #PRINT device.mac
           #PRINT device.vendor
           #PRINT device.hostname
            #PRINT device.latency + "ms"
            #PRINT device.timestamp
            #PRINT separator line
        #END FOR

        # Optional: export
        #IF export_enabled THEN
            #SAVE discovered_devices TO "scan_results.csv"
        #END IF

#END DeviceDiscovery