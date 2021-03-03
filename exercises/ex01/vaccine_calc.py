"""A vaccination calculator."""

__author__ = "YOUR PID HERE"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
population: int = int(input("Enter Population: "))
doses_administered: int = int(input("Ender Doses Administered: "))
doses_per_day: int = int(input("Number of doses given per day her on out: "))
target_percent_vaccinated: int = int(input("Target percent of population vaccinated: "))
today: datetime = datetime.today()
one_day: timedelta = timedelta(1)
tomorrow: datetime = today + one_day
fortnight: timedelta = timedelta(7 + 7)
future: datetime = today + fortnight


if target_percent_vaccinated < 101:
    print("We will reach" + target_percent_vaccinated + "in" + days_passed + ", which falls on" +