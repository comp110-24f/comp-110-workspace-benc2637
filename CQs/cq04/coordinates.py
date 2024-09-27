"""Importing + scope challenge question"""

__author__: str = "730658745"


def get_coords(xs: str, ys: str) -> None:
    index1: int = 0
    while index1 < len(xs):
        index2: int = 0  # has to be inside to reset counter
        while index2 < len(ys):
            print("(" + xs[index1] + "," + ys[index2] + ")")
            index2 += 1
        index1 += 1  # will continue until xs has gone through all its characters
