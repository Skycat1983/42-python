# Exercise requirements from python06.pdf:
# - ft_transmutation_1.py will use the import ... structure to import the
#   module transmutation directly and then achieve transformation of lead
#   into gold.

import alchemy.transmutation

if __name__ == "__main__":
    print("=== Transmutation 1 ===")
    print("Import transmutation module directly")
    print(f"Testing lead to gold: {alchemy.transmutation.lead_to_gold()}")
