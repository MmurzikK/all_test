from tests import test_base
import requests


class TestDeleteUser(test_base.TestBase):
    path = "/service/delete/users/{number}?access_token={delete_user}"

    def request(self):
        self.response = requests.request(method="GET", url=self.environment["host"] + self.path.format(
            number=self.environment["custom_variables"]["number"], delete_user=self.environment["delete_user"]))
        return self
