from tests import test_base
import requests


class TestQuantityBasket(test_base.TestBase):
    path = "/basket"

    def request(self):
        self.response = requests.request(
            method="POST", url=self.environment["host"] + self.path, headers=self.environment["headers"], data={
                "product_id": self.environment["custom_variables"]["basket_productid"],
                "quantity": "2"
            })
        return self
