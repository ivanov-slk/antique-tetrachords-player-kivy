# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 18:04:14 2019

@author: Slav
"""

from pysine import sine
from math import log
import time

def get_freq(freq, cents):
    new_freq = freq * 2 ** (cents / 1200)
    return new_freq

def get_cents(ratio):
    a, b = [int(x) for x in ratio.split('/')]
    cents = 1200 * log((a/b), 2)
    return cents
    
    
freq = 440

for i in range(12):
#    sine(freq, 1)
    freq = get_freq(freq, 100)
    print(freq)
    
base = 440
freq_list = [base]
archites_ratios = ['28/27', '36/35', '5/4']
ptolemy_encharmonic = ['46/45', '24/23', '5/4']
ptolemy_chromatic = ['28/27', '15/14', '6/5']
ptolemy_chromatic2 = ['22/21', '12/11', '7/6']
ptolemy_diathonic_soft = ['21/20', '10/9', '8/7']
ptolemy_diathonic_tonic = ['28/27', '8/7', '9/8']
ptolemy_diathonic_hard = ['16/15', '9/8', '10/9']
ptolemy_diathonic_flat = ['12/11', '11/10', '10/9']
ptolemy_diathonic_double = ['256/243', '9/8', '9/8']

names = ['Птолемей - енхармоничен',
         'Птолемей - хроматика',
         'Птолемей - хроматика твърда',
         'Птолемей - диатоника - мека',
         'Птолемей - диатоника - тонова',
         'Птолемей - диатоника - твърда',
         'Птолемей - диатоника - равна',
         'Птолемей - диатоника - двойна']

ptolemy_chords = [ptolemy_encharmonic,
                  ptolemy_chromatic,
                  ptolemy_chromatic2,
                  ptolemy_diathonic_soft,
                  ptolemy_diathonic_tonic,
                  ptolemy_diathonic_hard,
                  ptolemy_diathonic_flat,
                  ptolemy_diathonic_double]

for j in range(len(ptolemy_chords)):
    cents_list = []
    freq_list = [base]
    for i in range(3):
        new_cent = get_cents(ptolemy_chords[j][i])
        cents_list.append(new_cent)
        new_freq = get_freq(freq_list[-1], cents_list[-1])
        freq_list.append(new_freq)
    print('==============================================================')
    print(names[j])
    print(freq_list)
    print(cents_list)
    print(sum(cents_list))
    print('==============================================================')
    print()
        
    for freq in freq_list:
        sine(freq, 1.5)
    time.sleep(1)
    
