#!/usr/bin/env python3

import sys
from typing import IO


# Get the name of a file from the command line, then read the file’s
# contents and display
# them as the cat command would. Add a few headers
# and footers as shown in the exam-
# ple. You need to handle the various failure cases
# (nonexistent files, inaccessible files, etc.).

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        sys.exit(1)

    print("=== Cyber Archives- Recovery ===")
    filename = sys.argv[1]
    print(f"Accessing file '{filename}'")
    file: IO[str] | None = None

    try:
        file = open(filename, "r")
        content = file.read()

        print("---")
        print(content)
        print("---")

    except FileNotFoundError as e:
        print(f"Error opening file '{filename}': {e}")
        sys.exit(1)

    except PermissionError as e:
        print(f"Error opening file '{filename}': {e}")
        sys.exit(1)

    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

    finally:
        if file is not None and not file.closed:
            file.close()
            print(f"File '{filename}' closed.")
