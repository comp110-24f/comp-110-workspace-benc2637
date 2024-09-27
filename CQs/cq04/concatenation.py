"""Importing + scope challenge question"""

__author__: str = "730658745"


def concat(str1: str, str2: str) -> str:
    return str1 + str2


word1: str = "happy"
word2: str = "tuesday"

if __name__ == "__main__":  # occurs when ran but not when imported
    concat(word1, word2)
