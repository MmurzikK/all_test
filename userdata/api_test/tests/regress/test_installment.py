from tests import test_base
import requests


class TestInstallment(test_base.TestBase):
    path = "/installment?product_price=40800&period=6&guarantors=4"
