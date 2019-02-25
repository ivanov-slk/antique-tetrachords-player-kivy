# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 20:51:23 2019

@author: Slav
"""
import os
os.chdir('../')
from src.tone import Tone
from src.melody import Melody
from src.various_melodies import names, intervals
from multipledispatch import dispatch
from collections import OrderedDict
import abc

class MelodyCollectionInterface(abc.ABC):
    '''
    The interface defining the operations on a collection of melodies. In its 
    implementations this interface represents
    '''
    @abc.abstractmethod
    def add_melody(self):
        pass
    @abc.abstractmethod
    def get_melody(self, melody_name):
        pass
    @abc.abstractmethod
    def play_melody(self, melody_name):
        pass
    @abc.abstractmethod
    def play_all(self):
        pass
    @abc.abstractmethod
    def change_base_frequency(self, melody_name, new_frequency):
        pass
    @abc.abstractmethod
    def change_all_base_frequencies(self, new_frequency):
        pass
    
class MelodyCollection(MelodyCollectionInterface):
    # AF: Represents a sequence of tones
    # RI: True
    # SRE: the rep is mutable, so it is private and defensive copies are made if
    # necessary.
    def __init__(self):
        self._collection = OrderedDict()
        
    @dispatch(Melody, str)
    def add_melody(self, melody, melody_name):
        '''
        Adds an existing Melody to the collection.
        
        Parameters:
            melody: an existing Melody
            melody_name: str; the name of the melody
            
        Returns:
            None.
        '''
        self._collection[melody_name] = melody
        
    @dispatch((int, float), (int, float, str), str, (int, float))
    def add_melody(self, base_frequency, intervals, melody_name, durations=[]):
        '''
        Adds a new melody to the collection by calculating the intervals.
        The melody is as long as the intervals list. Durations are taken up to
        the length of the intervals list. If the durations list is shorter, the
        default duration (1 s.) is taken for the rest of the tones.
        
        Parameters:
            base_frequency: int/float - the base frequency of the melody;
            intervals: list of valid intervals (i.e. cents or ratios);
            melody_name: str; the name of the melody;
            durations: list of valid durations (int/float);
            
        Returns:
            None.
        '''
        # create a base tone, the new melody and add the former to the latter
        
        # loop over the intervals and add new tones to the melody
        
        # add the new melody into the collection
    
    def get_melody(self, melody_name):
        return self._collection[melody_name]
    
    def play_melody(self, melody_name):
        self._collection[melody_name].play()
        
    def play_all(self):
        for melody in self._collection.values():
            melody.play()
            
    def change_base_frequency(self, melody_name, new_frequency):
        self._collection[melody_name].set_base_frequency(new_frequency)
        
    def change_all_base_frequencies(self, new_frequency):
        for melody in self._collection:
            melody.set_base_frequency(new_frequency)
