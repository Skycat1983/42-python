#!/usr/bin/env python3

class Plant:
    class Stats:
        def __init__(self: "Plant.Stats") -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def add_grow(self: "Plant.Stats") -> None:
            self._grow_calls += 1

        def add_age(self: "Plant.Stats") -> None:
            self._age_calls += 1

        def add_show(self: "Plant.Stats") -> None:
            self._show_calls += 1

        def display(self: "Plant.Stats") -> None:
            print(
                f"Stats: {self._grow_calls} grow, "
                f"{self._age_calls} age, "
                f"{self._show_calls} show"
            )

    def __init__(self: "Plant", name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age
        self._stats = Plant.Stats()

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

    def grow(self: "Plant", cm: float) -> None:
        self._height += cm
        self._stats.add_grow()

    def age(self: "Plant", days: int) -> None:
        self._age += days
        self._stats.add_age()

    def show(self: "Plant") -> None:
        self._stats.add_show()
        print(f"{self.name}: {self.height}, {self.age_text}")

    def display_stats(self: "Plant") -> None:
        self._stats.display()

    @staticmethod
    def is_older_than_year(days: int) -> bool:
        return days > 365

    @classmethod
    def create_anonymous(cls: type["Plant"]) -> "Plant":
        return cls("unknown plant", 0.0, 0)


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


class Seed(Flower):
    def __init__(
        self: "Seed",
        name: str,
        height: float,
        age: int,
        color: str,
        seeds: int = 0,
    ) -> None:
        super().__init__(name, height, age, color)
        self._seeds = seeds

    def bloom(self: "Seed") -> None:
        super().bloom()
        self._seeds = 42

    def show(self: "Seed") -> None:
        super().show()
        print(f"Seeds: {self._seeds}")


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
        self._shade_calls = 0

    @property
    def diameter_text(self: "Tree") -> str:
        return f"Trunk diameter: {self._trunk_diameter:.1f}cm"

    def show(self: "Tree") -> None:
        super().show()
        print(self.diameter_text)

    def produce_shade(self: "Tree") -> None:
        self._shade_calls += 1
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self._height:.1f}cm long and "
            f"{self._trunk_diameter:.1f}cm wide."
        )

    def display_stats(self: "Tree") -> None:
        super().display_stats()
        print(f"{self._shade_calls} shade")


def display_plant_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant.display_stats()


if __name__ == "__main__":
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")

    print("=== Flower")
    rose = Flower("rose", 15.0, 10, "red")
    rose.show()
    display_plant_statistics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.bloom()
    rose.show()
    display_plant_statistics(rose)

    print("=== Tree")
    oak = Tree("oak", 200.0, 365, 5.0)
    oak.show()
    display_plant_statistics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_plant_statistics(oak)

    print("=== Seed")
    sunflower = Seed("sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    display_plant_statistics(sunflower)

    print("=== Anonymous")
    unknown = Plant.create_anonymous()
    unknown.show()
    display_plant_statistics(unknown)
