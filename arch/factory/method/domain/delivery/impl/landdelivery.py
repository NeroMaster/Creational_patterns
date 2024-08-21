from ..delivery import Delivery
from ...postman.impl.landpostman import LandPostman

class LandDelivery(Delivery):
    def _create_postman(self):
        return LandPostman()