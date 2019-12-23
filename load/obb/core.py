from abc import ABC, abstractmethod


class AbstractHttpRequestBehaviour(ABC):

    def __init__(self, index):
        self.index = index

    @abstractmethod
    def url(self):
        pass

    def method(self):
        return 'GET'

    @abstractmethod
    def headers(self):
        pass

    @abstractmethod
    def data(self):
        pass