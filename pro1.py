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


def pro1_exam():
    """
    Handle player input and call functions accordingly for PRO1-exam part of the game.

    # todo more info abt the loop, returns (for grades-function)
    """
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
    """  # fixme this only shows the first param!
    alice = nltk.corpus.gutenberg.sents('carroll-alice.txt')
    # take only sentences that are 10 tokens long and keep them in a list
    ten_token_sents = [x for x in alice if len(x) == 10]

    # take a random 10-tokens-sentence and turn it into a string
    sentence_raw: list[Any] = random.choice(ten_token_sents)
    sent_string: str = ' '.join(sentence_raw)
    # extract only the words from the string into a list
    only_words_list: list[Any] = re.findall(r'\w+', sent_string)
    # sub every word with '-'
    final_sentence: str = re.sub(r'\w+', '–', sent_string)

    # 'uncover' the first two words of the sentence
    for i in range(2):
        final_sentence = final_sentence.replace('–', only_words_list[i], 1)

    return [only_words_list, final_sentence]


def get_length(list_of_words: list):
    """
    Compute the length of every word in the list and save it to a new list

    Parameters
    ----------
    list_of_words: list
        all words from the sentence (final_sentence)

    Returns
    -------
    word_lengths: list
        length of each word
    """
    word_lengths = [len(x) for x in list_of_words]
    return word_lengths
# fixme: make it return a value instead, can then be called in pro1


def get_pos_tag(list_of_words: list):
    """
    Fetch the POS-tags for all words in the given sentence #todo: do we look up all words or leave the first two out?

    Parameters
    ---------
    list_of_words: list
        all the words to fetch the POS-tag of

    Return
    --------
    pos_list: list
        one POS-tag per word in the sentence
    """
    word_string = ' '.join(list_of_words)
    sent_tokenized = nltk.word_tokenize(word_string)
    sent_tagged = nltk.pos_tag(sent_tokenized, tagset='universal')
    pos_list = [x[1] for x in sent_tagged]
    return pos_list


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
