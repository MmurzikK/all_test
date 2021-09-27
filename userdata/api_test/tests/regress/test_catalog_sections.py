from tests import test_base
import requests
import base64
import json


class TestCatalogSections(test_base.TestBase):
    path = "/catalog/sections?seo_sections=получение_разделов_фильтров"
    sections = None

    def request(self):
        self.response = requests.request(
            method="GET", url=self.environment["host"] + self.path, headers=self.environment["headers"])
        self.errors = {}
        self.sections = self.response.json()["result"]
        self.__recursive_iterate(self.sections)
        return self

    def __recursive_iterate(self, sections):
        for section in sections:
            sectionPagePath = section["SECTION_PAGE_PATH"].encode('ascii')
            sectionPagePath = base64.b64encode(
                sectionPagePath).decode('ascii')
            result = requests.request(
                method="GET",
                url="{host}/snippets/vue/catalog?section_id={section_id}&seo_link={seo_link}".format(
                    host=self.environment["host"], section_id=section["ID"], seo_link=sectionPagePath),
                headers=self.environment["headers"]
            )
            isRequestSuccess = result.status_code == 200
            if not isRequestSuccess:
                try:
                    self.errors[section["ID"]] = result.json()
                except:
                    self.errors[section["ID"]] = result.raw
            if "CHILDREN" in section:
                self.__recursive_iterate(section["CHILDREN"])
