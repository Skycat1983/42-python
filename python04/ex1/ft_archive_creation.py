#!/usr/bin/env python3
import sys
from typing import IO

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
    else:
        print("=== Cyber Archives Recovery & Presentation ===")

        filename = sys.argv[1]
        print(f"Accessing file '{filename}'")
        read_file: IO[str] | None = None
        write_file: IO[str] | None = None

        try:
            read_file = open(filename, "r")
            content = read_file.read()

            print("---")
            print(content, end="")
            print("---")

            transformed = ""

            i = 0
            while i < len(content):
                if content[i] == "\n":
                    transformed = transformed + "#\n"
                else:
                    transformed = transformed + content[i]
                i += 1

            # check content isn't empty and last char isn't newline
            #  “If the input string content has at least one char
            # ... and does not end with a newline, add #.”
            if content and content[-1] != "\n":
                transformed += "#"

            print("Transform data:")
            print("---")
            print(transformed)
            print("---")

            new_name = input("Enter new file name (or empty): ")

            if len(new_name) < 1:
                print("Not saving data")
            else:
                print(f"Saving data to '{new_name}'")

                write_file = open(new_name, "w")
                write_file.write(transformed)

                print(f"Data saved in file '{new_name}'\n")

        except FileNotFoundError as e:
            print(f"Error opening file '{filename}': {e}")

        except PermissionError as e:
            print(f"Error opening file '{filename}': {e}")

        except Exception as e:
            print(f"Unexpected error: {e}")

        finally:
            if read_file is not None and not read_file.closed:
                read_file.close()
                print(f"File '{filename}' closed.")
            if write_file is not None and not write_file.closed:
                write_file.close()
