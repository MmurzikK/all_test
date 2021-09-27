from tests import test_base
import requests


class TestEventsViewed(test_base.TestBase):
    path = "/events/viewed/2/1"

    def request(self):
        self.response = requests.request(
            method="PATCH", url=self.environment["host"] + self.path, headers=self.environment["headers"])
        return self
