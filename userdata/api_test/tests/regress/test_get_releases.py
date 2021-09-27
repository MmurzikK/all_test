from tests import test_base
import requests


class TestGetReleases(test_base.TestBase):
    path = "/releases/5"
