from tests import test_base
import requests


class TestFavoriteProductDouble(test_base.TestBase):
    path = "/favorite/{favorite_id_double}?show_entity=598682"

    def request(self):
        self.response = requests.request(
            method="PUT", url=self.environment["host"] + self.path.format(
                favorite_id_double=self.environment["custom_variables"]["favorite_id_double"]), headers=self.environment["headers"])
        return self
