"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730336470"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    # TODO 2: Print the result of calling your fortune_cookie function.
    print(fortune_cookie(randint(1,100)))
    print("Now, go spread positive vibes!")


# TODO 1: Define your fortune_cookie function here.
def fortune_cookie(a: int) -> str:
    if a < 40:
        if a < 20:
            return "You are going to move mountains!"
        else:
            return "Good things are coming your way!"
    else:
        if a < 60:
            return "You shouldn't seek advice from fortune cookies."
        if a > 80:
            return "The stars of riches are watching over you."
        else:
            return "Life is a performance."
# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()