#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 2022

This file contains the function-calls for the main stages
of the PRS 2022 final project (also referred to as "game") to show the structure of the game and avoid clutter.
The main stages are: Beginning the semester (Prologue), Studying, Pro1 exam, CLT exam, Final state (Epilogue)
Depending on whether the player passed the exams, the final state will be different (Win or Lose).

@author: Elisa Lübbers
"""

from studying import study
from pro1 import pro1_exam
from clt import clt_exam
from misc import prologue, epilogue
from misc import game_txt
from misc import report


def main():
    """
    Run the game in its entirety, restart the game if the player is done and wants to play again.
    """
    while True:
        prologue()
        study()
        pro1_exam()
        # only proceed to CLT exam the PRO1 exam has been passed
        if report['PRO1 exam'] != 5.0:
            clt_exam()
            # print the game text for final state: win if PRO1 and CLT exam have been passed
            if report['CLT exam'] != 5.0:
                print(game_txt['epilogue_w'])
        # print the game text for final state: lose if either exam has been failed
        if report['CLT exam'] == 5.0 or report['PRO1 exam'] == 5.0:
            print(game_txt['epilogue_l'])
        epilogue()


if __name__ == '__main__':
    main()
