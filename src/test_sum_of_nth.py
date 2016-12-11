"""Testing for codewars sum_of_nth term in a series."""

import pytest

# These are the tests from code wars

# Test.assert_equals(series_sum(1), "1.00")
# Test.assert_equals(series_sum(2), "1.25")
# Test.assert_equals(series_sum(3), "1.39")

# These are my own tests

TERM_TABLE = [
    [1, '1.00'],
    [2, '1.25'],
    [3, '1.39'],
    [5, '1.57'],
    [0, '0.00'],

]


@pytest.mark.parametrize("n, result", TERM_TABLE)
def test_series_sum(n, result):
    """Test series sum returns string equal to nth term of given series."""
    from sum_of_nth import series_sum
    assert series_sum(n) == result
