#!/usr/bin/env python3

from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_healing_factory(factory: HealingCreatureFactory) -> None:
    print("Testing creature with healing capability")
    base = factory.create_base()
    evolved = factory.create_evolved()
    description = base.describe()
    attack = base.attack()
    action = base.heal()
    print(description)
    print(attack)
    print(action)
    description = evolved.describe()
    attack = evolved.attack()
    action = evolved.heal("others")
    print(description)
    print(attack)
    print(action)
    pass


def test_transform_factory(factory: TransformCreatureFactory) -> None:
    print("Testing creature with transform capability")
    base = factory.create_base()
    evolved = factory.create_evolved()
    description = base.describe()
    print(description)
    attack = base.attack()
    print(attack)
    action = base.transform()
    print(action)
    attack = base.attack()
    print(attack)
    revert = base.revert()
    print(revert)
    description = evolved.describe()
    print(description)
    attack = evolved.attack()
    print(attack)
    action = evolved.transform()
    print(action)
    attack = evolved.attack()
    print(attack)
    revert = evolved.revert()
    print(revert)


if __name__ == "__main__":
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()
    test_healing_factory(healing_factory)
    test_transform_factory(transform_factory)
    sproutling = healing_factory.create_base()
    bloomelle = healing_factory.create_evolved()
    sproutling.describe()
    sproutling.attack()
    sproutling.heal()
    bloomelle.describe()
    bloomelle.attack()
    bloomelle.heal()
