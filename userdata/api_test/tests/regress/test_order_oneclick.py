from tests import test_base
import requests


class TestOrderOneclick(test_base.TestBase):
    path = "/order/oneclick"

    def request(self):
        self.response = requests.request(
            method="POST", url=self.environment["host"] + self.path, headers=self.environment["headers"], data={
                "product_id": self.environment["custom_variables"]["basket_double"],
                "phone_number": self.environment["custom_variables"]["number"]
            })
        return self
