import unittest

import port_scanner


class UnitTests(unittest.TestCase):
    def test_verify_target(self):
        actual = port_scanner.verify_target("266.255.9.10")
        expected = (None, None, "Error: Invalid IP address")
        self.assertEqual(actual, expected, "Expected host/ip information to match.")
        actual = port_scanner.verify_target("209.216.230.240")
        expected = ("209.216.230.240", "news.ycombinator.com", None)
        self.assertEqual(actual, expected, "Expected host/ip information to match.")
        actual = port_scanner.verify_target("www.stackoverflow.com")
        host = "www.stackoverflow.com"
        ips = (
            "151.101.1.69",
            "151.101.65.69",
            "151.101.129.69",
            "151.101.193.69",
        )
        self.assertEqual(actual[1], host, "Expected hosts to match.")
        self.assertIn(actual[0], ips, "Expected IP address information to match.")
        self.assertIsNone(actual[2], "Expected error to be None.")
        actual = port_scanner.verify_target("scanme.nmap.org")
        expected = ("45.33.32.156", "scanme.nmap.org", None)
        self.assertEqual(actual, expected, "Expected host/ip information to match.")
        actual = port_scanner.verify_target("104.26.10.78")
        expected = ("104.26.10.78", None, None)
        self.assertEqual(actual, expected, "Expected host/ip information to match.")
        actual = port_scanner.verify_target("137.74.187.104")
        expected = ("137.74.187.104", "hackthissite.org", None)
        self.assertEqual(actual, expected, "Expected host/ip information to match.")
        actual = port_scanner.verify_target("scanme.nmap")
        expected = (None, None, "Error: Invalid hostname")
        self.assertEqual(actual, expected, "Expected host/ip information to match.")

    def test_port_scanner_ip(self):
        ports = port_scanner.get_open_ports("209.216.230.240", [440, 445], False)
        actual = ports
        expected = [443]
        self.assertEqual(
            actual,
            expected,
            "Expected scanning ports of IP address " "to return [443].",
        )

    def test_port_scanner_url(self):
        ports = port_scanner.get_open_ports("www.stackoverflow.com", [79, 82], False)
        actual = ports
        expected = [80]
        self.assertEqual(
            actual,
            expected,
            "Expected scanning ports of URL address " "to return [80].",
        )

    def test_port_scanner_url_multiple_ports(self):
        ports = port_scanner.get_open_ports("scanme.nmap.org", [20, 80], False)
        actual = ports
        expected = [22, 80]
        self.assertEqual(
            actual,
            expected,
            "Expected scanning ports of URL address " "to return [22, 80].",
        )

    def test_port_scanner_verbose_ip_no_hostname_returned_single_port(self):
        actual = port_scanner.get_open_ports("104.26.10.78", [440, 450], True)
        expected = "Open ports for 104.26.10.78\n" "PORT     SERVICE\n443      https"
        self.assertEqual(
            actual,
            expected,
            "Expected 'Open ports for 104.26.10.78\n"
            "PORT     SERVICE\n443      https'",
        )

    def test_port_scanner_verbose_ip_hostname_returned_multiple_ports(self):
        actual = port_scanner.get_open_ports("137.74.187.104", [440, 450], True)
        expected = (
            "Open ports for hackthissite.org (137.74.187.104)\n"
            "PORT     SERVICE\n443      https"
        )
        self.assertEqual(
            actual,
            expected,
            "Expected 'Open ports for "
            "hackthissite.org (137.74.187.104)\n"
            "PORT     SERVICE\n443      https'",
        )

    def test_port_scanner_verbose_hostname_multiple_ports(self):
        actual = port_scanner.get_open_ports("scanme.nmap.org", [20, 80], True)
        expected = (
            "Open ports for scanme.nmap.org (45.33.32.156)\n"
            "PORT     SERVICE\n"
            "22       ssh\n"
            "80       http"
        )
        self.assertEqual(
            actual,
            expected,
            "Expected 'Open ports for scanme.nmap.org"
            " (45.33.32.156)\n"
            "PORT     SERVICE\n"
            "22       ssh\n"
            "80       http'",
        )

    def test_port_scanner_invalid_hostname(self):
        actual = port_scanner.get_open_ports("scanme.nmap", [22, 42], False)
        expected = "Error: Invalid hostname"
        self.assertEqual(actual, expected, "Expected 'Error: Invalid hostname'")

    def test_port_scanner_invalid_ip_address(self):
        actual = port_scanner.get_open_ports("266.255.9.10", [22, 42], False)
        expected = "Error: Invalid IP address"
        self.assertEqual(actual, expected, "Expected 'Error: Invalid IP address'")


if __name__ == "__main__":
    unittest.main()
