from tests import test_base
import requests


class TestNegativeAuthUser(test_base.TestBase):
    path = "/oauth/token"

    def request(self):
        self.response = requests.request(
            method="POST", url=self.environment["host"] + self.path, headers=self.environment["headers"], data={
                "grant_type": "password",
                "client_id": self.environment["client_id"],
                "client_secret": self.environment["client_secret"],
                "username": self.faker.user_name(),
                'password': self.faker.password()
            })
        return self

    def test(self):
        assert self.response.status_code != 200
        return self
