import io
import tempfile

import pytest
from main import find_marker, iter_chars


@pytest.mark.parametrize(
    ["input", "expected"],
    [
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", (7, "jpqm")),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", (5, "vwbj")),
        ("nppdvjthqldpwncqszvftbrmjlhg", (6, "pdvj")),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", (10, "rfnt")),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", (11, "zqfr")),
    ],
)
def test_find_packet_start(input: str, expected: tuple[int, str]) -> None:
    assert find_marker(input) == expected


def test_iter_chars() -> None:
    file = io.StringIO("abcdefg")
    actual = iter_chars(file)
    assert list(actual) == ["a", "b", "c", "d", "e", "f", "g"]
