"""Codewars Sum of the first nth term of series."""


def series_sum(n):
    """Return the nth term of the series: 1 + 1/4 + 1/7 + 1/10 + 1/13."""
    total = 0
    for i in range(n):
        total += 1.0 / (3 * i + 1)
    return '%.2f' % total
