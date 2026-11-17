class PlantError(Exception):
    def __init__(self, message: str = "Invalid plant name to water") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    capitalized_name = plant_name.capitalize()
    if plant_name != capitalized_name:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {capitalized_name}: [OK]")


def test_watering_system() -> None:
    print("Testing valid plants...")
    print("Opening watering system")
    try:
        for plant_name in ("Tomato", "Lettuce", "Carrots"):
            water_plant(plant_name)
    finally:
        print("Closing watering system")

    print("Testing invalid plants...")
    print("Opening watering system")
    try:
        for plant_name in ("Tomato", "lettuce", "Carrots"):
            water_plant(plant_name)
    except PlantError as exc:
        print(f"Caught PlantError: {exc}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    test_watering_system()
    print("Cleanup always happens, even with errors!")
