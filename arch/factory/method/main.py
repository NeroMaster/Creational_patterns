from factory.delivery_factory import DeliveryFactory
from domain.shipment_type import ShipmentType
from domain.delivery.delivery import Delivery


def main():
    factory = DeliveryFactory.get_instance()
    land_delivery: Delivery = factory.create_delivery(ShipmentType.LAND)
    air_delivery: Delivery = factory.create_delivery(ShipmentType.AIR)

    land_delivery.deliver()
    air_delivery.deliver()

if __name__ == "__main__":
    main()
