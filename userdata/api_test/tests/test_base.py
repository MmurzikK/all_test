import json
import allure
import requests
from urllib.parse import unquote


class TestBase:
    environment_adapter = None
    environment = None
    variables = None
    response = None
    errors = None
    faker = None
    path = None

    def __init__(self, environment_adapter, faker):
        self.environment_adapter = environment_adapter
        self.environment = environment_adapter.get()
        self.faker = faker
        self.init_variables()

    def request(self):
        self.response = requests.request(
            method="GET", url=self.environment["host"] + self.path, headers=self.environment["headers"])
        return self

    def get_errors(self):
        return self.errors

    def get_json(self):
        return self.response.json()

    def get_json_result(self):
        return self.get_json()["result"]

    def init_variables(self):
        self.variables = self.environment["variables"]
        if not self.variables:
            self.variables = {}
        key = self.__class__.__name__
        if key not in self.variables:
            self.variables[key] = {}
        return self

    def set_variables(self, variables):
        for variable in variables:
            self.variables[self.__class__.__name__][list(variable.keys()).pop()] = list(
                variable.values()).pop()
        self.environment["variables"] = self.variables
        return self

    def assert_set_variables(self):
        return self

    def print_json_response(self):
        print(self.response.json())

    def test(self):
        assert self.response.status_code == 200
        return self

    def attach(self):
        allure.attach(unquote(self.response.request.url), "Request url",
                      allure.attachment_type.TEXT)
        allure.attach(self.response.request.method,
                      "Request method", allure.attachment_type.TEXT)
        requestHeaders = self.response.request.headers
        if requestHeaders:
            allure.attach(json.dumps(dict(requestHeaders), indent=4,
                          ensure_ascii=False), "Request headers", allure.attachment_type.JSON)
        responseHeaders = self.response.headers
        if responseHeaders:
            allure.attach(json.dumps(dict(responseHeaders), indent=4,
                                     ensure_ascii=False), "Response headers", allure.attachment_type.JSON)
        responseJson = self.get_json()
        if responseJson:
            allure.attach(json.dumps(responseJson, indent=4,
                                     ensure_ascii=False), "Response", allure.attachment_type.JSON)
        if self.response.request.body:
            allure.attach(unquote(self.response.request.body), "Body")
        return self

    def rewrite_token(self):
        self.environment_adapter.set_token(self.get_json())
        return self

    def rewrite_environment(self):
        self.environment_adapter.set(self.environment).write()
        return self
