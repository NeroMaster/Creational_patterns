from ..wear_factory import WearFactory
from domain.hat.woman_hat import WomanHat
from domain.jacket.woman_jacket import WomanJacket

class WomanWearFactory(WearFactory):
    def create_hat(self):
        return WomanHat()

    def create_jacket(self):
        return WomanJacket()