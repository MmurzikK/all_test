from tests import test_base
import requests


class TestRecommendDeveloper(test_base.TestBase):
    path = "/about/recommend/developer"

    def request(self):
        self.response = requests.request(
            method="POST", url=self.environment["host"] + self.path, headers=self.environment["headers"], data={
                "user_name": elf.environment["custom_variables"]["name"],
                "user_phone": self.environment["custom_variables"]["number"],
                "user_email": self.environment["custom_variables"]["user_email"],
                "candidate_profile": "www.05.ru",
                "candidate_name": elf.environment["custom_variables"]["name"],
                "candidate_phone": "79996666777"
            })
        return self
