# Lab02avst.py
# This is the Student, Starting file of Lab02a.
# The Quarter, Dime & Nickel Program
#
def main() -> None:
    for quarters in range(3): # 0 - 2 quarters (2 is max)
        for dimes in range(6): # 0 - 5 dimes
            for nickels in range(11): # 0 - 10 nickels
                if quarters * 25 + dimes * 10 + nickels * 5 == 50:
                    print(f"{quarters} Quarters {dimes} dimes {nickels} nickels == 50 cents")


if __name__ == "__main__":
    main()