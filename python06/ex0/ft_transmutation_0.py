# Source for the requirement comments below: python06.pdf v2.0,
# printed pp. 12-13. These describe the assignment, not verified compliance.

# Exercise requirements from python06.pdf:
# - ft_transmutation_0.py will use the import ... structure to access
#   alchemy/transmutation/recipes.py directly and then achieve
#   transformation of lead into gold.

import alchemy.transmutation.recipes


if __name__ == "__main__":
    print("=== Transmutation 0 ===")
    print("Using file alchemy/transmutation/recipes.py directly")
    print(
        "Testing lead to gold: "
        f"{alchemy.transmutation.recipes.lead_to_gold()}"
    )
