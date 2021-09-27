import allure
import pytest
from faker import Faker
from pathlib import Path
from tests.negative import test_negative_auth_user
from tests.negative import test_negative_register_user
from tests.negative import test_negative_register_code
from tests.negative import test_negative_compare_all_products
from tests.negative import test_negative_favorite_prod
from tests.negative import test_negative_favorite_all_del
from tests.negative import test_negative_norm_reg_user
from tests.negative import test_negative_norm_auth_user
from tests.negative import test_negative_delete_user
from environment import yaml_environment


class Test():
    environment_adapter = yaml_environment.YamlEnvironment(
        "/environment/test_negative_environment.yml")
    faker = Faker()

    @allure.title("Отправка кода подтверждения")
    @allure.description("Отправка кода подтверждения")
    def test_negative_register_code(self):
        test_negative_register_code.TestNegativeRegisterCode(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Регистрация пользователя")
    @allure.description("Регистрация пользователя")
    @allure.severity("Blocker")
    @pytest.mark.parametrize("x", [0000, 3, "++=="])
    @pytest.mark.parametrize("y", ["11 11", "nhjrr", 000])
    def test_negative_register_user(self, x, y):
        test_negative_register_user.TestNegativeRegisterUser(
            self.environment_adapter, self.faker).request(x, y).rewrite_token().rewrite_environment().attach().test()

    @allure.title("Аутентификация пользователя")
    @allure.description("Аутентификация пользователя")
    @allure.severity("Blocker")
    def test_negative_auth_user(self):
        test_negative_auth_user.TestNegativeAuthUser(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Получить структуру")
    @allure.description("Получить структуру")
    @allure.severity("Blocker")
    def test_negative_compare_all_products(self):
        test_negative_compare_all_products.TestNegativeCompareAllProducts(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Зарегистрировать Пользователя Негатив")
    @allure.description("Зарегистрировать Пользователя Негатив")
    @allure.severity("Blocker")
    def test_negative_norm_reg_user(self):
        test_negative_norm_reg_user.TestNegativeNormRegisterUser(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Авторизовать Пользователя Негатив")
    @allure.description("Авторизовать Пользователя Негатив")
    @allure.severity("Blocker")
    def test_negative_norm_auth_user(self):
        test_negative_norm_auth_user.TestNegativeNormAuthUser(
            self.environment_adapter, self.faker).request().attach().test()

    # @allure.title("Добавить в Избранное")
    # @allure.description("Добавить в Избранное")
    # @allure.severity("Blocker")
    # def test_negative_favorite_prod(self):
    #     test_negative_favorite_prod.TestNegativeFavoriteProd(
    #         self.environment_adapter, self.faker).request().attach().test()

    # @allure.title("Удалить всё из Избранного")
    # @allure.description("Удалить всё из Избранного")
    # @allure.severity("Blocker")
    # def test_negative_favorite_all_del(self):
    #     test_negative_favorite_all_del.TestNegativeFavoriteProductAllDel(
    #         self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Удалить Пользователя Негатив")
    @allure.description("Удалить Пользователя Негатив")
    @allure.severity("Blocker")
    def test_negative_delete_user(self):
        test_negative_delete_user.TestNegativeDeleteUser(
            self.environment_adapter, self.faker).request().attach().test()
