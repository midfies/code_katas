"""Tests for codewars problem sum from string."""

import pytest

# These are the tests from code wars

# test.assert_equals(sum_from_string("In 2015, I want to know how much does iPhone 6+ cost?"),2021)
# test.assert_equals(sum_from_string("1+1=2"),4)
# test.assert_equals(sum_from_string("e=mc^2"),2)

# These are my own tests

SUM_STRING_TABLE = [
    ["In 2015, I want to know how much does iPhone 6+ cost?", 2021],
    ["1+1=2", 4],
    ["e=mc^2", 2],
    ["There are no numbers in this string", 0],
]


@pytest.mark.parametrize("string, result", SUM_STRING_TABLE)
def test_sum_from_string(string, result):
    """Return sum of long string."""
    from sum_from_string import sum_from_string
    assert sum_from_string(string) == result
