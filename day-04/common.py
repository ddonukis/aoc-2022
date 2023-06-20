import sys
from pathlib import Path


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
