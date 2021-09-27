import requests


class BaseEnvironment:
    filename = None
    environment = None

    def __init__(self, filename):
        self.filename = filename
        self.environment = self.read()
        self.set_token(self.get_token(), True)

    def read(self):
        return None

    def get(self):
        return self.environment

    def set(self, environment):
        self.environment = environment
        return self

    def get_token(self):
        return requests.request(
            method="POST", url=self.environment["host"] + "/oauth/token", headers=self.environment["headers"], data={
                "grant_type": "client_credentials",
                "client_id": self.environment["client_id"],
                "client_secret": self.environment["client_secret"],
            }).json()

    def set_token(self, result, error=False):
        try:
            token = result["result"]
            self.environment["access_token"] = token["access_token"]
            self.environment["refresh_token"] = token["refresh_token"]
            self.environment["headers"] = {"Authorization": "Bearer {access_token}".format(
                access_token=token["access_token"])}
        except:
            if error:
                raise Exception('Не удалось получить токен')
        return self

    def write(self):
        return self
