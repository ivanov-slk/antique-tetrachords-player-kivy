# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 15:41:10 2019

@author: Slav
"""

import pytest
import unittest
import os
os.chdir('../')
from src.tone import Tone
from src.melody import Melody
from src.various_melodies import names, melodies

class TestMelody(unittest.TestCase):
    '''
    Testing strategy: 
        1. Playing music tested "by ear";
        2. Test adding tone by passing Tone, int, float and string;
    '''
    def setUp(self):
        base_tone = Tone(440)
        self.melody = Melody(base_tone)
        
    def test_play_one_tone(self):
#        self.melody.play()
        pass
        
    def test_add_tone_float(self):
        self.melody.add_tone(90.225)
        self.assertEqual(len(self.melody.get_melody()), 2)
        self.assertLess(abs(self.melody.get_melody()[-2]._calculate_frequency(90.225)\
                             - (self.melody.get_melody()[-1].get_frequency())), 0.1)
    
    def test_add_tone_int(self):
        self.melody.add_tone(100)
        self.assertEqual(len(self.melody.get_melody()), 2)
        self.assertLess(abs(self.melody.get_melody()[-1].get_frequency()-466.16), 0.1)
        
    def test_add_tone_string(self):
        self.melody.add_tone('256/243')
        self.assertEqual(len(self.melody.get_melody()), 2)
        self.assertLess(abs(self.melody.get_melody()[-1]._calculate_cents('256/243')\
                             - 90.225), 0.1)
        
    def test_play_more_tones(self):
        self.melody.add_tone(Tone(466.16))
        self.melody.add_tone(Tone(493.88))
#        self.melody.play()
        
    def test_tempered_major(self):
        self.mel = melodies['Темпериран\nмажорен']
        result = self.mel.get_intervals()
        correct = [0, 200, 200, 100]
        for i in range(len(result)):
            self.assertLess(abs(result[i] - correct[i]), 0.01)
            
    def test_archites_enharmonic(self):
        self.mel = melodies['Архит\nенхармоничен']
        result = self.mel.get_intervals()
        correct = [0, 62.960903872962575, 48.77038139681492, 386.3137138648348]
        for i in range(len(result)):
            self.assertLess(abs(result[i] - correct[i]), 0.01)
            
    def test_set_base_frequency(self):
        self.mel = melodies['Темпериран\nмажорен']
        self.mel.set_base_frequency(200)
        result = self.mel.get_intervals()
        correct = [0, 200, 200, 100]
        for i in range(len(result)):
            self.assertLess(abs(result[i] - correct[i]), 0.01)
            
    def test_set_base_frequency2(self):
        self.mel = melodies['Темпериран\nмажорен']
        self.mel.set_base_frequency(200)
        result = self.mel.get_frequencies()
        correct = [200, 224.4924096618746, 251.98420997897466, 266.9679708340069]
        for i in range(len(result)):
            self.assertLess(abs(result[i] - correct[i]), 0.01)
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestMelody('test_play_one_tone'))
    suite.addTest(TestMelody('test_add_tone_float'))
    suite.addTest(TestMelody('test_add_tone_int'))
    suite.addTest(TestMelody('test_add_tone_string'))
    suite.addTest(TestMelody('test_play_more_tones'))
    suite.addTest(TestMelody('test_tempered_major'))
    suite.addTest(TestMelody('test_archites_enharmonic'))
    suite.addTest(TestMelody('test_set_base_frequency'))
    suite.addTest(TestMelody('test_set_base_frequency2'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())