from copy import deepcopy
from pathlib import Path
from time import perf_counter_ns
from typing import Generator, Iterable, NamedTuple

from common import get_input_file


State = tuple[list[str], ...]


class Crate(NamedTuple):
    stack_index: int
    label: str


class Command(NamedTuple):
    quantity: int
    from_index: int
    to_index: int


def iter_str_slices(
    string: str, slice_width: int = 3, space_width: int = 1
) -> Generator[str, None, None]:
    crate_start = 0
    crate_end = slice_width

    while (crate_end := crate_start + slice_width) <= len(string):
        yield string[crate_start:crate_end]
        crate_start += slice_width + space_width


def parse_crates_level(level: str) -> list[Crate]:
    crates: list[Crate] = []

    for stack_index, crate_slot in enumerate(iter_str_slices(level)):
        if crate_slot.startswith("["):
            crates.append(Crate(stack_index, crate_slot[1:2]))

    return crates


def parse_crates(raw_crates: list[str]) -> State:
    crate_labels = raw_crates.pop().split()
    crate_stacks: State = tuple([] for _ in crate_labels)

    raw_crates.reverse()
    for level in raw_crates:
        for crate in parse_crates_level(level):
            crate_stacks[crate.stack_index].append(crate.label)

    return crate_stacks


def parse_commands(lines: Iterable[str]) -> Generator[Command, None, None]:
    for line in lines:
        parts = line.split()  # ["move", "1", "from", "1", "to", "2"]
        yield Command(
            quantity=int(parts[1]), from_index=int(parts[3]) - 1, to_index=int(parts[-1]) - 1
        )


def simulate_commands(
    state: State, commands: Iterable[Command], multi_crate: bool = False
) -> State:
    state = deepcopy(state)
    for command in commands:
        moved_crates = state[command.from_index][-command.quantity :]

        if not multi_crate:
            moved_crates.reverse()

        state[command.to_index].extend(moved_crates)
        del state[command.from_index][-command.quantity :]
    return state


def get_top_crates(state: State) -> str:
    return "".join(stack[-1] for stack in state)


def solve_puzzle(input_path: Path) -> None:
    initial_state = []
    with input_path.open() as f:
        while (line := next(f).rstrip("\n")) != "":
            initial_state.append(line)

        commands = list(parse_commands(f))

    state = parse_crates(initial_state)

    part_1_answer = get_top_crates(simulate_commands(state, commands))
    print(f"Part 1: {part_1_answer}")

    part_2_answer = get_top_crates(simulate_commands(state, commands, multi_crate=True))
    print(f"Part 2: {part_2_answer}")


def main() -> None:
    path = get_input_file()

    t0 = perf_counter_ns()
    solve_puzzle(path)
    time_taken = perf_counter_ns() - t0

    s_taken = time_taken / 1_000_000.0
    print(f"Time taken: {s_taken:.3f} s")


if __name__ == "__main__":
    main()
