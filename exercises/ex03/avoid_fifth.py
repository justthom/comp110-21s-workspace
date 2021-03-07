"""EX03 - avoid_fifth function."""

__author__: str = "730336470"

def main() -> None:
    """Entrypoint of the program."""
    print(avoid_fifth("Ellen went to the state fair to eat the funnel cakes."))
    print(avoid_fifth("Audre Lorde wrote ''The Master's Tools Will Never Dismantle the Master's House.''"))
    print(avoid_fifth(input("Type a sentence:\n")))
    # Put print statements here to test your function
    # ex. print(avoid_fifth("hello there"))

def avoid_fifth(a: str) -> str:
    for i in 'Ee':
        return a.translate({ord(i): None for i in 'eE'})

if __name__ == "__main__":
    main()