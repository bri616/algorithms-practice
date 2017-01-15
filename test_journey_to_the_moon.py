import pytest

from journey_to_the_moon import get_combinations


@pytest.mark.parametrize(
    'N, l, list_of_pairs, expected_result', [
        (
            10,
            7,
            (
                [0, 2],
                [1, 8],
                [1, 4],
                [2, 8],
                [2, 6],
                [3, 5],
                [6, 9],

            ),
            23,
        ),
        (
            4,
            0,
            (),
            6,
        ),
        (
            4,
            2,
            (
                [0, 1],
                [2, 3],
            ),
            4,
        ),
        (
            100000,
            2,
            (
                [1, 2],
                [3, 4],
            ),
            4999949998,
        ),
    ]
)
def test_get_combinations(N, l, list_of_pairs, expected_result):
    assert get_combinations(N, l, list_of_pairs) == expected_result
