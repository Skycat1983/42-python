#!/usr/bin/env python3
# Source for the requirement comments below: python06.pdf v2.0,
# printed pp. 10-11. These describe the assignment, not verified compliance.

#
# Exercise requirements from python06.pdf:
# - ft_distillation_0.py will use the from ... import ... structure to
#   access alchemy/potions.py directly and then brew both healing and
#   strength potions.

from alchemy.potions import healing_potion, strength_potion

if __name__ == "__main__":
    print("=== Distillation 0 ===")
    print("Direct access to alchemy/potions.py")
    print(f"Testing strength_potion: {strength_potion()}")
    print(f"Testing healing_potion: {healing_potion()}")
