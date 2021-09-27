from tests import test_base
import requests


class TestQuestionProductId(test_base.TestBase):
    path = "/question/570829?page=номер_страницы&size=количество_записей_на_странице&answers_size=количество_ответов_у_каждого_вопроса"
