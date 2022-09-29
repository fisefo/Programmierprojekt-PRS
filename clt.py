"""
Created on Mon Sep 26 2022

All functions and variables necessary for the CLT-exam part of the PRS 2022 final project.
This script checks user input for whether the player entered a correct codeword* and computes an according
grade on a pass or fail basis.
* The codeword is a 'lattice word', meaning every substring of it must have as much or more letters of the letter i as
i+1, i.e. aabbcc, aaabbcdecbdf, ab; the word must begin with an "a".

@author: Elisa Lübbers
"""

import sys
from misc import inspect_report
from misc import report
from misc import game_txt


def clt_exam():
    """
    Handle player input according to the CLT-exam's rules. As this is an exam-simulation, only state-specific
    valid input and correct answers are handled as valid, everything else will be treated as wrong answers.
    """
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
                print('Correct!\n')
                report['CLT exam'] = 1.0
                break
            elif not correct and tries != 1:
                tries -= 1
                print('Wrong! Tries remaining: {}\n'.format(tries))
            else:
                print('Wrong!')
                report['CLT exam'] = 5.0
                break
    print('You finished the exam, your grade is: {}\n'.format(report['CLT exam']))


def is_codeword(player_input: str):
    """
    Check whether the submitted codeword is an acceptable lattice-word, using recursion.

    :param player_input: a codeword the player submits.
    :return: true if the codeword is accepted, otherwise false.
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

