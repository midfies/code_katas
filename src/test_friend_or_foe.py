"""Tests for codewars Crazed Templating."""

import pytest

# These are the tests from code wars

# Test.assert_equals(friend(["Ryan", "Kieran", "Mark",]), ["Ryan", "Mark"])

# These are my own tests

FRIEND_TABLE = [
    [["Ryan", "Kieran", "Mark"], ["Ryan", "Mark"]],
    [["Billy", "Kieran", "Markus"], []],
    [["Bill", "Marc", "Mark", "Paul"], ["Bill", "Marc", "Mark", "Paul"]],
]


@pytest.mark.parametrize("people, result", FRIEND_TABLE)
def test_friend_or_foe(people, result):
    """Test friend function which returns array of names with four letters."""
    from friend_or_foe import friend
    assert friend(people) == result
