from domain.hat.hat import Hat
from domain.jacket.jacket import Jacket
from factory.wear_factory import WearFactory

class Store:
    _hat: Hat
    _jacket: Jacket

    def __init__(self, factory: WearFactory) -> None:
        self._hat = factory.create_hat()
        self._jacket = factory.create_jacket()

    def present(self):
        print("Store assortment presentation!\n")
        self._hat.present()
        self._jacket.present()