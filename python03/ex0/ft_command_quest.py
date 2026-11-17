#!/usr/bin/env python3

import sys


def print_value(label: str, value: str) -> None:
    print(f"{label.capitalize()}: {value}")


if __name__ == "__main__":
    print("=== Command Quest ===")
    argc = len(sys.argv)

    print_value("program name", sys.argv[0])

    if argc > 1:
        print_value("arguments received", str(argc - 1))
        i = 1
        while i < argc:
            print_value(f"argument {i}", sys.argv[i])
            i += 1
    else:
        print("No arguments provided!")

    print_value("total arguments", str(argc))


# _, *args = sys.argv
# for arg in args:
#     print(arg)


# for i in range(1, len(sys.argv)):
#     print(sys.argv[i])
