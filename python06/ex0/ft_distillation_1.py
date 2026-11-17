#!/usr/bin/env python3
# Source for the requirement comments below: python06.pdf v2.0,
# printed pp. 10-11. These describe the assignment, not verified compliance.

#
# Exercise requirements from python06.pdf:
# - ft_distillation_1.py will use the import alchemy structure to access
#   the alchemy module, then brew the original strength potion and the
#   special heal() potion, which is a package alias of the healing potion.
# - You will need to improve your __init__.py.

import alchemy

if __name__ == "__main__":
    print("=== Distillation 1 ===")
    print("Using: 'import alchemy' structure to access potions")
    print(f"Testing strength_potion: {alchemy.strength_potion()}")
    print(f"Testing heal alias: {alchemy.heal()}")
