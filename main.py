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
from misc import prologue, epilogue
from misc import game_txt
from misc import report


def main():
    while True:
        prologue()
        study()
        pro1_exam()
        if report['PRO1 exam'] != 5.0:
            clt_exam()
            if report['CLT exam'] != 5.0:
                print(game_txt['epilogue_w'])
        if report['CLT exam'] == 5.0 or report['PRO1 exam'] == 5.0:
            print(game_txt['epilogue_l'])
        epilogue()


if __name__ == '__main__':
    main()
