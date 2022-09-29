#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 2022

Auxiliary script for the PRS 2022 final project. Contains miscellaneous functions and variables
that are not specific to any sole part of the game, as well as prologue and epilogue functions.

@author: Elisa Lübbers
"""

import sys

# all valid input for every part of the game
valid_input = {
    'all': ['read book', 'watch video', 'ask tutor', 'submit clt', 'submit pro1', 'inspect report',
            'take pro1 exam', 'study', 'go on holidays', 'play again'],
    'starting out': ['study', 'inspect report', 'go on holidays'],
    'studying': ['read book', 'watch video', 'ask tutor', 'submit clt', 'submit pro1', 'inspect report'],
    'assignments': ['study', 'submit clt', 'submit pro1', 'take pro1 exam', 'inspect report'],
    'pro1 exam': ['take clt exam', 'inspect report', ':#+!?', 'help!!!'],
    'epilogue': ['play again', 'inspect report', 'exit']
}
# the report of the player, to be updated in different parts of the game
report = {
    'study points': 0,
    'CLT submitted': 0,
    'PRO1 submitted': 0,
    'PRO1 exam': 'N/A',
    'CLT exam': 'N/A'
}
# save whether the player can take the exam
take_exam = {
    'possible': False
}


def inspect_report():
    """Display the report of the player on screen."""
    print('Study points:......... ' + str(report['study points']))
    print('CLT submitted:........ ' + str(report['CLT submitted']))
    print('PRO1 submitted:....... ' + str(report['PRO1 submitted']))
    print('PRO1 exam:............ ' + str(report['PRO1 exam']))
    print('CLT exam:............. ' + str(report['CLT exam']))


def text_out(scene):
    """
    Take a list of strings and turn it into a single string for further use.

    :param scene: a list of strings
    :return: a single string
    """
    output = ''
    for i in scene:
        output += i
    return output


with open('texts.txt', 'r') as f:
    """
    Read the scene descriptions from the texts.txt file and store them as single strings in a dictionary.
    
    :param texts.txt: the text file with all scene descriptions
    :return: a dictionary will all scene descriptions seperated by name
    """
    raw = f.readlines()
    game_txt = {
        'prologue': text_out(raw[0:6]),
        'study': text_out(raw[43:46]),
        'book': text_out(raw[8:12]),
        'video_w': text_out(raw[14:18]),
        'video_l': text_out(raw[19:23]),
        'tutor_w': text_out(raw[25:29]),
        'tutor_l': text_out(raw[30:34]),
        'exam_warning': text_out(raw[36:41]),
        'pro1_exam': text_out(raw[48:53]),
        'clt_exam': text_out(raw[55:59]),
        'epilogue_w': text_out(raw[60:68]),
        'epilogue_l': text_out(raw[70:79]),
        'pro1_exercise': text_out(raw[81:84]),
        'clt_exercise': text_out(raw[86:89])
    }


def prologue():
    """Show the prologue of the game and make sure the player proceeds to the study-state"""
    print(game_txt['prologue'])
    while True:
        user_input = input('Proceed to -> "study"ing?\n').lower()
        if user_input == 'exit':
            sys.exit()
        elif user_input == 'study':
            break
        elif user_input == 'inspect report':
            inspect_report()
            continue
        elif user_input == 'go on holidays':
            print('No way, you have to pass the exams first!')
        else:
            print('..what?')


def epilogue():
    """
    Handle all input for the final state of the game and restart the game-loop if commanded.
    Valid input will lead to the corresponding actions, invalid input is distinguished into wholly invalid and
    valid in a different state.
    """
    while True:
        user_input = input('What will you do now?\n')
        if user_input == 'exit':
            sys.exit()
        elif user_input in valid_input['epilogue']:
            if user_input == 'inspect report':
                inspect_report()
                continue
            # flush the player's stats if they want to play again
            elif user_input == 'play again':
                report['study points'] = 0
                report['CLT submitted'] = 0
                report['PRO1 submitted'] = 0
                report['PRO1 exam'] = 'N/A'
                report['CLT exam'] = 'N/A'
                take_exam['possible'] = False
                break
        elif user_input in valid_input['all']:
            print('You can\'t do that now!')
        else:
            print('..what?')
            continue
