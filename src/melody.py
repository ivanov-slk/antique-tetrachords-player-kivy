# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 11:02:57 2019

@author: Slav
"""
import os
os.chdir('../')
from pysine import sine
from math import log
from src.tone import Tone
from multipledispatch import dispatch
from copy import deepcopy
import abc

class MelodyInterface(abc.ABC):
    @abc.abstractmethod
    def add_tone():
        pass
    
    @abc.abstractmethod
    def play(self):
        pass

class Melody(MelodyInterface):
    '''
    A melody comprised of various Tones. It has a base tone and may have a name.
    '''
    # AF: Represents a sequence of tones
    # RI: True
    # SRE: the rep is mutable, so it is private and defensive copies are made if
    # necessary. "Finality" can't be enforced in Python.
    
    def __init__(self, base_tone, name=''):
        self._melody = [base_tone]
        self._name = name
    
    @dispatch(Tone)
    def add_tone(self, tone):
        '''
        Add an existing tone to the end of the melody.
        Parameters:
            tone: Tone
        '''
        self._melody.append(tone)
        
    @dispatch((float, int))
    def add_tone(self, interval):
        '''
        Add a tone to the end of the melody by taking an interval from the last
        tone in Melody.
        Parameters:
            interval: float
        '''
        new_tone = self._melody[-1].create_tone(interval)
        self._melody.append(new_tone)
        
    @dispatch(str)
    def add_tone(self, interval):
        '''
        Add a tone to the end of the melody.
        Parameters:
            tone: Tone
        '''
        new_tone = self._melody[-1].create_tone(interval)
        self._melody.append(new_tone)
        
    def play(self):
        '''
        Plays the melody.
        '''
        for tone in self._melody:
            tone.play()
    
    def get_melody(self):
        return deepcopy(self._melody)
    
    def set_name(self, new_name):
        self._name = new_name
        
    def get_name(self):
        return self._name
    
    def get_duration(self):
        duration_list = []
        for tone in self.get_melody():
            duration_list.append(tone.get_duration())
            
    @dispatch((list, tuple))
    def set_duration(self, duration):
        for i in range(min(len(duration), len(self._melody))):
            self._melody[i].set_duration(duration[i])
    
    @dispatch((int, float))
    def set_duration(self, duration):
        for tone in self._melody:
            tone.set_duration(duration)