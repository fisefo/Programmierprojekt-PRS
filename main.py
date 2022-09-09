# Elisa Lübbers
# 16.08.2022
# This file is where all main functions necessary for the game are called to avoid clutter.
import sys

from studying import study
from miscellaneous import prologue


def main():
    prologue()
    study()
    print('you will now take the Pro1 exam.')


if __name__ == '__main__':
    main()
