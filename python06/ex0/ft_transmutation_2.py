# Exercise requirements from python06.pdf:
# - ft_transmutation_2.py will use the import ... structure to import the
#   module alchemy directly and then achieve transformation of lead into
#   gold.

import alchemy

if __name__ == "__main__":
    print("=== Transmutation 2 ===")
    print("Import alchemy module only")
    print(f"Testing lead to gold: {alchemy.lead_to_gold()}")
