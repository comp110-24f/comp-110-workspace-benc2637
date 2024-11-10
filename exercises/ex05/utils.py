"""EX05 - List Utility Functions"""

__author__ = "730658745"


def only_evens(input: list[int]) -> list[int]:
    even_list: list[int] = []
    idx: int = 0
    while idx < len(input):
        if input[idx] % 2 == 0:
            even_list.append(input[idx])
        idx += 1
    return even_list


def sub(input: list[int], start_idx: int, end_idx: int) -> list[int]:
    sub_list: list[int] = []
    idx: int = start_idx
    if start_idx < 0:
        idx = 0
    if end_idx > len(input):
        end_idx = len(input)
    if len(input) == 0 or start_idx >= len(input) or end_idx <= 0:
        return sub_list
    while idx < end_idx:
        sub_list.append(input[idx])
        idx += 1
    return sub_list


def add_at_index(input: list[int], elem_add: int, idx_add: int) -> None:
    if idx_add < 0 or idx_add > len(input):
        raise IndexError("Index is out of bounds for the input list")
    input.append(input[len(input) - 1])
    idx: int = idx_add + 1
    while idx + 1 < len(input):
        input[idx] = input[idx + 1]
        idx += 1
    input[idx_add] = elem_add
