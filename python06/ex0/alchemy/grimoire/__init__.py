# Exercise requirements from python06.pdf:
# - ft_kaboom_0.py will access the grimoire module directly and then
#   record a light spell, flawlessly.
# - There are multiple ways to avoid circular dependencies; you pick one.
#   Be prepared to explain the different approaches during the evaluation.

from .light_spellbook import (
    light_spell_allowed_ingredients,
    light_spell_record,
)
from .light_validator import validate_ingredients

__all__ = [
    "validate_ingredients",
    "light_spell_allowed_ingredients",
    "light_spell_record",
]
