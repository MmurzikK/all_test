import requests
import os.path
from bs4 import BeautifulSoup
from base_test_catalog import TestCatalog
from concurrent.futures import ThreadPoolExecutor
from api_catalog import Token_api
from urllib.parse import urlparse

catalog_all = Token_api.catalog_json()


class Test_bot:

    def bot(bot_request, new_catalog_all):
        bot_request = urlparse(bot_request).path
        for link in catalog_all:
            if link.startswith(bot_request, 0):
                new_catalog_all.append(link)
        catalog_respose.one(new_catalog_all,catalog_respose.filename_user_catalog)


class catalog_respose:
    filename_user = None
    filename_user_catalog = None
    stop_bot = None
    
    errors_url = []
    def one(testCatalogAll, fileName, number='one'):

        def do():
            a = 0
            status_bar = open(catalog_respose.filename_user, 'w+')
            status_bar.close() 
            for url in testCatalogAll:
                response = requests.request('GET', url=TestCatalog.host
                        + url, headers=TestCatalog.headers)
                
                while True:
                      
                    if catalog_respose.stop_bot is not None: 
                        catalog_respose.stop_bot = None
                        return

                    tree = BeautifulSoup(response.content, 'html.parser')

                    for link in tree.find_all('img',
                            {'src': TestCatalog.image_default}):
                        catalog_respose.errors_url.append(TestCatalog.host
                                + link.parent.get('href'))
                        my_file = open(fileName, 'a+')
                        my_file.write(TestCatalog.host
                                + link.parent.get('href') + '\n')
                        my_file.close()

                        

                    try:
                        next_page_element = tree.find('a',
                                {'class': 'bem-page-nav__arrow_right'
                                }).get('href')

                        response = requests.request('GET',
                                url=TestCatalog.host
                                + next_page_element,
                                headers=TestCatalog.headers)
                    except:

                        break
                 
                a = a+1
                status_bar = open(catalog_respose.filename_user, 'w+')
                status_bar.write('{index_string}'.format(index_string=str(a)))
                status_bar.close()

        do()
        if os.path.isfile(catalog_respose.filename_user) == True:
            os.remove(os.path.join(os.path.abspath(os.path.dirname(__file__)), catalog_respose.filename_user))

    def run_io_tasks_in_parallel(tasks):
        with ThreadPoolExecutor() as executor:
            running_tasks = [executor.submit(task) for task in tasks]
            for running_task in running_tasks:
                running_task.result()

    def start():
        testCatalogAllLinksQuantityHalf = int(len(catalog_all) / 2)
        catalog_respose.run_io_tasks_in_parallel([lambda : \
                catalog_respose.one(catalog_all[testCatalogAllLinksQuantityHalf:],
               catalog_respose.filename_user_catalog, 'two'), lambda : \
                catalog_respose.one(catalog_all[:testCatalogAllLinksQuantityHalf],
                catalog_respose.filename_user_catalog)])
