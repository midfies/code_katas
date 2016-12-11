"""Testing solutions for CodeWars Problem flatten me."""

# These are the tests from code wars

# Test.assert_equals(flatten_me([1, [2, 3], 4]), [1, 2, 3, 4])
# Test.assert_equals(flatten_me([['a', 'b'], 'c', ['d']]), ['a', 'b', 'c', 'd'])
# Test.assert_equals(flatten_me(['!', '?']), ['!', '?'])
# Test.assert_equals(
#     flatten_me([[True, False], ['!'], ['?'], [71, '@']]),
#     [True, False, '!', '?', 71, '@']
# )

# These are my own tests


def test_flatten_me_nums():
    """Return flattened array of numbers from nested number lists."""
    from flatten_me import flatten_me
    assert flatten_me([1, [2, 3], 4]) == [1, 2, 3, 4]


def test_flatten_me_letters():
    """Return flattened array of numbers from nested number lists."""
    from flatten_me import flatten_me
    assert flatten_me([['a', 'b'], 'c', ['d']]) == ['a', 'b', 'c', 'd']


def test_flatten_me_unnessted():
    """Return flattened array of numbers from nested number lists."""
    from flatten_me import flatten_me
    assert flatten_me(['a', 'b']) == ['a', 'b']


def test_flatten_me_mixed():
    """Return flattened array of numbers from nested number lists."""
    from flatten_me import flatten_me
    assert flatten_me([[True, False], ['!'], ['?'], [71, '@']]) == [True, False, '!', '?', 71, '@']
