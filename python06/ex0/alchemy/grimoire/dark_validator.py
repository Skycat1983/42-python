# Exercise requirements from python06.pdf:
# - Duplicate light_validator.py to obtain dark_validator.py, and change
#   the function names as well.
# - Let's say that dark magic uses the following ingredients: "bats",
#   "frogs", "arsenic", and "eyeball".
# - dark magic is dangerous and explodes because of circular
#   dependencies.

from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    lower_ingredients = ingredients.lower()
    validity = "INVALID"

    if any(ingredient.lower() in lower_ingredients for ingredient in allowed):
        validity = "VALID"

    return f"{ingredients} - {validity}"
