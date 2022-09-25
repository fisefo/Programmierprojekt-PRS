"""
Created on Sun Sep 11 2022

All necessary functions for the PRO1-exam part of the game.  # todo make this more helpful?

@author: Elisa Lübbers
"""
import random
import re
import nltk
from nltk.corpus import wordnet
from typing import Any
from misc import valid_input

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
    only_words_string: str = ' '.join(only_words_list)
    # sub every word with '-'
    final_sentence: str = re.sub(r'\w+', '–', sent_string)
    # 'uncover' the first two words of the sentence to finalize it
    for i in range(2):
        final_sentence = final_sentence.replace('–', only_words_list[i], 1)

    # compute the hints for the player
    hint1 = [len(x) for x in only_words_list]

    sent_tokenized = nltk.word_tokenize(only_words_string)
    sent_tagged = nltk.pos_tag(sent_tokenized, tagset='universal')
    hint2 = [x[1] for x in sent_tagged]

    hint3 = [get_synonym(x) for x in only_words_list]

    print(sent_string)
    print(final_sentence)
    print(hint1)
    print(hint2)
    print(hint3)

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