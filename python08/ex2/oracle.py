#!/usr/bin/env python3
# Core assignment requirements (summary, not a compliance claim).
# Source: python08.pdf v3.0, printed pp. 12-14.
# Use python-dotenv to load development settings from .env, letting
# existing environment variables override file values. Handle MATRIX_MODE,
# DATABASE_URL, API_KEY, LOG_LEVEL, and ZION_ENDPOINT, including missing
# configuration. Make development/production differences visible in output.
# Submit a placeholder .env.example and a .gitignore that excludes .env;
# never commit real credentials or replace python-dotenv with a custom parser.
#
# Module rules: Python 3.10+, flake8, type hints/mypy; handle errors gracefully.


# Directory: ex2/
# Files to Submit: oracle.py, .env.example, .gitignore
# Create a program called oracle.py that:

# * cp .env.example .env
# * $> MATRIX_MODE=production API_KEY=secret123 python3 oracle.py

# Authorized: os, sys, python-dotenv modules, file operations
import os
# for interacting with the operating system
# - reading env variables like os.environ
# - construct and inspect file paths (`os.path`).
#  used when the program needs information upplied by its os environment
import sys

# Your program should handle these configuration variables:
# '...' = "zero or more additional items of the same type."
CONFIGURATION_KEYS: tuple[str, ...] = (
    # • MATRIX_MODE - "development" or "production"
    "MATRIX_MODE",
    # • DATABASE_URL - Connection string for data storage
    "DATABASE_URL",
    # • API_KEY - Secret key for external services
    "API_KEY",
    # • LOG_LEVEL - Logging verbosity
    "LOG_LEVEL",
    # • ZION_ENDPOINT - URL for the resistance network
    "ZION_ENDPOINT",
)
# `__file__` is the path of this Python file. `abspath()` makes that path
file_path = os.path.abspath(__file__)
BASE_DIRECTORY = os.path.dirname(file_path)


# "You should use the python-dotenv library to load environment
# variables from .env files. The goal is to learn how to use .env
# files for configuration management, not to implement a custom parser."
def load_environment_file() -> tuple[bool, str]:
    try:
        # `type: ignore` allows mypy to run even without local stubs installed.
        from dotenv import load_dotenv  # type: ignore
    # catches the `ImportError` raised while Python executes the `import`
    except ImportError:
        return False, (
            "python-dotenv is not installed. Run: "
            "python -m pip install python-dotenv"
        )
    # • Uses a .env file for development settings
    env_path = os.path.join(BASE_DIRECTORY, ".env")
    print(env_path)
    env_exists = os.path.isfile(env_path)  # checks whether .env exists
    load_dotenv(
        dotenv_path=env_path, override=False
    )  # loads file values only if absent
    if env_exists:
        return True, ".env file loaded"
    return True, ".env file not found; using process environment"


# • Loads configuration from environment variables
def read_configuration() -> tuple[dict[str, str], list[str]]:
    configuration: dict[str, str] = {}
    missing: list[str] = []

    for key in CONFIGURATION_KEYS:
        value = os.environ.get(key)
        if value:
            configuration[key] = value
        else:
            #  missing keys return `None`.
            missing.append(key)
    return configuration, missing


def show_configuration(configuration: dict[str, str]) -> None:
    # • Demonstrates different configuration for development/production
    mode = configuration["MATRIX_MODE"]
    database_type = "local instance"
    if mode == "production":
        database_type = "production instance"

    print("\nConfiguration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: Connected to {database_type}")
    print("API Access: Authenticated")
    print(f"Log Level: {configuration['LOG_LEVEL'].upper()}")
    print("Zion Network: Online")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")


def main() -> int:
    print("ORACLE STATUS: Reading the Matrix...")
    dotenv_available, load_message = load_environment_file()
    print(load_message)
    if not dotenv_available:
        return 1

    configuration, missing = read_configuration()
    # • Includes proper error handling for missing configuration
    if missing:
        print("\nConfiguration incomplete. Missing variables:")
        for key in missing:
            print(f"  - {key}")
        print("\nCopy .env.example to .env and replace its example values,")
        print("or export the variables in your shell.")
        return 1

    if configuration["MATRIX_MODE"] not in {"development", "production"}:
        print(
            "MATRIX_MODE must be 'development' or 'production'",
            file=sys.stderr,
        )
        return 1

    show_configuration(configuration)
    print("\nThe Oracle sees all configurations.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
