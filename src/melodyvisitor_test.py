# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 08:46:06 2019

@author: Slav
"""

import pytest
import unittest
#import os
#os.chdir('../')
from src.tone import Tone
from src.melody import Melody
from src.melodyvisitor import MelodyIntervalExtractor
from src.various_melodies import melodies, names

class TestVisitor(unittest.TestCase):
    '''
    Testing strategy:
        1. Test correctness of a tetrachord interval extraction.
    '''
    def setUp(self):
        self.vis = MelodyIntervalExtractor()
        
    def test_tempered_major(self):
        self.mel = melodies['Темпериран мажорен']
        result = self.mel.accept(self.vis)
        correct = [0, 200, 200, 100]
        for i in range(len(result)):
            self.assertLess(abs(result[i] - correct[i]), 0.01)
            
    def test_archites_enharmonic(self):
        self.mel = melodies['Архит - енхармоничен']
        result = self.mel.accept(self.vis)
        correct = [0, 62.960903872962575, 48.77038139681492, 386.3137138648348]
        for i in range(len(result)):
            self.assertLess(abs(result[i] - correct[i]), 0.01)
        

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestVisitor('test_tempered_major'))
    suite.addTest(TestVisitor('test_archites_enharmonic'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())