#!/usr/bin/env python3
#
# Exercise requirements from python06.pdf:
# - ft_alembic_0.py will use the import ... structure to access
#   elements.py directly and then create fire.

import elements


if __name__ == "__main__":
    print("=== Alembic 0 ===")
    print("Using: 'import ...' structure to access elements.py")
    print(f"Testing create_fire: {elements.create_fire()}")
