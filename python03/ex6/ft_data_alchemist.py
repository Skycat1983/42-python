#!/usr/bin/env python3
# Core assignment requirements (summary, not a compliance claim).
# Source: python03.pdf v3.0, printed pp. 19-20.
# Use list comprehensions to capitalize all player names and separately
# select names already capitalized in the original list. Use dictionary
# comprehensions to assign random scores to the capitalized names and
# select scores above their average. Keep comprehensions on one line
# unless the line-length limit requires wrapping.
#
# Module rules: Python 3.10+, flake8, type hints/mypy; no file I/O.


import random


if __name__ == "__main__":
    print("=== Game Data Alchemist ===")

    players: list[str] = [
        "Alice",
        "bob",
        "Charlie",
        "dylan",
        "Emma",
        "Gregory",
        "john",
        "kevin",
        "Liam",
    ]

    capitalized_players: list[str] = [
        player.capitalize() for player in players
    ]
    only_capitalized: list[str] = [
        player for player in players if player.istitle()
    ]
    score_dict: dict[str, int] = {
        name: random.randint(1, 1000) for name in capitalized_players
    }
    score_average = round(sum(score_dict.values()) / len(score_dict), 2)
    high_scores: dict[str, int] = {
        name: score
        for name, score in score_dict.items()
        if score > score_average
    }

    print(f"Initial list of players: {players}")
    print(f"New list with all names capitalized: {capitalized_players}")
    print(f"New list of capitalized names only: {only_capitalized}")
    print(f"Score dict: {score_dict}")
    print(f"Score average is {score_average}")
    print(f"High scores: {high_scores}")
