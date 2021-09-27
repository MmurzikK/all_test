from tests import test_base
import requests


class TestUserExist(test_base.TestBase):
    path = "/user/exist/{number}"

    def request(self):
        self.response = requests.request(method="GET", url=self.environment["host"] + self.path.format(
            number=self.environment["custom_variables"]["number"]), headers=self.environment["headers"])
        return self
