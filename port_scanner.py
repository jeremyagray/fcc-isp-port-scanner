#!/usr/bin/env python

import socket
import common_ports

def verify_target(target):
    # determine if target is hostname or ip.
    # verify the host and ip.
    # store and return in a dict.

    host = ''
    ip = ''

    return {'host': host, 'ip': ip}

def get_open_ports(target, port_range, verbose=False):
    open_ports = []

    # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    for port in range(port_range[0], port_range[1] + 1, 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)

        try:
            ip = socket.gethostbyname(target)
            # socket.inet_pton(socket.gethostbyname(target))
        except socket.error:
            return 'Error: Invalid IP address'
        try:
            host = socket.getfqdn(target)
        except socket.error:
            return 'Error: Invalid hostname'

        # do something with sock to test if open
        addr = (ip, port)
        status = sock.connect_ex(addr)
        sock.close()
        # sock.detach()

        print('ip: {} port: {} status: {}'.format(ip, port, status))

        if (status == 0):
            open_ports.append(port)

    # process based on verbose
    if verbose:
        report = []
        if (host == ip):
            report.append('Open ports for ' + ip)
        else:
            report.append('Open ports for ' + host + ' (' + ip + ')')
        report.append('PORT     SERVICE')
        for port in open_ports:
            try:
                report.append('{: <9}'.format(str(port)) + common_ports.ports_and_services[port])
            except KeyError:
                report.append('{: <9}'.format(str(port)) + str(port))
        return '\n'.join(report)
    else:
        return open_ports
