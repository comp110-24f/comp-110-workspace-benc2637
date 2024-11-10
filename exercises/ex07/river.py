"""File to define River class."""

__author__ = "730658745"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """River class."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Removes fish that are over 3 years old and removes bears that are over 5."""
        fish_copy = self.fish.copy()  # copied list since to remove elements easier
        bears_copy = self.bears.copy()
        for fish in self.fish:
            if fish.age > 3:
                fish_copy.remove(
                    fish
                )  # removes first occurence of a specified element in a list
        for bear in self.bears:
            if bear.age > 5:
                bears_copy.remove(bear)
        self.fish = fish_copy  # updates self.fish
        self.bears = bears_copy
        return None

    def remove_fish(self, amount: int):
        """Removes fish from the list."""
        if amount > len(
            self.fish
        ):  # handles when the amount given is greater than the length of the list
            amount = len(self.fish)
        for _ in range(amount):
            self.fish.pop(0)
        return None

    def bears_eating(self):
        """If 5 or more fish are in the river a bear will eat 3."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None

    def check_hunger(self):
        """Removes bears that have a hunger score of 0."""
        surviving_bears: list = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                surviving_bears.append(bear)
        self.bears = surviving_bears
        return None

    def repopulate_fish(self):
        """Every pair of fish will have 4 offspring."""
        pairs = len(self.fish) // 2  # // handles an odd number of fish
        offspring = pairs * 4
        for _ in range(offspring):
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        """Every pair of bears will have 1 offspring."""
        pairs = len(self.bears) // 2  # handles an odd number of bears
        for _ in range(pairs):
            self.bears.append(Bear())
        return None

    def view_river(self):
        """View fish and bear population on x day."""
        print("~~~ Day " + str(self.day) + ": ~~~")
        print("Fish population: " + str(len(self.fish)))
        print("Bear population: " + str(len(self.bears)))
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulate one week of life in the river."""
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        return None
