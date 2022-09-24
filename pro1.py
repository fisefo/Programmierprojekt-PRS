"""
Created on Sun Sep 11 2022

All necessary functions for the PRO1-exam part of the game.  # todo make this more helpful?

@author: Elisa Lübbers
"""
import random
import re
from typing import Any
import nltk
from nltk.corpus import wordnet


hint1 = []
hint2 = []    # todo: probs wont need these anymore
hint3 = []

word_list = []
final_sentence = []


def pro1_exam():
    """Handle player input and call functions accordingly for PRO1-exam part of the game."""
    points = 0
    tries = 3
    hints = 3


def prep_sentence():
    """
    Fetch a sentence from Alice in Wonderland that is 10 tokens long. Process it for display for the player.

    Returns
    ------
    word_list: list
        all the words in the sentence
    final_sentence: str
        the sentence to be shown to the player
    """  #fixme this only shows the first param!
    return [word_list, final_sentence]


def get_length(word_list: list):
    """
    Compute the length of every word in the list and save it to a new list

    Parameters
    ----------
    word_list: list
        all words from the sentence (final_sentence)

    Returns
    -------
    word_lengths: list
        length of each word
    """
    word_lengths = [len(x) for x in word_list]
    return word_lengths
# fixme: make it return a value instead, can then be called in pro1


def get_pos_tag(word_list: list):
    """
    Fetch the POS-tags for all words in the given sentence #todo: do we look up all words or leave the first two out?

    Parameters
    ---------
    word_list: list
        all the words to fetch the POS-tag of

    Return
    --------
    pos_list: list
        one POS-tag per word in the sentence
    """
    word_string = ' '.join(word_list)
    sent_tokenized = nltk.word_tokenize(word_string)
    sent_tagged = nltk.pos_tag(sent_tokenized, tagset='universal')
    pos_list = [x[1] for x in sent_tagged]
    return pos_list


def get_synonym(word_list: list):
    """
    Fetch the synonym for every word in the sentence and save it to a list.
    If there is no synonym, save a stand-in string to the list.

    Parameters
    ---------
     word_list: list
        all the words to fetch a synonym of

    Return
    ------
    synonym_list: list
        all the synonyms
    """
    synonym_list = []

    return synonym_list
