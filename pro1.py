"""
Created on Sun Sep 11 2022

All necessary functions and variables for the PRO1-exam part of the PRS 2022 final project.
This script processes a sentence from Lewis Carrol's Alice in Wonderland for the player to
guess the words, given the first two, in a hangman-like manner. The player is then given a grade
representing their success in guessing the words; they also have a two-minute time constraint.

@author: Elisa Lübbers
"""
import random
import re
import sys
import time

import nltk
from nltk.corpus import wordnet
from typing import Any
from misc import valid_input
from misc import inspect_report
from misc import report
from grades import convert_points


def pro1_exam():
    """
    Create and handle all variables and input necessary to play the Pro1-exam part of the game.

    Part one: Fetch and prepare a sentence from Alice in Wonderland for the guessing game;
        fetch and compute all info necessary for the hints and the score.

    Part two: Handle player input according to the games' rules.
    """
    # download the Alice in Wonderland text from the nltk corpus
    alice = nltk.corpus.gutenberg.sents('carroll-alice.txt')
    # take only sentences that are 10 tokens long and keep them in a list
    ten_token_sents = [x for x in alice if len(x) == 10]

    # take a random 10-tokens-sentence; then save it also a string
    sentence_raw: list[Any] = random.choice(ten_token_sents)
    sent_string: str = ' '.join(sentence_raw)
    # extract only the words from the string into a list
    only_words_list: list[Any] = re.findall(r'\w+', sent_string)
    # sub every word with '-'
    final_sentence: str = re.sub(r'\w+', '–', sent_string)
    # 'uncover' the first two words of the sentence to finalize it
    for i in range(2):
        final_sentence = final_sentence.replace('–', only_words_list[i], 1)

    # compute the hints for the player
    words_to_guess = only_words_list[2:]
    hint1 = [len(x) for x in words_to_guess]

    hint2 = [x[1] for x in nltk.pos_tag(words_to_guess)]

    hint3 = [get_synonym(x) for x in words_to_guess]

    score = 0
    guesses = 3
    hints = 3
    current_index = 0
    time_start = time.time()

    while True:
        user_input = input('[{} points] What is the next word? {}\n'
                           .format(score, final_sentence)).lower()
        time_end = time.time()
        delta_t = time_end - time_start
        if delta_t > 120:
            print('Oh no, you exceeded the time limit!')
            break
        if user_input == 'exit':
            sys.exit()
        elif user_input in valid_input['pro1 exam']:
            if user_input == 'inspect report':
                inspect_report()
                continue
            elif user_input == '#+!?':
                break
            elif user_input == 'help!!!':
                if hints == 3:
                    print('The next word is {} charakter(s) long.'.format(hint1[current_index]))
                    hints -= 1
                    continue
                elif hints == 2:
                    print('The next word is a(n) {}'.format(hint2[current_index]))
                    hints -= 1
                    continue
                elif hints == 1:
                    print('Here is a synonym for the next word: {}'.format(hint3[current_index]))
                    hints -= 1
                    continue
                elif hints == 0:
                    print('You have used all hints for this word!')
                    continue
            elif user_input == '#+!?':
                break

        elif user_input == words_to_guess[current_index].lower():
            print('Correct!')
            final_sentence = final_sentence.replace('–', words_to_guess[current_index], 1)
            if hints == 3:
                score += 10
            elif hints == 2:
                score += 8
            elif hints == 1:
                score += 6
            elif hints == 0:
                score += 4
            if words_to_guess[current_index] == words_to_guess[-1]:
                break
            current_index += 1
            hints = 3
            guesses = 3
            continue

        else:
            print('Wrong!')
            if guesses > 1:
                guesses -= 1
                continue
            else:
                final_sentence = final_sentence.replace('–', words_to_guess[current_index], 1)
                score -= 5
                if words_to_guess[current_index] == words_to_guess[-1]:
                    break
                current_index += 1
                hints = 3
                guesses = 3
                continue
    print('[{} points] The whole sentence is: {}'.format(score, sent_string))
    if delta_t > 120:
        report['PRO1 exam'] = 5.0
    else:
        report['PRO1 exam'] = convert_points(score, len(words_to_guess))
    print('You finished the exam, your grade is: {}'.format(report['PRO1 exam']))


def get_synonym(word: str):
    """
    Fetch the synonym for the given word from WordNet. If no synonym exists, return a stand-in string. If the word is
    a wh-question word, give the hint that it is.

    Fetch the first synonym from the second synset of the word;
    make sure that the found synonym is not the same as the given word, if so take the next word in the synset.
    Replace underscores with white space if necessary.

    Parameters
    ---------
     word: str
        the word to fetch a synonym of

    Return
    ------
    synonym: str
        the synonym
    """
    word = word.lower()
    try:
        synonym = wordnet.synsets(word)[1].lemma_names()[0]
        if synonym == word:
            synonym = wordnet.synsets(word)[1].lemma_names()[1]
    except IndexError:
        return 'Could not find a synonym, sorry!'
    else:
        if word in ['what', 'where', 'who', 'why', 'when']:
            synonym = 'No synonym found, but it\'s a wh-question word!'
        else:
            synonym = wordnet.synsets(word)[1].lemma_names()[0]
            if synonym == word:
                synonym = wordnet.synsets(word)[1].lemma_names()[1]
        synonym = synonym.replace('_', ' ')
        return synonym
