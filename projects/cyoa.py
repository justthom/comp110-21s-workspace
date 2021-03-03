"""THE NOURISHING AND DELICIOUS, LUXURY PARFAIT STAND"""

__author__ = "730336470"

from random import randint

def main () -> None:
    player: str = input(greet())
    points: int = int(input(f"NOW, { player }, HOW MUCH MONEY HAVE YOU GOT IN YOUR WALLET?  (PLEASE ENTER AN INTERGER): "))
    base: int = int(input(f"WHAT TYPE OF YOGURT WOULD YOU LIKE THE BASE TO YOUR PARFAIT, { player }: (1) WHOLE MILK VANILLA, (2) GREEK VANILLA, OR (3)LOW-FAT VANILLA?" ))
    RUNNING_MAN: str = str(f"\U0001F3C3")
    if base == 3:
        print(f"{ player }, YOU HAVE ${ points - points } REMAINING! SEE YA SUCKER! { RUNNING_MAN }")
    else:
        if base == 2:
            fruittopping(int(input(f"{ player }, DO YOU PREFER (1) STRAWBERRIES OR (2) BANANAS?  (PLEASE INPUT AND INTERGER) ")))
        else:
            candy()
    

def fruittopping(a: int) -> int:
    if a < 2:
        input(candy())
    else:
        input(candy())

def candy() -> str:
    print("WOULD YOU LIKE CANDY?  (YES/NO)  ")

def greet() -> None:
    print("HELLO AND WELCOME TO MY NOURISHING AND DELICIOUS, LUXURY PARFAIT STAND, WHERE YOU CAN BUILD YOUR OWN PARFAIT!  WHAT'S YOUR NAME? ")

if __name__ == "__main__":
    main()