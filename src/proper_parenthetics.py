"""A function to determine if proper parenthetics are used in text."""

from queue import Queue


def is_proper(string):
    """Return 0 if proper parethesis use, 1 if left open, -1 if improper."""
    q = Queue()
    state = 0
    for char in string:
        if char in ['(', ')']:
            q.enqueue(char)
    while q._queue.head:
        if q.dequeue() == '(':
            state += 1
        else:
            state -= 1
        if state < 0:
            return -1
    if state:
        return 1
    return 0
