#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import cast

from ex0.creature_factory import Creature
from ex1 import HealCapability, TransformCapability
from ex2.errors import InvalidStrategyError


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> str:
        pass


class NormalStrategy(BattleStrategy):
    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise InvalidStrategyError("NormalStrategy requires a creature")
        return creature.attack()

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature._name}' "
                "for this aggressive strategy"
            )

        transformed_creature = cast(TransformCapability, creature)
        return (
            f"{transformed_creature.transform()}\n"
            f"{creature.attack()}\n"
            f"{transformed_creature.revert()}"
        )


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature._name}' "
                "for this defensive strategy"
            )

        healing_creature = cast(HealCapability, creature)
        return f"{creature.attack()}\n{healing_creature.heal()}"
