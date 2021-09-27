from tests import test_base
import requests


class TestChangePersonalDataUser(test_base.TestBase):
    path = "/user"

    def request(self):
        self.response = requests.request(
            method="POST", url=self.environment["host"] + self.path, headers=self.environment["headers"], data={
                "last_name": self.environment["custom_variables"]["user_name"],
                "name": self.environment["custom_variables"]["user_name"],
                "second_name": self.environment["custom_variables"]["user_name"],
                "confirm_code": self.environment["custom_variables"]["confirm_code"],
                "password": "11111111"
            })
        return self
