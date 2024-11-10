"""File to define Bear class."""

__author__ = "730658745"


class Bear:
    """Bear class."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initializes bear attributes."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Increases age by 1."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Increases hunger score based on number of fish consumed."""
        self.hunger_score += num_fish
        return None
