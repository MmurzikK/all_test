from tests import test_base
import requests


class TestFeedbacks(test_base.TestBase):
    path = "/feedbacks/error"

    def request(self):
        self.response = requests.request(
            method="POST", url=self.environment["host"] + self.path, headers=self.environment["headers"], data={
                "UF_SOURCE": "24617",
                "UF_USER_COMMENTS": "DNS Rules"
            })
        return self
