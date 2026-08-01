from datetime import timedelta
import unittest
from unittest.mock import patch

from health_report import bytes_to_gib, get_disk_status, get_uptime


class TestGetUptime(unittest.TestCase):
    def test_controlled_uptime_text_returns_expected_duration(self):
        with patch(
            "health_report.Path.read_text",
            return_value="3661.75 99999.00\n",
        ) as mock_read_text:
            result = get_uptime()

            self.assertEqual(result, timedelta(seconds=3661))
            mock_read_text.assert_called_once_with()


class TestBytesToGib(unittest.TestCase):
    def test_zero_bytes_returns_zero_gib(self):
        self.assertEqual(bytes_to_gib(0), 0.0)

    def test_half_gibibyte_returns_half_gib(self):
        self.assertEqual(bytes_to_gib(536870912), 0.5)

    def test_one_gibibyte_returns_one_gib(self):
        self.assertEqual(bytes_to_gib(1073741824), 1.0)


class TestGetDiskStatus(unittest.TestCase):
    def test_value_below_80_returns_ok(self):
        self.assertEqual(get_disk_status(79.9), "OK")

    def test_80_returns_warning(self):
        self.assertEqual(get_disk_status(80), "WARNING")

    def test_value_below_90_returns_warning(self):
        self.assertEqual(get_disk_status(89.9), "WARNING")

    def test_90_returns_critical(self):
        self.assertEqual(get_disk_status(90), "CRITICAL")

    def test_value_below_zero_raises_value_error(self):
        with self.assertRaises(ValueError):
            get_disk_status(-0.1)

    def test_value_above_100_raises_value_error(self):
        with self.assertRaises(ValueError):
            get_disk_status(100.1)

    def test_zero_returns_ok(self):
        self.assertEqual(get_disk_status(0), "OK")

    def test_100_returns_critical(self):
        self.assertEqual(get_disk_status(100), "CRITICAL")
