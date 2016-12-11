"""Tests for codewars problem what century is it?."""

import pytest

# These are the tests from code wars

# test.expect(whatCentury(2200), '23rd')

# These are my own tests

CENTURY_TABLE = [
    [1000, '10th'],
    [1110, '12th'],
    [1210, '13th'],
    [1310, '14th'],
    [1400, '14th'],
    [1510, '16th'],
    [2000, '20th'],
    [2016, '21st'],
    [2101, '22nd'],
    [2203, '23rd'],
    [2307, '24th'],
]


@pytest.mark.parametrize("year, result", CENTURY_TABLE)
def test_what_century(year, result):
    """Return century of the given year."""
    from what_century import what_century
    assert what_century(year) == result
