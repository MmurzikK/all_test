from tests import test_base
import requests


class TestOrderCoupon(test_base.TestBase):
    path = "/order/coupon/{order_coupon}"

    def request(self):
        self.response = requests.request(
            method="PUT", url=self.environment["host"] + self.path.format(
                order_coupon=self.environment["custom_variables"]["order_coupon"]), headers=self.environment["headers"], data={
            })
        return self
