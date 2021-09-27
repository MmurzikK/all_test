from tests import test_base
from tests.regress import test_order_create
import requests


class TestOrderCancel(test_base.TestBase):
    path = "/order/{orderId}/cancel?reason=тест&show_entity=тест&comment=Тест"

    def request(self):
        self.response = requests.request(method="DELETE", url=self.environment["host"] + self.path.format(
            orderId=self.variables[test_order_create.TestOrderCreate.__name__]["ORDER_ID"]), headers=self.environment["headers"])
        return self
