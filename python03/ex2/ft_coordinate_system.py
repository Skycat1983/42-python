#!/usr/bin/env python3
# Core assignment requirements (summary, not a compliance claim).
# Source: python03.pdf v3.0, printed pp. 11-12.
# Implement get_player_pos() to request x,y,z coordinates, retry invalid
# input, and return a three-dimensional tuple. Display the first tuple
# and its individual coordinates, its Euclidean distance from the origin,
# then the distance between that position and a second entered position.
#
# Module rules: Python 3.10+, flake8, type hints/mypy; no file I/O.


import math


def calc_distance(
    first: tuple[float, float, float],
    second: tuple[float, float, float]
) -> float:
    x1, y1, z1 = first
    x2, y2, z2 = second
    # euclidean distance: square each axis difference, add them,
    # then take the square root.
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def parse_coordinates(raw: str) -> tuple[float, float, float]:
    parts = raw.split(",")

    if len(parts) != 3:
        raise ValueError("Invalid syntax")

    coords: list[float] = []
    for part in parts:
        stripped = part.strip()
        try:
            coords.append(float(stripped))
        except ValueError as error:
            raise ValueError(
                f"Error on parameter '{stripped}': {error}"
            ) from error

    return coords[0], coords[1], coords[2]


def get_player_pos() -> tuple[float, float, float]:
    while True:
        raw = input("Enter new coordinates as floats in format 'x,y,z': ")
        try:
            return parse_coordinates(raw)
        except ValueError as error:
            print(error)


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    first = get_player_pos()
    print(f"Got a first tuple: {first}")
    print(f"It includes: X={first[0]}, Y={first[1]}, Z={first[2]}")
    print(f"Distance to center: {round(calc_distance((0, 0, 0), first), 4)}")

    print("Get a second set of coordinates")
    second = get_player_pos()
    print(
        "Distance between the 2 sets of coordinates: "
        f"{round(calc_distance(first, second), 4)}"
    )
