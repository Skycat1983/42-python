#!/usr/bin/env python3
# Source for the requirement comments below: python06.pdf v2.0,
# printed pp. 7-9. These describe the assignment, not verified compliance.

#
# Exercise requirements from python06.pdf:
# - ft_alembic_3.py will use the from ... import ... structure to access
#   alchemy/elements.py directly and then create air.

from alchemy.elements import create_air


if __name__ == "__main__":
    print("=== Alembic 3 ===")
    print(
        "Accessing alchemy/elements.py using "
        "'from ... import ...' structure"
    )
    print(f"Testing create_air: {create_air()}")
