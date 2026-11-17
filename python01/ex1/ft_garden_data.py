#!/usr/bin/env python3
class Plant:
    def __init__(self: "Plant") -> None:
        self._name = ""
        self._height = ""
        self._age = ""

    @property
    def name(self: "Plant") -> str:
        return self._name.capitalize() + ": "

    @property
    def height(self: "Plant") -> str:
        return self._height + "cm, "

    @property
    def age(self: "Plant") -> str:
        return self._age + " days old"

    def show(self: "Plant") -> None:
        print(self.name + self.height + self.age)


if __name__ == "__main__":
    rose = Plant()
    sunflower = Plant()
    cactus = Plant()

    rose._name = "rose"
    rose._height = "25"
    rose._age = "30"

    sunflower._name = "sunflower"
    sunflower._height = "80"
    sunflower._age = "45"

    cactus._name = "cactus"
    cactus._height = "15"
    cactus._age = "120"

    print("=== Garden Plant Registry ===")

    rose.show()
    sunflower.show()
    cactus.show()
