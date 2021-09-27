from tests import test_base
import requests


class TestQuestionDislikeQuestionId(test_base.TestBase):
    path = "/question/dislike/1654?show_entity=возврат_объекта"

    def request(self):
        self.response = requests.request(
            method="PUT", url=self.environment["host"] + self.path, headers=self.environment["headers"])
        return self
