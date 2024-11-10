"""File to define Fish class."""

__author__ = "730658745"


class Fish:
    """Fish class."""

    age: int

    def __init__(self):
        """Initializing fish attributes."""
        self.age = 0
        return None

    def one_day(self):
        """Increases age by 1."""
        self.age += 1
        return None
