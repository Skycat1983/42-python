#!/usr/bin/env python3

from ex0 import FlameFactory, AquaFactory
from ex0.creature_factory import Creature, CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import BattleStrategy
from ex2 import DefensiveStrategy, NormalStrategy, AggressiveStrategy
from ex2.errors import InvalidStrategyError

# def run_strategy(strategy: BattleStrategy) -> None:
#     # TODO: create or receive creatures and call the strategy when valid.
#     pass


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    fighters: list[tuple[Creature, BattleStrategy]] = []

    for factory, strategy in opponents:
        fighters.append((factory.create_base(), strategy))

    print(f"{len(opponents)} opponents involved")
    try:
        for i in range(len(fighters)):
            for j in range(i + 1, len(fighters)):
                left_creature, left_strategy = fighters[i]
                right_creature, right_strategy = fighters[j]

                print("* Battle *")
                print(left_creature.describe())
                print("vs.")
                print(right_creature.describe())
                print("now fight!")
                print(left_strategy.act(left_creature))
                print(right_strategy.act(right_creature))
    except InvalidStrategyError as error:
        print(f"Battle error, aborting tournament: {error}")

    pass


if __name__ == "__main__":
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    healing_factory = HealingCreatureFactory()

    normal_strategy = NormalStrategy()
    aggressive_strategy = AggressiveStrategy()
    defensive_strategy = DefensiveStrategy()
    transforming_factory = TransformCreatureFactory()

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    print("*** Tournament ***")
    battle([
        (flame_factory, normal_strategy),
        (healing_factory, defensive_strategy),
    ])

    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    print("*** Tournament ***")
    battle([
        (flame_factory, aggressive_strategy),
        (healing_factory, defensive_strategy),
    ])

    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    print("*** Tournament ***")
    battle([
        (aqua_factory, normal_strategy),
        (healing_factory, defensive_strategy),
        (transforming_factory, aggressive_strategy),
    ])

    pass
