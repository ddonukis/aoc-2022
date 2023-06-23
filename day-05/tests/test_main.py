import pytest

from main import (
    Command,
    Crate,
    State,
    iter_str_slices,
    parse_commands,
    parse_crates,
    parse_crates_level,
    simulate_commands,
)


@pytest.mark.parametrize(
    ["input", "expected"],
    [
        ("    [D]", ["   ", "[D]"]),
        ("[Z] [M] [P]", ["[Z]", "[M]", "[P]"]),
        ("", []),
        ("    [A] [B]     [C]", ["   ", "[A]", "[B]", "   ", "[C]"]),
    ],
)
def test_iter_str_slices(input: str, expected: list[str]) -> None:
    assert expected == list(iter_str_slices(input))


@pytest.mark.parametrize(
    ["line", "expected"],
    [
        ("    [D]", [Crate(1, "D")]),
        ("[Z] [M] [P]", [Crate(0, "Z"), Crate(1, "M"), Crate(2, "P")]),
        ("", []),
        ("    [A] [B]     [C]", [Crate(1, "A"), Crate(2, "B"), Crate(4, "C")]),
    ],
)
def test_parse_crates_level(line: str, expected: list[Crate]) -> None:
    assert expected == parse_crates_level(line)


def test_parse_crates() -> None:
    raw_lines = [
        "    [D]",
        "[N] [C]",
        "[Z] [M] [P]",
        " 1   2   3",
    ]
    expected = (
        ["Z", "N"],
        ["M", "C", "D"],
        ["P"],
    )
    assert expected == parse_crates(raw_lines)


def test_parse_commands() -> None:
    raw_lines = [
        "move 1 from 1 to 2",
        "move 4 from 3 to 4",
        "move 42 from 1 to 199",
    ]
    expected = [
        Command(1, 0, 1),
        Command(4, 2, 3),
        Command(42, 0, 198),
    ]
    assert expected == list(parse_commands(raw_lines))


@pytest.mark.parametrize(
    ["initial_state", "commands", "expected"],
    [
        ((["A"], []), [Command(1, 0, 1)], ([], ["A"])),
        ((["A", "B"], []), [Command(2, 0, 1)], ([], ["B", "A"])),
        ((["A", "B"], ["C"], []), [Command(2, 0, 2), Command(1, 1, 0)], (["C"], [], ["B", "A"])),
    ],
)
def test_simulate_commands(initial_state: State, commands: list[Command], expected: State) -> None:
    state = simulate_commands(initial_state, commands)
    assert expected == state
    for a, b in zip(initial_state, state):
        assert id(a) != id(b)
