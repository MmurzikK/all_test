from tests import test_base
import requests


class TestPcbuildComponents(test_base.TestBase):
    path = "/pcbuild/77315,530599,530811,530815,539384"

    def request(self):
        self.response = requests.request(
            method="PUT", url=self.environment["host"] + self.path, headers=self.environment["headers"], data={
            })
        return self
