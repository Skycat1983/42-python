#!/usr/bin/env python3
# Core assignment requirements (summary, not a compliance claim).
# Source: python10.pdf v3.2, printed pp. 21-23.
# spell_timer preserves metadata with wraps, reports the function name
# and elapsed seconds to three decimals, and returns the original result.
# power_validator(min_power) wraps standalone functions and the guild method,
# allowing power >= the threshold and otherwise returning
# "Insufficient power for this spell". retry_spell retries exceptions within
# max_attempts, reports retries, returns a successful result, or reports
# exhaustion. MageGuild.validate_mage_name is static and accepts names of
# at least three characters containing only letters/spaces. cast_spell uses
# power_validator(10) and returns a success message with spell and power.
#
# Module rules: Python 3.10+, flake8, type hints; no globals, file I/O, external
# packages, eval, or exec. Keep processing focused on functional patterns.


from collections.abc import Callable
from functools import wraps
from typing import Any
import time


# * ALL decorators return a decorator. wraps keeps naming intact
# * A decorator accepts a callable and returns a replacement callable,
# * adding reusable behavior around the original function or method.

# ?• Print "Casting function_name..." before calling the function
# ?• Measure execution and print completion time to 3 decimal places
# ?• Preserve metadata with functools.wraps and return the original result
def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    # * args = tuple (positional), kwargs = dictionary (keywords)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # performance counter. it's monotonic (never goes backwardss)
        print(f"Casting {func.__name__}...")
        # ? adding timing as separate to core job of func
        start = time.perf_counter()

        result = func(*args, **kwargs)
        # print(result)

        elapsed = time.perf_counter() - start
        print(f"Spell completed in {elapsed:.3f} seconds")

        return result

    return wrapper

# ================================================================
#
# !DECORATION TIME                        CALL TIME

# Python reads the function               Code calls fireball()
#           │                                      │
#           ▼                                      ▼
# Passes it to spell_timer                 wrapper() executes
#           │                                      │
#           ▼                                      ▼
# Receives wrapper                         wrapper calls original function
#           │                                      │
#           ▼                                      ▼
# Stores wrapper as fireball               wrapper returns final result
#
# ================================================================


# ?• Create a decorator factory that validates power >= min_power
# ?• Run the wrapped function when valid; otherwise return the required message
# ?• Preserve the wrapped function's metadata with functools.wraps
# ! decorator factory
# * needs extra layer because it receives config first
def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if "power" in kwargs:
                power = kwargs["power"]
            elif args:
                # ? Q: why -1?
                # ! A: python supplies 'self'
                # * validator works both as standalone func + instance method
                power = args[-1]
            else:
                raise TypeError("Missing power argument")
            if not isinstance(power, int):
                raise TypeError("Power must be an integer")
            if power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)

        return wrapper

    return decorator


# ?• Retry a function that raises, up to max_attempts total attempts
# ?• Print the required retry message after each retryable failure
# ?• Return the required failure message if every attempt fails
def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        # ! preserve metadata for func
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            "Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                        )
            return (
                "Spell casting failed after "
                f"{max_attempts} attempts"
            )

        return wrapper

    return decorator


# ?• Demonstrate a static validation method and a decorated instance method
class MageGuild:
    # ?• A valid name has at least 3 characters and only letters or spaces
    # ?• Use staticmethod because validation does not require instance state
    # * @staticmethod prevents Python from injecting `self`
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return (
            len(name) >= 3
            and all(
                character.isalpha() or character == " "
                for character in name
            )
        )

    # ?• Apply power_validator with min_power=10 to this instance method
    # ?• On success, report the spell name and supplied power
    # ?• Let the decorator return its insufficient-power message on failure
    @power_validator(min_power=10)  # ! invoked before runtime
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"

    # guild.cast_spell("Lightning", 15)
    #         │
    #         ▼
    # wrapper(guild, "Lightning", 15)
    #         │
    #         ├── validate 15
    #         ├── call original cast_spell(
    #         │       guild, "Lightning", 15
    #         │   )
    #         └── return the result


if __name__ == "__main__":
    print("Testing spell timer...")

    # * take the function 'fireball' and pass it to 'spell_timer'
    # * use whatever spell_timer returns as the new fireball (wrapper)
    @spell_timer
    def fireball() -> str:
        time.sleep(0.1)
        return "Fireball cast!"

    # * equivalent to:
    # def fireball() -> str:
    #   return "Fireball cast!"
    # fireball = spell_timer(fireball)

    # ! flow:
    # original fireball
    #        │
    #        ▼
    # spell_timer(original fireball)
    #        │
    #        ▼
    # returns wrapper
    #        │
    #        ▼
    # name "fireball" now refers to wrapper

    # calling 'wrapper'
    print("Result:", fireball())

    print("\nTesting power validator...")

    @power_validator(min_power=10)
    def standalone_spell(spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"

    # * equivalent to:
    # decorator = power_validator(min_power=10)
    # standalone_spell = decorator(standalone_spell)

    print(standalone_spell("Fireball", 15))
    print(standalone_spell("Fireball", 5))

    # * exammple
    # standalone_spell("Fireball", 15)
    # wrapper("Fireball", 15)
    #     │
    #     ├── args = ("Fireball", 15)
    #     ├── power = args[-1] = 15
    #     ├── 15 >= 10, so validation passes
    #     ├── call original standalone_spell("Fireball", 15)
    #     └── return the original function's result

    print("\nTesting retrying spell...")

    # 1. before run time python invokes retry_spell, passing in max_attempts
    # * decoration time
    # 2. returns decorator, which receives 'unstable_spell()'
    # ! invocation
    @retry_spell(max_attempts=3)
    def unstable_spell() -> str:
        raise RuntimeError("The spell failed")

    print(unstable_spell())

    @retry_spell(max_attempts=3)
    def stable_spell() -> str:
        return "success"

    print("\nTesting retrying spell again...")

    print(stable_spell())

    print("\nTesting MageGuild...")
    guild = MageGuild()
    print(guild.validate_mage_name("Merlin"))
    print(guild.validate_mage_name("Al"))
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))
