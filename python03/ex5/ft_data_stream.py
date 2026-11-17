#!/usr/bin/env python3
# Core assignment requirements (summary, not a compliance claim).
# Source: python03.pdf v3.0, printed pp. 17-18.
# Use yield in an endless gen_event() generator of random (name, action)
# tuples. Pull and display 1,000 events without storing the whole stream.
# Build a separate ten-event list; consume_event() must randomly remove
# and yield its entries until empty, and be consumed with a for loop.
#
# Module rules: Python 3.10+, flake8, type hints/mypy; no file I/O.


import random
from typing import Generator

# generator is a function that does not return all its results at once
# it produces values one by one, on demand, each time we call next()


def gen_event(
    names: list[str],
    actions: list[str]
) -> Generator[tuple[str, str], None, None]:
    # 'yield' creates generator
    # runs until yield, pauses state, return 1 value, resumes where left
    while True:
        yield random.choice(names), random.choice(actions)


def consume_event(
    events: list[tuple[str, str]]
) -> Generator[tuple[str, str], None, None]:
    while events:
        idx = random.randrange(len(events))
        yield events.pop(idx)


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    names: list[str] = ["alice", "bob", "charlie", "dylan"]
    actions: list[str] = [
        "run",
        "eat",
        "sleep",
        "grab",
        "move",
        "climb",
        "swim",
        "release",
        "use",
    ]
    # first call creates and returns generator object
    event_gen: Generator[tuple[str, str], None, None] = gen_event(
        names,
        actions,
    )

    for i in range(1000):
        player, action = next(event_gen)
        print(f"Event {i}: Player {player} did action {action}")

    ten_tuples: list[tuple[str, str]] = []
    for _ in range(10):
        ten_tuples.append(next(event_gen))

    print(f"Built list of 10 events: {ten_tuples}")

    for event in consume_event(ten_tuples):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {ten_tuples}")
