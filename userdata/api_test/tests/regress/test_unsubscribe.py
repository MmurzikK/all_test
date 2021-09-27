from tests import test_base
import requests


class TestUnsubscribe(test_base.TestBase):
    path = "/events/unsubscribe/{subscribe_device}"

    def request(self):
        self.response = requests.request(
            method="DELETE", url=self.environment["host"] + self.path.format(
                subscribe_device=self.environment["custom_variables"]["subscribe_device"]), headers=self.environment["headers"], data={
            })
        return self
