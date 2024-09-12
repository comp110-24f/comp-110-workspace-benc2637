"""Calculating # of teabags, treats, and cost based on the # of guests"""

__author__: str = "730658745"


def main_planner(guests: int) -> None:
    """pulls together all the functions below and prints their output"""
    print("A Cozy Tea Party for", guests, "People!")
    print("Tea bags:", tea_bags(people=guests))  # must specify the argument people
    print("Treats:", treats(people=guests))
    print(
        "Cost: $",
        cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests)),
        sep="",
    )  # must specify the arguments


def tea_bags(people: int) -> int:
    """# of teabags based on # of guests"""
    return people * 2


def treats(people: int) -> int:
    """# of treats based on # of guests"""
    return int(
        (tea_bags(people=people) * 1.5)
    )  # seems silly but the value for people has to equal the argument for treats which is also people


def cost(tea_count: int, treat_count: int) -> float:
    """combined cost of teabags and treats"""
    return tea_count * 0.50 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
