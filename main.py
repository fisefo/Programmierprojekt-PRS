"""
Created on Tue Aug 16 2022

This file contains the function-calls for the main stages
of the PRS 2022 final project to show the structure of the game and avoid clutter.
The main stages are: Beginning the semester (Prologue), Studying, Pro1 exam, CLT exam, Final state (Epilogue)

@author: Elisa Lübbers
"""
from studying import study
from pro1 import pro1_exam
from clt import clt_exam
from misc import prologue


def main():
    # prologue()
    # study()
    # pro1_exam()
    clt_exam()


if __name__ == '__main__':
    main()
