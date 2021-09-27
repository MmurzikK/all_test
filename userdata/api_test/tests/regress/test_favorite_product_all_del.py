from tests import test_base
import requests


class TestFavoriteProductAllDel(test_base.TestBase):
    path = "/favorite/all"

    def request(self):
        self.response = requests.request(
            method="DELETE", url=self.environment["host"] + self.path, headers=self.environment["headers"])
        return self
