class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def raise_plant_error() -> None:
    raise PlantError("The tomato plant is wilting!")


def raise_water_error() -> None:
    raise WaterError("Not enough water in the tank!")


def test_specific_errors() -> None:
    print("Testing PlantError...")
    try:
        raise_plant_error()
    except PlantError as exc:
        print(f"Caught PlantError: {exc}")

    print("Testing WaterError...")
    try:
        raise_water_error()
    except WaterError as exc:
        print(f"Caught WaterError: {exc}")


def test_garden_error() -> None:
    print("Testing catching all garden errors...")

    try:
        raise_plant_error()
    except GardenError as exc:
        print(f"Caught GardenError: {exc}")

    try:
        raise_water_error()
    except GardenError as exc:
        print(f"Caught GardenError: {exc}")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    test_specific_errors()
    test_garden_error()
    print("All custom error types work correctly!")
