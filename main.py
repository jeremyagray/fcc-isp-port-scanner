#!/usr/bin/env python

from unittest import main
# import port_scanner

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

# Verbose called with ip address and no host name returned -- single
# open port
# ports = port_scanner.get_open_ports("104.26.10.78", [440, 450], True) or ''
# print(ports + '\n')

# Verbose called with ip address and valid host name returned --
# single open port
# ports = port_scanner.get_open_ports("137.74.187.104", [440, 450], True) or ''
# print(ports + '\n')

# Verbose called with host name -- multiple ports returned
# ports = port_scanner.get_open_ports("scanme.nmap.org", [20, 80], True) or ''
# print(ports + '\n')

# new.ycombinator.com
# ports = port_scanner.get_open_ports("209.216.230.240", [440, 445], False)

# Run unit tests.
main(module='test_module', exit=False)
