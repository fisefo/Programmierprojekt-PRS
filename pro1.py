"""
Created on Sun Sep 11 2022

All necessary functions for the PRO1-exam part of the game.  # todo make this more helpful?

@author: Elisa Lübbers
"""
import random
import re
import sys

import nltk
from nltk.corpus import wordnet
from typing import Any
from misc import valid_input
from misc import inspect_report

# FIXME timer!!


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
    # extract only the words from the string into a list; then save it also as a string
    only_words_list: list[Any] = re.findall(r'\w+', sent_string)
    only_words_string: str = ' '.join(only_words_list[2:])
    # sub every word with '-'
    final_sentence: str = re.sub(r'\w+', '–', sent_string)
    # 'uncover' the first two words of the sentence to finalize it
    for i in range(2):
        final_sentence = final_sentence.replace('–', only_words_list[i], 1)

    # compute the hints for the player
    words_to_guess = only_words_list[2:]
    hint1 = [len(x) for x in words_to_guess]

    sent_tokenized = nltk.word_tokenize(only_words_string)
    sent_tagged = nltk.pos_tag(sent_tokenized, tagset='universal')
    hint2 = [x[1] for x in sent_tagged]

    hint3 = [get_synonym(x) for x in words_to_guess]

    score = 0
    guesses = 3
    hints = 3
    current_index = 0

    while True:
        user_input = input('[{score} points] What is the next word? {sentence}'
                           .format(score, final_sentence)).lower() # fixme: ignore '!!!' ?
        if user_input == 'exit':
            sys.exit()
        elif user_input in valid_input:
            if user_input == 'inspect report':
                inspect_report()
                continue
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
                pass  # todo: end exam with current stats -> just break the loop?
        elif user_input == words_to_guess[current_index]:
            print('Correct!')  # todo: check whether the player has won, act accordingly; up the index, up the score, update final_sentence
            current_index += 1
            if hints == 3:
                score += 10
            elif hints == 2:
                score += 8
            elif hints == 1:
                score += 6
            elif hints == 0:
                score += 4
        else:
            pass  # todo: wrong word entry; check whether it was the last word, act accordingly 
        # todo: end of exam, going to next exam, epilogue


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