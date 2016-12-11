"""Codewars problem for summing all numbers found in a string."""

import re


def sum_from_string(str):
    """Return the sum of all numbers found in string."""
    return sum(int(x) for x in re.sub("\D", " ", str).split())
