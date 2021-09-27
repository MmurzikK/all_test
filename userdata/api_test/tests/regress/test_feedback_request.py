from tests import test_base
import requests


class TestFeedbacksRequest(test_base.TestBase):
    path = "/feedbacks"

    def request(self):
        self.response = requests.request(
            method="POST", url=self.environment["host"] + self.path, headers=self.environment["headers"], data={
                "UF_PHONE_NUMBER": self.environment["custom_variables"]["number"],
                "UF_ID_PROD_OR_SALE": "24617",
                "UF_USER_NAME": self.environment["custom_variables"]["user_name"],
                "UF_USER_COMMENTS": self.environment["custom_variables"]["user_name"],
                "UF_SOURCE": self.environment["custom_variables"]["user_name"],
                "UF_EMAIL": self.environment["custom_variables"]["user_email"],
                "UF_USER_NAME": self.environment["custom_variables"]["user_name"],
                "APPEAL_TYPE": "1"
            })
        return self
