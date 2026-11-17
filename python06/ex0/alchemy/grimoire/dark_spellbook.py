# Source for the requirement comments below: python06.pdf v2.0,
# printed pp. 14-15. These describe the assignment, not verified compliance.

# Exercise requirements from python06.pdf:
# - Duplicate light_spellbook.py to obtain dark_spellbook.py, and change
#   the function names as well.
# - Let's say that dark magic uses the following ingredients: "bats",
#   "frogs", "arsenic", and "eyeball".
# - ft_kaboom_1.py will secretly access the dark_spellbook.py directly
#   and then try to record a dark spell. This must fail and raise an
#   exception, indicating that your alchemist laboratory has just
#   exploded.

# from .dark_validator import validate_ingredients
from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]

#   - A function light_spell_record(spell_name: str, ingredients: str)
#     that returns a string that indicates whether the spell is recorded
#     or rejected. The decision comes from the validation function
#     described below.


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    validation = validate_ingredients(ingredients)
    result = "rejected" if "- INVALID" in validation else "recorded"
    return f"Spell {result}: {spell_name} ({validation})"


# if __name__ == "__main__":
#     print(validate_ingredients("bats, arsenic and fire"))
#     print(dark_spell_record("test", "bats, arsenic and fire"))
    # print(validate_ingredients(["eyeball", "bats", "frog", "arsenic"]))
