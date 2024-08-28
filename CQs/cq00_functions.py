"""Functions challenge question"""

__author__ = "730658745"


def mimic(message: str) -> str:
    """It will take the input and repeat it back"""
    return message


def main() -> None:
    """The main function will pull together the functions into a main function that implements the logic"""
    print(mimic(message=input("What is your message?")))
    return None


if __name__ == "__main__":
    main()
