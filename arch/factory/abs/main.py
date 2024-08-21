from domain.weartype import WearType
from factory.wear_factory import WearFactory
from factory.impl.man_wear_factory import ManWearFactory
from factory.impl.woman_wear_factory import WomanWearFactory
from store import Store

def configure_store(type: WearType):
    factory: WearFactory
    if type == WearType.MAN:
        factory = ManWearFactory()
        return Store(factory)
    if type == WearType.WOMAN:
        factory = WomanWearFactory()
        return Store(factory)

def main():
    woman_wear_store = configure_store(WearType.WOMAN)
    man_wear_store = configure_store(WearType.MAN)

    woman_wear_store.present()
    man_wear_store.present()

if __name__ == "__main__":
    main()

