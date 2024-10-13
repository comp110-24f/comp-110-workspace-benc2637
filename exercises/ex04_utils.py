"""EX04 - list Utility Functions"""

__author__: str = "730658745"


def all(list: list[int], num: int) -> bool:
    if len(list) == 0:
        return False
    idx: int = 0
    while idx < len(list):  # checks if all elements match num
        if list[idx] == num:
            idx += 1
        else:
            return False
    return True


def max(list: list[int]) -> int:
    idx: int = 0
    max: int = list[idx]
    while idx < len(
        list
    ):  # updates the max value by comparing the current index with the previous max
        if list[idx] > max:
            max = list[idx]
        idx += 1
    if len(list) == 0:
        raise ValueError("max() arg is an empty List")
    return max


def is_equal(list1: list[int], list2: list[int]) -> bool:
    idx: int = 0
    if len(list1) != len(list2):
        return False
    while idx < len(list1):  # checks to see if the lists equal each other
        if list1[idx] == list2[idx]:
            idx += 1
        else:
            return False
    return True


def extend(list1: list[int], list2: list[int]) -> None:
    idx: int = 0
    while idx < len(list2):  # adds list2 to list1
        list1.append(list2[idx])
        idx += 1
