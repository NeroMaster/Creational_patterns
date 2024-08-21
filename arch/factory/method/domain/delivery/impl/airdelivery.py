from ..delivery import Delivery
from ...postman.impl.airpostman import AirPostman

class AirDelivery(Delivery):
    def _create_postman(self):
        return AirPostman()


