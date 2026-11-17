#!/usr/bin/env python3
# Core assignment requirements (summary, not a compliance claim).
# Source: python05.pdf v3.0, printed pp. 11-12.
# Extend exercise 1 with an ExportPlugin Protocol defining
# process_output(data: list[tuple[int, str]]) -> None. DataStream's
# output_pipeline(nb, plugin) consumes up to nb entries from each processor
# and hands them to a compatible plugin using structural/duck typing.
# Provide CSV and JSON plugins that manually produce valid serialized
# strings without importing CSV or JSON libraries.
#
# Module rules: Python 3.10+, flake8, type hints/mypy; imports: abc and typing.


from typing import Any, Protocol
import typing
from abc import ABC, abstractmethod


# Duck typing means Python cares more about what an object can do than what
# class it belongs to. if it walks like a duck...

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


# abc      = "you are part of this class family"
# protocol = "you have the required shape"
class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass

# protocol cares about shape, not family.
# duck typing:
# python cares whether an object has the needed behavior
# not what exact class it belongs to.


class JsonExporter(ExportPlugin):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        items = []
        for rank, value in data:
            # this manually builds JSON, so special characters must be escaped.
            # a quote in the value, like: She said "hi", would close the JSON
            # string too early unless it becomes: She said \"hi\".
            # backslash is also an escape marker, so each real backslash must
            # be doubled before printing the JSON text.
            escaped = value.replace("\\", "\\\\").replace('"', '\\"')
            items.append(f'"item_{rank}": "{escaped}"')
        print("{" + ", ".join(items) + "}")


class CSVExporter(ExportPlugin):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        print(",".join(value for _, value in data))


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        if not self._processors:
            print("No processor found, no data")
            return

        for item in stream:
            processed = False
            for processor in self._processors:
                if processor.validate(item):
                    processor.ingest(item)
                    processed = True
                    break

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

        # to be used after calling process_stream, that will consume nb
        # elements from all registered data processors and export them using
        # the provided compatible plugin

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for processor in self._processors:
            to_export = []
            for n in range(nb):
                remaining = len(processor._data)
                if remaining:
                    item = processor.output()
                    to_export.append(item)
            if to_export:
                plugin.process_output(to_export)


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
                "log_message": "User wil is connected",
            },
        ],
        42,
        ["Hi", "five"],
    ]
    stream2 = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {
                "log_level": "ERROR",
                "log_message": "500 server crash",
            },
            {
                "log_level": "NOTICE",
                "log_message": "Certificate expires in 10 days",
            },
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]

    print("=== Code Nexus - Data Pipeline ===\n")
    print("Initialize Data Stream...")
    data_stream = DataStream()
    data_stream.print_processors_stats()

    print("Registering Processors")
    numeric_processor = NumericProcessor()
    log_processor = LogProcessor()
    text_processor = TextProcessor()

    data_stream.register_processor(numeric_processor)
    data_stream.register_processor(text_processor)
    data_stream.register_processor(log_processor)

    print(f"Send first batch of data on stream: {stream1}")
    data_stream.process_stream(stream1)
    data_stream.print_processors_stats()

    csv_plugin = CSVExporter()
    json_plugin = JsonExporter()

    print("Send 3 processed data from each processor to a CSV plugin:")
    data_stream.output_pipeline(3, csv_plugin)
    data_stream.print_processors_stats()

    print(f"Send another batch of data: {stream2}")
    data_stream.process_stream(stream2)
    data_stream.print_processors_stats()

    print("Send 5 processed data from each processor to a JSON plugin:")
    data_stream.output_pipeline(5, json_plugin)
    data_stream.print_processors_stats()
