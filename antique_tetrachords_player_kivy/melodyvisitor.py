# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 08:02:39 2019

@author: Slav
"""
from abc import ABC, abstractmethod
from multipledispatch import dispatch
from src.melody import Melody
from math import log

class MelodyVisitor(ABC):
    '''
    A visitor to Melody, which can add/alter existing functionalities.
    (Not that this can't be directly added to Melody, but implementing a 
    Visitor is more fun.)
    '''
    @abstractmethod
    def visitMelody(self):
        pass
    
    
    
class MelodyIntervalExtractor(MelodyVisitor):
    '''
    This class is a Visitor designed to extract the intervals between the tones
    of a given melody.
    '''
    # Disclaimer: this functionality can be easily added to Tone/Melody directly, 
    # but there are quite a few methods already. Also, there is no immediate need
    # to add tons of different (and perhaps conflicting) functionalities to one
    # and the same class. So let's keep things simple (and "single-purposed") and
    # separate the various functionalities, unless strictly necessary.
    def __init__(self):
        pass
    
    @dispatch(Melody)
    def visitMelody(self, melody):
        '''
        Extracts the intervals in cents from a given melody.
        Parameters:
            melody: Melody
            
        Returns:
            list: a list with the melody tones' intervals in cents.
        '''
        # get all frequencies
        frequency_list = []
        for tone in melody.get_melody():
            frequency_list.append(tone.get_frequency())
            
        # calculate the cents by the formula = 1200*log2(freq1/freq2)
        cents_list = [0]
        for i in range(1, len(frequency_list)):
            cents = 1200 * log((frequency_list[i] / frequency_list[i-1]), 2)
            cents_list.append(cents)
            
        return cents_list