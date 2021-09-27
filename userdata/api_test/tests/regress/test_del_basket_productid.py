from tests import test_base
import requests


class TestDelBasketProductId(test_base.TestBase):
    path = "/basket/{basket_productid}?total=1"

    def request(self):
        self.response = requests.request(
            method="DELETE", url=self.environment["host"] + self.path.format(
                basket_productid=self.environment["custom_variables"]["basket_productid"]), headers=self.environment["headers"], data={
            })
        return self
