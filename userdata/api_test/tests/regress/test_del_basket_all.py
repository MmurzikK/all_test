from tests import test_base
import requests


class TestDelBasketAll(test_base.TestBase):
    path = "/basket/all"

    def request(self):
        self.response = requests.request(
            method="DELETE", url=self.environment["host"] + self.path, headers=self.environment["headers"], data={
            })
        return self
