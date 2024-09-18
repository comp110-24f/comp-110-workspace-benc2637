"""While loops challenge questeion"""

__author__ = "730658745"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0
    instances: int = 0
    while count < len(phrase):
        if phrase[count] == search_char:
            instances += 1
        count += 1
    return instances
