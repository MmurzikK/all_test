from tests import test_base
import requests


class TestCompare(test_base.TestBase):
    path = "/compare/598682"

    def request(self):
        self.response = requests.request(
            method="PUT", url=self.environment["host"] + self.path, headers=self.environment["headers"])
        return self
