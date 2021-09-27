from tests import test_base
import requests


class TestBrandPopulars(test_base.TestBase):
    path = "/brand/populars?size=7"
