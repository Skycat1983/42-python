#!/usr/bin/env python3


from ex0 import FlameFactory
from ex0 import AquaFactory
from ex0 import CreatureFactory


def test_creation(factory: CreatureFactory) -> None:
    print("Testing factory")
    base = factory.create_base()
    evolved = factory.create_evolved()
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def test_fight(f: FlameFactory, a: AquaFactory) -> None:
    print("Testing battle")
    f_base = f.create_base()
    a_base = a.create_base()
    left = f_base.describe()
    right = a_base.describe()
    print(f"{left} vs {right}")
    print("Fight")
    print(f_base.attack())
    print(a_base.attack())


if __name__ == "__main__":
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    test_creation(flame_factory)
    test_creation(aqua_factory)
    test_fight(flame_factory, aqua_factory)
    pass
