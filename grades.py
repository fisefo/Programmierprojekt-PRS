#!/usr/bin/env python3  # FIXME does every script need this?
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 13:05:22 2022

Auxiliary script for the PRS 2022 final project. This script contains a 
function that maps points in a word guessing game to a grade in the German 
grading system.

@author: PRS Team
"""


def convert_points(points, valid_tokens):
    """
    Convert points to the German grading system, proportionally to the number 
    of valid tokens.

    Parameters
    ----------
    points : int
        Points the player got for the sentence guessing game.
    valid_tokens :int
        Number of tokens the player had to guess (i.e. tokens excluding 
                                                  punctuation).

    Returns
    -------
    float
        The player's final grade.'

    """
    assert valid_tokens <= 10, "The number of valid tokens must be at most 10!"
    
    if points <= 0:
        return 5.0
    
    percentage = get_percentage(points, valid_tokens)
    
    assert percentage <= 100, "Points exceed the maximum!"
    
    if 0 < percentage <= 10:
        return 4.0
    if 10 < percentage <= 20:
        return 3.7
    if 20 < percentage <= 30:
        return 3.3
    if 30 < percentage <= 40:
        return 3.0
    if 40 < percentage <= 50:
        return 2.7
    if 50 < percentage <= 60:
        return 2.3
    if 60 < percentage <= 70:
        return 2.0
    if 70 < percentage <= 80:
        return 1.7
    if 80 < percentage <= 90:
        return 1.3
    if 90 < percentage <= 100:
        return 1.0


def get_percentage(points, valid_tokens):
    """Compute the percentage of points."""
    max_points = valid_tokens * 10
    return (points * 100) / max_points
