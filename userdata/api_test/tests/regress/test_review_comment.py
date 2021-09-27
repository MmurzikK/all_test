from tests import test_base
import requests


class TestReviewComment(test_base.TestBase):
    path = "/review/comment"

    def request(self):
        self.response = requests.request(
            method="POST", url=self.environment["host"] + self.path, headers=self.environment["headers"], data={
                "product_id": "748",
                "entity_id": "111",
                "user_name": self.environment["custom_variables"]["user_name"],
                "user_email": self.environment["custom_variables"]["user_email"],
                "text": self.environment["custom_variables"]["user_name"]
            })
        return self
