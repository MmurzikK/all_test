from tests import test_base
import requests


class TestWholesaler(test_base.TestBase):
    path = "/about/wholesaler"

    def request(self):
        self.response = requests.request(
            method="POST", url=self.environment["host"] + self.path, headers=self.environment["headers"], data={
                "user_name": self.environment["custom_variables"]["user_name"],
                "user_phone": self.environment["custom_variables"]["number"],
                "city": self.environment["custom_variables"]["user_name"],
                "products": self.environment["custom_variables"]["user_name"],
                "products_category": self.environment["custom_variables"]["user_name"]
            })
        return self
