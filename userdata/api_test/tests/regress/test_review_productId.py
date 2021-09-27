from tests import test_base
import requests


class TestReviewProductId(test_base.TestBase):
    path = "/review/589375?page=1&size=2&comments_size=2"
