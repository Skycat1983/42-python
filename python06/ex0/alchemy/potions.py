#!/usr/bin/env python3
#
# Exercise requirements from python06.pdf:
# - alchemy/potions.py will contain:
#   - A function healing_potion() that returns the string
#     "Healing potion brewed with '[created earth element]' and
#     '[created air element]'".
#   - A function strength_potion() that returns the string
#     "Strength potion brewed with '[created fire element]' and
#     '[created water element]'".
#   - Anything else useful to access the four fundamental elements.

import elements

from .elements import create_air, create_earth


def healing_potion() -> str:
    return (
        f"Healing potion brewed with '{create_earth()}' "
        f"and '{create_air()}'"
    )


def strength_potion() -> str:
    return (
        f"Strength potion brewed with '{elements.create_fire()}' "
        f"and '{elements.create_water()}'"
    )
