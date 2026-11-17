#!/usr/bin/env python3

class Plant:
    def __init__(self: "Plant", name: str, height: int, days: int) -> None:
        self.name = name
        self.height = height
        self.days = days
        self.show()

    @property
    def growth_rate(self: "Plant") -> float:
        return self.height / self.days if self.days != 0 else 0.0

    @property
    def name_str(self: "Plant") -> str:
        return self.name.capitalize()

    @property
    def height_str(self: "Plant") -> str:
        return f"{self.height:.1f}cm"

    @property
    def age_str(self: "Plant") -> str:
        return f"{self.days} days old"

    def show(self: "Plant") -> None:
        print(f"Created: {self.name_str}: {self.height_str}, {self.age_str}")

    def age(self: "Plant", days: int = 1) -> None:
        rate = self.growth_rate
        self.days += days
        self.height += int(rate * days)

    def grow(self: "Plant", cm: int) -> None:
        rate = self.growth_rate
        self.height += cm
        if rate > 0:
            self.days += int(cm / rate)


if __name__ == "__main__":
    print("== Plant Factory Output ===")

    plant_data = [
        ["rose", 25, 30],
        ["oak", 200, 365],
        ["cactus", 5, 90],
        ["sunflower", 80, 45],
        ["fern", 15, 120],
    ]

    plant_instances = []
    for name, height, days in plant_data:
        instance = Plant(name, height, days)
        plant_instances.append(instance)
