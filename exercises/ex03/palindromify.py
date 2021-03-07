"""EX03 - palindromify function."""

__author__: str = "730336470"


def main() -> None:
    """Entrypoint of the program."""
    print(palindromify("bi", False))
    print(palindromify("nu", False))
    print(palindromify("el", True))
    print(palindromify("na", True))
    # Put print statements here to test your function
    # ex. print(palindromify("race", false))

def palindromify(a: str, b: bool) -> str:
    if b == True:
        return evenpal(a)
    else:
        return oddpal(a)

def evenpal(a: str) -> str:
    reverse: str = a[::-1]
    pal: str = a + reverse
    return pal

def oddpal(a: str) -> str:
    reverse: str = a[::-1]
    pal: str = a[:-1] + reverse
    return pal

if __name__ == "__main__":
    main()