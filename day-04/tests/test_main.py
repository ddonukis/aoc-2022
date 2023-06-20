import pytest

from main import Interval, contained_intervals, overlapping_intervals


class TestInterval:
    @pytest.mark.parametrize(
        ["s", "expected"],
        [
            ("1-2", Interval(start=1, end=2)),
            ("21-13", Interval(start=13, end=21)),
        ],
    )
    def test_from_string(self, s, expected):
        assert Interval.from_string(s) == expected

    @pytest.mark.parametrize("s", ["a-b", "one-two"])
    def test_invalid_inputs(self, s):
        with pytest.raises(ValueError):
            Interval.from_string(s)


class TestContainingIntervals:
    @pytest.mark.parametrize(
        ["a", "b"],
        [
            (Interval(1, 10), Interval(1, 1)),
            (Interval(1, 10), Interval(2, 8)),
            (Interval(2, 8), Interval(1, 10)),
        ],
    )
    def test_true(self, a, b):
        assert contained_intervals(a, b) is True

    @pytest.mark.parametrize(
        ["a", "b"],
        [
            (Interval(1, 10), Interval(11, 12)),
            (Interval(2, 3), Interval(3, 5)),
            (Interval(2, 8), Interval(3, 10)),
        ],
    )
    def test_false(self, a, b):
        assert contained_intervals(a, b) is False


class TestOverlappingIntervals:
    @pytest.mark.parametrize(
        ["a", "b"],
        [
            (Interval(1, 10), Interval(1, 1)),
            (Interval(1, 10), Interval(2, 8)),
            (Interval(2, 8), Interval(1, 10)),
            (Interval(2, 3), Interval(3, 5)),
            (Interval(2, 8), Interval(3, 10)),
        ],
    )
    def test_true(self, a, b):
        assert overlapping_intervals(a, b) is True

    @pytest.mark.parametrize(
        ["a", "b"],
        [
            (Interval(1, 10), Interval(11, 12)),
            (Interval(3, 4), Interval(9, 20)),
        ],
    )
    def test_false(self, a, b):
        assert contained_intervals(a, b) is False
