from tests import test_base
import requests


class TestDelOrderCoupon(test_base.TestBase):
    path = "/order/coupon/{coupon}"

    def request(self):
        self.response = requests.request(
            method="DELETE", url=self.environment["host"] + self.path.format(
                coupon=self.environment["custom_variables"]["coupon"]), headers=self.environment["headers"], data={
            })
        return self
