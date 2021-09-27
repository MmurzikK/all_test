from tests import test_base
import requests


class TestReviewCommentDislike(test_base.TestBase):
    path = "/review/comment/dislike/608814dec086e100188c7a3a?show_entity=возврат_объекта&parent_entity_id=150"

    def request(self):
        self.response = requests.request(
            method="PUT", url=self.environment["host"] + self.path, headers=self.environment["headers"])
        return self
