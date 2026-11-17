#!/usr/bin/env python3

from ex0.creature_factory import Creature

from .capabilities import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):
    def attack(self) -> str:
        weapon = "Vine Whip"
        return f"{self._name} uses {weapon}!"

    def heal(self) -> str:
        return f"{self._name} heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    def attack(self) -> str:
        weapon = "Petal Dance"
        return f"{self._name} uses {weapon}!"

    def heal(self, target: str = "") -> str:
        if target:
            return (
                f"{self._name} heals itself and {target} "
                "for a large amount"
            )
        return f"{self._name} heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__()
        self._transformed = False

    def attack(self) -> str:
        if self._transformed:
            action = "performs a boosted strike!"
        else:
            action = "attacks normally."
        return f"{self._name} {action}"

    def transform(self) -> str:
        if not self._transformed:
            self._transformed = True
            return f"{self._name} shifts into a sharper form!"
        return f"{self._name} is already transformed."

    def revert(self) -> str:
        if self._transformed:
            self._transformed = False
            return f"{self._name} returns to normal."
        return f"{self._name} is already normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__()
        self._transformed = False

    def attack(self) -> str:
        if self._transformed:
            action = "unleashes a devastating morph strike!"
        else:
            action = "attacks normally."
        return f"{self._name} {action}"

    def transform(self) -> str:
        if not self._transformed:
            self._transformed = True
            return f"{self._name} morphs into a dragonic battle form!"
        return f"{self._name} is already transformed."

    def revert(self) -> str:
        if self._transformed:
            self._transformed = False
            return f"{self._name} stabilizes its form."
        return f"{self._name} is already normal."
