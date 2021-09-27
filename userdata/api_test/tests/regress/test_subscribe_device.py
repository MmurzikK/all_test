from tests import test_base
import requests


class TestSubscribeDevice(test_base.TestBase):
    path = "/events/subscribe/{subscribe_device}"

    def request(self):
        self.response = requests.request(
            method="PUT", url=self.environment["host"] + self.path.format(
                subscribe_device=self.environment["custom_variables"]["subscribe_device"]), headers=self.environment["headers"])
        return self
