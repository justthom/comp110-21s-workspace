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
    days_to_target: float = float(days_to_target())
    # TODO 4: Call future_date and store result in a variable.
    future_date: str = str(future_date())
    # TODO 5: Print the expected output using the variables above.
    print("We will reach" + target + "% vaccination in" + days_to_target + "days, on" + future_date)
    


# TODO 1: Define days_to_target function
def days_to_target(population: int, doses: int, doses_per_day: int, target: int) -> float:
    d: float = float((population * (target / 100 ) - doses)/ doses_per_day)
    return d


# TODO 3: Define future_date function
def future_date(d: float) -> str:
    today: datetime = datetime.today
    one_day: timedelta = timedelta(1)
    future: datetime = d * one_day + today
    return future


if __name__ == "__main__":
    main()
