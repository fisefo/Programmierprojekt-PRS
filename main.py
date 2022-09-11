# Elisa Lübbers
# 16.08.2022
# This file is where all main functions necessary for the game are called to avoid clutter.
"""
Created on Tue Aug 16 2022

This file contains the function-calls for the main stages
of the game (prologue, studying, PRO1 exam, CLT exam, epilogue)
to show the structure of the game and avoid clutter.

@author: Elisa Lübbers
"""


from studying import study
from misc import prologue


def main():
    prologue()
    study()
    print('you will now take the Pro1 exam.')


if __name__ == '__main__':
    main()
