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


def get_outcome(opponent: Pick, me: Pick) -> Outcome:
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


def score_round(opponents_pick: Pick, my_pick: Pick) -> int:
    outcome = get_outcome(opponents_pick, my_pick)
    return outcome + my_pick


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
