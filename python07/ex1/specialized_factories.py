#!/usr/bin/env python3

from ex0 import CreatureFactory

from .creatures import Bloomelle, Morphagon, Shiftling, Sproutling


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Sproutling:
        creature = Sproutling()
        creature._name = "Sproutling"
        creature._type = "Grass"
        return creature

    def create_evolved(self) -> Bloomelle:
        creature = Bloomelle()
        creature._name = "Bloomelle"
        creature._type = "Grass/Fairy"
        return creature


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Shiftling:
        creature = Shiftling()
        creature._name = "Shiftling"
        creature._type = "Normal"
        return creature

    def create_evolved(self) -> Morphagon:
        creature = Morphagon()
        creature._name = "Morphagon"
        creature._type = "Normal/Dragon"
        return creature
