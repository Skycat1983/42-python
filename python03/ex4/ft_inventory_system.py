#!/usr/bin/env python3
# Core assignment requirements (summary, not a compliance claim).
# Source: python03.pdf v3.0, printed pp. 15-16.
# Parse item:quantity arguments into a dictionary of integer quantities.
# Report and discard malformed or repeated items. Display the inventory,
# item names, total quantity, and each item's percentage. Report the most
# and least abundant items, resolving ties by command-line order; then
# add a new item and display the updated inventory.
#
# Module rules: Python 3.10+, flake8, type hints/mypy; no file I/O.


import sys


# sword:1 potion:5 shield:2 armor:3 helmet:1 sword:2 hello key:value

if __name__ == "__main__":
    print("=== Inventory System Analysis ===")

    inventory: dict[str, int] = {}

    for parameter in sys.argv[1:]:
        parts = parameter.split(":")

        if len(parts) != 2 or not parts[0] or not parts[1]:
            print(f"Error - invalid parameter '{parameter}'")
            continue

        item_name, quantity_text = parts

        if item_name in inventory:
            print(f"Redundant item '{item_name}' - discarding")
            continue

        try:
            quantity = int(quantity_text)
        except ValueError as error:
            print(f"Quantity error for '{item_name}': {error}")
            continue

        inventory[item_name] = quantity

    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")

    total_quantity = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total_quantity}")

    for item_name, quantity in inventory.items():
        percent = round(quantity / total_quantity * 100, 1)
        print(f"Item {item_name} represents {percent}%")

    most_name = ""
    most_quantity = -1
    least_name = ""
    least_quantity = 0

    for item_name, quantity in inventory.items():
        if quantity > most_quantity:
            most_name = item_name
            most_quantity = quantity

        if least_name == "" or quantity < least_quantity:
            least_name = item_name
            least_quantity = quantity

    print(
        f"Item most abundant: {most_name} "
        f"with quantity {most_quantity}"
    )
    print(
        f"Item least abundant: {least_name} "
        f"with quantity {least_quantity}"
    )

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")
