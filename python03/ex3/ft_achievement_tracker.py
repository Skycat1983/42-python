#!/usr/bin/env python3
# Core assignment requirements (summary, not a compliance claim).
# Source: python03.pdf v3.0, printed pp. 13-14.
# Randomly generate achievement sets for at least four players from a
# fixed achievement catalogue. Use set operations to report all distinct
# achievements, those common to every player, each player's exclusive
# achievements, and those each player lacks from the full catalogue.
#
# Module rules: Python 3.10+, flake8, type hints/mypy; no file I/O.


import random


def gen_player_achievements(a_list: list[str]) -> set[str]:
    num = random.randrange(1, len(a_list) + 1)
    a_set: set[str] = set()
    while len(a_set) < num:
        a_set.add(random.choice(a_list))
    return a_set


def gen_players(p_list: list[str], num: int) -> set[str]:
    p_set: set[str] = set()
    while len(p_set) < num:
        p_set.add(random.choice(p_list))
    return p_set


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    names: list[str] = ["Alice", "Bob", "Charlie", "Dylan"]
    achievements: list[str] = [
        "Crafting Genius",
        "Strategist",
        "World Savior",
        "Speed Runner",
        "Survivor",
        "Master Explorer",
        "Treasure Hunter",
        "Unstoppable",
        "First Steps",
        "Collector Supreme",
        "Untouchable",
        "Sharp Mind",
        "Boss Slayer",
        "Hidden Path Finder"
    ]
    players = gen_players(names, len(names))
    player1, player2, player3, player4 = tuple(players)
    achievements1 = gen_player_achievements(achievements)
    achievements2 = gen_player_achievements(achievements)
    achievements3 = gen_player_achievements(achievements)
    achievements4 = gen_player_achievements(achievements)

    print(f"Player {player1}: {achievements1}")
    print(f"Player {player2}: {achievements2}")
    print(f"Player {player3}: {achievements3}")
    print(f"Player {player4}: {achievements4}")

    unique_achievements = set(achievements)
    print()
    print(f"All distinct achievements: {unique_achievements}")
    # intersection = overlap
    common_achievements = set.intersection(
        achievements1,
        achievements2,
        achievements3,
        achievements4
    )
    print()
    print(f"Common achievements: {common_achievements}\n")
    # union = everything
    all_achievements = set.union(
        achievements1,
        achievements2,
        achievements3,
        achievements4
    )
    other_players1: set[str] = set()
    other_players1 = set.union(other_players1, achievements2, achievements3)
    other_players1 = set.union(other_players1, achievements4)
    other_players2: set[str] = set()
    other_players2 = set.union(other_players2, achievements1, achievements3)
    other_players2 = set.union(other_players2, achievements4)
    other_players3: set[str] = set()
    other_players3 = set.union(other_players3, achievements1, achievements2)
    other_players3 = set.union(other_players3, achievements4)
    other_players4: set[str] = set()
    other_players4 = set.union(other_players4, achievements1, achievements2)
    other_players4 = set.union(other_players4, achievements3)

    # difference = left in first set when second set is removed.
    only_player1 = set.difference(
        achievements1,
        other_players1
    )
    only_player2 = set.difference(
        achievements2,
        other_players2
    )
    only_player3 = set.difference(
        achievements3,
        other_players3
    )
    only_player4 = set.difference(
        achievements4,
        other_players4
    )

    print(f"Only {player1} has: {only_player1}")
    print(f"Only {player2} has: {only_player2}")
    print(f"Only {player3} has: {only_player3}")
    print(f"Only {player4} has: {only_player4}")

    print()

    missing1 = set.difference(all_achievements, achievements1)
    missing2 = set.difference(all_achievements, achievements2)
    missing3 = set.difference(all_achievements, achievements3)
    missing4 = set.difference(all_achievements, achievements4)

    print(f"{player1} is missing: {missing1}")
    print(f"{player2} is missing: {missing2}")
    print(f"{player3} is missing: {missing3}")
    print(f"{player4} is missing: {missing4}")
