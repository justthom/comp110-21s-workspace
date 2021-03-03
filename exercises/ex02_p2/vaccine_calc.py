"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "730336470"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))
    # TODO 2: Call days_to_target and store result in a variable.
    d: int = int(days_to_target(population, doses, doses_per_day, target))
    # TODO 4: Call future_date and store result in a variable.
    future: str = str(future_date(d))
    # TODO 5: Print the expected output using the variables above.
    print("We will reach" + target + "% vaccination in" + d + "days, on" + future + ".")
    


# TODO 1: Define days_to_target function
def days_to_target(population: int, doses: int, doses_per_day: int, target: int) -> int:
    d: int = int((population * (target/100) - doses)/ doses_per_day)
    return d


# TODO 3: Define future_date function
def future_date(d: int) -> str:
    today: datetime = datetime.today
    days_to_pass: timedelta = timedelta(d)
    future: datetime = days_to_pass + today
    return future


if __name__ == "__main__":
    main()
