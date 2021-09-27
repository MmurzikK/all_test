from tests import test_base
import requests


class TestFoundCheaper(test_base.TestBase):
    path = "/feedbacks/found_cheaper"

    def request(self):
        self.response = requests.request(
            method="POST", url=self.environment["host"] + self.path, headers=self.environment["headers"], data={
                "UF_PHONE_NUMBER": self.environment["custom_variables"]["number"],
                "UF_SOURCE": "24617",
                "UF_ID_PROD_OR_SALE": "24617",
                "UF_USER_NAME": self.environment["custom_variables"]["user_name"]
            })
        return self
