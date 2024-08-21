from ..wear_factory import WearFactory
from domain.hat.man_hat import ManHat
from domain.jacket.man_jacket import ManJacket

class ManWearFactory(WearFactory):
    def create_hat(self):
        return ManHat()

    def create_jacket(self):
        return ManJacket()