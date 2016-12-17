"""Implemetation of a queue data structure."""


from doubly_linked_list import Dll


class Queue():
    """Class to represent the queue data structure."""

    def __init__(self):
        """Initialize a queue."""
        self._queue = Dll()

    def enqueue(self, val):
        """Add a value to the tail of the queue."""
        self._queue.append(val)

    def dequeue(self):
        """Remove the head of the queue and return its value."""
        return self._queue.pop()
