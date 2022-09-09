# Elisa Lübbers
# 16.08.2022
# this file contains the "studying"- and "assignments"-part of the game and all related functions.

import sys
from miscellaneous import report
from miscellaneous import valid_input
from miscellaneous import take_exam
from miscellaneous import game_txt
from miscellaneous import inspect_report
import random


def study():
    """Check user input for valid commands and execute the according functions in a loop while the player is
    studying. """
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
    """Increment studypoints by 1 and print feedback."""
    report['study points'] += 1
    print(game_txt['book'])


def watch_video():
    """Subtract 1 from studypoints with a .6 chance or add 2 with a .4 chance, print feedback according to outcome."""
    if random.randint(1, 100) <= 60:
        report['study points'] -= 1
        print(game_txt['video_l'])
    else:
        report['study points'] += 2
        print(game_txt['video_w'])


def ask_tutor():
    """Add 3 to studypoints with a .7 chance or do nothing with a .3 chance, print feedback according to outcome."""
    if random.randint(1, 100) <= 70:
        report['study points'] += 3
        print(game_txt['tutor_w'])
    else:
        print(game_txt['tutor_l'])


def submit_clt():
    """Update report and enter assignment-loop if submission-conditions are met. Else throw specific in-game error."""
    if report['CLT submitted'] < 3 and report['CLT submitted'] <= report['PRO1 submitted'] and report[
            'study points'] >= 4:
        report['CLT submitted'] += 1
        report['study points'] -= 4
        print('You submitted a CLT assignment.')
        if report['CLT submitted'] == 3 and report['PRO1 submitted'] == 4:
            print(game_txt['exam_warning'])
            assignment_input()
    elif report['CLT submitted'] == 3:
        print('You dont have to submit any more of these!')
    elif report['study points'] < 4:
        print('You dont have enough study points for this!')
    elif report['CLT submitted'] > report['PRO1 submitted']:
        print('You have to submit one more PRO1 assignment first!')


def submit_pro1():
    """Update report and enter assignment-loop if submission-conditions are met. Else throw specific in-game error."""
    if report['PRO1 submitted'] < 4 and report['PRO1 submitted'] <= report['CLT submitted'] and report[
            'study points'] >= 3:
        report['PRO1 submitted'] += 1
        report['study points'] -= 3
        print('You submitted a PRO1 assignment.')
        if report['CLT submitted'] == 3 and report['PRO1 submitted'] == 4:
            print(game_txt['exam_warning'])
            assignment_input()
    elif report['PRO1 submitted'] == 4:
        print('You dont have to submit any more of these!')
    elif report['study points'] < 3:
        print('You dont have enough study points for this!')
    elif report['PRO1 submitted'] > report['CLT submitted']:
        print('You have to submit one more CLT assignment first!')


def assignment_input():
    """Handle the valid input for assignments in a loop and call functions accordingly."""
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
                study()
                # break  # fixme why doesnt break work?
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
