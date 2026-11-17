#!/usr/bin/env python3
from abc import ABC, abstractmethod


# Your ex0 package cannot expose concrete Creature directly, it must only
# expose factories.

# A concrete class means a real, instantiable class (not abstract).


class Creature(ABC):
    def __init__(self) -> None:
        self._name: str = ""
        self._type: str = ""

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self._name} is a {self._type} type Creature"


class Flameling(Creature):
    def attack(self) -> str:
        weapon = "Ember"
        return f"{self._name} uses {weapon}!"


class Pyrodon(Creature):
    def attack(self) -> str:
        weapon = "Flamethrower"
        return f"{self._name} uses {weapon}!"


class Aquabub(Creature):
    def attack(self) -> str:
        weapon = "Water Gun"
        return f"{self._name} uses {weapon}!"


class Torragon(Creature):
    def attack(self) -> str:
        weapon = "Hydro Pump"
        return f"{self._name} uses {weapon}!"


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self) -> Flameling:
        creature = Flameling()
        creature._name = "Flameling"
        creature._type = "Fire"
        return creature

    def create_evolved(self) -> Pyrodon:
        creature = Pyrodon()
        creature._name = "Pyrodon"
        creature._type = "Fire/Flying"
        return creature


class AquaFactory(CreatureFactory):
    def create_base(self) -> Aquabub:
        creature = Aquabub()
        creature._name = "Aquabub"
        creature._type = "Water"
        return creature

    def create_evolved(self) -> Torragon:
        creature = Torragon()
        creature._name = "Torragon"
        creature._type = "Water"
        return creature
