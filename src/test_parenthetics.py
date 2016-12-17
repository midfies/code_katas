"""Tests for proper_parenthetics."""

import pytest

PAREN_TABLE = [
    ["This ( is ( only ) a ) test", 0],
    ["()()()", 0],
    ["(a(b(c(d(e(f(g(h(i(j(k(l(mn)o)p)q)r)s)t)u)v)w)x)y)z)", 0],
    [")fail right now(", -1],
    ["(fail at the end))", -1],
    ["()fail())()too()", -1],
    ["))))((((", -1],
    ["(", 1],
    ["(left open)at the end(", 1],
    ["(((()))", 1],
    ["How (many( ways ( to make) a mistake)", 1],
]


@pytest.mark.parametrize("string, result", PAREN_TABLE)
def test_is_proper(string, result):
    """Test if string has valid parenthetics."""
    from proper_parenthetics import is_proper
    assert is_proper(string) == result
