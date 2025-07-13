import urllib.request
from abc import abstractmethod


class Resource:
    @abstractmethod
    def load(sefl, url):
        pass


class RealResource(Resource):
    def load(self, url):
        with urllib.request.urlopen(url) as response:
            data = response.read()  # Читаем всё как байты

        return data


class ProxyResource(Resource):
    def __init__(self):
        self.resource = None

    def load(self, url):
        if not self.resource:
            self.resource = RealResource()
        return self.resource.load(url)
