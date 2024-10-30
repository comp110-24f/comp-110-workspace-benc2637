"""EX06 - Dictionary Utility Functions"""

__author__ = "730658745"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    new_dict: dict[str, str] = {}
    for key in input_dict:
        value = input_dict[key]
        if (
            value in new_dict
        ):  # indentation is important. If the value is already in the dict it will raise an error
            raise KeyError("All keys must be unique!")
        new_dict[value] = key
    return new_dict


def favorite_color(input_dict: dict[str, str]) -> str:
    if not input_dict:
        return ""
    color_num = {}
    order = []
    max = 0
    favorite = ""
    for name in input_dict:
        color = input_dict[name]  # the color is the value of each key
        if color not in color_num:
            color_num[color] = 0
            order.append(color)  # adds colors not already in the list
        color_num[color] += 1
    for color in order:
        if (
            color_num[color] > max
        ):  # updates the max to find the color that appears the most
            max = color_num[color]
            favorite = color
    return favorite


def count(input_list: list[str]) -> dict[str, int]:
    if not input_list:  # empty list case
        return {}
    new_dict: dict[str, int] = {}
    for item in input_list:
        if item in new_dict:
            new_dict[item] += 1  # add if its already in the dict
        else:
            new_dict[item] = 1  # if not initialize
    return new_dict


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    new_dict: dict[str, list[str]] = {}
    for word in words:
        if word:
            initial = word[0].lower()  # .lower returns lowercase string
            if initial not in new_dict:
                new_dict[initial] = []
            new_dict[initial].append(word)
    return new_dict


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    if day not in attendance:
        attendance[day] = (
            []
        )  # adding empty lists for days not already in the attendance dictionary
    if student not in attendance[day]:
        attendance[day].append(student)
    return None
