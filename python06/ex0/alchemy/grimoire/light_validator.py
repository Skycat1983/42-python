# Source for the requirement comments below: python06.pdf v2.0,
# printed pp. 14-15. These describe the assignment, not verified compliance.

# Exercise requirements from python06.pdf:
# - alchemy/grimoire/light_validator.py will contain:
#   - A function validate_ingredients(ingredients: str) that returns a
#     string with the ingredients and the "VALID" or "INVALID" keyword.
#     The ingredients are valid if they include at least one of the
#     allowed ingredients from the spellbook (case insensitive).

from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = light_spell_allowed_ingredients()
    lower_ingredients = ingredients.lower()
    validity = "INVALID"

    if any(ingredient.lower() in lower_ingredients for ingredient in allowed):
        validity = "VALID"

    return f"{ingredients} - {validity}"


# if __name__ == "__main__":
#     print(validate_ingredients("Earth, wind and fire"))
