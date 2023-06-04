import sys
from pathlib import Path


try:
    input_file_path = sys.argv[1]
except IndexError:
    print("Please provide input data file path")
    sys.exit(1)

if not ((input_data := Path(input_file_path)).exists() and input_data.is_file()):
    print("Please provide valid input data file path")
    sys.exit(1)

totals = [0]
with input_data.open() as f:
    for line in f:
        line = line.strip()

        if not line:
            totals.append(0)
            continue

        totals[-1] += int(line)


def top_n_totals(input: list, n: int) -> int:
    return sum(sorted(totals, reverse=True)[:n])


print(f"Max total calories: {max(totals)}")
print(f"Top 3 total calories: {top_n_totals(totals, 3)}")
