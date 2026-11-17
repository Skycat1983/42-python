#!/usr/bin/env python3

# ! A lambda is an anonymous function containing exactly one expression:

# • Use sorted() with a lambda to sort by ’power’ level (descending)
# • Each artifact is a dict: {’name’: str, ’power’: int, ’type’: str}
# • Return the sorted list
# !`key`is a function that produces a value to sort by, not the value itself
def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(
        artifacts, key=lambda artifact: artifact["power"], reverse=True
    )

# ! equivalent of above but using named func
# def get_artifact_power(artifact: dict) -> int:
#     return artifact["power"]
#
# def artifact_sorter(artifacts: list[dict]) -> list[dict]:
#     return sorted(artifacts, key=get_artifact_power, reverse=True)


# • Use filter() with a lambda to find mages with power >= min_power
# • Each mage is a dict with name, power, and element fields
# • Return a list of filtered mages
def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


# • Use map() with a lambda to add a "* " prefix and " *" suffix
# • Input is a list of spell-name strings
# • Return a list of transformed spell names
def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


# • Use lambdas with max() and min() to find the power extremes
# • Calculate the average power and round it to 2 decimal places
# • Return max_power, min_power, and avg_power in a dictionary
def mage_stats(mages: list[dict]) -> dict:
    return {
        "max_power": max(mages, key=lambda mage: mage["power"])["power"],
        "min_power": min(mages, key=lambda mage: mage["power"])["power"],
        "avg_power": round(
            sum(map(lambda mage: mage["power"], mages)) / len(mages),
            2,
        ),
    }


if __name__ == "__main__":
    artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "orb"},
        {"name": "Fire Staff", "power": 92, "type": "staff"},
        {"name": "Moon Dagger", "power": 70, "type": "weapon"},
    ]
    mages = [
        {"name": "Lyra", "power": 78, "element": "fire"},
        {"name": "Orin", "power": 91, "element": "water"},
        {"name": "Selene", "power": 64, "element": "moon"},
        {"name": "Kael", "power": 88, "element": "storm"},
    ]
    min_power = 80
    spells = [
        "fireball",
        "heal",
        "shield",
        "lightning",
    ]

    sorted_artifacts = artifact_sorter(artifacts)
    filtered_mages = power_filter(mages, min_power)
    transformed_spells = spell_transformer(spells)
    stats = mage_stats(mages)

    print("Testing artifact sorter...")
    for artifact in sorted_artifacts:
        print(f"{artifact['name']} ({artifact['power']} power)")

    print("Testing mage filter...")
    for mage in filtered_mages:
        print(f"{mage['name']} {mage['power']}")

    print("Testing spell transformer...")
    for spell in transformed_spells:
        print(f"{spell}")

    print("Testing stats...")
    for k, v in stats.items():
        print(f"{k} {v}")
    pass
