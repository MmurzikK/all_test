from tests import test_base
import requests


class TestFavoriteProduct(test_base.TestBase):
    path = "/favorite/{favorite_id}?show_entity=598682"

    def request(self):
        self.response = requests.request(
            method="PUT", url=self.environment["host"] + self.path.format(
                favorite_id=self.environment["custom_variables"]["favorite_id"]), headers=self.environment["headers"])
        return self
