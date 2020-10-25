#!/usr/bin/env python

# This entrypoint file to be used in development. Start by reading README.md
import port_scanner
from unittest import main

# # Called with URL
# ports = port_scanner.get_open_ports("www.freecodecamp.org", [75,85]) or ''
# print("Open ports:", ports)

# # Called with ip address
# ports = port_scanner.get_open_ports("104.26.10.78", [8079, 8090]) or ''
# print("Open ports:", ports)

# Local.
# ports = port_scanner.get_open_ports("192.168.1.78", [2990, 3010]) or ''
# print("Open ports:", ports)
# ports = port_scanner.get_open_ports("192.168.1.254", [70, 90]) or ''
# print("Open ports:", ports)
# ports = port_scanner.get_open_ports("192.168.1.78", [2990, 3010], True) or ''
# print(ports, '\n')
# ports = port_scanner.get_open_ports("192.168.1.254", [70, 90], True) or ''
# print(ports, '\n')

# # Verbose called with ip address and no host name returned -- single open port
# ports = port_scanner.get_open_ports("104.26.10.78", [440, 450], True) or ''
# print(ports + '\n')

# Verbose called with ip address and valid host name returned -- single open port
# ports = port_scanner.get_open_ports("137.74.187.104", [440, 450], True) or ''
# print(ports + '\n')

# Verbose called with host name -- multiple ports returned
ports = port_scanner.get_open_ports("scanme.nmap.org", [20, 80], True) or ''
print(ports + '\n')

# # Run unit tests automatically
# main(module='test_module', exit=False)