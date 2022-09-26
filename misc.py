"""
Created on Tue Aug 16 2022

Auxiliary script for the PRS 2022 final project. Contains miscellaneous functions and variables
that are not specific to any sole part of the game, as well as prologue and epilogue.

@author: Elisa Lübbers
"""
import sys


valid_input = {
    'all': ['read book', 'watch video', 'ask tutor', 'submit clt', 'submit pro1', 'inspect report',
            'take pro1 exam', 'study'],
    'starting out': ['study', 'inspect report'],
    'studying': ['read book', 'watch video', 'ask tutor', 'submit clt', 'submit pro1', 'inspect report'],
    'assignments': ['study', 'submit clt', 'submit pro1', 'take pro1 exam', 'inspect report'],
    'pro1 exam': ['take clt exam', 'inspect report', '#+!?', 'help!!!'],
    'clt exam': ['inspect report'],
    'ending': ['play again', 'inspect report']
}
report = {
    'study points': 0,
    'CLT submitted': 0,
    'PRO1 submitted': 0,
    'PRO1 exam': 'N/A',
    'CLT exam': 'N/A'
}
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
    """Take a list of strings and turn it into a single string."""
    output = ''
    for i in scene:
        output += i
    return output


with open('texts.txt', 'r') as f:
    """Read the scene descriptions from the texts.txt file and store them as single strings in a dictionary."""
    raw = f.readlines()
    game_txt = {
        'prologue': text_out(raw[0:6]),
        'study': text_out(raw[43:46]),
        'book': text_out(raw[8:12]),
        'video_w': text_out(raw[14:18]),
        'video_l': text_out(raw[19:23]),
        'tutor_w': text_out(raw[25:29]),
        'tutor_l': text_out(raw[30:34]),
        'exam_warning': text_out(raw[36:41])
    }


def prologue():
    """Show the Prologue to the game and make sure the player proceeds to the study-state"""
    print(game_txt['prologue'])
    while True:
        user_input = input('Proceed to -> "study"ing?\n').lower()
        if user_input == 'study':
            break
        elif user_input == 'inspect report':
            inspect_report()
            continue
        elif user_input == 'exit':
            sys.exit()
        else:
            print('The shortest distance between two points is a straight line. In your case, you are point A,\n '
                  'the holidays are point B, and the straight line is studying. No way around it, either.')
