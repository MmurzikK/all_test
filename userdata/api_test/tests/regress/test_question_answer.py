from tests import test_base
import requests


class TestQuestionAnswer(test_base.TestBase):
    path = "/question/answer"

    def request(self):
        self.response = requests.request(
            method="POST", url=self.environment["host"] + self.path, headers=self.environment["headers"], data={
                "product_id": "748",
                "entity_id": self.environment["custom_variables"]["name"],
                "user_name": self.environment["custom_variables"]["name"],
                "user_email": self.environment["custom_variables"]["user_email"],
                "text": self.environment["custom_variables"]["name"]
            })
        return self
