from tests import test_base
import requests


class TestReviewLike(test_base.TestBase):
    path = "/review/like/150?show_entity=возврат_объекта"

    def request(self):
        self.response = requests.request(
            method="PUT", url=self.environment["host"] + self.path, headers=self.environment["headers"])
        return self
