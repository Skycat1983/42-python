
def input_temperature(temp_str: str) -> int:
    print(f"Input data is '{temp_str}'")
    temp = int(temp_str)
    print(f"Temperature is now {temp}°C")
    return temp


def test_temperature() -> None:
    try:
        input_temperature("25")
    except ValueError as exc:
        print(f"Caught input_temperature error: {exc}")
    try:
        input_temperature("abc")
    except ValueError as exc:
        print(f"Caught input_temperature error: {exc}")


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    test_temperature()
    print("All tests completed - program didn't crash!")
