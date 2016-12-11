"""Testing solutions for CodeWars Problem flatten me."""

import pytest

# These are the tests from code wars

# Test.assert_equals(flatten_me([1, [2, 3], 4]), [1, 2, 3, 4])
# Test.assert_equals(flatten_me([['a', 'b'], 'c', ['d']]), ['a', 'b', 'c', 'd'])
# Test.assert_equals(flatten_me(['!', '?']), ['!', '?'])
# Test.assert_equals(
#     flatten_me([[True, False], ['!'], ['?'], [71, '@']]),
#     [True, False, '!', '?', 71, '@']
# )

# These are my own tests


TEST_TABLE = [
    [[1, [2, 3], 4], [1, 2, 3, 4]],
    [[['a', 'b'], 'c', ['d']], ['a', 'b', 'c', 'd']],
    [['a', 'b'], ['a', 'b']],
    [[[True, False], ['!'], ['?'], [71, '@']], [True, False, '!', '?', 71, '@']],
]


@pytest.mark.parametrize("string, result", TEST_TABLE)
def test_flatten_me_nums(string, result):
    """Return flattened array of numbers from nested number lists."""
    from flatten_me import flatten_me
    assert flatten_me(string) == result
