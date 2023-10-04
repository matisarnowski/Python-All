#! python3
from randomQuizCountryGenerator import *


def main():
    total = play_total()
    with open("Wynik.txt", "a+") as total_total:
        total_total.write(total)
    print("Hello World!")
    return 0


if __name__ == "__main__":
    main()
