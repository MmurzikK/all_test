from tests import test_base
import requests


class TestNegativeNormAuthUser(test_base.TestBase):
    path = "/oauth/token"

    def request(self):
        self.response = requests.request(
            method="POST", url=self.environment["host"] + self.path, headers=self.environment["headers"], data={
                "grant_type": "password",
                "client_id": "main",
                "client_secret": "ac178876-b829-11e9-b8c8-ac1f6b94fd9c",
                "username": "79996666667",
                'password': "111111"
            })
        return self
