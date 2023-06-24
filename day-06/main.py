import io
from pathlib import Path
from time import perf_counter_ns
from typing import Generator, Iterable

from common import get_input_file


def find_marker(message: Iterable[str], marker_length: int = 4) -> tuple[int, str]:
    batch: list[str] = []
    for i, ch in enumerate(message):
        if len(batch) == marker_length:
            return i, "".join(batch)
        try:
            idx = batch.index(ch)
        except ValueError:
            pass
        else:
            batch = batch[idx + 1 :]
        batch.append(ch)

    raise ValueError("packet start not found")


def iter_chars(file: io.TextIOWrapper) -> Generator[str, None, None]:
    while ch := file.read(1):
        yield ch


def iter_chars_in_file(filepath: Path) -> Generator[str, None, None]:
    with filepath.open(mode="r") as file:
        while ch := file.read(1):
            yield ch


def solve_puzzle(path: Path) -> None:
    index, marker = find_marker(iter_chars_in_file(path))
    print(f"Part 1: {index}")

    index, marker = find_marker(iter_chars_in_file(path), 14)
    print(f"Part 2: {index}")


def main() -> None:
    path = get_input_file()

    t0 = perf_counter_ns()
    solve_puzzle(path)
    time_taken = perf_counter_ns() - t0

    s_taken = time_taken / 1_000_000.0
    print(f"Time taken: {s_taken:.3f} s")


if __name__ == "__main__":
    main()
