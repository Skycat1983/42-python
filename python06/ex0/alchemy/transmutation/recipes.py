# Exercise requirements from python06.pdf:
# - alchemy/transmutation/recipes.py will contain:
#   - A function lead_to_gold() that returns the string "Recipe
#     transmuting Lead to Gold: brew '[created air]' and '[created
#     strength potion]' mixed with '[created fire]'".
#   - At least one absolute import and one relative import.

import elements as base_elements

from ..elements import create_air
from ..potions import strength_potion


def lead_to_gold() -> str:
    return (
        "Recipe transmuting Lead to Gold: "
        f"brew '{create_air()}' and '{strength_potion()}' "
        f"mixed with '{base_elements.create_fire()}'"
    )
