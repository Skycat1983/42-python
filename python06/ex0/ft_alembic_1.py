#!/usr/bin/env python3
# Source for the requirement comments below: python06.pdf v2.0,
# printed pp. 7-9. These describe the assignment, not verified compliance.

#
# Exercise requirements from python06.pdf:
# - ft_alembic_1.py will use the from ... import ... structure to access
#   elements.py directly and then create water.

from elements import create_water


if __name__ == "__main__":
    print("=== Alembic 1 ===")
    print("Using: 'from ... import ...' structure to access elements.py")
    print(f"Testing create_water: {create_water()}")
