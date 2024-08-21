from abc import ABCMeta, abstractmethod
from ..postman.postman import Postman

class Delivery:
    __metaclass__ = ABCMeta

    def _create_postman(self):
        pass

    def deliver(self):
        postman: Postman = self._create_postman()
        postman.deliver()

