# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 21:20:00 2019

@author: Slav
"""

import pytest
import unittest
import os
os.chdir('../')
from src.tone import Tone
from src.melody import Melody
from src.various_melodies import names, intervals, melodies
from src.melodycollection import MelodyCollection

class TestMelody(unittest.TestCase):
    '''
    Testing strategy: 
        1. Playing music tested "by ear";
        2. Test multiple dispatch for add_melody
        3. Test changing frequencies
    '''
    def setUp(self):
        base_tone = Tone(240)
        self.mel = MelodyCollection()
        
    def test_play_one_melody(self):
        self.mel.add_melody(melodies['Темпериран\nмажорен'], 'Темпериран\nмажорен')
        self.mel.play_melody('Темпериран\nмажорен')
    
    def test_play_all_melodies(self):
        self.mel.add_melody(melodies['Темпериран\nмажорен'], 'Темпериран\nмажорен')
        self.mel.add_melody(melodies['Архит\nенхармоничен'], 'Архит\nенхармоничен')
        self.mel.play_all()
        
    def test_add_melody_1(self):
        '''
        Create externally a new melody, add it and compare its intervals with 
        the correct intervals (calculated manually).
        '''
        new_melody = melodies['Ератостен\nенхармоничен']
        new_name = 'Ератостен\nенхармоничен'
        self.mel.add_melody(new_melody, new_name)
        result = self.mel.get_intervals('Ератостен\nенхармоничен')
        correct = [0, 43.83105123013666, 44.969646502395555, 409.2443014020803]
        self.assertTrue(result, correct)
        
    def test_add_melody_2(self):
        '''
        Create a new melody internally and compare its intervals with the correct
        ones.
        '''
        self.mel.add_melody(base_frequency=250,
                     intervals=['32/31', '31/30', '5/4'],
                     melody_name='Дидим\nенхармоничен')
        result = self.mel.get_intervals('Дидим\nенхармоничен')
            
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestMelody('test_play_one_melody'))
    suite.addTest(TestMelody('test_play_all_melodies'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())