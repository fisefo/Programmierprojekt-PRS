"""
Created on Mon Sep 26 2022

All functions and variables necessary for the CLT-exam part of the PRS 2022 final project.
This script checks user input for whether the player entered a correct codeword* and computes an according
grade on a pass or fail basis.
* The codeword is a 'lattice word'.

@author: Elisa Lübbers
"""
import sys

from misc import inspect_report
from misc import report
from misc import game_txt
from misc import valid_input


def clt_exam():
    print(game_txt['clt_exam'])
    tries = 3
    while True:
        user_input = input('Enter a codeword:\n').lower()
        if user_input == 'exit':
            sys.exit()
        if user_input == 'inspect report':
            inspect_report()
        else:
            correct = is_codeword(user_input)
            if correct:
                print('Correct!')
                report['CLT exam'] = 1.0
                break
            elif not correct and tries != 1:
                tries -= 1
                print('Wrong! Tries remaining: {}'.format(tries))
            else:
                print('Wrong!')
                report['CLT exam'] = 5.0
                break
    print('You finished the exam, your grade is: {}\n'.format(report['CLT exam']))


def is_codeword(player_input: str):
    """
    Check whether the submitted codeword is an acceptable lattice-word.
    :param player_input: a codeword the player submits.
    :return: bool: true if the codeword is accepted, otherwise false.
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if player_input == 'a':
        return True
    elif len(player_input) > 1:
        iplus1 = player_input[-1]
        i = alphabet[alphabet.index(iplus1)-1]
        if player_input.count(i) >= player_input.count(iplus1) or iplus1 == 'a':
            return is_codeword(player_input[:-1])
        else:
            return False
    else:
        return False

