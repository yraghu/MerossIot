import os
import unittest

from meross_iot.manager import MerossManager

EMAIL = os.environ.get('MEROSS_EMAIL')
PASSWORD = os.environ.get('MEROSS_PASSWORD')


class TestMS100Test(unittest.TestCase):
    def setUp(self):
        self.manager = MerossManager(meross_email=EMAIL, meross_password=PASSWORD)
        self.manager.start()

        # Retrieves the list of supported devices
        devices = self.manager.get_devices_by_type('ms100')
        if len(devices) > 0:
            self.device = devices[0]
        else:
            self.skipTest("Could not find any MS100 device.")

    def test_properties(self):
        t = self.device.temperature
        h = self.device.humidity
        self.assertTrue(t is not None)
        self.assertTrue(h is not None)

    def test_get_info(self):
        state = self.device.get_status()
        assert state is not None

        wifi_list = self.device.get_wifi_list()
        assert wifi_list is not None

        trace = self.device.get_trace()
        assert trace is not None

        debug = self.device.get_debug()
        assert debug is not None

    def tearDown(self):
        self.manager.stop()


if __name__ == '__main__':
    unittest.main()

