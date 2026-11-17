# Source for the requirement comments below: python06.pdf v2.0,
# printed pp. 14-15. These describe the assignment, not verified compliance.

# Exercise requirements from python06.pdf:
# - alchemy/grimoire/light_spellbook.py will contain:
#   - A function light_spell_allowed_ingredients() that returns a list of
#     allowed ingredients for light magic, let's say "earth", "air",
#     "fire", "water".


def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


#   - A function light_spell_record(spell_name: str, ingredients: str)
#     that returns a string that indicates whether the spell is recorded
#     or rejected. The decision comes from the validation function
#     described below.
def light_spell_record(spell_name: str, ingredients: str) -> str:
    from .light_validator import validate_ingredients

    validation = validate_ingredients(ingredients)
    result = "rejected" if "- INVALID" in validation else "recorded"
    return f"Spell {result}: {spell_name} ({validation})"
