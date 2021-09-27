import allure
from faker import Faker
from pathlib import Path
import faker
from tests.regress import test_register_code
from tests.regress import test_register_user
from tests.regress import test_home_screen
from tests.regress import test_catalog_sections
from tests.regress import test_confirm_code
from tests.regress import test_register_fields
from tests.regress import test_auth_user
from tests.regress import test_recover_send
from tests.regress import test_recover_change
from tests.regress import test_user_verify_email
from tests.regress import test_personal_area
from tests.regress import test_change_personal_data_user
from tests.regress import test_favorite_product
from tests.regress import test_favorite_product_double
from tests.regress import test_favorite_product_del
from tests.regress import test_favorite_product_all_del
from tests.regress import test_catalog_products_viewed
from tests.regress import test_review_product
from tests.regress import test_question
from tests.regress import test_favorite_list
from tests.regress import test_product_card
from tests.regress import test_products_viewed
from tests.regress import test_delete_user
from tests.regress import test_catalog_categories
from tests.regress import test_sliders
from tests.regress import test_vue_catalog
from tests.regress import test_catalog
from tests.regress import test_catalog_panel
from tests.regress import test_catalog_banners
from tests.regress import test_catalog_paths
from tests.regress import test_user_orders
from tests.regress import test_user_exist
from tests.regress import test_oauth_token
from tests.regress import test_get_basket
from tests.regress import test_quantity_basket
from tests.regress import test_order_payment
from tests.regress import test_order_delivery
from tests.regress import test_order_gifts
from tests.regress import test_order_coupon
from tests.regress import test_del_order_coupon
from tests.regress import test_del_basket_productid
from tests.regress import test_del_basket_all
from tests.regress import test_locations_current
from tests.regress import test_set_location
from tests.regress import test_location
from tests.regress import test_complaint
from tests.regress import test_search_phrases
from tests.regress import test_search_hints
from tests.regress import test_installment
from tests.regress import test_feedbacks
from tests.regress import test_feedback_request
from tests.regress import test_found_cheaper
from tests.regress import test_feedbacks_paragraphs
from tests.regress import test_reg_bonus
from tests.regress import test_bonus_info
from tests.regress import test_bonus_fields
from tests.regress import test_bonus_code_send
from tests.regress import test_brand
from tests.regress import test_compare
from tests.regress import test_del_compare
from tests.regress import test_del_compare_section
from tests.regress import test_compare_products
from tests.regress import test_compare_struct
from tests.regress import test_compare_sections
from tests.regress import test_compare_all_products
from tests.regress import test_subscribe_device
from tests.regress import test_unsubscribe
from tests.regress import test_push_events
from tests.regress import test_del_push
from tests.regress import test_events_viewed
from tests.regress import test_order_basket
from tests.regress import test_order_create
from tests.regress import test_order_basket_double
from tests.regress import test_rec_order_creation
from tests.regress import test_order_oneclick
from tests.regress import test_add_review
from tests.regress import test_add_question
from tests.regress import test_favorite
from tests.regress import test_search
from tests.regress import test_vacancy
from tests.regress import test_wholesaler
from tests.regress import test_provider
from tests.regress import test_support_stores
from tests.regress import test_support_information
from tests.regress import test_brand_populars
from tests.regress import test_brand_groupped
from tests.regress import test_bonus_physical
from tests.regress import test_review_comment
from tests.regress import test_review_comment_like
from tests.regress import test_review_comment_dislike
from tests.regress import test_review_comment_fields
from tests.regress import test_reviewId_comments
from tests.regress import test_review_productId
from tests.regress import test_review_fields
from tests.regress import test_review_like
from tests.regress import test_review_dislike
from tests.regress import test_question_answer
from tests.regress import test_question_answer_like
from tests.regress import test_question_answer_dislike
from tests.regress import test_question_questionId
from tests.regress import test_question_answer_fields
from tests.regress import test_question_productId
from tests.regress import test_question_fields
from tests.regress import test_question_like_questionId
from tests.regress import test_question_dislike_questionId
from tests.regress import test_recommend_developer
from tests.regress import test_about_recommend_developer
from tests.regress import test_vacancyid
from tests.regress import test_order_cancel
from tests.regress import test_releases_list
from tests.regress import test_get_releases
from tests.regress import test_pcbuild
from tests.regress import test_pcbuild_scheme
from tests.regress import test_pcbuild_components
from environment import yaml_environment


class Test():
    environment_adapter = yaml_environment.YamlEnvironment(
        "/environment/test_environment.yml")
    faker = Faker()

    @allure.title("Отправка кода подтверждения")
    @allure.description("Отправка кода подтверждения")
    def test_register_code(self):
        test_register_code.TestRegisterCode(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Проверка кода подтверждения")
    @allure.description("Проверка кода подтверждения")
    def test_confirm_code(self):
        test_confirm_code.TestConfirmCode(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Получение полей для регистрации")
    @allure.description("Получение полей для регистрации")
    def test_register_fields(self):
        test_register_fields.TestRegisterFields(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Регистрация пользователя")
    @allure.description("Регистрация пользователя")
    @allure.severity("Blocker")
    def test_register_user(self):
        test_register_user.TestRegisterUser(
            self.environment_adapter, self.faker).request().rewrite_token().rewrite_environment().attach().test()

    @allure.title("Авторизация пользователя")
    @allure.description("Авторизация пользователя")
    @allure.severity("Blocker")
    def test_auth_user(self):
        test_auth_user.TestAuthUser(
            self.environment_adapter, self.faker).request().rewrite_token().rewrite_environment().attach().test()

    @allure.title("Отправка кода подтверждения")
    @allure.description("Отправка кода подтверждения")
    def test_recover_send(self):
        test_recover_send.TestRecoverSend(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Изменить пароль во время восстановления")
    @allure.description("Изменить пароль во время восстановления")
    def test_recover_change(self):
        test_recover_change.TestRecoverChange(
            self.environment_adapter, self.faker).request().rewrite_token().rewrite_environment().attach().test()

    @allure.title("Подтвердить электронную почту")
    @allure.description("Подтвердить электронную почту")
    def test_user_verify_email(self):
        test_user_verify_email.TestUserVerifyEmail(
            self.environment_adapter, self.faker).request().rewrite_token().rewrite_environment().attach().test()

    @allure.title("Изменение личных данных пользователя")
    @allure.description("Изменение личных данных пользователя")
    def test_change_personal_data_user(self):
        test_change_personal_data_user.TestChangePersonalDataUser(
            self.environment_adapter, self.faker).request().rewrite_token().rewrite_environment().attach().test()

    @allure.title("Личный кабинет")
    @allure.description("Личный кабинет")
    def test_personal_area(self):
        test_personal_area.TestPersonalArea(
            self.environment_adapter, self.faker).request().rewrite_token().rewrite_environment().attach().test()

    @allure.title('Добавление в избранное')
    @allure.description('Добавление в избранное')
    def test_favorite_product(self):
        test_favorite_product.TestFavoriteProduct(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Добавить в избранное дубль")
    @allure.description("Добавить в избранное дубль")
    def test_favorite_product_double(self):
        test_favorite_product_double.TestFavoriteProductDouble(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Удаление из избранного")
    @allure.description("Удаление из избранного")
    def test_favorite_product_del(self):
        test_favorite_product_del.TestFavoriteProductDel(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Удалить все из избранного")
    @allure.description("Удалить все из избранного")
    def test_favorite_product_all_del(self):
        test_favorite_product_all_del.TestFavoriteProductAllDel(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Список избранных")
    @allure.description("Список избранных")
    def test_favorite_list(self):
        test_favorite_list.TestFavoriteList(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Получение главного экрана")
    @allure.description("Получение главного экрана")
    def test_home_screen(self):
        test_home_screen.TestHomeScreen(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Получение просмотренных товаров")
    @allure.description("Получение просмотренных товаров")
    def test_catalog_products_viewed(self):
        test_catalog_products_viewed.TestCatalogProductsViewed(
            self.environment_adapter, self.faker).request().attach().test()

    # @allure.title("Добавить отзыв")
    # @allure.description("Добавить отзыв")
    # def test_review_product(self):
    #     test_review_product.TestReviewProduct(
    #         self.environment_adapter, self.faker).request().attach().test()

    # @allure.title("Добавить вопрос")
    # @allure.description("Добавить вопрос")
    # def test_question(self):
    #     test_question.TestQuetion(
    #         self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Карточка товара")
    @allure.description("Карточка товара")
    def test_product_card(self):
        test_product_card.TestProductCard(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Просмотренные товары")
    @allure.description("Просмотренные товары")
    def test_products_viewed(self):
        test_products_viewed.TestProductViewed(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Список категорий")
    @allure.description("Список категорий")
    def test_catalog_categories(self):
        test_catalog_categories.TestCatalogCategories(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Слайдеры")
    @allure.description("Слайдеры")
    def test_sliders(self):
        test_sliders.TestSliders(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Vue каталог")
    @allure.description("Vue каталог")
    def test_vue_catalog(self):
        test_vue_catalog.TestVueCatalog(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Каталог")
    @allure.description("Каталог")
    def test_catalog(self):
        test_catalog.TestCatalog(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Панель каталога")
    @allure.description("Панель каталога")
    def test_catalog_panel(self):
        test_catalog_panel.TestCatalogPanel(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Список баннеров")
    @allure.description("Список баннеров")
    def test_catalog_banners(self):
        test_catalog_banners.TestCatalogBanners(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Получить все ссылки")
    @allure.description("Получить все ссылки")
    def test_catalog_paths(self):
        test_catalog_paths.TestCatalogPaths(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Проверка существования Пользователя")
    @allure.description("Проверка существования Пользователя")
    def test_user_exist(self):
        test_user_exist.TestUserExist(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Получить информацию о токене")
    @allure.description("Получить информацию о токене")
    def test_oauth_token(self):
        test_oauth_token.TestOauthToken(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Получить корзину")
    @allure.description("Получить корзину")
    def test_get_basket(self):
        test_get_basket.TestGetBasket(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Установить количество товара в коризне")
    @allure.description("Установить количество товара в коризне")
    def test_quantity_basket(self):
        test_quantity_basket.TestQuantityBasket(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Получить способы оплаты")
    @allure.description("Получить способы оплаты")
    def test_order_payment(self):
        test_order_payment.TestOrderPayment(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Получить данные доставки")
    @allure.description("Получить данные доставки")
    @allure.severity("Blocker")
    def test_order_delivery(self):
        test_order_delivery.TestOrderDelivery(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Получить подарки")
    @allure.description("Получить подарки")
    def test_order_gifts(self):
        test_order_gifts.TestOrderGifts(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Добавить промокод")
    @allure.description("Добавить промокод")
    def test_order_coupon(self):
        test_order_coupon.TestOrderCoupon(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Удалить промокод")
    @allure.description("Удалить промокод")
    def test_del_order_coupon(self):
        test_del_order_coupon.TestDelOrderCoupon(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Удалить товар из корзины")
    @allure.description("Удалить товар из корзины")
    def test_del_basket_productid(self):
        test_del_basket_productid.TestDelBasketProductId(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Удалить все товары из корзины")
    @allure.description("Удалить все товары из корзины")
    def test_del_basket_all(self):
        test_del_basket_all.TestDelBasketAll(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Получить текущее местоположение")
    @allure.description("Получить текущее местоположение")
    def test_locations_current(self):
        test_locations_current.TestLocationsCurrent(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Установить местоположение")
    @allure.description("Установить местоположение")
    def test_set_location(self):
        test_set_location.TestSetLocation(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Получить местоположения")
    @allure.description("Получить местоположения")
    def test_location(self):
        test_location.TestLocations(
            self.environment_adapter, self.faker).request().attach().test()

    # @allure.title("Отправить жалобу")
    # @allure.description("Отправить жалобу")
    # def test_complaint(self):
        # test_complaint.TestComplaint(
        # self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Популярные поисковые фразы")
    @allure.description("Популярные поисковые фразы")
    def test_search_phrases(self):
        test_search_phrases.TestSearchPhrases(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Поисковик подсказки")
    @allure.description("Поисковик подсказки")
    def test_search_hints(self):
        test_search_hints.TestSearchHints(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Калькулятор рассрочки")
    @allure.description("Калькулятор рассрочки")
    def test_installment(self):
        test_installment.TestInstallment(
            self.environment_adapter, self.faker).request().attach().test()

    # @allure.title("Нашли ошибку?")
    # @allure.description("Нашли ошибку?")
    # def test_feedbacks(self):
        # test_feedbacks.TestFeedbacks(
        # self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Запрос обратной связи")
    @allure.description("Запрос обратной связи")
    def test_feedback_request(self):
        test_feedback_request.TestFeedbacksRequest(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Нашли дешевле?")
    @allure.description("Нашли дешевле?")
    def test_found_cheaper(self):
        test_found_cheaper.TestFoundCheaper(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Получить пункты")
    @allure.description("Получить пункты")
    def test_feedbacks_paragraphs(self):
        test_feedbacks_paragraphs.TestFeedbackParagraphs(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Зарегистрировать бонусную карту")
    @allure.description("Зарегистрировать бонусную карту")
    def test_reg_bonus(self):
        test_reg_bonus.TestRegBonus(
            self.environment_adapter, self.faker).request().attach().test()

    # @allure.title("Получить информацию о бонусной карте")
    # @allure.description("Получить информацию о бонусной карте")
    # def test_bonus_info(self):
    #     test_bonus_info.TestBonusInfo(
    #         self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Получить поля о бонусной карте")
    @allure.description("Получить поля о бонусной карте")
    def test_bonus_fields(self):
        test_bonus_fields.TestBonusFields(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Отправить код Бонустная карта")
    @allure.description("Отправить код Бонусная карта")
    @allure.severity("Minor")
    def test_bonus_code_send(self):
        test_bonus_code_send.TestBonusCodeSend(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Получить карточку бренда")
    @allure.description("Получить карточку бренда")
    @allure.severity("Minor")
    def test_brand(self):
        test_brand.TestBrand(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Добавить товар - Сравнение")
    @allure.description("Добавить товар - Сравнение")
    @allure.severity("Minor")
    def test_compare(self):
        test_compare.TestCompare(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Удалить товар - Сравнение")
    @allure.description("Удалить товар - Сравнение")
    @allure.severity("Minor")
    def test_del_compare(self):
        test_del_compare.TestDelCompare(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Удалить раздел - Сравнение")
    @allure.description("Удалить раздел - Сравнение")
    @allure.severity("Minor")
    def test_del_compare_section(self):
        test_del_compare_section.TestDelCompareSection(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Удалить товары - Сравнение")
    @allure.description("Удалить товары - Сравнение")
    @allure.severity("Minor")
    def test_compare_products(self):
        test_compare_products.TestDelCompareProducts(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Получить структуру - Сравнение")
    @allure.description("Получить структуру - Сравнение")
    @allure.severity("Trivial")
    def test_compare_struct(self):
        test_compare_struct.TestCompareStruct(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Получить список разделов - Сравнение")
    @allure.description("Получить список разделов - Сравнение")
    @allure.severity("Minor")
    def test_compare_sections(self):
        test_compare_sections.TestCompareSections(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Получить все товары - Сравнение")
    @allure.description("Получить все товары - Сравнение")
    @allure.severity("Minor")
    def test_compare_all_products(self):
        test_compare_all_products.TestCompareAllProducts(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Подписаться")
    @allure.description("Подписаться")
    @allure.severity("Critical")
    def test_subscribe_device(self):
        test_subscribe_device.TestSubscribeDevice(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Отменить подписку")
    @allure.description("Отменить подписку")
    @allure.severity("Minor")
    def test_unsubscribe(self):
        test_unsubscribe.TestUnsubscribe(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Получить список")
    @allure.description("Получить список")
    @allure.severity("Minor")
    def test_push_events(self):
        test_push_events.TestPushEvents(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Удалить PUSH")
    @allure.description("Удалить PUSH")
    @allure.severity("Minor")
    def test_del_push(self):
        test_del_push.TestDelPush(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Установить статус просмотра")
    @allure.description("Установить статус просмотра")
    @allure.severity("Minor")
    def test_events_viewed(self):
        test_events_viewed.TestEventsViewed(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Установить количество товара в коризне - Заказ")
    @allure.description("Установить количество товара в коризне - Заказ")
    @allure.severity("Minor")
    def test_order_basket(self):
        test_order_basket.TestOrderBasket(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Сделать заказ")
    @allure.description("Сделать заказ")
    @allure.severity("Blocker")
    def test_order_create(self):
        test_order_create.TestOrderCreate(
            self.environment_adapter, self.faker).request().attach().test().assert_set_variables().rewrite_environment()

    @allure.title("Установить количество товара в коризне - Заказ - Дубль")
    @allure.description("Установить количество товара в коризне - Заказ - Дубль")
    @allure.severity("Blocker")
    def test_order_basket_double(self):
        test_order_basket_double.TestOrderBasketDouble(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Получить данные для создания заказа")
    @allure.description("Получить данные для создания заказа")
    @allure.severity("Minor")
    def test_rec_order_creation(self):
        test_rec_order_creation.TestRecOrderCreation(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Купить в один клик")
    @allure.description("Купить в один клик")
    @allure.severity("Blocker")
    def test_order_oneclick(self):
        test_order_oneclick.TestOrderOneclick(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Получить заказы")
    @allure.description("Получить заказы")
    def test_user_orders(self):
        test_user_orders.TestUserOrders(
            self.environment_adapter, self.faker).request().attach().test()

    # @allure.title("Добавить отзыв")
    # @allure.description("Добавить отзыв")
    # @allure.severity("Minor")
    # def test_add_review(self):
    #     test_add_review.TestAddReview(
    #         self.environment_adapter, self.faker).request().attach().test()

    # @allure.title("Добавить вопрос")
    # @allure.description("Добавить вопрос")
    # @allure.severity("Minor")
    # def test_add_question(self):
    #     test_add_question.TestAddQuestion(
    #         self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Список избранных")
    @allure.description("Список избранных")
    @allure.severity("Minor")
    def test_favorite(self):
        test_favorite.TestFavorite(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Поиск")
    @allure.description("Поиск")
    @allure.severity("Critical")
    def test_search(self):
        test_search.TestSearch(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Получить список Вакансий")
    @allure.description("Получить список Вакансий")
    @allure.severity("Minor")
    def test_vacancy(self):
        test_vacancy.TestVacancy(
            self.environment_adapter, self.faker).request().attach().test()

    # @allure.title("Оптовики")
    # @allure.description("Оптовики")
    # @allure.severity("Minor")
    # def test_wholesaler(self):
        # test_wholesaler.TestWholesaler(
        # self.environment_adapter, self.faker).request().attach().test()

    # @allure.title("Поставщики")
    # @allure.description("Поставщики")
    # @allure.severity("Minor")
    # def test_provider(self):
        # test_provider.TestProvider(
        # self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Получить список магазинов")
    @allure.description("Получить список магазинов")
    @allure.severity("Minor")
    def test_support_stores(self):
        test_support_stores.TestSupportStores(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Получить общую информацию")
    @allure.description("Получить общую информацию")
    @allure.severity("Minor")
    def test_support_information(self):
        test_support_information.TestSupportInformation(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Получить популярные Бренды")
    @allure.description("Получить популярные Бренды")
    @allure.severity("Minor")
    def test_brand_populars(self):
        test_brand_populars.TestBrandPopulars(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Получить сгруппированные Бренды")
    @allure.description("Получить сгруппированные Бренды")
    @allure.severity("Minor")
    def test_brand_groupped(self):
        test_brand_groupped.TestBrandGroupped(
            self.environment_adapter, self.faker).request().attach().test()

    # @allure.title("Зарегистрировать физическую бонусную карту")
    # @allure.description("Зарегистрировать физическую бонусную карту")
    # @allure.severity("Minor")
    # def test_bonus_physical(self):
        # test_bonus_physical.TestBonusPhysical(
        # self.environment_adapter, self.faker).request().attach().test()

    # @allure.title("Добавить комментарий")
    # @allure.description("Добавить комментарий")
    # @allure.severity("Minor")
    # def test_review_comment(self):
        # test_review_comment.TestReviewComment(
        # self.environment_adapter, self.faker).request().attach().test()

    # @allure.title("Нравится комментарий")
    # @allure.description("Нравится комментарий")
    # @allure.severity("Minor")
    # def test_review_comment_like(self):
        # test_review_comment_like.TestReviewCommentLike(
        # self.environment_adapter, self.faker).request().attach().test()

    # @allure.title("Не нравится комментарий")
    # @allure.description("Не нравится комментарий")
    # @allure.severity("Minor")
    # def test_review_comment_dislike(self):
        # test_review_comment_dislike.TestReviewCommentDislike(
        # self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Получить поля комментарий")
    @allure.description("Получить поля комментарий")
    @allure.severity("Minor")
    def test_review_comment_fields(self):
        test_review_comment_fields.TestReviewCommentFields(
            self.environment_adapter, self.faker).request().attach().test()

    # @allure.title("Получить комментарии")
    # @allure.description("Получить комментарии")
    # @allure.severity("Minor")
    # def test_reviewId_comments(self):
        # test_reviewId_comments.TestReviewidComments(
        # self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Получить отзывы и комментарии товара")
    @allure.description("Получить отзывы и комментарии товара")
    @allure.severity("Minor")
    def test_review_productId(self):
        test_review_productId.TestReviewProductId(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Получить поля - Комментарии")
    @allure.description("Получить поля - Комментарии")
    @allure.severity("Minor")
    def test_review_fields(self):
        test_review_fields.TestReviewFields(
            self.environment_adapter, self.faker).request().attach().test()

    # @allure.title("Нравится - Комментарии")
    # @allure.description("Нравится - Комментарии")
    # @allure.severity("Minor")
    # def test_review_like(self):
        # test_review_like.TestReviewLike(
        # self.environment_adapter, self.faker).request().attach().test()

    # @allure.title("Не нравится - Комментарии")
    # @allure.description("Не нравится - Комментарии")
    # @allure.severity("Minor")
    # def test_review_dislike(self):
        # test_review_dislike.TestReviewDislike(
        # self.environment_adapter, self.faker).request().attach().test()

    # @allure.title("Добавить ответ")
    # @allure.description("Добавить ответ")
    # @allure.severity("Minor")
    # def test_question_answer(self):
        # test_question_answer.TestQuestionAnswer(
        # self.environment_adapter, self.faker).request().attach().test()

    # @allure.title("Нравится ответ")
    # @allure.description("Нравится ответ")
    # @allure.severity("Minor")
    # def test_question_answer_like(self):
        # test_question_answer_like.TestQuestionAnswerLike(
        # self.environment_adapter, self.faker).request().attach().test()

    # @allure.title("Не нравится ответ")
    # @allure.description("Не нравится ответ")
    # @allure.severity("Minor")
    # def test_question_answer_dislike(self):
        # test_question_answer_dislike.TestQuestionAnswerDislike(
        # self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Получить ответы - Ответ")
    @allure.description("Получить ответы - Ответ")
    @allure.severity("Minor")
    def test_question_questionId(self):
        test_question_questionId.TestQuestionQuestionId(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Получить поля - Вопросы")
    @allure.description("Получить поля - Вопросы")
    @allure.severity("Minor")
    def test_question_answer_fields(self):
        test_question_answer_fields.TestQuestionAnswerFields(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Получить вопросы и ответы товара")
    @allure.description("Получить вопросы и ответы товара")
    @allure.severity("Minor")
    def test_question_productId(self):
        test_question_productId.TestQuestionProductId(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Получить поля - Ответы")
    @allure.description("Получить поля - Ответы")
    @allure.severity("Minor")
    def test_question_fields(self):
        test_question_fields.TestQuestionFields(
            self.environment_adapter, self.faker).request().attach().test()

    # @allure.title("Нравится Ответ")
    # @allure.description("Нравится Ответ")
    # @allure.severity("Minor")
    # def test_question_like_questionId(self):
        # test_question_like_questionId.TestQuestionLikeQuestionId(
        # self.environment_adapter, self.faker).request().attach().test()

    # @allure.title("Не нравится Ответ")
    # @allure.description("Не нравится Ответ")
    # @allure.severity("Minor")
    # def test_question_dislike_questionId(self):
        # test_question_dislike_questionId.TestQuestionDislikeQuestionId(
        # self.environment_adapter, self.faker).request().attach().test()

    # @allure.title("Рекомендация разработчика")
    # @allure.description("Рекомендация разработчика")
    # @allure.severity("Minor")
    # def test_recommend_developer(self):
        # test_recommend_developer.TestRecommendDeveloper(
        # self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Вакансии для рекомендации разработчика")
    @allure.description("Вакансии для рекомендации разработчика")
    @allure.severity("Minor")
    def test_about_recommend_developer(self):
        test_about_recommend_developer.TestAboutRecomendDeveloper(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Получить Вакансию")
    @allure.description("Получить Вакансию")
    @allure.severity("Minor")
    def test_vacancyid(self):
        test_vacancyid.TestVacancyId(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Отменить Заказ")
    @allure.description("Отменить Заказ")
    @allure.severity("Minor")
    def test_order_cancel(self):
        test_order_cancel.TestOrderCancel(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Получить список - Релизы")
    @allure.description("Получить список - Релизы")
    @allure.severity("Minor")
    def test_releases_list(self):
        test_releases_list.TestReleasesList(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Получить релиз")
    @allure.description("Получить релиз")
    @allure.severity("Minor")
    def test_get_releases(self):
        test_get_releases.TestGetReleases(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Получить сборку конфигуратора сборок")
    @allure.description("Получить сборку конфигуратора сборок")
    @allure.severity("Minor")
    def test_pcbuild(self):
        test_pcbuild.TestPcbuild(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Получить структуру конфигуратора сборок")
    @allure.description("Получить структуру конфигуратора сборок")
    @allure.severity("Minor")
    def test_pcbuild_scheme(self):
        test_pcbuild_scheme.TestPcbuildScheme(
            self.environment_adapter, self.faker).request().attach().test()

    # @allure.title("Сохранить сборку конфигуратора сборок")
    # @allure.description("Сохранить сборку конфигуратора сборок")
    # @allure.severity("Minor")
    # def test_pcbuild_components(self):
        # test_pcbuild_components.TestPcbuildComponents(
        # self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Удаление пользователя")
    @allure.description("Удаление пользователя")
    @allure.severity("Critical")
    def test_delete_user(self):
        test_delete_user.TestDeleteUser(
            self.environment_adapter, self.faker).request().rewrite_token().rewrite_environment().attach().test()

    # @allure.title("Разделы каталога")
    # @allure.description("Разделы каталога")
    # def test_catalog_sections(self):
    #     test_catalog_sections.TestCatalogSections(
    #         self.environment_adapter, self.faker).request().rewrite_token().rewrite_environment().attach().test()
