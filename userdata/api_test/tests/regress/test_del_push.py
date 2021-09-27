from tests import test_base
import requests


class TestDelPush(test_base.TestBase):
    path = "/events/2"

    def request(self):
        self.response = requests.request(
            method="DELETE", url=self.environment["host"] + self.path, headers=self.environment["headers"])
        return self
