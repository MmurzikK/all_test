from tests import test_base
import requests


class TestRecoverChange(test_base.TestBase):
    path = "/user/recover/change/password"

    def request(self):
        self.response = requests.request(
            method="POST", url=self.environment["host"] + self.path, headers=self.environment["headers"], data={
                "password": 11111111,
                "confirm_code": self.environment["custom_variables"]["confirm_code"]

            })
        return self
