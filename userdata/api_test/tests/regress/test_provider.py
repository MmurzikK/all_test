from tests import test_base
import requests


class TestProvider(test_base.TestBase):
    path = "/about/provider"

    def request(self):
        self.response = requests.request(
            method="POST", url=self.environment["host"] + self.path, headers=self.environment["headers"], data={
                "user_name": self.environment["custom_variables"]["user_name"],
                "user_phone": self.environment["custom_variables"]["number"],
                "user_email": self.environment["custom_variables"]["user_email"],
                "products_category": self.environment["custom_variables"]["user_name"],
                "message": self.environment["custom_variables"]["user_name"],
                "type": self.environment["custom_variables"]["user_name"]
            })
        return self
