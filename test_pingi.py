import unittest
import pingi

class TestPingi(unittest.TestCase):

    def test_cmd_parser_default(self):
        addr, interval, file_name = pingi.parse_pingi_args([])
        self.assertEqual(addr, "8.8.8.8")
        self.assertAlmostEqual(interval, 5.0)
        self.assertEqual(file_name, "ping.csv")

    def test_cmd_parser(self):
        addr, interval, file_name = pingi.parse_pingi_args(["-d", "www.blick.ch", "-i", "2.0", "-o", "abc.csv"])
        self.assertEqual(addr, "www.blick.ch")
        self.assertAlmostEqual(interval, 2.0)
        self.assertAlmostEqual(file_name, "abc.csv")

if __name__ == '__main__':
    unittest.main()
