#!/usr/bin/env python

import common_ports
import re
import socket


def scan(addr, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    status = sock.connect_ex((addr, port))
    sock.close()

    return status


# Convert the target ip/host into a ip, host tuple.
def verify_target(target):
    host = None
    ip = None
    error = None
    match = re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', target)

    if match:
        ip = match.group(0)

        try:
            host = socket.gethostbyaddr(ip)[0]
        except socket.herror:
            host = None
        except socket.gaierror:
            host = None
            ip = None
            error = 'Error: Invalid IP address'
    else:
        if re.match(target, socket.getfqdn(target)) \
           or re.match(socket.getfqdn(target), target):
            try:
                host = target
                ip = socket.gethostbyname_ex(host)[2][0]
            except (socket.herror, socket.gaierror):
                host = None
                ip = None
                error = 'Error: Invalid hostname'
        else:
            host = None
            ip = None
            error = 'Error: Invalid hostname'

    return (ip, host, error)


def get_open_ports(target, port_range, verbose=False):
    # print('verifying target:  {}'.format(target))
    (ip, host, error) = verify_target(target)
    # print('verification ip:  {} host:  {} error:  {}'.format(ip, host, error))

    if error:
        return error

    open_ports = []

    for port in range(port_range[0], port_range[1] + 1, 1):
        # print('scanning {}:{}'.format(ip, port))
        if (scan(ip, port) == 0):
            # print('{}:{} open'.format(ip, port))
            open_ports.append(port)

    # process based on verbose
    if verbose:
        report = []

        if host:
            report.append('Open ports for ' + host + ' (' + ip + ')')
        else:
            report.append('Open ports for ' + ip)

        report.append('PORT     SERVICE')

        for port in open_ports:
            try:
                report.append('{: <9}{}'
                              .format(str(port),
                                      common_ports.ports_and_services[port]))
            except KeyError:
                report.append('{: <9}{}'.format(str(port), str(port)))

        return '\n'.join(report)

    else:
        return open_ports
