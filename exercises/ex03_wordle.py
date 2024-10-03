"""EX03 - Wordle - Guess the word in 6 tries"""

__author__: str = "730658745"


def main(secret: str) -> None:  # draws all the functions together
    """The entrypoint of the program and main game loop."""
    idx: int = 0
    turns: int = 6
    while idx < turns:
        input: str = input_guess(len(secret))
        print(("=== Turn " + str(idx + 1) + "/6 ==="))
        print(
            emojified(input, secret)
        )  # returns the result of the guess using emojified function
        if input == secret:
            print("You won in " + str(idx + 1) + "/6 turns!")  # when you win
            return
        idx += 1
    else:
        print("X/6 - Sorry, try again tomorrow!")  # when you lose
        return


def input_guess(secret_word_len: int) -> str:
    guess: str = input(
        "Enter a " + str(secret_word_len) + " character word:"
    )  # prompts for an input
    while len(guess) != secret_word_len:
        guess = input(
            "That wasn't " + str(secret_word_len) + " chars! Try again:"
        )  # will continue to ask until it is the correct length
    else:
        return guess


"""Tests to see if the character is in the secret word"""


def contains_char(secret_word: str, char_guess: str) -> bool:
    assert len(char_guess) == 1
    idx: int = 0
    instances: int = 0
    while idx < len(secret_word):
        if secret_word[idx] == char_guess:  # tracks if the character matches the secret
            instances += 1  # stores the number of instances
        idx += 1
    if instances >= 1:
        return True
    else:
        return False


"""Compare the length of the guess and the secret word"""


def emojified(guess: str, secret: str) -> str:
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index: int = 0
    emoji_list: str = ""  # compiles the boxes together into a string
    while index < len(guess):
        if secret[index] == guess[index]:  # green box if they match
            emoji_list += GREEN_BOX
        elif contains_char(
            secret_word=secret, char_guess=guess[index]
        ):  # yellow if it's in the wrong place
            emoji_list += YELLOW_BOX
        else:  # when it's not in the word
            emoji_list += WHITE_BOX
        index += 1
    return emoji_list


if __name__ == "__main__":
    main(secret="codes")
