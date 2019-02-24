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
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestMelody('test_play_one_melody'))
    suite.addTest(TestMelody('test_play_all_melodies'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())