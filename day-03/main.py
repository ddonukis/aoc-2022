from functools import wraps
from time import perf_counter_ns
from typing import Any, Callable

from common import get_input_file


MEASURED_PERF = []
MEASURED_PERF_SETS = []


def measure_time(db: list) -> Callable:
    def inner(f) -> Callable:
        @wraps(f)
        def wrapper(*args, **kwds) -> Any:
            t0 = perf_counter_ns()
            result = f(*args, **kwds)
            time_took = perf_counter_ns() - t0
            db.append(time_took)
            return result

        return wrapper

    return inner


def calc_priority(item: str) -> int:
    if not item.isalpha():
        raise ValueError(f"Invalid item: {item}")
    if item.isupper():
        return ord(item) - ord("A") + 27
    return ord(item) - ord("a") + 1


def process_line(line: str) -> int:
    line = line.strip()
    compartment_size = len(line) // 2

    compartment1, compartment2 = line[:compartment_size], line[compartment_size:]

    for item in compartment1:
        if item in compartment2:
            return calc_priority(item)
    raise ValueError(f"No shared item found in: {line!r}")


@measure_time(MEASURED_PERF)
def process_group(group: list[str]) -> int:
    for item in group[0]:
        if (
            item in group[1] and item in group[2]
        ):  # string membershiop lookups are fast + short circuit when found
            return calc_priority(item)
    raise ValueError(f"No shared item found in: {group!r}")


@measure_time(MEASURED_PERF_SETS)
def process_group_with_sets(group: list[str]) -> int:
    #  set comparisons are fast in theory but for small strings it is not going to pay off
    common = set(group[0]) & set(group[1]) & set(group[2])
    return calc_priority(common.pop())


def main() -> None:
    p = get_input_file()

    part1_total = 0
    part2_total = 0
    part2_total_sets = 0
    group = []
    with p.open() as f:
        for line in f:
            part1_total += process_line(line)

            group.append(line.strip())
            if len(group) == 3:
                part2_total_sets += process_group_with_sets(group)

                part2_total += process_group(group)
                group.clear()

    assert part2_total == part2_total_sets
    print(f"Part 1 answer: {part1_total}")
    print(f"Part 2 answer: {part2_total}")


if __name__ == "__main__":
    main()
    s = sum(MEASURED_PERF)
    s2 = sum(MEASURED_PERF_SETS)
    print(f"Duration: total {s / 1_000_000} ms, avg {s / len(MEASURED_PERF) / 1_000_000} ms")
    print(
        f"Duration (sets): total {s2 / 1_000_000} ms, avg {s2 / len(MEASURED_PERF) / 1_000_000} ms"
    )
