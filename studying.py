#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 2022

This file contains all functions for the 'studying'- and 'assignments'-parts of
the game. These functions handle the input for this stage of the game and update the player's report if necessary.

@author: Elisa Lübbers
"""

import sys
from misc import report
from misc import valid_input
from misc import take_exam
from misc import game_txt
from misc import inspect_report
import random


def study():
    """
    Handle all user input and execute the according functions while the player is
    studying; this includes accumulating study points and submitting assignments.

    All valid commands will lead to the corresponding action, i.e. updating the player's report or transitioning
    to the first exam. Commands that are valid to a different part of the game raise a different in-game error-message
    to the player than wholly invalid commands.
    """
    print(game_txt['study'])
    while True:
        if take_exam['possible']:
            break
        user_input = input('\n').lower()
        if user_input == 'exit':
            sys.exit()
        elif user_input in valid_input['studying']:
            if user_input == 'read book':
                read_book()
                continue
            elif user_input == 'watch video':
                watch_video()
                continue
            elif user_input == 'ask tutor':
                ask_tutor()
                continue
            elif user_input == 'submit clt':
                submit_clt()
                continue
            elif user_input == 'submit pro1':
                submit_pro1()
                continue
            elif user_input == 'inspect report':
                inspect_report()
                continue
        elif user_input in valid_input['all']:
            print('You can not use that command here!')
        elif user_input == 'cheat':
            report['PRO1 submitted'] = 4
            report['CLT submitted'] = 2
            report['study points'] = 4
            print(inspect_report())
        else:
            print('..what?')


def read_book():
    """Increment study points by 1 and print feedback."""
    report['study points'] += 1
    print(game_txt['book'])


def watch_video():
    """Subtract 1 from study points with a .6 chance or add 2 with a .4 chance, print feedback according to outcome."""
    if random.randint(1, 100) <= 60:
        report['study points'] -= 1
        print(game_txt['video_l'])
    else:
        report['study points'] += 2
        print(game_txt['video_w'])


def ask_tutor():
    """Add 3 to study points with a .7 chance or do nothing with a .3 chance, print feedback according to outcome."""
    if random.randint(1, 100) <= 70:
        report['study points'] += 3
        print(game_txt['tutor_w'])
    else:
        print(game_txt['tutor_l'])


def submit_clt():
    """
    Update report and enter assignment-loop if submission-conditions are met. Else throw specific in-game error.

    The in-game errors are specific to the problem at hand, i.e. not enough study points. Should the player qualify
    for taking the first exam, they are notified automatically.
    """
    if report['CLT submitted'] < 3 and report['CLT submitted'] <= report['PRO1 submitted'] and report[
            'study points'] >= 4:
        report['CLT submitted'] += 1
        report['study points'] -= 4
        print(game_txt['clt_exercise'])
        if report['CLT submitted'] == 3 and report['PRO1 submitted'] == 4:
            print(game_txt['exam_warning'])
        assignment_input()
    elif report['CLT submitted'] == 3 and report['PRO1 submitted'] == 4:
        print(game_txt['exam_warning'])
        assignment_input()
    elif report['CLT submitted'] == 3:
        print('You dont have to submit any more of these!')
    elif report['study points'] < 4:
        print('You dont have enough study points for this!')
    elif report['CLT submitted'] > report['PRO1 submitted']:
        print('You have to submit one more PRO1 assignment first!')


def submit_pro1():
    """
    Update report and enter assignment-loop if submission-conditions are met. Else throw specific in-game error.

    The in-game errors are specific to the problem at hand, i.e. not enough study points. Should the player qualify
    for taking the first exam, they are notified automatically.
    """
    if report['PRO1 submitted'] < 4 and report['PRO1 submitted'] <= report['CLT submitted'] and report[
            'study points'] >= 3:
        report['PRO1 submitted'] += 1
        report['study points'] -= 3
        print(game_txt['pro1_exercise'])
        if report['CLT submitted'] == 3 and report['PRO1 submitted'] == 4:
            print(game_txt['exam_warning'])
        assignment_input()
    elif report['CLT submitted'] == 3 and report['PRO1 submitted'] == 4:
        print(game_txt['exam_warning'])
        assignment_input()
    elif report['PRO1 submitted'] == 4:
        print('You dont have to submit any more of these!')
    elif report['study points'] < 3:
        print('You dont have enough study points for this!')
    elif report['PRO1 submitted'] > report['CLT submitted']:
        print('You have to submit one more CLT assignment first!')


def assignment_input():
    """
    Handle all user input for assignments and call functions accordingly.

    Valid input after submitting an assignment differs from that while studying, this function acts much the same way
    as study(). All valid input will call the corresponding actions and invalid input is distinguished in wholly
    invalid and valid in a different state. This function will lead to the first exam if conditions are met and the
    player wants to proceed.
    """
    while True:
        user_input = input('\n').lower()
        if user_input == 'exit':
            sys.exit()
        elif user_input in valid_input['assignments']:
            if user_input == 'submit clt':
                submit_clt()
                continue
            elif user_input == 'submit pro1':
                submit_pro1()
                continue
            elif user_input == 'study':
                print(game_txt['study'])
                break
            elif user_input == 'inspect report':
                inspect_report()
                continue
            elif user_input == 'take pro1 exam':
                if report['CLT submitted'] == 3 and report['PRO1 submitted'] == 4:
                    take_exam['possible'] = True
                    break
                else:
                    print('You have to submit all assignments first!')
                    continue
        elif user_input in valid_input['all']:
            print('You can\'t do that here!')
        else:
            print('..what?')
