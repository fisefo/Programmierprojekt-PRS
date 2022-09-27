"""
Created on Mon Sep 26 2022

All functions and variables necessary for the CLT-exam part of the PRS 2022 final project.
This script checks user input for whether the player entered a correct codeword* and computes an according
grade on a pass or fail basis.
* The codeword is a 'lattice word'.

@author: Elisa Lübbers
"""

from misc import valid_input
from misc import report
from misc import game_txt


def is_codeword(player_input: str):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if player_input == 'a':
        return True
    elif len(player_input) > 1:
        iplus1 = player_input[-1]
        i = alphabet[alphabet.index(iplus1)-1]
        if player_input.count(i) >= player_input.count(iplus1):
            return is_codeword(player_input[:-1])
        else:
            return False
