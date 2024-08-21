from abc import ABCMeta, abstractmethod

class Hat:
    __metaclass__ = ABCMeta

    @abstractmethod
    def present(self):
        '''Present method'''