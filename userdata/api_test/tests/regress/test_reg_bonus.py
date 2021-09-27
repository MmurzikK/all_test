from tests import test_base
import requests


class TestRegBonus(test_base.TestBase):
    path = "/bonus?name={user_name}&last_name={user_name}&second_name={user_name}"

    def request(self):
        self.response = requests.request(
            method="POST", url=self.environment["host"] + self.path.format(
                user_name=self.environment["custom_variables"]["user_name"]), headers=self.environment["headers"])
        return self
