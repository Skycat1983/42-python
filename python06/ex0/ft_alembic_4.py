#!/usr/bin/env python3
# Source for the requirement comments below: python06.pdf v2.0,
# printed pp. 7-9. These describe the assignment, not verified compliance.

#
# Exercise requirements from python06.pdf:
# - ft_alembic_4.py will use import alchemy to access the alchemy module
#   and then create air.
# - The create_earth() function will not be exposed through the module
#   interface and raise an exception when called. You can catch the
#   exception or not; this is only for pedagogical purposes.
# - A mypy error will also raise, again, on purpose.

import alchemy


if __name__ == "__main__":
    print("=== Alembic 4 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    print(f"Testing create_air: {alchemy.create_air()}")
    print("Now show that not all functions can be reached")
    print("This will raise an exception!")
    print("Testing the hidden create_earth: ", end="", flush=True)
    print(f"{alchemy.create_earth()}")
