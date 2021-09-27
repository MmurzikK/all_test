from tests import test_base
import requests


class TestDelCompareProducts(test_base.TestBase):
    path = "/compare/products/598682"

    def request(self):
        self.response = requests.request(
            method="DELETE", url=self.environment["host"] + self.path, headers=self.environment["headers"], data={
            })
        return self
