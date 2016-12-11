"""Codewars Sum of the first nth term of series."""


def series_sum(n):
    """Return the nth term of the series : 1 + 1/4 + 1/7 + 1/10 + 1/13."""
    sum = 0
    for i in range(n):
        sum += 1.0 / (3 * i + 1)
    return '%.2f' % sum

print(series_sum(5))
