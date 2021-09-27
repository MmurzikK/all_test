from tests import test_base
import requests


class TestAuthUser(test_base.TestBase):
    path = "/oauth/token"

    def request(self):
        self.response = requests.request(
            method="POST", url=self.environment["host"] + self.path, headers=self.environment["headers"], data={
                "grant_type": "password",
                "client_id": self.environment["client_id"],
                "client_secret": self.environment["client_secret"],
                "username": self.environment["custom_variables"]["number"],
                'password': self.environment["custom_variables"]["password"]
            })
        return self
