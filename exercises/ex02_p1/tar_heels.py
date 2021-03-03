"""Tar Heels exercise redux as a structured program."""

__author__ = "730336470"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    choice: int = int(input("Enter an int: "))
    # TODO 2: Print the response of calling the tar_heels function here.
    print(tar_heels(choice))


# TODO 1: Define the tar_heels function, and its logic, here.
def tar_heels(a: int) -> str:
    if a % 14 == 0:
        return str("TAR HEELS")
    else:
        if a % 2 == 0:
            return str("TAR")
        else:
            if a % 7 == 0:
                return str("HEELS")
            else:
                return str("CAROLINA")

if __name__ == "__main__":
    main()
