#!/usr/bin/env python3
# Core assignment requirements (summary, not a compliance claim).
# Source: python03.pdf v3.0, printed pp. 9-10.
# Parse command-line scores into a list. Report and discard invalid
# values, continuing with valid ones; handle an empty result gracefully.
# Display count, total, average, maximum, minimum, and score range.
#
# Module rules: Python 3.10+, flake8, type hints/mypy; no file I/O.


import sys


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    scores: list[int] = []

    i = 1
    while i < len(sys.argv):
        try:
            scores.append(int(sys.argv[i]))
        except ValueError:
            print(f"Invalid parameter: '{sys.argv[i]}'")
        i += 1

    if len(scores):
        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores) / len(scores)}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")
    else:
        print(
            f"No scores provided. Usage: python3 {sys.argv[0]} "
            "<score1> <score2> ..."
        )
