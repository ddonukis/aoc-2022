from typing import NamedTuple

from common import get_input_file


class Interval(NamedTuple):
    start: int
    end: int

    @classmethod
    def from_string(cls, s: str) -> "Interval":
        n1, n2 = s.split("-")
        if n1.isnumeric() and n2.isnumeric():
            n1, n2 = int(n1), int(n2)
            if n1 > n2:
                n1, n2 = n2, n1
            return cls(n1, n2)
        else:
            raise ValueError(f"{n1=} and {n2=} must be integers")


def contained_intervals(a: Interval, b: Interval) -> bool:
    if a.start <= b.start and a.end >= b.end:
        return True
    elif b.start <= a.start and b.end >= a.end:
        return True
    else:
        return False


def overlapping_intervals(a: Interval, b: Interval) -> bool:
    if a.start <= b.start <= a.end:
        return True
    elif b.start <= a.start <= b.end:
        return True
    else:
        return False


def parse_line(line: str) -> tuple[Interval, Interval]:
    a, b = line.strip().split(",", maxsplit=1)
    try:
        a, b = Interval.from_string(a), Interval.from_string(b)
        return a, b
    except ValueError:
        raise ValueError(f"Could not parse line: {line!r}")


def main() -> None:
    path = get_input_file()

    part1_total = 0
    part2_total = 0
    with path.open() as f:
        for line in f:
            a, b = parse_line(line)
            if contained_intervals(a, b):
                part1_total += 1

            if overlapping_intervals(a, b):
                part2_total += 1

    print(f"Part 1 answer: {part1_total}")
    print(f"Part 2 answer: {part2_total}")


if __name__ == "__main__":
    main()
