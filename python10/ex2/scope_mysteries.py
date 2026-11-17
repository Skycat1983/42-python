#!/usr/bin/env python3
# Core assignment requirements (summary, not a compliance claim).
# Source: python10.pdf v3.2, printed pp. 15-17.
# Use closures, not globals, for persistent private state. mage_counter
# starts at one and separate counters remain independent. spell_accumulator
# adds each amount to its initial power and returns the running total.
# enchantment_factory returns a function producing "enchantment_type item".
# memory_vault returns store(key, value) and recall(key) callables sharing
# private storage; an absent key returns "Memory not found".
#
# Module rules: Python 3.10+, flake8, type hints; no globals, file I/O, external
# packages, eval, or exec. Keep processing focused on functional patterns.

from collections.abc import Callable
from typing import Any


# ! Python resolves names using Local -> Enclosing -> Global -> Built-ins.
# ! A closure is a returned inner function that remembers its enclosing values.

# • Return a closure that counts how many times it has been called
# • Start at 1 and preserve the count between calls
# • Keep separately created counters independent; do not use globals
def mage_counter() -> Callable:
    count = 0

    def increment() -> int:
        # nonlocal = look one level outward, but not all the way to global.
        nonlocal count
        count += 1
        return count

    return increment


# • Return a closure whose total starts at initial_power
# • Add the amount supplied on each call and return the new total
def spell_accumulator(initial_power: int) -> Callable:
    power = initial_power

    def accumulate(gains: int) -> int:
        nonlocal power
        power += gains
        return power

    return accumulate


# • Return a function that captures the specified enchantment type
# • Accept an item name and return "enchantment_type item_name"
def enchantment_factory(enchantment_type: str) -> Callable:
    e_type = enchantment_type

    def enchant(item_name: str) -> str:
        return f"{e_type} {item_name}"

    return enchant


# • Return a dictionary containing "store" and "recall" functions
# • Keep stored key/value memories private in a shared closure
# • Return "Memory not found" when recall receives an unknown key
def memory_vault() -> dict[str, Callable]:
    memories: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        memories[key] = value

    def recall(key: str) -> Any:
        return memories.get(key, "Memory not found")

    return {
        "store": store,
        "recall": recall,
    }


if __name__ == "__main__":
    print("Testing mage counter...")
    counter = mage_counter()
    print("mage_counter first call:", counter())
    print("mage_counter second call:", counter())
    print("mage_counter third call:", counter())

    second_counter = mage_counter()
    print("second mage_counter first call:", second_counter())

    print("\nTesting spell accumulator...")
    accumulator = spell_accumulator(10)
    print("spell_accumulator starts at 10, gain 5:", accumulator(5))
    print("spell_accumulator gain 20:", accumulator(20))
    print("spell_accumulator gain -3:", accumulator(-3))

    print("\nTesting enchantment factory...")
    fire_enchant = enchantment_factory("Fire")
    frost_enchant = enchantment_factory("Frost")
    print("fire enchant sword:", fire_enchant("Sword"))
    print("fire enchant shield:", fire_enchant("Shield"))
    print("frost enchant staff:", frost_enchant("Staff"))

    print("\nTesting memory vault...")
    vault = memory_vault()
    vault["store"]("secret", "42")
    print("recall secret:", vault["recall"]("secret"))
    print("recall missing:", vault["recall"]("castle"))
