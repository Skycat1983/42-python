def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        1 / 0
    elif operation_number == 2:
        open("/non/existent/file", "r")
    elif operation_number == 3:
        "str" + 1
    else:
        return


def test_error_types() -> None:
    for operation_number in range(5):
        print(f"Testing operation {operation_number}...")
        try:
            garden_operations(operation_number)
        except ValueError as exc:
            print(f"Caught ValueError: {exc}")
        except ZeroDivisionError as exc:
            print(f"Caught ZeroDivisionError: {exc}")
        except FileNotFoundError as exc:
            print(f"Caught FileNotFoundError: {exc}")
        except TypeError as exc:
            print(f"Caught TypeError: {exc}")
        else:
            print("Operation completed successfully")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print("All error types tested successfully!")
