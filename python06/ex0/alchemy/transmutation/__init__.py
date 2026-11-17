# Source for the requirement comments below: python06.pdf v2.0,
# printed pp. 12-13. These describe the assignment, not verified compliance.

# Exercise requirements from python06.pdf:
# - ft_transmutation_1.py will use the import ... structure to import the
#   module transmutation directly and then achieve transformation of lead
#   into gold.
# - You may need to create and/or update a few extra files to complete
#   these scripts.

from .recipes import lead_to_gold

__all__ = ["lead_to_gold"]
