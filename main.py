# Lab02avst.py
# This is the Student, Starting file of Lab02a.
# The Quarter, Dime & Nickel Program
#
from math import floor


def main() -> None:
    cents: int = eval(input("Enter # of cents:"))
    for quarters in range(floor(cents / 25) + 1): # 0 - 2 quarters (2 is max)
        for dimes in range(floor(cents / 10) + 1): # 0 - 5 dimes
            for nickels in range(floor(cents / 5) + 1): # 0 - 10 nickels
                if quarters * 25 + dimes * 10 + nickels * 5 == cents:
                    print(f"{quarters} Quarters {dimes} dimes {nickels} nickels == {cents} cents")


if __name__ == "__main__":
    main()