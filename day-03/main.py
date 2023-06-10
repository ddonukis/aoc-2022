from common import get_input_file


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


def process_group(group: list[str]) -> int:
    group.sort(key=lambda g: len(g))
    for item in group[0]:
        if item in group[1] and item in group[2]:
            return calc_priority(item)
    raise ValueError(f"No shared item found in: {group!r}")


def main() -> None:
    p = get_input_file()

    part1_total = 0
    part2_total = 0
    group = []
    with p.open() as f:
        for line in f:
            part1_total += process_line(line)

            group.append(line.strip())
            if len(group) == 3:
                part2_total += process_group(group)
                group.clear()

    print(f"Part 1 answer: {part1_total}")
    print(f"Part 2 answer: {part2_total}")


if __name__ == "__main__":
    main()
