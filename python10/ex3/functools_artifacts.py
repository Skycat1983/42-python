#!/usr/bin/env python3
# Core assignment requirements (summary, not a compliance claim).
# Source: python10.pdf v3.2, printed pp. 18-20.
# spell_reducer uses reduce and operator helpers for add/multiply/max/min,
# returns zero for empty input, and handles unknown operations.
# partial_enchanter uses partial to make three specialized enchantments
# with power=50 and preset elements. memoized_fibonacci uses lru_cache to
# compute Fibonacci numbers and reuse results. spell_dispatcher returns
# a singledispatch function handling int, str, list, and unknown types.
#
# Module rules: Python 3.10+, flake8, type hints; no globals, file I/O, external
# packages, eval, or exec. Keep processing focused on functional patterns.

from collections.abc import Callable
from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from typing import Any


# ! functools provides standard tools for reduction, partial application,
# ! memoization, and type-based dispatch.

# • Use functools.reduce to combine all spell powers
# • Support "add", "multiply", "max", and "min"
# • Use operator-module functions such as add and mul where appropriate
# • Return 0 for an empty list and handle unknown operations properly
def spell_reducer(spells: list[int], operation: str) -> int:
    operations: dict[str, Callable[[int, int], int]] = {
        "add": add,
        "multiply": mul,
        "max": lambda left, right: left if left >= right else right,
        "min": lambda left, right: left if left <= right else right,
    }
    if operation not in operations:
        raise ValueError("Unknown operation")
    if not spells:
        return 0
    operation_fn = operations[operation]
    return reduce(operation_fn, spells)


# • Accept a base function with signature (power, element, target) -> str
# • Use functools.partial to return three specialized functions
# • Pre-fill power=50 and an element in each specialized version
def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "fire": partial(base_enchantment, 50, "fire"),
        "ice": partial(base_enchantment, 50, "ice"),
        "lightning": partial(base_enchantment, 50, "lightning"),
    }


# • Use functools.lru_cache to memoize Fibonacci calculations
# • Return the nth Fibonacci number and expose cache_info() for verification
# ! lru_cache stores results by arguments so repeated calls reuse
# ! cached values.
@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


# • Use functools.singledispatch and return the resulting dispatcher
# • Register int damage, str enchantment, and list multi-cast handlers
# • Let the base Any handler process unknown spell types
# ! singledispatch selects an implementation from the first
# ! argument's runtime type.
def spell_dispatcher() -> Callable[[Any], str]:
    # exception
    @singledispatch
    def spell(value: Any) -> str:
        return "Unknown spell type"

    # enchantment
    @spell.register
    def _(value: str) -> str:
        return f"Enchantment: {value}"

    # damage
    @spell.register
    def _(value: int) -> str:
        return f"Damage spell: {value} damage"

    # multi cast
    @spell.register(list)
    def _(value: list[str]) -> str:
        return f"Multi-cast: {len(value)} spells"

    return spell


if __name__ == "__main__":
    spell_powers = [10, 20, 30, 40]

    print("Testing spell reducer...")
    print("Sum:", spell_reducer(spell_powers, "add"))
    print("Product:", spell_reducer(spell_powers, "multiply"))
    print("Max:", spell_reducer(spell_powers, "max"))
    print("Min:", spell_reducer(spell_powers, "min"))
    print("Empty:", spell_reducer([], "add"))
    try:
        print("Unknown operation:", spell_reducer(spell_powers, "divide"))
    except ValueError as error:
        print("Unknown operation error:", error)

    print("\nTesting partial enchanter...")

    def base_enchantment(power: int, element: str, target: str) -> str:
        return f"{element} enchantment empowers {target} with {power} power"

    enchantments = partial_enchanter(base_enchantment)
    # print("Created enchantments:", enchantments)
    if isinstance(enchantments, dict):
        for name, enchantment in enchantments.items():
            print(f"{name}:", enchantment("Sword"))

    print("\nTesting memoized fibonacci...")
    print("Fib(0):", memoized_fibonacci(0))
    print("Fib(1):", memoized_fibonacci(1))
    print("Fib(10):", memoized_fibonacci(10))
    print("Fib(15):", memoized_fibonacci(15))

# ! @lru_cache adds cache_info(); hasattr safely checks that it
# ! exists before calling it.
    if hasattr(memoized_fibonacci, "cache_info"):
        print("Cache info:", memoized_fibonacci.cache_info())

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    if callable(dispatcher):
        print(dispatcher(42))
        print(dispatcher("fireball"))
        print(dispatcher(["fire", "ice", "heal"]))
        print(dispatcher({"spell": "mystery"}))
