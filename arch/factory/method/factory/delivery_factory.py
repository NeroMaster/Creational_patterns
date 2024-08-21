from domain.shipment_type import ShipmentType
from domain.delivery.impl.airdelivery import AirDelivery
from domain.delivery.impl.landdelivery import LandDelivery

class DeliveryFactory:
    _instance = None

    def __init__(self) -> None:
        pass

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = cls()
        return cls._instance

    def create_delivery(self, type: ShipmentType):
        if type == ShipmentType.LAND:
            return LandDelivery()
        if type == ShipmentType.AIR:
            return AirDelivery()

