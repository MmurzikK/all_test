from tests import test_base
import requests


class TestConfirmCode(test_base.TestBase):
    path = "/register/code/check/{confirm_code}"

    def request(self):
        self.response = requests.request(method="GET", url=self.environment["host"] + self.path.format(
            confirm_code=self.environment["custom_variables"]["confirm_code"]), headers=self.environment["headers"])
        return self
