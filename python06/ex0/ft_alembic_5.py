#!/usr/bin/env python3
# Source for the requirement comments below: python06.pdf v2.0,
# printed pp. 7-9. These describe the assignment, not verified compliance.

#
# Exercise requirements from python06.pdf:
# - ft_alembic_5.py will use the from alchemy import ... structure to
#   access the alchemy module and then create air.

from alchemy import create_air


if __name__ == "__main__":
    print("=== Alembic 5 ===")
    print("Accessing the alchemy module using 'from alchemy import ...'")
    print(f"Testing create_air: {create_air()}")
