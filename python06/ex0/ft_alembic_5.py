#!/usr/bin/env python3
#
# Exercise requirements from python06.pdf:
# - ft_alembic_5.py will use the from alchemy import ... structure to
#   access the alchemy module and then create air.

from alchemy import create_air


if __name__ == "__main__":
    print("=== Alembic 5 ===")
    print("Accessing the alchemy module using 'from alchemy import ...'")
    print(f"Testing create_air: {create_air()}")
