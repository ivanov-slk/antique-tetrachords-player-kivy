# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 08:31:58 2019

@author: Slav
"""

from pysine import sine
from math import log
from multipledispatch import dispatch
import abc

class ToneInterface(abc.ABC):
    @abc.abstractmethod
    def play(self):
        pass

class Tone(ToneInterface):
    '''
    A single tone. It has frequency and can be played with a chosen duration.
    '''
    # AF: represents a tone.
    # RI: self.frequency int or float
    
    def __init__(self, frequency, duration=1):
        self._frequency = frequency
        self._duration = duration
        self._check_rep()
        
    def play(self):
        '''
        Plays the tone for `duration` seconds.
        '''
        sine(self._frequency, self._duration)
        self._check_rep()
    
    @dispatch((int, float))        
    def create_tone(self, interval):
        '''
        Creates a new tone which is an `interval` higher than `self`.
        
        Parameters:
            interval: int/float; in cents. The interval between the current tone and 
            the new one.
            
        Returns:
            Tone: the new tone, an `interval` higher than `self`.
        '''
        new_frequency = self._calculate_frequency(interval)
        new_tone = Tone(new_frequency)
        self._check_rep()
        return new_tone # this can be reduced to one line, but let's stay clear.
        
    @dispatch(str) 
    def create_tone(self, interval):
        '''
        Creates a new tone which is an `interval` higher than `self`.
        
        Parameters:
            interval: str; a ratio. The interval between the current tone and 
            the new one.
            
        Returns:
            Tone: the new tone, an `interval` higher than `self`.
        '''
        try:
            a, b = [int(x) for x in interval.split('/')]
        except ValueError:
            raise ValueError('Incorrect interval supplied. Should be a valid ratio in the form a/b')
        cents = 1200 * log((a/b), 2)
        new_frequency = self._calculate_frequency(cents)
        new_tone = Tone(new_frequency)
        self._check_rep()
        return new_tone
        
    def get_frequency(self):
        return self._frequency
    
    def get_duration(self):
        return self._duration
    
    def set_duration(self, new_duration):
        self._duration = new_duration
        
    def _calculate_cents(self, ratio):
        '''
        Private method for calculating the cents from a given ratio according to
        the formula `cents = 1200*log2(numerator/denominator), where the numerator and
        the denominator are taken from `ratio`.
        
        Parameters:
            ratio: str; a valid ratio (e.g. `28/27`, `256/243`, etc.)
            
        Returns:
            float: the cents calculated from the ratio.
        '''
        a, b = [int(x) for x in ratio.split('/')]
        cents = 1200 * log((a/b), 2)
        self._check_rep()
        return cents
    
    def _calculate_frequency(self, cents):
        '''
        Calculates new frequency given a base frequency and the interval in cents.
        '''
        new_frequency = self._frequency * 2 ** (cents / 1200)
        self._check_rep()
        return new_frequency
    
    def _check_rep(self):
        assert isinstance(self._frequency, (int, float))