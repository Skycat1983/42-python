#!/usr/bin/env python3

from collections.abc import Callable

# ! A higher-order function accepts a function, returns a function, or both.
# functions are first-class objects, meaning they can be:
# - assigned to variables
# - passed as arguments
# - returned
# - stored in lists/dictionaries
# -... called later.

# *
#   lambda is a way to make a function.
#   Callable is a way to type a function.


def poison(target: str, power: int) -> str:
    return f"Poison weakens {target} for {power} damage"


def frost(target: str, power: int) -> str:
    return f"Frost chills {target} for {power} damage"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fire(target: str, power: int) -> str:
    return f"Fire damages {target} for {power} damage"


# !Callable[[argument type 1, argument type 2], return type]
# • Return a new function that calls both spells with the same arguments
# • Return a tuple containing both spell results
def spell_combiner(
    spell1: Callable[[str, int], str], spell2: Callable[[str, int], str]
) -> Callable[[str, int], tuple[str, str]]:
    def combined(target: str, power: int) -> tuple[str, str]:
        return spell1(target, power), spell2(target, power)

    return combined


# • Return a new function with the same signature as the base spell
# • Multiply the supplied power before passing it to the base spell
def power_amplifier(
    base_spell: Callable[[str, int], str], multiplier: int
) -> Callable[[str, int], str]:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)

    return amplified


# • Return a new function that casts only when condition returns True
# • Pass the same arguments to both condition and spell
# • Return "Spell fizzled" when the condition fails
def conditional_caster(
    condition: Callable[[str, int], bool], spell: Callable[[str, int], str]
) -> Callable[[str, int], str]:
    def conditional(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"

    return conditional


# • Return a function that casts every spell in the supplied order
# • Pass the same arguments to every spell
# • Return a list containing all spell results
def spell_sequence(spells: list[Callable]) -> Callable:
    def cast_all(target: str, power: int) -> list[str]:
        results: list[str] = []

        for spell in spells:
            result = spell(target, power)
            results.append(result)

        return results

    return cast_all


if __name__ == "__main__":
    target = "Dragon"

    print("Testing spell combiner...")
    combined = spell_combiner(heal, fire)
    print(combined(target, 10))

    print("\nTesting power amplifier...")
    amplified = power_amplifier(heal, 3)
    print(amplified(target, 3))

    def is_strong_enough(target: str, power: int) -> bool:
        return power >= 10

    conditional_fire = conditional_caster(is_strong_enough, fire)

    print("\nTesting conditional caster...")
    print(conditional_fire(target, 10))
    print(conditional_fire(target, 5))

    print("\nTesting spell sequence...")
    sequential_spells = spell_sequence([heal, fire, poison, frost])
    print(sequential_spells(target, 10))

    pass
