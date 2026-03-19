from scapy.arch.windows import get_windows_if_list

for iface in get_windows_if_list():
    print(iface['name'], '|', iface['description'])