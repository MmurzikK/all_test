from tests import test_base
import requests


class TestFavoriteProductDel(test_base.TestBase):
    path = "/favorite/{favorite_id}?show_entity=возврат_добавленного_товара"

    def request(self):
        self.response = requests.request(
            method="DELETE", url=self.environment["host"] + self.path.format(
                favorite_id=self.environment["custom_variables"]["favorite_id"]), headers=self.environment["headers"])
        return self
