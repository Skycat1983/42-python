#!/usr/bin/env python3
# Core assignment requirements (summary, not a compliance claim).
# Source: python08.pdf v3.0, printed pp. 6-8.
# Detect whether Python runs in a virtual environment and display the
# interpreter, environment information, and package installation paths.
# When outside one, show creation and activation instructions. Demonstrate
# global versus isolated package locations and test both environments.
# Do not submit the virtual environment itself.
#
# Module rules: Python 3.10+, flake8, type hints/mypy; handle errors gracefully.


# python3 -m venv matrix_env
# source matrix_env/bin/activate
# python construct.py

import os
import site
import sys


def is_virtual_environment() -> bool:
    # `base_prefix` is the base Python installation; `prefix` is the
    # environment used by the interpreter that is running this file.
    # inside a venv:
    # sys.prefix -> "/path/to/matrix_env"
    # sys.base_prefix -> "/usr"
    # sys.prefix != sys.base_prefix -> True
    return (
        sys.prefix != sys.base_prefix
        # The first check covers standard `venv`. The fallbacks also cover
        # older virtualenv environments and unusual interpreter setups.
        #: hasattr(sys, "real_prefix") -> False
        or hasattr(sys, "real_prefix")
        # in an activated venv:
        # os.environ.get("VIRTUAL_ENV") -> "/path/to/matrix_env"
        # bool("/path/to/matrix_env") -> True
        or bool(os.environ.get("VIRTUAL_ENV"))
    )


def package_paths() -> list[str]:
    # return package directories reported for the exact python executable
    # running this program (shown by `sys.executable`).
    # ["/path/to/matrix_env/lib/python3.11/site-packages"]
    paths = site.getsitepackages()

    # example return:
    # "/home/neo/.local/lib/python3.11/site-packages"
    user_path = site.getusersitepackages()

    # True when the user package path is not already in paths.
    if user_path not in paths:
        #  paths now also contains the user package path.
        # list.append() itself returns None.
        paths.append(user_path)

    # ["/path/to/matrix_env/lib/python3.11/site-packages",
    #  "/home/neo/.local/lib/python3.11/site-packages"]
    return paths


def show_activation_instructions() -> None:
    # Print portable instructions for creating and activating a venv.
    print("\nTo enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate       # On Unix")
    print(r"matrix_env\Scripts\activate          # On Windows")
    print("\nThen run this program again.")


def show_global_environment() -> None:
    # explain the risks of installing into the global interpreter.
    print("MATRIX STATUS: You're still plugged in")
    # Example value: sys.executable -> "/usr/bin/python3.11"
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    # Example value: sys.base_prefix -> "/usr"
    print(f"Global prefix: {sys.base_prefix}")
    print("\nWARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print("Global/user package locations:")
    # Example return from package_paths():
    # ["/usr/lib/python3.11/site-packages",
    #  "/home/neo/.local/lib/python3.11/site-packages"]
    for path in package_paths():
        print(f"  - {path}")
    # Example return: None. The function prints the activation instructions.
    show_activation_instructions()


def show_virtual_environment() -> None:
    # display details about the active isolated environment.
    #: "/path/to/matrix_env"
    path = os.environ.get("VIRTUAL_ENV", sys.prefix)

    #: "/path/to/matrix_env"
    normalized_path = os.path.normpath(path)
    #: "matrix_env"
    name = os.path.basename(normalized_path)

    print("MATRIX STATUS: Welcome to the construct")
    # sys.executable -> "/path/to/matrix_env/bin/python"
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {name}")
    print(f"Environment Path: {path}")
    # e.g: sys.base_prefix -> "/usr"
    print(f"Global Python prefix: {sys.base_prefix}")
    print("\nSUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system.")
    print("\nPackage installation path(s):")
    # ["/path/to/matrix_env/lib/python3.11/site-packages",
    #  "/home/neo/.local/lib/python3.11/site-packages"]
    for package_path in package_paths():
        # package_path.startswith(path) -> True
        is_virtual_path = package_path.startswith(path)
        location = "virtual" if is_virtual_path else "user/global"
        print(f"  - {package_path} ({location})")


def main() -> None:
    # whether the current interpreter is inside a virtual environment.
    # True when this file runs with matrix_env/bin/python.
    if is_virtual_environment():
        show_virtual_environment()
    else:
        show_global_environment()


if __name__ == "__main__":
    main()
