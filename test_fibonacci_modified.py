import pytest

from fibonacci_modified import get_nth_term


@pytest.mark.parametrize(
    't1, t2, N, expected_result', [
        (0, 1, 5, 5),
    ]
)
def test_get_nth_term(t1, t2, N, expected_result):
    assert get_nth_term(t1, t2, N) == expected_result
