from tests import test_base
import requests


class TestOrderDelivery(test_base.TestBase):
    path = "/order/delivery"

    def request(self):
        self.response = requests.request(
            method="POST", url=self.environment["host"] + self.path, headers=self.environment["headers"], data={
            })
        return self
