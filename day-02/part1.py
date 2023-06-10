from common import Outcome, Pick, get_input_file


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


def parse_round(line: str) -> tuple[Pick, Pick]:
    opponent, me = line.strip().split(" ")
    return parse_code(opponent), parse_code(me)


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
