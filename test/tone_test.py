# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 12:50:46 2019

@author: Slav
"""

import pytest
import unittest
import os
os.chdir('../')
from src.tone import Tone

class TestTone(unittest.TestCase):
    '''
    Testing strategy: 
        1. Playing music tested "by ear";
        2. Test dispatching by passing, int, float and string;
        3. Test calculate frequency by using known tones (e.g. from A to H);
        4. Test calculate ratio by using know ratios from the book;
        
    Nota bene: boundary conditions not tested (yet) - although you should begin
    with them :D
    '''
    def setUp(self):
        self.tone = Tone(440)
        self.correct_H = 466.16
        self.correct_cents = 90.225 # 256/243
    
    def test_calc_freq(self):
        result = self.tone._calculate_frequency(100)
        self.assertLess(abs(result - self.correct_H), 0.1)
        
    def test_calc_ratio(self):
        result = self.tone._calculate_cents('256/243')
        self.assertLess(abs(result - self.correct_cents), 0.1)
        
    def test_play_two_tones_cent_interval(self):
        self.tone2 = self.tone.create_tone(100)
#        self.tone.play()
#        self.tone2.play()
        self.assertLess(abs(self.tone2.get_frequency() - self.correct_H), 0.1)
    
    def test_play_two_tones_ratio_interval(self):
        self.tone2 = self.tone.create_tone('256/243')
#        self.tone.play()
#        self.tone2.play()
        self.assertLess(abs(self.tone2.get_frequency() - self.tone._calculate_frequency(self.correct_cents)), 0.1)    
    
    def test_incorrect_ratio(self):    
        with self.assertRaises(ValueError):
            self.tone2 = self.tone.create_tone('256//243') # Any incorrect ratio should do the trick.
    
    def test_incorrect_ratio2(self):    
        with self.assertRaises(ValueError):
            self.tone2 = self.tone.create_tone('256243') # Any incorrect ratio should do the trick.    
            
    def test_set_frequency_right(self):
        self.tone.set_frequency(314.159)
        self.assertEqual(self.tone.get_frequency(), 314.159)
        
    def test_set_frequency_right2(self):
        self.tone.set_frequency('314.159')
        self.assertEqual(self.tone.get_frequency(), 314.159)
        
    def test_set_frequency_wrong(self):
        with self.assertRaises(ValueError):
            self.tone.set_frequency('not a number')
            
def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestTone('test_calc_freq'))
    suite.addTest(TestTone('test_calc_ratio'))
    suite.addTest(TestTone('test_play_two_tones_cent_interval'))
    suite.addTest(TestTone('test_play_two_tones_ratio_interval'))
    suite.addTest(TestTone('test_incorrect_ratio'))
    suite.addTest(TestTone('test_incorrect_ratio2'))
    suite.addTest(TestTone('test_set_frequency_right'))
    suite.addTest(TestTone('test_set_frequency_right2'))
    suite.addTest(TestTone('test_set_frequency_wrong'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())