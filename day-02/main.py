import enum
import sys
from pathlib import Path


class Pick(enum.IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Outcome(enum.IntEnum):
    LOSS = 0
    DRAW = 3
    WIN = 6


def get_input_file() -> Path:
    try:
        input_file_path = sys.argv[1]
    except IndexError:
        print("Please provide input data file path")
        sys.exit(1)

    if not ((input_data := Path(input_file_path)).exists() and input_data.is_file()):
        print("Please provide valid input data file path")
        sys.exit(1)

    return input_data


def parse_code(code: str) -> Pick:
    match code:
        case "A" | "X":
            return Pick.ROCK
        case "B" | "Y":
            return Pick.PAPER
        case "C" | "Z":
            return Pick.SCISSORS
        case _:
            raise ValueError(f"Invalid code: {code}")


def get_outcome(opponent, me) -> Outcome:
    match (me, opponent):
        case (Pick.ROCK, Pick.SCISSORS):
            return Outcome.WIN
        case (Pick.PAPER, Pick.ROCK):
            return Outcome.WIN
        case (Pick.SCISSORS, Pick.PAPER):
            return Outcome.WIN
        case (m, o) if m == o:
            return Outcome.DRAW
        case _:
            return Outcome.LOSS


def parse_round(line: str) -> tuple[Pick, Pick]:
    opponent, me = line.strip().split(" ")
    return parse_code(opponent), parse_code(me)


def score_round(opponents_pick: str, my_pick: str) -> int:
    outcome = get_outcome(opponents_pick, my_pick)
    return outcome + my_pick


def main():
    input_data = get_input_file()

    total = 0
    with input_data.open() as f:
        for line in f:
            opponent, me = parse_round(line)
            score = score_round(opponent, me)
            total += score

    print(f"Total score: {total}")


if __name__ == "__main__":
    main()
