from tests import test_base
import requests


class TestRegisterUser(test_base.TestBase):
    path = "/register"

    def request(self):
        self.response = requests.request(
            method="POST", url=self.environment["host"] + self.path, headers=self.environment["headers"], data={
                "name": self.environment["custom_variables"]["user_name"],
                "last_name": self.environment["custom_variables"]["user_name"],
                "second_name": self.environment["custom_variables"]["user_name"],
                "confirm_code": self.environment["custom_variables"]["confirm_code"],
                "password": self.environment["custom_variables"]["password"],
                "email": self.environment["custom_variables"]["user_email"]
            })
        return self
