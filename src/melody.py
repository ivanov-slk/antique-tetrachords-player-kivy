# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 11:02:57 2019

@author: Slav
"""
#import os
#os.chdir('../')
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
    # necessary.

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

    @dispatch((float, int), (int, float))
    def add_tone(self, interval, duration):
        '''
        Add a tone to the end of the melody by taking an interval from the last
        tone in Melody.
        Parameters:
            interval: float
        '''
        new_tone = self._melody[-1].create_tone(interval, duration)
        self._melody.append(new_tone)

    @dispatch(str, (int, float))
    def add_tone(self, interval, duration):
        '''
        Add a tone to the end of the melody.
        Parameters:
            tone: Tone
        '''
        new_tone = self._melody[-1].create_tone(interval, duration)
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

    def get_durations(self):
        duration_list = []
        for tone in self.get_melody():
            duration_list.append(tone.get_duration())
        return duration_list

    @dispatch((list, tuple))
    def set_duration(self, duration):
        for i in range(min(len(duration), len(self._melody))):
            self._melody[i].set_duration(duration[i])

    @dispatch((int, float))
    def set_duration(self, duration):
        for tone in self._melody:
            tone.set_duration(duration)

    def get_frequencies(self):
        '''
        Returns a list with the frequencies of the melody's tones.
        '''
        frequencies_list = []
        for tone in self.get_melody():
            frequencies_list.append(tone.get_frequency())
        return frequencies_list

    def get_intervals(self):
        '''
        Returns a list with the intervals of the melody's tones.
        '''
        cents_list = [0]
        frequency_list = self.get_frequencies()
        for i in range(1, len(frequency_list)):
            cents = 1200 * log((frequency_list[i] / frequency_list[i - 1]), 2)
            cents_list.append(cents)
        return cents_list

    def set_base_frequency(self, new_base_frequency):
        '''
        Sets the base frequency to new_base_frequency and recalculates the
        existing frequencies, so that the intervals of the melody stay the same.
        
        Parameters:
            new_base_frequency: int/float - the new base frequency.
            
        Returns:
            None.
        '''
        new_melody = []
        intervals = self.get_intervals()
        new_base_tone = Tone(frequency=new_base_frequency,
                             duration=self._melody[0].get_duration())
        new_melody.append(new_base_tone)
        for i in range(1, len(self._melody)):
            new_tone = new_melody[-1].create_tone(intervals[i], 1)
            new_tone.set_duration(self._melody[i].get_duration())
            new_melody.append(new_tone)
        self._melody = new_melody

    def accept(self, melody_visitor):
        return melody_visitor.visitMelody(self)