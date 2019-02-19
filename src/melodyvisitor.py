# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 08:02:39 2019

@author: Slav
"""
from abc import ABC, abstractmethod
from multipledispatch import dispatch

class MelodyVisitor(ABC):
    '''
    A visitor to Melody, which can add/alter existing functionalities.
    '''
    
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
        
    @dispatch(Melody)
    def visitMelody(self, melody):
        # do the extraction