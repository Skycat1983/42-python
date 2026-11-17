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

        try:
            read_file: IO[str] = open(filename, "r")
            try:
                content = read_file.read()
            finally:
                read_file.close()

            print("---")
            print(content, end="")
            print("---")

            print(f"File '{filename}' closed.")

            transformed = ""

            i = 0
            while i < len(content):
                if content[i] == "\n":
                    transformed = transformed + "#\n"
                else:
                    transformed = transformed + content[i]
                i += 1

            if len(content) > 0 and content[len(content) - 1] != "\n":
                transformed = transformed + "#"

            print("Transform data:")
            print("---")
            print(transformed)
            print("---")

            sys.stdout.write("Enter new file name (or empty): ")
            # flush out the 'write' from the buffer
            sys.stdout.flush()
            new_name = sys.stdin.readline()

            if len(new_name) < 1:
                print("Not saving data")
            else:
                print(f"Saving data to '{new_name}'")

                write_file: IO[str] = open(new_name, "w")
                try:
                    write_file.write(transformed)
                finally:
                    write_file.close()

                print(f"Data saved in file '{new_name}'\n")

        except FileNotFoundError as e:
            sys.stderr.write(f"Error opening file '{filename}': {e}")

        except PermissionError as e:
            sys.stderr.write(f"Error opening file '{filename}': {e}")

        except Exception as e:
            sys.stderr.write(f"Unexpected error: {e}")
