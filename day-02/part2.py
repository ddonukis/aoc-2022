from common import Outcome, Pick, get_input_file


def parse_pick(s: str) -> Pick:
    match s:
        case "A":
            return Pick.ROCK
        case "B":
            return Pick.PAPER
        case "C":
            return Pick.SCISSORS
        case _:
            raise ValueError(f"Invalid pick code: {s}")


def parse_outcome(s: str) -> Outcome:
    match s:
        case "X":
            return Outcome.LOSS
        case "Y":
            return Outcome.DRAW
        case "Z":
            return Outcome.WIN
        case _:
            raise ValueError(f"Invalid outcome code: {s}")


def parse_line(line: str) -> tuple[Pick, Outcome]:
    raw_pick, raw_outcome = line.strip().split()

    return parse_pick(raw_pick), parse_outcome(raw_outcome)


def get_my_pick(outcome: Outcome, opponent: Pick) -> Pick:
    match (outcome, opponent):
        case (Outcome.LOSS, Pick.ROCK):
            return Pick.SCISSORS
        case (Outcome.LOSS, Pick.PAPER):
            return Pick.ROCK
        case (Outcome.LOSS, Pick.SCISSORS):
            return Pick.PAPER
        case (Outcome.WIN, Pick.ROCK):
            return Pick.PAPER
        case (Outcome.WIN, Pick.PAPER):
            return Pick.SCISSORS
        case (Outcome.WIN, Pick.SCISSORS):
            return Pick.ROCK
        case _:  # draw
            return opponent


def score_round(outcome: Outcome, opponent: Pick) -> int:
    return outcome + get_my_pick(outcome, opponent)


def main() -> None:
    input_data = get_input_file()

    total = 0
    with input_data.open() as f:
        for line in f:
            opponents_pick, outcome = parse_line(line)
            total += score_round(outcome, opponents_pick)

    print(f"Total score: {total}")


if __name__ == "__main__":
    main()
