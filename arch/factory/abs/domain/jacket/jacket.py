from abc import ABCMeta, abstractmethod

class Jacket:
    __metaclass__ = ABCMeta

    @abstractmethod
    def present(self):
        '''Present method'''