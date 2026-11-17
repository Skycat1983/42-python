#!/usr/bin/env python3

class Plant:
    def __init__(self: "Plant", name: str, height: float, age: int) -> None:
        self._name = name.capitalize()
        height_valid = self._validate(height)
        age_valid = self._validate(age)
        if height_valid:
            self._height = height
        else:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
            self._height = 0
        if age_valid:
            self._age = age
        else:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
            self._age = 0
        if height_valid and age_valid:
            self.show(prefix="Plant created")

    def set_height(self: "Plant", height: float) -> None:
        if self._validate(height):
            self._height = height
            print(f"Height updated: {self.get_height()}cm")
        else:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self: "Plant", age: int) -> None:
        if self._validate(age):
            self._age = age
            print(f"Age updated: {self.get_age()} days")
        else:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")

    def get_height(self: "Plant") -> float:
        return self._height

    def get_age(self: "Plant") -> int:
        return self._age

    def h_str(self: "Plant") -> str:
        return f"{self._height:.1f}cm"

    def a_str(self: "Plant") -> str:
        return f"{self._age} days old"

    def show(self: "Plant", prefix: str = "Current state") -> None:
        print(f"{prefix}: {self._name}: {self.h_str()}, {self.a_str()}")

    @staticmethod
    def _validate(value: float) -> bool:
        return value >= 0


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15, 10)
    print()

    rose.set_height(25)
    rose.set_age(30)
    print()

    rose.set_height(-5)
    rose.set_age(-3)
    print()

    rose.show()
