"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730658745"


def input_word() -> str:
    word: str = input("Enter a 5-character word: ")  # stores value that user types
    if len(word) == 5:
        return word
    else:
        print("Error: Word must contain 5 characters.")
        exit()  # stops the program here if true


def input_letter() -> str:
    letter: str = input("Enter a single character: ")
    if len(letter) == 1:
        return letter
    else:
        print("Error: Character must be a single character.")
        exit()


def contains_char(word: str, letter: str) -> None:
    index: int = 0
    instances: int = 0
    print("Searching for", letter, "in", word)
    while index < len(word):  # checking for all matching characters 1-4
        if word[index] == letter:
            print(letter, "found at index", index)
            instances += 1  # increases the instances by 1 when true
        index += 1
    if instances > 1:
        print(instances, "instances of", letter, "found in", word)
    elif instances == 1:
        print(instances, "instance of", letter, "found in", word)
    else:
        print("No instances of", letter, "found in", word)


def main() -> None:  # makes it so that we don't have to type the thing below
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
