from tests import test_base
import requests


class TestDelCompareSection(test_base.TestBase):
    path = "/compare/section/{compare_sections}/{compare_sections}"

    def request(self):
        self.response = requests.request(
            method="DELETE", url=self.environment["host"] + self.path.format(
                compare_sections=self.environment["custom_variables"]["compare_sections"]), headers=self.environment["headers"])
        return self
