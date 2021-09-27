from tests import test_base
import requests


class TestComplaint(test_base.TestBase):
    path = "/complaint"

    def request(self):
        self.response = requests.request(
            method="POST", url=self.environment["host"] + self.path, headers=self.environment["headers"], data={
                "product_id": "748",
                "user_name": self.environment["custom_variables"]["user_name"],
                "user_email": self.environment["custom_variables"]["user_email"],
                "text": "TESTO"
            })
        return self
