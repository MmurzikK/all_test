from tests import test_base
import requests


class TestSearch(test_base.TestBase):
    path = "/search?q=Fly FS408"
