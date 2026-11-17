#!/usr/bin/env python3

class Plant:
    def __init__(self: "Plant") -> None:
        self.name = ""
        self.height = 0.0
        self.days = 0

    @property
    def name_str(self: "Plant") -> str:
        return self.name.capitalize()

    @property
    def growth_rate(self: "Plant") -> float:
        return self.height / self.days if self.days != 0 else 0.0

    def get_info(self: "Plant") -> str:
        return f"{self.name_str}: {self.height:.1f}cm, {self.days} days old"

    def age(self: "Plant", n: int = 1) -> None:
        self.days += n

    def grow(self: "Plant") -> None:
        self.height += self.growth_rate


if __name__ == "__main__":
    rose = Plant()
    rose.name = "Rose"
    rose.height = 25
    rose.days = 30

    print("=== Garden Plant Growth ===")

    start_height = rose.height

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        print(rose.get_info())

        rose.age()
        rose.grow()

    total_growth = rose.height - start_height
    print(f"Growth this week: {int(round(total_growth))}cm")
