"""An exercise in remainders and boolean logic."""

__author__ = "730336470"


# Begin your solution here...
value: int = int(input("Enter an integer: "))
if value % 14 == 0:
    print("TAR HEELS")
else:
    if value % 2 == 0:
        print("TAR")
    else:
        if value % 7 == 0:
            print("HEELS")
        else:
            print("CAROLINA")