#!/usr/bin/env python3
# Source for the requirement comments below: python06.pdf v2.0,
# printed pp. 7-13. These describe the assignment, not verified compliance.

#
# Exercise requirements from python06.pdf:
# - alchemy/__init__.py will contain:
#   - Anything useful to partially import the alchemy module.
#     See ft_alembic_4.py.
# - ft_distillation_1.py will use the import alchemy structure to access
#   the alchemy module, then brew the original strength potion and the
#   special heal() potion, which is a package alias of the healing potion.
#   You will need to improve your __init__.py.
# - ft_transmutation_2.py will use the import ... structure to import
#   the module alchemy directly and then achieve transformation of lead
#   into gold.

from .elements import create_air
from .transmutation import lead_to_gold
from .potions import strength_potion, healing_potion as heal

__all__ = ["create_air", "heal", "strength_potion", "lead_to_gold"]
