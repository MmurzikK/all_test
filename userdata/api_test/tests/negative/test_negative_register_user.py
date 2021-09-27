from tests import test_base
import requests
import pytest


class TestNegativeRegisterUser(test_base.TestBase):
    path = "/register"

    def request(self, x, y):
        self.response = requests.request(
            method="POST", url=self.environment["host"] + self.path, headers=self.environment["headers"], data={
                "name": x,  # self.faker.first_name(),
                "last_name": self.faker.user_name(),
                "second_name": self.faker.last_name(),
                "confirm_code": "111111",
                "password": y,  # elf.faker.password(length=4),
                "email": self.faker.company_email()
            })
        return self

    def test(self):
        assert self.response.status_code != 200
        return self
