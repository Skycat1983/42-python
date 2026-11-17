#!/usr/bin/env python3

from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data: list[tuple[int, str]] = []
        self._rank = 0

    # The validate method will be defined as validate(self, data: Any) -> bool
    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    # The ingest method is defined as ingest(self, data: Any) -> None
    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        return self._data.pop(0)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, int | float):
            return True
        if isinstance(data, list):
            return all(isinstance(item, int | float) for item in data)
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        if isinstance(data, list):
            for item in data:
                self._data.append((self._rank, str(item)))
                self._rank += 1
        else:
            self._data.append((self._rank, str(data)))
            self._rank += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")

        if isinstance(data, list):
            for item in data:
                self._data.append((self._rank, item))
                self._rank += 1
        else:
            self._data.append((self._rank, data))
            self._rank += 1


class LogProcessor(DataProcessor):
    def _format_log_entry(self, entry: dict[str, str]) -> str:
        values = list(entry.values())
        return f"{values[0]}: {values[1]}"

    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return len(data) == 2 and all(
                isinstance(key, str) and isinstance(value, str)
                for key, value in data.items()
            )

        if isinstance(data, list):
            return all(self.validate(item) for item in data)

        return False

    def ingest(
        self,
        data: dict[str, str] | list[dict[str, str]],
    ) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        if isinstance(data, list):
            for item in data:
                log_entry = self._format_log_entry(item)
                self._data.append((self._rank, log_entry))
                self._rank += 1
        else:
            log_entry = self._format_log_entry(data)
            self._data.append((self._rank, log_entry))
            self._rank += 1


if __name__ == "__main__":
    numeric_processor = NumericProcessor()
    text_processor = TextProcessor()
    log_processor = LogProcessor()

    print("=== Code Nexus - Data Processor ===")
    print("Testing Numeric Processor...")
    print(f"Trying to validate input '42': {numeric_processor.validate(42)}")
    print(
        "Trying to validate input 'Hello': "
        f"{numeric_processor.validate('Hello')}"
    )

    print("Test invalid ingestion of string 'foo' without prior validation:")

    try:
        numeric_processor.ingest("foo")  # intentional mypy warning
    except ValueError as exc:
        print(f"Got exception: {exc}")

    nums: list[int | float] = [1, 2, 3, 4, 5]
    numeric_processor.ingest(nums)

    print(f"Processing data: {nums}")
    print("Extracting 3 values...")

    for _ in range(3):
        rank, value = numeric_processor.output()
        print(f"Numeric value {rank}: {value}")

    print("Testing Text Processor...")
    print(f"Trying to validate input '42': {text_processor.validate(42)}")

    text_data = ["Hello", "Nexus", "World"]
    text_processor.ingest(text_data)

    print(f"Processing data: {text_data}")
    print("Extracting 1 value...")

    rank, value = text_processor.output()
    print(f"Text value {rank}: {value}")

    print("Testing Log Processor...")
    print(
        "Trying to validate input 'Hello': "
        f"{log_processor.validate('Hello')}"
    )
    log_data = [
        {
            "log_level": "NOTICE",
            "log_message": "Connection to server",
        },
        {
            "log_level": "ERROR",
            "log_message": "Unauthorized access!!",
        },
    ]
    log_processor.ingest(log_data)

    print(f"Processing data: {log_data}")
    print("Extracting 2 values...")

    for _ in range(2):
        rank, value = log_processor.output()
        print(f"Log entry {rank}: {value}")


# You use super() when the parent method does real setup/shared work:
