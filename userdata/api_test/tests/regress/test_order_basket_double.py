from tests import test_base
import requests


class TestOrderBasketDouble(test_base.TestBase):
    path = "/basket"

    def request(self):
        self.response = requests.request(
            method="POST", url=self.environment["host"] + self.path, headers=self.environment["headers"], data={
                "product_id": self.environment["custom_variables"]["basket_double"],
                "quantity": "2"
            })
        return self
