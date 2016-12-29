"""Testing for code wars sort a deck of cards."""

import pytest

TERM_TABLE = [
    [['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K'], ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']],
    [['K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'A'], ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']],
    [['A', '5', 'K', 'A', '5', 'K', 'A', '5', 'K', 'A', '5', 'K', 'K'], ['A', 'A', 'A', 'A', '5', '5', '5', '5', 'K', 'K', 'K', 'K', 'K']],
    [['3', '8', 'A', 'K'], ['A', '3', '8', 'K']]
]


@pytest.mark.parametrize("c, result", TERM_TABLE)
def test_sort_deck(c, result):
    """Test sort deck return the deck in order."""
    from sort_deck import sort_cards
    assert sort_cards(c) == result
