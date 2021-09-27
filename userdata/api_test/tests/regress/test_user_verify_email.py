from tests import test_base
import requests


class TestUserVerifyEmail(test_base.TestBase):
    path = "/user/verify/email/{user_email}"

    def request(self):
        self.response = requests.request(method="GET", url=self.environment["host"] + self.path.format(
            user_email=self.environment["custom_variables"]["user_email"]), headers=self.environment["headers"])
        return self
