import  requests, random,time,allure
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from all_base_test import All_base
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup, element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
class TestRegister():
    faker = Faker()
    
    base_url = All_base.base_url
    def setup_method(self, method):
        capabilities = {
    "browserName": "firefox",
    "browserVersion": "92.0",
    "selenoid:options": {
        "enableVNC": True,
        "enableVideo": False
    }
}
        self.driver = webdriver.Remote(command_executor='http://172.20.96.221:4444/wd/hub',
        desired_capabilities=capabilities)
        self.new_catalog = All_base().test_catalog()
        
    def teardown_method(self, method):
        self.driver.quit()
    def findElement(self,url=None, tag=None, attributes=None):
        t=[]
        response = requests.request('GET', url=url, headers=All_base.headers)
        tree = BeautifulSoup(response.content, 'html.parser')
        for link in tree.find_all(tag, attributes):
            t.append(link.get('data-ymap-coordinates'))
        return t   
    def randoms(self,products,z):
        section = random.randint(1, len(products) - 1)
        if z == section:
            self.randoms(products,z)
        return section
    def close_modal_city(self):
        base = {'close': 'div.h3__subtext a.city-modal__close'}
        close_button =  WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, base['close'])))
        close_button.click()
    
    def add_to_basket(element = None):
        pass
    @allure.title("Close choose sity")
    @allure.description("WTF!&BRO!&")
    def test_close_sity(self):
        self.driver.get(self.base_url)
        timeout = 30
        time.sleep(2)
        sity_first = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,".h3__title > .highlighted")))
        sity_first= sity_first.text
        self.close_modal_city()
        element_present = EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.main-slider__slide-wrapper'))
        WebDriverWait(self.driver, timeout).until(element_present)
        sity_in_header = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,".header__choose-city")))
        sity_in_header = sity_in_header.text        
        assert sity_first == sity_in_header, "города не совпадают"
        #self.driver.quit()  
        
    
    @allure.title("Close choose sity click yes")
    @allure.description("WTF!&BRO!&")
    def test_close_sity_click_yes(self):
        
        
        self.driver.get(self.base_url)
        timeout = 30
        element_present = EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.main-slider__slide-wrapper'))
        WebDriverWait(self.driver, timeout).until(element_present)
        
        time.sleep(2)
        sity_first = self.driver.find_element_by_css_selector(
            ".h3__title > .highlighted").text
        t = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,".confirmed-city_btn__js")))
        t.click()
        sity_in_header = self.driver.find_element_by_css_selector(
            ".header__choose-city").text    
        with allure.step("Проверка чего то"):
            assert sity_first == sity_in_header, "города совпадают"
    @allure.title("Close choose sity click no")
    @allure.description("WTF!&BRO!&")
    def test_close_sity_click_no(self):
        
        
        self.driver.get(self.base_url)
        timeout = 30
        element_present = EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.main-slider__slide-wrapper'))
        WebDriverWait(self.driver, timeout).until(element_present)
        
        time.sleep(2)
        
        t = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,".notconfirmed-city_btn__js")))
        t.click()
       
        all_sity =  WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"div.city-modal__list > a")))
        t = all_sity[random.randint(0, 11)]
        
        sity_first = t.text
        t.click()
        sity_in_header =  WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".header__choose-city"))).text
            
        with allure.step("Проверка чего то"):
            assert sity_first == sity_in_header, "города совпадают"                 

    @allure.title("Register")
    @allure.description("Проверка на регистрацию")
    def test_register(self):
        
        self.driver.get(self.base_url)
        timeout = 30
        self.close_modal_city()
        element_present = EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.main-slider__slide-wrapper'))
        WebDriverWait(self.driver, timeout).until(element_present)
        register = {
            'register': {
                'reg': '.user-panel__registration',
                'name': 'REGISTER[NAME]',
                'Phone': 'REGISTER[PHONE_NUMBER]',
                'add_code': 'span.bem-icon-link__span.b',
                'code': 'REGISTER[SMS_CODE]',
                'mail': 'REGISTER[EMAIL]',
                'password': 'REGISTER[PASSWORD]',
                'confirm_password': 'REGISTER[CONFIRM_PASSWORD]',
                'in_register': '.bem-button',
            }
        }
        
        if  All_base().delete_user_close() == True:
            
            self.driver.implicitly_wait(5)
            register_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, register['register']['reg'])))
            register_button.click()
            self.driver.implicitly_wait(5)
            self.driver.find_element_by_name(register['register']['name']).send_keys('test')
            self.driver.find_element_by_name(register['register']['Phone']).send_keys('89997777777')
            time.sleep(5)
            button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR,register['register']['add_code'])))
            button.click()
            #self.driver.find_element_by_css_selector(register['register']['add_code']).click()
            self.driver.find_element_by_name(register['register']['code']).send_keys('111111')           
            self.driver.find_element_by_name(register['register']['mail']).send_keys(f'{self.faker.company_email()}')
            self.driver.find_element_by_name(register['register']['password']).send_keys('111111')           
            self.driver.find_element_by_name(register['register']['confirm_password']).send_keys('111111')
            self.driver.find_element_by_css_selector(register['register']['in_register']).click()
            
            menu = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "user-panel__wrap")))
            text_for_test = menu.find_element_by_class_name(
                "user-panel__name").text        
            
        assert  text_for_test  == "test"    

    @allure.title("Autorizationr")
    @allure.description("Проверка на авторизацию")
    def test_autorization(self,ifyouwantautorization = None):
        
        self.driver.get(self.base_url)
        timeout = 30
        
        autorization = {
            'autorization': {
                'Вход': 'user-panel__login'
            },
            'url':f'{self.base_url}/?logout=yes',
        
        }

        if ifyouwantautorization == None: 
            #self.driver.get(autorization['url'])
            
            self.close_modal_city()
            element_present = EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.main-slider__slide-wrapper'))
            WebDriverWait(self.driver, timeout).until(element_present)
           
            self.driver.find_element_by_class_name(
                autorization['autorization']["Вход"]).click()
            model_window = self.driver.find_element_by_css_selector(".bem-modal_active")
            model_window.find_element_by_name("LOGIN").send_keys('89997777777')
            model_window.find_element_by_name("PASSWORD").send_keys('111111')
            model_window.find_element_by_class_name("bem-button").click()

            text_for_test  = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.user-panel__name"))).text
            
            
            assert text_for_test == "test"
        else : 
            self.driver.find_element_by_class_name(
                autorization['autorization']["Вход"]).click()
            model_window = self.driver.find_element_by_css_selector(".bem-modal_active")
            model_window.find_element_by_name("LOGIN").send_keys('89997777777')
            model_window.find_element_by_name("PASSWORD").send_keys('111111')
            model_window.find_element_by_class_name("bem-button").click()
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.user-panel__wrap")))
            return True
    
   
    @allure.title("Sravnenie")
    @allure.description("Проверка на сравнение")
    def test_sravnenie(self):
        
        self.driver.get(self.base_url)
        timeout = 30
        self.close_modal_city()
        element_present = EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.main-slider__slide-wrapper'))
        WebDriverWait(self.driver, timeout).until(element_present)
        new_catalog = self.new_catalog
        t = 0
        for link in self.new_catalog:

            self.driver.get(link)
            products = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.product-card")))

            for i in range(len(new_catalog)):
                section = random.randint(1, len(products) - 1)
                self.driver.execute_script("arguments[0].scrollIntoView();",
                                           products[section])
                t = t + 1
                button = products[section].find_element_by_css_selector(".js-tool-product-cart__content-wrapper")  #добавить проверку появления нижнего слайдера
                button.click()
                added_to_comparison =  WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.p.p_fz11.p_tac"))) 
                
                    
        button_for_basket =  WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.tippy-content > div > a")))
            
        button_for_basket.click()
        
        srav_chek = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".tabs-row__tab")))
        check = 0
        for one_chek in srav_chek:
            nubmer_tovarov = one_chek.find_element_by_class_name("tabs-row__sup").text
            check = check + int(nubmer_tovarov)
            
        assert check == t

    @allure.title("Добавление в корзину")
    @allure.description("Проверка на добавление в корзину")
    def test_addbasket(self):
        self.driver.get(self.base_url)
        timeout = 30
        self.close_modal_city()
        element_present = EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.main-slider__slide-wrapper'))
        WebDriverWait(self.driver, timeout).until(element_present)
        new_catalog = self.new_catalog
        t = 0
        for link in self.new_catalog:

            self.driver.get(link)
            products = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.product-card")))

            for i in range(len(new_catalog)):
                section = random.randint(1, len(products) - 1)
                self.driver.execute_script("arguments[0].scrollIntoView();",
                                           products[section])
                t = t + 1
                button = products[section].find_element_by_css_selector(".bem-icon-link_to-cart")  #добавить проверку появления нижнего слайдера
                button.click()

                added_to_basket = WebDriverWait(self.driver, 10).until(lambda _: button.text == "В корзине")
        self.driver.find_element_by_css_selector("#show-cart a").click()
        
        all_add_to_basket_chek = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".cart-item")))
        check = 0

        for add_to_basket_chek in all_add_to_basket_chek:
            nubmer_tovarov = add_to_basket_chek.find_element_by_css_selector("input").get_property("value")
            check = check + int(nubmer_tovarov)
        assert check == t

    @allure.title("Добавление в корзину ")
    @allure.description("Переход через нижний слайдер")
    def test_addbasket_bottom_slider(self):
        
        self.driver.get(self.base_url)
        timeout = 30
        self.close_modal_city()
        element_present = EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.main-slider__slide-wrapper'))
        WebDriverWait(self.driver, timeout).until(element_present)
        new_catalog = self.new_catalog
        t = 0
        for link in self.new_catalog:

            self.driver.get(link)
            products = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.product-card")))

            for i in range(len(new_catalog)):
                section = random.randint(1, len(products) - 1)
                self.driver.execute_script("arguments[0].scrollIntoView();",
                                           products[section])
                t = t + 1
                button = products[section].find_element_by_css_selector(".bem-icon-link_to-cart")
                button.click()

                added_to_basket = WebDriverWait(self.driver, 10).until(lambda _: button.text == "В корзине")
                
        self.driver.find_element_by_css_selector(".window-cart__buttons > .window-cart__button.window-cart__button_cart.bem-button.bem-button_link.bem-button_red").click()
        all_add_to_basket_chek = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".cart-item")))
        check = 0

        for add_to_basket_chek in all_add_to_basket_chek:
            nubmer_tovarov = add_to_basket_chek.find_element_by_css_selector("input").get_property("value")
            check = check + int(nubmer_tovarov)

        assert check == t    
    
    @allure.title("Add to favoutites")
    @allure.description("Test add to favourites")
    def test_add_to_favourites(self): 
        All_base().close_all_favourites()
        
        self.driver.get(self.base_url)
        timeout = 30
        
        self.close_modal_city()
        element_present = EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.main-slider__slide-wrapper'))
        WebDriverWait(self.driver, timeout).until(element_present)
        new_catalog = self.new_catalog
        t = 0
        if self.test_autorization(ifyouwantautorization=1) == True:
            for link in self.new_catalog:

                self.driver.get(link)
                products = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.product-card")))

                for i in range(len(new_catalog)):

                    #first_status = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-hover-popup__title")))
                    section = random.randint(1, len(products) - 1)
                    self.driver.execute_script("arguments[0].scrollIntoView();",
                                               products[section])
                    t = t + 1
                    button = products[section].find_element_by_css_selector("div.js-tool-product-cart__content-wrapper.user-tool.user-tool_favorite.bem-modal-show")  #element for add to favourites
                    time.sleep(1)
                    button.click()



            self.driver.find_element_by_css_selector("a.user-panel__el.user-panel__el_favorite.bem-link.bem-link_wu").click()

            time.sleep(1)
            add_to_favourites= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".d-inline-block.p.p_vam.p_fz13.grey-text"))).text

            

            assert int(add_to_favourites[0]) == t

    @allure.title("Add to favoutites")
    @allure.description("Test add to favourites in personal ")
    def test_add_to_favourites_in_personal(self): 
        All_base().close_all_favourites()
        
        self.driver.get(self.base_url)
        timeout = 30
        self.close_modal_city()
        element_present = EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.main-slider__slide-wrapper'))
        WebDriverWait(self.driver, timeout).until(element_present)
        new_catalog = self.new_catalog
        t = 0
        if self.test_autorization(ifyouwantautorization=1) == True:
            for link in self.new_catalog:

                self.driver.get(link)
                products = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.product-card")))

                for i in range(len(new_catalog)):

                    #first_status = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-hover-popup__title")))
                    section = random.randint(1, len(products) - 1)
                    self.driver.execute_script("arguments[0].scrollIntoView();",
                                               products[section])
                    t = t + 1
                    button = products[section].find_element_by_css_selector("div.js-tool-product-cart__content-wrapper.user-tool.user-tool_favorite.bem-modal-show")  #element for add to favourites
                    time.sleep(1)
                    button.click()



            self.driver.find_element_by_css_selector(".user-panel__name-wrap > .user-panel__name").click()
            block_personal = self.driver.find_element_by_css_selector(".bem-navigation-menu.bem-profile__menu > .bem-navigation-menu__list")
            button_fabourites = block_personal.find_elements_by_css_selector(".bem-navigation-menu__list-item")[2]
            button_fabourites.click()


            time.sleep(1)
            add_to_favourites= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".d-inline-block.p.p_vam.p_fz13.grey-text"))).text
            assert int(add_to_favourites[0]) == t
    @allure.title("Add to favoutites")
    @allure.description("Test add to favourites in personal ")
    def test_fitler_in_favourites(self): 
        All_base().close_all_favourites()
        
        self.driver.get(self.base_url)
        timeout = 30
        self.close_modal_city()
        element_present = EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.main-slider__slide-wrapper'))
        WebDriverWait(self.driver, timeout).until(element_present)
        new_catalog = self.new_catalog
        t = 0
        if self.test_autorization(ifyouwantautorization=1) == True:
            for link in self.new_catalog:

                self.driver.get(link)
                products = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.product-card")))

                for i in range(len(new_catalog)):
                    section = random.randint(1, len(products) - 1)
                    self.driver.execute_script("arguments[0].scrollIntoView();",
                                               products[section])
                    t = t + 1
                    button = products[section].find_element_by_css_selector("div.js-tool-product-cart__content-wrapper.user-tool.user-tool_favorite.bem-modal-show")  #element for add to favourites
                    time.sleep(1)
                    button.click()

            self.driver.find_element_by_css_selector(".user-panel__name-wrap > .user-panel__name").click()
            block_personal = self.driver.find_element_by_css_selector(".bem-navigation-menu.bem-profile__menu > .bem-navigation-menu__list")
            button_fabourites = block_personal.find_elements_by_css_selector(".bem-navigation-menu__list-item")[2]
            button_fabourites.click() 
            filter_buttons = WebDriverWait(self.driver,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"div.sort-row__el")))
            filter_buttons[1].click()
            all_products =WebDriverWait(self.driver,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"div.product-card__price div.price-row__col")))
            cheap_products = []
            for i in range(0,len(all_products)):
                cheap_products.append(int((all_products[i].text[:-1]).replace(" ","")))             
            z = sorted(cheap_products)
            assert z == cheap_products,"Фильтр дешевые не рабочий"   

            filter_buttons = WebDriverWait(self.driver,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"div.sort-row__el")))
            filter_buttons[2].click()
            all_products =WebDriverWait(self.driver,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"div.product-card__price div.price-row__col")))
            cheap_products = []

            for i in range(0,len(all_products)):
                cheap_products.append(int((all_products[i].text[:-1]).replace(" ","")))  
            z = sorted(cheap_products,reverse=True)  

            assert z == cheap_products,"Фильтр дорогие не рабочий"      
            
               
    
    @allure.title("Смена города")
    @allure.description("Проверка на смену города")
    def test_sity(self):
        errors_url = []
        
        self.driver.get(self.base_url)
        timeout = 30
        self.close_modal_city()
        element_present = EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.main-slider__slide-wrapper'))
        WebDriverWait(self.driver, timeout).until(element_present)
        response = requests.request("GET",
                                    url="https://05.ru/services/choose_city/",
                                    headers=All_base.headers)
        tree = BeautifulSoup(response.content, "html.parser")
        all_sity = tree.find_all("a", {"class": "city-select__list-link"})
        for sity in range(All_base.value_range):
            try:
                section = random.randint(1,len(tree.find_all("a", {"class": "city-select__list-link"})) - 1)
                self.driver.get(all_sity[section].get("href"))
                first_sity = (all_sity[section].text).strip()
                try:

                    second_sity = self.driver.find_element_by_class_name(
                        'bem-icon-link__span').text

                except:
                    pass

                if second_sity != first_sity:
                    errors_url.append(first_sity)
            except:
                pass
                
        assert len(errors_url) == 0    

    @allure.title("Header shop")
    @allure.description("Проверка на Header shop")
    def test_shop(self):
        
        self.driver.get(self.base_url)
        timeout = 30
        self.close_modal_city()
        element_present = EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.main-slider__slide-wrapper'))
        WebDriverWait(self.driver, timeout).until(element_present)
        test_social_url = []
        
        social_url = [self.base_url+'/about/contacts/', 'https://teleg.run/www05ru_bot',
                      'https://vk.com/05ru.shop', 'https://www.youtube.com/user/The05ru', 
                      'https://www.instagram.com/accounts/login/']
        
        self.driver.find_element_by_css_selector(".header__sub-nav > .row-list > .row-list__el:nth-child(2) > a").click()
        all_social_network = self.driver.find_elements_by_css_selector(".contact-page__contact-col > .social-block")
        
        test_shop_location = self.findElement(url=self.base_url +'/about/contacts/',tag='a', attributes={'href': 'javascript:;','class': ['bem-link ymap-store-el-js']})
        shop_location = ['42.9685-47.4955','42.971384-47.419259','42.9802-47.4763',
                        '55.6845-37.6219','43.2389-46.5788','42.0619-48.2896',
                        '42.0434-48.2942','43.231528-46.594865']
        assert shop_location ==test_shop_location ,"локации не прошли"  
        
        for block in all_social_network:
            in_block_element =block.find_elements_by_css_selector(".bem-link")
            if int(len(in_block_element)) == 1:
                in_block_element[0].send_keys(Keys.CONTROL + Keys.RETURN)
            else:
                for element in in_block_element:
                    element.send_keys(Keys.CONTROL + Keys.RETURN)
               
        for windows in range(len(social_url)):
            window_after = self.driver.window_handles[windows]  
            self.driver.switch_to_window(window_after)
            time.sleep(1)
            test_social_url.append(self.driver.current_url)
        assert test_social_url == social_url ,"тест на ссылки на странице магазины не прошел"
    
    @allure.title("Header Catalog")
    @allure.description("Test Catalog")
    def test_catalog_in_header(self):  
        
        self.driver.get(self.base_url)
        timeout = 30
        self.close_modal_city()
        element_present = EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.main-slider__slide-wrapper'))
        WebDriverWait(self.driver, timeout).until(element_present)
        self.driver.find_element_by_css_selector(".header__sub-nav > .row-list > .row-list__el:nth-child(3) > a").click()
        menu_catalog_in_catalog = self.driver.find_elements_by_css_selector('div.catalog-root__menu div.bem-navigation-menu__list .bem-navigation-menu__list-item')
        catalog_name = self.driver.find_elements_by_css_selector('a.h2.catalog-root__list-el-name.bem-link.bem-link_wu')
        new_catalog_name= []
        t = True
        for i in catalog_name:
            if i.text =='':
                continue 
            new_catalog_name.append(i)   

        for i in range(len(menu_catalog_in_catalog)):
            menu_catalog_in_catalog[i].click()
            name_in_menu=menu_catalog_in_catalog[i].text
            name_catalog = new_catalog_name[i].text


            if  name_in_menu!=name_catalog :
                t = False    
                 
        assert t==True,"WTF BRO"

    @allure.title("Header shipping_and_payment")
    @allure.description("Test shipping_and_payment")
    def test_shipping_and_payment(self):       
        
        self.driver.get(self.base_url)
        timeout = 30
        test_link = [self.base_url+'/about/delivery/', self.base_url+'/about/corp/', self.base_url+'/vacancy/makhachkala/', 
        self.base_url+'about/rassrochka/', self.base_url+'/about/guaranty/', self.base_url+'/about/kredit/']

        test_link_for_firefox = [self.base_url+'/about/delivery/',self.base_url+'/about/kredit/',self.base_url+'/about/guaranty/',
        self.base_url+'/about/rassrochka/',self.base_url+'/vacancy/makhachkala/',self.base_url+'/about/corp/']
        test_shipping_url = []            
        self.close_modal_city()
        element_present = EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.main-slider__slide-wrapper'))
        WebDriverWait(self.driver, timeout).until(element_present)
        self.driver.find_element_by_css_selector(" div.header__sub-menu.p.p_fz13 > div > div > div:nth-child(4) > a").click()
        block_in_shipping_and_payment =self.driver.find_element_by_css_selector(".site-carcass__footer-margin")
        all_href_in_block = block_in_shipping_and_payment.find_elements_by_css_selector(".bem-link.bem-subtitle")
        for link in all_href_in_block:
            link.send_keys(Keys.CONTROL + Keys.ENTER)
        for windows in range(len(all_href_in_block)+1):
            window_after = self.driver.window_handles[windows]  
            self.driver.switch_to_window(window_after)
            time.sleep(1)
            test_shipping_url.append(self.driver.current_url)    
        assert test_shipping_url == test_link_for_firefox , "False"        
    
    @allure.title("Catalog test_ordering")
    @allure.description("Test test_ordering")
    def test_ordering(self):
        self.driver.get(self.base_url)
        timeout = 30
        all_selector = {"all_block_checkout":".order-detail__fields-wrapper",
                        "mail":"test"}
        text_for_examination="Внимание! Дождитесь звонка оператора - менеджер проверит наличие товара и подтвердит заказ. Отследить статус заказа можно в Личном кабинете."
        self.close_modal_city()
        element_present = EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.main-slider__slide-wrapper'))
        WebDriverWait(self.driver, timeout).until(element_present)
        self.driver.get(self.base_url+"/catalog/knigi_i_kanctovary/ruchki_karandashi/ruchki/118468/")  
       
        block_with_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.product-price-block__buttons')))
        block_with_button.find_element_by_css_selector(".add-to-cart.add-to-cart_large.product-price-block__button.detail-page-add-to-cart-btn__js").click()#Кнопка добавить в корзину
        time.sleep(5)
        block_with_button.find_element_by_css_selector(".added-to-cart__current").click() #Кнопка "В корзине" после добавление товара в корзину
        ordering_block = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, all_selector["all_block_checkout"])))
        t = ordering_block.find_elements_by_css_selector(".input-radio.order-detail__radio")
        t[1].click()
        elemeint_in_ordering_block = ordering_block.find_elements_by_css_selector(".order-detail__input")
        elemeint_in_ordering_block[1].send_keys(f'{self.faker.address()}')
        elemeint_in_ordering_block[2].send_keys(f'89997777777')
        elemeint_in_ordering_block[3].send_keys('loxuilox@yandex.ru')
        elemeint_in_ordering_block[4].send_keys(f'{self.faker.name()}+test')
        elemeint_in_ordering_block[5].send_keys('test')
        #elemeint_in_ordering_block[6].semd_keys('') #использовать при необходимости ввода промокода
        self.driver.find_element_by_css_selector(".order-detail__send").click()
        t = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.success-order > div.bem-paragraph >strong"))).text
        
        assert t == text_for_examination 
    
    @allure.title(" test stocks")
    @allure.description("Test test stocks")
    def test_stocks(self):
        
        self.driver.get(self.base_url)
        timeout = 30
        all_selector = {"blockheader":"div.header__sub-menu.p.p_fz13 > div > div > div:nth-child(7) > a"}
        text_for_examination=[]
        self.close_modal_city()
        element_present = EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.main-slider__slide-wrapper'))
        WebDriverWait(self.driver, timeout).until(element_present)
        element = 0
        block_with_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.header > div.header__sub-menu.p.p_fz13 >div>div")))
        block_with_button.find_element_by_css_selector( all_selector["blockheader"]).click()#
   
        elements_in_stocks = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,".sales-list__grid > .sales-list__item")))
        while element < All_base.value_range:
            
            self.driver.execute_script("arguments[0].scrollIntoView();",
                                           elements_in_stocks[element])
            firtst = elements_in_stocks[element].find_element_by_css_selector(".sales-list__item-title").text                               
            elements_in_stocks[element].click()
            block =  WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,".sale-page__description.inner-tag-transform ")))
            second = block.find_element_by_css_selector(".bem-title").text
            if firtst == second:
                block.find_element_by_css_selector(".sale-page__description-banner> .sale-page__banner")
                WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,".product-card__photo")))
                
            else:
                text_for_examination.append("False")
            element=element+1
            
            self.driver.get(self.base_url+"/sales/")
            elements_in_stocks = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,".sales-list__grid > .sales-list__item")))    

                                           
         
        assert len(text_for_examination) == 0
    
    @allure.title(" test profile")
    @allure.description("Test test profile")
    def test_profile_home(self):
        
        self.driver.get(self.base_url)
        timeout = 30
        self.close_modal_city()
        element_present = EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.main-slider__slide-wrapper'))
        WebDriverWait(self.driver, timeout).until(element_present)  
        self.test_autorization(ifyouwantautorization =1)  
        block_with_buttons =  WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,".user-panel__name-wrap"))) 
        
        time.sleep(5)
        Hover = ActionChains(self.driver).move_to_element(block_with_buttons)
        Hover.perform()
        add = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,".user-panel__hidden-block")))
        add = add.find_elements_by_css_selector(".user-panel__hidden-el")
        time.sleep(2)
        add[0].click()
       
        element_for_test = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,".h2.h2_mt.h2_mb10"))) 
        element_for_test = element_for_test.text 
        
        assert "test" == element_for_test
    @allure.title(" test profile Order list")
    @allure.description("Test test profile Order list")
    def test_profile_order_list(self):
        
        self.driver.get(self.base_url)
        timeout = 30
        self.close_modal_city()  
        element_present = EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.main-slider__slide-wrapper'))
        WebDriverWait(self.driver, timeout).until(element_present)
        self.test_autorization(ifyouwantautorization =1)  
        block_with_buttons =  WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,".user-panel__name-wrap"))) 
        
        time.sleep(5)
        Hover = ActionChains(self.driver).move_to_element(block_with_buttons)
        Hover.perform()
        add = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,".user-panel__hidden-block")))
        add = add.find_elements_by_css_selector(".user-panel__hidden-el")
        time.sleep(2)
        add[1].click()
       
        element_for_test = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,".h2.h2_mb10"))) 
        element_for_test = element_for_test[1].text 
        
        assert "Заказы" == element_for_test
    @allure.title(" test profile personal_information")
    @allure.description("Test test profile personal_information")
    def test_profile_personal_information(self):
        
        self.driver.get(self.base_url)
        timeout = 30
        self.close_modal_city()
        element_present = EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.main-slider__slide-wrapper'))
        WebDriverWait(self.driver, timeout).until(element_present)  
        self.test_autorization(ifyouwantautorization =1)  
        block_with_buttons =  WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,".user-panel__name-wrap"))) 
        
        time.sleep(5)
        Hover = ActionChains(self.driver).move_to_element(block_with_buttons)
        Hover.perform()
        add = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,".user-panel__hidden-block")))
        add = add.find_elements_by_css_selector(".user-panel__hidden-el")
        time.sleep(2)
        add[2].click()
       
        element_for_test = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,".h2"))) 
        element_for_test = element_for_test[1].text 
        
        assert "Личная информация" == element_for_test          
    @allure.title(" test logo")
    @allure.description("Test test logo")
    def test_base_home(self):
        timeout = 30
        self.driver.get(self.base_url+"/t")
        self.close_modal_city()
        self.driver.find_element_by_css_selector(".header__main-menu > .header__logo").click()
        phone_in_home =  WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"a.bem-icon-link.bem-icon-link_wu.bem-icon-link_gift.catalog-overview__link.catalog-overview__link_sale > span.bem-icon-link__span")))
        phone_in_home=phone_in_home.text
        
        assert "Акции" == phone_in_home
    @allure.title(" test request_a_call_back")
    @allure.description("Test test request_a_call_back")
    def test_base_request_a_call_back(self):
        self.driver.get(self.base_url)
        timeout = 30       
        self.close_modal_city()
        element_present = EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.main-slider__slide-wrapper'))
        WebDriverWait(self.driver, timeout).until(element_present)
        call_to_me = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,".bem-modal-show.header__phone-show")))
        call_to_me.click()
        phone_in_home =  WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,".bem-modal.bem-modal_w280.bem-modal_small.bem-modal_active")))
        buttons = phone_in_home.find_elements_by_css_selector(".bem-form.bem-form_small > .bem-form__row")
        buttons[0].find_element_by_css_selector(".bem-input.bem-input_text").send_keys("test") 
        buttons[1].find_element_by_css_selector(".bem-input.bem-input_text").send_keys("89997777777")
        t = buttons[2].find_elements_by_css_selector(".bem-form__right  > .input-radio")
        t[2].click()
        buttons[4].click()
        t = buttons[4].find_element_by_css_selector(".bem-button.bem-button_red.bem-button_medium").get_attribute("value")
        
        assert "Отправлено" == t   
    
    @allure.title("Кнопка Забыл пароль")
    @allure.description("Кнопка Забыл пароль")
    def test_forgot_password(self):
        
        self.driver.get(self.base_url)
        timeout = 30
        all_selector = {
            'autorization': {
                'Вход': 'user-panel__login'
            },
        }
        
        self.close_modal_city()
        element_present = EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.main-slider__slide-wrapper'))
        WebDriverWait(self.driver, timeout).until(element_present)
        self.driver.find_element_by_class_name(all_selector['autorization']["Вход"]).click()
        model_window = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".bem-modal_active")))        
        button =model_window.find_element_by_css_selector("form > div > div > div > a")
        button.click()
        model_window = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".restore_password_form__js")))        
        model_window.find_element_by_name("RESTORE_PSSWD[LOGIN]").send_keys('79997777777') 
        WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[src^='https://www.google.com/recaptcha/api2/anchor?']")))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".rc-anchor-checkbox"))).click()
        self.driver.switch_to.default_content()
        time.sleep(5)
        close_button =  WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.site-carcass__container > div > div > div > form > div > div:nth-child(5) > div > input")))
        close_button.click()
        text_for_test = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,".bem-content>.h2"))).text
        assert text_for_test == "Восстановление пароля"
    @allure.title("Проверка отображения фотографий товара")
    @allure.description("Проверка отображения фотографий товара")
    def test_photo_in_busket(self):
        self.driver.get(self.base_url)
        timeout = 30     
        self.close_modal_city()
        element_present = EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.main-slider__slide-wrapper'))
        WebDriverWait(self.driver, timeout).until(element_present)
        new_catalog = self.new_catalog
        t = 0
        for link in self.new_catalog:

            self.driver.get(link)
            products = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.product-card")))

            for i in range(len(new_catalog)):
                section = random.randint(1, len(products) - 1)
                self.driver.execute_script("arguments[0].scrollIntoView();",
                                           products[section])
                t = t + 1
                button = products[section].find_element_by_css_selector(".bem-icon-link_to-cart")  #добавить проверку появления нижнего слайдера
                button.click()

                added_to_basket = WebDriverWait(self.driver, 10).until(lambda _: button.text == "В корзине")
        self.driver.find_element_by_css_selector("#show-cart a").click()
        
        all_add_to_basket_chek = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.cart-item__photo > img")))
        check = []

        for add_to_basket_chek in all_add_to_basket_chek:
            if add_to_basket_chek.get_attribute("src") == "https://img."+ self.base_url+ "/resize/HC-KFbKxNIBN-FCfD_ujNhCmNDir3kNSAAnP6EzIjf4//rs:fit:300:300:0:0/q:100/bG9jYWw6Ly8vdXBsb2FkLzFmYi8xZmI2NGJiOTVjNTJmOTgwMTJiOGI2NWUyMzQ5N2ZlNS5wbmc":
                check.append(add_to_basket_chek.get_attribute("src"))
        assert len(check) == 0        
    @allure.title("Проверка отображения наименования")
    @allure.description("Проверка отображения наименования")
    def test_naimenovanie_in_busket(self):
        self.driver.get(self.base_url)
        timeout = 30     
        self.close_modal_city()
        element_present = EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.main-slider__slide-wrapper'))
        WebDriverWait(self.driver, timeout).until(element_present)
        new_catalog = self.new_catalog
        t = 0
        for link in self.new_catalog:

            self.driver.get(link)
            products = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.product-card")))

            for i in range(len(new_catalog)):
                section = random.randint(1, len(products) - 1)
                self.driver.execute_script("arguments[0].scrollIntoView();",
                                           products[section])
                t = t + 1
                button = products[section].find_element_by_css_selector(".bem-icon-link_to-cart")  #добавить проверку появления нижнего слайдера
                button.click()

                added_to_basket = WebDriverWait(self.driver, 10).until(lambda _: button.text == "В корзине")
        self.driver.find_element_by_css_selector("#show-cart a").click()
        
        all_add_to_basket_chek = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.cart-item__crop-link")))
        check = []

        for add_to_basket_chek in all_add_to_basket_chek:
            if not len(add_to_basket_chek.text):
                check.append(add_to_basket_chek.get_attribute("href"))
        assert len(check) == 0 
    @allure.title("Проверка отображения цены")
    @allure.description("Проверка отображения цены")
    def test_price_in_busket(self):
        self.driver.get(self.base_url)
        timeout = 30     
        self.close_modal_city()
        element_present = EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.main-slider__slide-wrapper'))
        WebDriverWait(self.driver, timeout).until(element_present)
        new_catalog = self.new_catalog
        t = 0
        for link in self.new_catalog:

                self.driver.get(link)
                products = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.product-card")))

                for i in range(len(new_catalog)):
                    t = t + 1
                    #section = list(range(0, len(products) - 1))
                    #section = random.randint(1, len(products) - 1)
                    self.driver.execute_script("arguments[0].scrollIntoView();",
                                               products[t])
                    
                    button = products[t].find_element_by_css_selector(".bem-icon-link_to-cart")  #добавить проверку появления нижнего слайдера
                    button.click()
                    
                    added_to_basket = WebDriverWait(self.driver, 20).until(lambda _: button.text == "В корзине")
        self.driver.find_element_by_css_selector("#show-cart a").click()
        
        all_add_to_basket_chek = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.cart-item")))
        check = []
        
        for add_to_basket_chek in all_add_to_basket_chek:
        
            if not len(add_to_basket_chek.find_element_by_css_selector("div.cart-item__current-price").text):
                check.append(add_to_basket_chek.find_element_by_css_selector("a.cart-item__crop-link").get_attribute("href"))
        assert len(check) == 0   
    @allure.title("Проверка отображения информации наличия товара")
    @allure.description("Проверка отображения информации наличия товара")
    def test_info_in_busket(self):
        self.driver.get(self.base_url)
        timeout = 30     
        self.close_modal_city()
        element_present = EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.main-slider__slide-wrapper'))
        WebDriverWait(self.driver, timeout).until(element_present)
        new_catalog = self.new_catalog
        t = 0
        for link in self.new_catalog:

                self.driver.get(link)
                products = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.product-card")))

                for i in range(len(new_catalog)):
                    t = t + 1
                    #section = list(range(0, len(products) - 1))
                    #section = random.randint(1, len(products) - 1)
                    self.driver.execute_script("arguments[0].scrollIntoView();",
                                               products[t])
                    
                    button = products[t].find_element_by_css_selector(".bem-icon-link_to-cart")  #добавить проверку появления нижнего слайдера
                    button.click()
                    
                    added_to_basket = WebDriverWait(self.driver, 20).until(lambda _: button.text == "В корзине")
        self.driver.find_element_by_css_selector("#show-cart a").click()
        
        all_add_to_basket_chek = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.cart-item")))
        check = []
        
        for add_to_basket_chek in all_add_to_basket_chek:
        
            if not len(add_to_basket_chek.find_element_by_css_selector("span.cart-item__available").text):
                check.append(add_to_basket_chek.find_element_by_css_selector("a.cart-item__crop-link").get_attribute("href"))
        assert len(check) == 0     
    @allure.title("Проверка удаления товара")
    @allure.description("Проверка удаления товара")
    def test_delete_in_busket(self):
        self.driver.get(self.base_url)
        timeout = 30     
        self.close_modal_city()
        element_present = EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.main-slider__slide-wrapper'))
        WebDriverWait(self.driver, timeout).until(element_present)
        new_catalog = self.new_catalog
        t = 0
        for link in self.new_catalog:

                self.driver.get(link)
                products = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.product-card")))

                for i in range(len(new_catalog)):
                    
                    #section = list(range(0, len(products) - 1))
                    #section = random.randint(1, len(products) - 1)
                    self.driver.execute_script("arguments[0].scrollIntoView();",
                                               products[t])
                    
                    button = products[t].find_element_by_css_selector(".bem-icon-link_to-cart")  #добавить проверку появления нижнего слайдера
                    button.click()
                    t = t + 1
                    #added_to_basket = WebDriverWait(self.driver, 20).until(lambda _: button.text == "В корзине")
        self.driver.find_element_by_css_selector("#show-cart a").click()
        
        all_add_to_basket_chek = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.cart-item")))
        check = []
        
        for add_to_basket_chek in all_add_to_basket_chek:
            first_text = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"h1.cart-page__title > span"))).text
            self.driver.find_elements_by_css_selector("a.cart-item__clear")[0].click()

            if first_text != self.driver.find_element_by_css_selector("h1.cart-page__title > span").text:
                check.append(add_to_basket_chek.find_element_by_css_selector("a.cart-item__crop-link").get_attribute("href"))
        assert len(check) == 0,"Кнопка убрать не работает"       
    @allure.title("Проверка удаления всех товаров")
    @allure.description("Проверка удаления всех товаров")
    def test_all_delete_in_busket(self):
        self.driver.get(self.base_url)
        timeout = 30     
        self.close_modal_city()
        element_present = EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.main-slider__slide-wrapper'))
        WebDriverWait(self.driver, timeout).until(element_present)
        new_catalog = self.new_catalog
        t = 0
        for link in self.new_catalog:

                self.driver.get(link)
                products = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.product-card")))

                for i in range(len(new_catalog)):
                    t = t + 1
                    #section = list(range(0, len(products) - 1))
                    #section = random.randint(1, len(products) - 1)
                    self.driver.execute_script("arguments[0].scrollIntoView();",
                                               products[t])
                    
                    button = products[t].find_element_by_css_selector(".bem-icon-link_to-cart")  #добавить проверку появления нижнего слайдера
                    button.click()
                    
                    #added_to_basket = WebDriverWait(self.driver, 20).until(lambda _: button.text == "В корзине")
        self.driver.find_element_by_css_selector("#show-cart a").click()
        
        all_add_to_basket_chek = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.cart-item")))
        check = []
        
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"h1.cart-page__title > a"))).click()
        first_text = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.empty-basket-node div.unavailable__wrapper > div.h3"))).text
        assert first_text == 'В корзине нет товаров',"Кнопка удалить все товары из корзины не работает"    
    @allure.title("Проверка удаления всех товаров")
    @allure.description("Проверка удаления всех товаров")
    def test_clever_tovary_in_busket(self):
        self.driver.get(self.base_url)
        timeout = 30     
        self.close_modal_city()
        element_present = EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.main-slider__slide-wrapper'))
        WebDriverWait(self.driver, timeout).until(element_present)
        new_catalog = self.new_catalog
        t = 0
        for link in self.new_catalog:

                self.driver.get(link)
                products = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.product-card")))

                for i in range(len(new_catalog)):
                    
                    #section = list(range(0, len(products) - 1))
                    #section = random.randint(1, len(products) - 1)
                    self.driver.execute_script("arguments[0].scrollIntoView();",
                                               products[t])
                    
                    button = products[t].find_element_by_css_selector(".bem-icon-link_to-cart")  #добавить проверку появления нижнего слайдера
                    button.click()
                    t = t + 1
                    #added_to_basket = WebDriverWait(self.driver, 20).until(lambda _: button.text == "В корзине")
        self.driver.find_element_by_css_selector("#show-cart a").click()
        
        all_add_to_basket_chek = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.cart-item")))
        check = []

        for add_to_basket_chek in all_add_to_basket_chek:
            add_to_basket_chek.find_element_by_css_selector("div.cart-item__count input.item-counter__input").send_keys('10')
        for add_to_basket_chek in all_add_to_basket_chek:
            add_to_basket_chek.find_element_by_css_selector("div.cart-item__count input.item-counter__input").clear()
            first_text = add_to_basket_chek.find_element_by_css_selector("div.cart-item__count input.item-counter__input").get_attribute("value")   
            add_to_basket_chek.find_element_by_css_selector("div.cart-item__count input.item-counter__input").send_keys('5')
            second_text = add_to_basket_chek.find_element_by_css_selector("div.cart-item__count input.item-counter__input").get_attribute("value")
            
            if first_text == second_text:
                check.append(add_to_basket_chek.find_element_by_css_selector("a.cart-item__crop-link").get_attribute("href"))        
        assert len(check) == 0,"Значения не меняются" 
    @allure.title("Sravnenie")
    @allure.description("Проверка удаления из сравнения")
    def test_dell_sravnenie(self):
        
        self.driver.get(self.base_url)
        timeout = 30
        self.close_modal_city()
        element_present = EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.main-slider__slide-wrapper'))
        WebDriverWait(self.driver, timeout).until(element_present)
        new_catalog = self.new_catalog
        t = 0
        z = 0
        for link in self.new_catalog:

            self.driver.get(link)
            products = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.product-card")))

            for i in range(len(new_catalog)):
                section = self.randoms(products,z)
                #section = random.randint(1, len(products) - 1)
                self.driver.execute_script("arguments[0].scrollIntoView();",
                                           products[section])
                t = t + 1
                button = products[section].find_element_by_css_selector(".js-tool-product-cart__content-wrapper")  #добавить проверку появления нижнего слайдера
                button.click()
                added_to_comparison =  WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.p.p_fz11.p_tac"))) 
                
                    
        button_for_basket =  WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.tippy-content > div > a")))
            
        button_for_basket.click()
        
        srav_chek = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".tabs-row__tab")))
        check = 0
        for one_chek in srav_chek:
            nubmer_tovarov = one_chek.find_element_by_class_name("tabs-row__sup").text
            check = check + int(nubmer_tovarov)
        SearchButton = self.driver.find_element_by_css_selector("div.product-card-compare__photo-wrapper.product-card-compare__photo-wrapper_zoom")  
        s = self.driver.find_element_by_css_selector("div.product-card-compare__photo-icons >a")
        action = ActionChains(self.driver)
        if action.move_to_element(SearchButton).move_to_element(s).click().perform() :
            t = t -1
        assert check == t ,"Удаление товара из сравнения не работает"  
    @allure.title("Add to favoutites")
    @allure.description("Test add and delete to  favourites in personal ")
    def test_add_and_del_to_favourites_in_personal(self): 
        All_base().close_all_favourites()
        self.driver.get(self.base_url)
        timeout = 30
        self.close_modal_city()
        element_present = EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.main-slider__slide-wrapper'))
        WebDriverWait(self.driver, timeout).until(element_present)
        new_catalog = self.new_catalog
        t = 0
        if self.test_autorization(ifyouwantautorization=1) == True:
            for link in self.new_catalog:

                self.driver.get(link)
                products = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.product-card")))

                for i in range(len(new_catalog)):

                    #first_status = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-hover-popup__title")))
                    section = random.randint(1, len(products) - 1)
                    self.driver.execute_script("arguments[0].scrollIntoView();",
                                               products[section])
                    t = t + 1
                    button = products[section].find_element_by_css_selector("div.js-tool-product-cart__content-wrapper.user-tool.user-tool_favorite.bem-modal-show")  #element for add to favourites
                    time.sleep(1)
                    button.click()



            self.driver.find_element_by_css_selector(".user-panel__name-wrap > .user-panel__name").click()
            block_personal = self.driver.find_element_by_css_selector(".bem-navigation-menu.bem-profile__menu > .bem-navigation-menu__list")
            button_fabourites = block_personal.find_elements_by_css_selector(".bem-navigation-menu__list-item")[2]
            button_fabourites.click()
            products = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.product-card")))
            for i in range(len(products)-1):

                #first_status = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-hover-popup__title")))
                self.driver.execute_script("arguments[0].scrollIntoView();",
                                           products[i])
                button = products[i].find_element_by_css_selector("div.js-tool-product-cart__content-wrapper.user-tool.user-tool_favorite.bem-modal-show")  #element for add to favourites
                time.sleep(1)
                button.click()

            time.sleep(1)
            add_to_favourites= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".d-inline-block.p.p_vam.p_fz13.grey-text"))).text
            assert int(add_to_favourites[0]) == t , "Удаление из избранного не работает"   

    @allure.title("Проверка окрытия карточки товара")
    @allure.description("Проверка окрытия карточки товара")
    def test_open_in_busket(self):
        self.driver.get(self.base_url)
        timeout = 30     
        self.close_modal_city()
        element_present = EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.main-slider__slide-wrapper'))
        WebDriverWait(self.driver, timeout).until(element_present)
        new_catalog = self.new_catalog
        t = []
        for link in self.new_catalog:

            self.driver.get(link)
            products = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.product-card")))

            for i in range(len(new_catalog)):
                section = random.randint(1, len(products) - 1)
                self.driver.execute_script("arguments[0].scrollIntoView();",
                                           products[section])
                
                button = products[section].find_element_by_css_selector(".bem-icon-link_to-cart")  #добавить проверку появления нижнего слайдера
                button.click()

                #added_to_basket = WebDriverWait(self.driver, 10).until(lambda _: button.text == "В корзине")
        self.driver.find_element_by_css_selector("#show-cart a").click()
        
        all_add_to_basket_chek = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.cart-item__crop-link")))
        check = []

        for add_to_basket_chek in all_add_to_basket_chek:
            if len(add_to_basket_chek.text):
                check.append(add_to_basket_chek.text)
                add_to_basket_chek.send_keys(Keys.CONTROL + Keys.RETURN)
            else:
                assert False,"Товары не открываются в корзине"         
        for windows in range(1,len(all_add_to_basket_chek)+1):
                
            window_after = self.driver.window_handles[windows]  
            self.driver.switch_to_window(window_after)
            time.sleep(3)
            z = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.product-page__title > h1")))
            t.append(z.text)               
        
        assert check == t 
    @allure.title("Проверка увелечение цены всех товаров")
    @allure.description("Проверка увелечение цены всех товаров")
    def test_price_increase_tovary_in_busket(self):
        self.driver.get(self.base_url)
        timeout = 30     
        self.close_modal_city()
        element_present = EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.main-slider__slide-wrapper'))
        WebDriverWait(self.driver, timeout).until(element_present)
        new_catalog = self.new_catalog
        t = 0
        for link in self.new_catalog:

                self.driver.get(link)
                products = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.product-card")))

                for i in range(len(new_catalog)):
                    
                    section = random.randint(1, len(products) - 1)
                    self.driver.execute_script("arguments[0].scrollIntoView();",
                                               products[section])
                    
                    button = products[section].find_element_by_css_selector(".bem-icon-link_to-cart")  #добавить проверку появления нижнего слайдера
                    button.click()
                    t = t + 1
                    #added_to_basket = WebDriverWait(self.driver, 20).until(lambda _: button.text == "В корзине")
        self.driver.find_element_by_css_selector("#show-cart a").click()
        
        all_add_to_basket_chek = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.cart-item")))
        check = []

        first_price = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.props-list__value.black-text > div"))).text.replace("₽","").replace(" ","")
        for i in range(0,len(all_add_to_basket_chek)-1):
            z = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.cart-item div.cart-item__current-price")))[i]
            if z.text == "цена не указана":
                continue
            #else:
            WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.cart-item div.cart-item__count input.item-counter__input")))[i].send_keys('5')
            second_price = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.props-list__value.black-text > div"))).text.replace("₽","").replace(" ","")
            time.sleep(10)
        assert first_price < second_price,"Значения не меняются" 
    @allure.title("Проверка отображения наименования")
    @allure.description("Проверка отображения наименования")
    def test_naimenovanie_copy_url_in_busket(self):
        self.driver.get(self.base_url)
        timeout = 30     
        self.close_modal_city()
        element_present = EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.main-slider__slide-wrapper'))
        WebDriverWait(self.driver, timeout).until(element_present)
        new_catalog = self.new_catalog
        
        for link in self.new_catalog:

            self.driver.get(link)
            products = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.product-card")))

            for i in range(len(new_catalog)):
                section = random.randint(1, len(products) - 1)
                self.driver.execute_script("arguments[0].scrollIntoView();",
                                           products[section])
                
                button = products[section].find_element_by_css_selector(".bem-icon-link_to-cart")  #добавить проверку появления нижнего слайдера
                button.click()

                #added_to_basket = WebDriverWait(self.driver, 10).until(lambda _: button.text == "В корзине")
        self.driver.find_element_by_css_selector("#show-cart a").click()
        
        all_add_to_basket_chek = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.cart-item__crop-link")))
        check = []

        for add_to_basket_chek in all_add_to_basket_chek:
            if len(add_to_basket_chek.get_attribute("href")):
                check.append(add_to_basket_chek.get_attribute("href"))
        t = []
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div span.bem-icon-link.bem-icon-link_pseudo.bem-icon-link_share span.bem-icon-link__span"))).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "label.search-bar__field input.search-bar__input"))).send_keys(Keys.CONTROL, 'v')
        z = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "label.search-bar__field input.search-bar__input"))).get_attribute("value")
        self.driver.get(z)
        all_add_to_basket_chek = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.cart-page__item-list div.cart-item  > a.cart-item__photo")))
        for add_to_basket_chek in all_add_to_basket_chek:
            if len(add_to_basket_chek.get_attribute("href")):
                t.append(add_to_basket_chek.get_attribute("href"))         
        assert check == t    
    @allure.title("Проверка работы фильтров дешевые")
    @allure.description("Проверка работы фильтров дешевые")
    def test_filter_in_catalog(self):
        self.driver.get(self.base_url)
        timeout = 30     
        self.close_modal_city()
        element_present = EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.main-slider__slide-wrapper'))
        WebDriverWait(self.driver, timeout).until(element_present)
       
        check = []
        t = []
        link  = self.new_catalog[random.randint(0,len(self.new_catalog)-1)]
        self.driver.get(link)
        products = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.product-card")))
        for product in products:
            if product.find_element_by_css_selector("div.product-card__price  div.price-row__col").text == "Цена не указана":
                continue
            try:
                if product.find_element_by_css_selector("div.product-card__black") == True:
                    t.append(product.find_element_by_css_selector("div.product-card__black").text)
            except:      
                t.append(product.find_element_by_css_selector("div.product-card__price  div.price-row__col").text)
            t.append(product.find_element_by_css_selector("div.product-card__price  div.price-row__col").text)    
        
        all_fitler__in_catalog = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.sort-row__el")))
        all_fitler__in_catalog[1].click()
        
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.bem-icon-link_red ")))
        products = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.product-card")))
        for product in products:
            if product.find_element_by_css_selector("div.product-card__price  div.price-row__col").text == "Цена не указана":
                continue
            try:
                if product.find_element_by_css_selector("div.product-card__black") == True:
                    check.append(product.find_element_by_css_selector("div.product-card__black").text.replace("₽","").replace(" ",""))
            except:      
                check.append(product.find_element_by_css_selector("div.product-card__price  div.price-row__col").text.replace("₽","").replace(" ",""))
        if check != t:
            t = sorted(check)
            if t == check:
                t =True
            else: 
                t = False
        assert check != t        
    @allure.title("Проверка работы фильтров дешевые")
    @allure.description("Проверка работы фильтров дешевые")
    def test_filter_more_in_catalog(self):
        self.driver.get(self.base_url)
        timeout = 30     
        self.close_modal_city()
        element_present = EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.main-slider__slide-wrapper'))
        WebDriverWait(self.driver, timeout).until(element_present)
       
        check = []
        t = []
        link  = self.new_catalog[random.randint(0,len(self.new_catalog)-1)]
        self.driver.get(link)
        products = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.product-card")))
        for product in products:
            
            try:
                if product.find_element_by_css_selector("div.product-card__price  div.price-row__col").text == "Цена не указана":
                    continue
                if product.find_element_by_css_selector("div.product-card__black") == True:
                    t.append(product.find_element_by_css_selector("div.product-card__black").text.replace("₽","").replace(" ",""))
            except:      
                t.append(product.find_element_by_css_selector("div.product-card__price  div.price-row__col").text.replace("₽","").replace(" ",""))
            t.append(product.find_element_by_css_selector("div.product-card__price  div.price-row__col").text.replace("₽","").replace(" ",""))    
        
        all_fitler__in_catalog = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.sort-row__el")))
        all_fitler__in_catalog[2].click()
        print(self.driver.current_url)
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.bem-icon-link_red ")))
        products = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.product-card")))
        for product in products:
            
            try:
                if product.find_element_by_css_selector("div.product-card__price  div.price-row__col").text == "Цена не указана":
                    continue
                if product.find_element_by_css_selector("div.product-card__black") == True:
                    check.append(product.find_element_by_css_selector("div.product-card__black").text.replace("₽","").replace(" ",""))
            except:      
                check.append(product.find_element_by_css_selector("div.product-card__price  div.price-row__col").text.replace("₽","").replace(" ",""))
            check.append(product.find_element_by_css_selector("div.product-card__price  div.price-row__col").text.replace("₽","").replace(" ",""))    
        if check != t:
            t = sorted(check,reverse=True)
            if t == check:
                t =True
            else: 
                t = False
        assert t == True   
print("1")    