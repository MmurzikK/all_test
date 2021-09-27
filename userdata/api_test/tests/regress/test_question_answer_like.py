from tests import test_base
import requests


class TestQuestionAnswerLike(test_base.TestBase):
    path = "/question/answer/like/5ffd5769249348000ee0c643?show_entity=возврат_объекта&parent_entity_id=1654"

    def request(self):
        self.response = requests.request(
            method="PUT", url=self.environment["host"] + self.path, headers=self.environment["headers"])
        return self
