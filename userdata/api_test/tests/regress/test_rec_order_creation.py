from tests import test_base
import requests


class TestRecOrderCreation(test_base.TestBase):
    path = "/order"

    def request(self):
        self.response = requests.request(
            method="POST", url=self.environment["host"] + self.path, headers=self.environment["headers"], data={
                "ORDER_PROP_1": self.environment["custom_variables"]["user_name"],
                "ORDER_PROP_2": self.environment["custom_variables"]["user_email"],
                "ORDER_PROP_7": self.environment["custom_variables"]["user_name"],
                "ORDER_PROP_3": self.environment["custom_variables"]["user_name"]
            })
        return self
