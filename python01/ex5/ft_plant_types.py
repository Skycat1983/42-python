#!/usr/bin/env python3

class Plant:
    def __init__(self: "Plant", name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age

    @property
    def name(self: "Plant") -> str:
        return self._name.capitalize()

    @property
    def height(self: "Plant") -> str:
        return f"{self._height:.1f}cm"

    @property
    def age_text(self: "Plant") -> str:
        unit = "day" if self._age == 1 else "days"
        return f"{self._age} {unit} old"

    def show(self: "Plant") -> None:
        print(f"{self.name}: {self.height}, {self.age_text}")


class Flower(Plant):
    def __init__(self: "Flower", n: str, h: float, a: int, c: str) -> None:
        super().__init__(n, h, a)
        self._color = c
        self._has_bloomed = False

    @property
    def color_text(self: "Flower") -> str:
        return f"Color: {self._color}"

    @property
    def bloom_text(self: "Flower") -> str:
        if self._has_bloomed:
            return f"{self.name} is blooming beautifully!"
        return f"{self.name} has not bloomed yet"

    def bloom(self: "Flower") -> None:
        self._has_bloomed = True

    def show(self: "Flower") -> None:
        super().show()
        print(self.color_text)
        print(self.bloom_text)


class Tree(Plant):
    def __init__(
        self: "Tree",
        name: str,
        height: float,
        age: int,
        trunk_diameter: float,
    ) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    @property
    def diameter_text(self: "Tree") -> str:
        return f"Trunk diameter: {self._trunk_diameter:.1f}cm"

    def produce_shade(self: "Tree") -> None:
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self._height:.1f}cm long and "
            f"{self._trunk_diameter:.1f}cm wide."
        )

    def show(self: "Tree") -> None:
        super().show()
        print(self.diameter_text)


class Vegetable(Plant):
    def __init__(
        self: "Vegetable",
        name: str,
        height: float,
        age: int,
        harvest_season: str,
    ) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def age(self: "Vegetable", days: int) -> None:
        self._age += days
        self._nutritional_value += days

    def grow(self: "Vegetable", cm: float) -> None:
        self._height += cm
        self._nutritional_value += int(cm)

    def show(self: "Vegetable") -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print()

    print("=== Tree")
    oak = Tree("oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print()

    print("=== Vegetable")
    tomato = Vegetable("tomato", 5.0, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    tomato.grow(42.0)
    tomato.age(20)
    tomato.show()
