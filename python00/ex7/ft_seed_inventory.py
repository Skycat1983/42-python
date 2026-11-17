def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed = seed_type.capitalize()

    if unit == "packets":
        print(f"{seed} seeds: {int(quantity)} packets available")
    elif unit == "grams":
        print(f"{seed} seeds: {int(quantity)} grams total")
    elif unit == "area":
        print(f"{seed} seeds: covers {int(quantity)} square meters")
    else:
        print("Unknown unit type")
