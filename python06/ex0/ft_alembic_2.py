#!/usr/bin/env python3
# Source for the requirement comments below: python06.pdf v2.0,
# printed pp. 7-9. These describe the assignment, not verified compliance.

#
# Exercise requirements from python06.pdf:
# - ft_alembic_2.py will use the import ... structure to access
#   alchemy/elements.py directly and then create earth.

import alchemy.elements


if __name__ == "__main__":
    print("=== Alembic 2 ===")
    print("Accessing alchemy/elements.py using 'import ...' structure")
    print(f"Testing create_earth: {alchemy.elements.create_earth()}")
