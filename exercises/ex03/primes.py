"""EX03 - prime functions."""

__author__: str = "730336470"


def main() -> None:
    """Entrypoint of the program."""
    # Put print statements here to test your function
    # ex. print(is_prime(5)), print(list_primes(10, 20))
    print(is_prime(17))
    print(is_prime(10))
    print(is_prime(-13))
    print(list_primes(2,100))

def is_prime(a: int) -> bool:
    if a > 1:
        for i in range(2, a):
            if (a % i) == 0:
                return False
        else:
            return True
    else:
        return False

def list_primes(a: int, b: int) -> list[int]:
    primenum = []
    for n in range(a, b - 1):
        if n > 1:
            for i in range(2, n):
                if (n % i) == 0:
                    break
            else:
                primenum.append(n)
    return primenum


if __name__ == "__main__":
    main()