#!/usr/bin/env python3

from typing import Any
import typing
from abc import ABC, abstractmethod


# what is polymorphism and polymorphic behaviour?
# common interface with different outcomes
# same method or function on different classes
# one way to formulate polymorphism

class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data: list[tuple[int, str]] = []
        self._rank = 0

    # The validate method will be defined as validate(self, data: Any) -> bool
    # in the DataProcessor clas
    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    # The ingest method is defined as ingest(self, data: Any) -> None in the
    # DataProcessor class.
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


# Create a DataStream class that will receive a stream of data containing
# different types and then will route each element to the appropriate data
# processor using polymorphic behavior.

class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    # method that allows you to register a new data processor
    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    # method that will analyze each element of the list received as a parameter
    # and send it to the appropriate registered data processor. Error messages
    # will be printed if no data processor can handle an element
    def process_stream(self, stream: list[typing.Any]) -> None:
        if not self._processors:
            print("No processor found, no data")
            return

        for item in stream:
            processed = False
            # for each item stop processing when validation passes
            for processor in self._processors:
                if processor.validate(item):
                    processor.ingest(item)
                    processed = True
                    break
            # this is only read when we can't find processor for the item
            if not processed:
                print(
                    "DataStream error - Can't process element in "
                    f"stream: {item}"
                )

    # method in order to print stream statistics
    def print_processors_stats(self) -> None:
        print("=== DataStream statistics ===\n")
        for processor in self._processors:
            name = type(processor).__name__.replace("Processor", " Processor")
            total = processor._rank
            remaining = len(processor._data)
            print(
                f"{name}: total {total} items processed, "
                f"remaining {remaining} on processor"
            )


if __name__ == "__main__":
    stream1 = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead",
            },
            {
                "log_level": "INFO",
                "log_message": "User wil isconnected",
            },
        ],
        42,
        ["Hi", "five"],
    ]
    print("=== Code Nexus - Data Stream ===\n")
    print("Initialize Data Stream...")
    data_stream = DataStream()
    data_stream.process_stream(stream1)
    print("Registering Numeric Processor")
    print(f"Send first batch of data on stream {stream1}")
    numeric_processor = NumericProcessor()
    data_stream.register_processor(numeric_processor)
    data_stream.process_stream(stream1)
    data_stream.print_processors_stats()
    print("Registering other data processors")
    print("Sned the same batch again")
    log_processor = LogProcessor()
    text_processor = TextProcessor()
    data_stream.register_processor(log_processor)
    data_stream.register_processor(text_processor)
    data_stream.process_stream(stream1)
    data_stream.print_processors_stats()
    print(
        "Consume some elements from the data processors: "
        "Numeric 3, Text 2, Log 1"
    )
    for _ in range(3):
        numeric_processor.output()

    for _ in range(2):
        text_processor.output()

    for _ in range(1):
        log_processor.output()

    data_stream.print_processors_stats()
