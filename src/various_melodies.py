# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 20:06:04 2019

@author: Slav

Various melodies.

Направи го на клас - интерфейс КолекцияОтМелодии, който да има методи добавяне,
получаване и - най-важното - пресмятане на интервалите на всяка мелодия според
зададена честота (оправи и другата текстова кутийка в интерефейса). Този интерфейс
може да има две конкретни имплементации (тук по-скоро йерархията е основен клас ->
два конкретни наследника) - КолекцияОтАнтичниТетрахорди и КолекцияОтВизантийскиГласове.
"""
#import os
#os.chdir('../')
from src.tone import Tone
from src.melody import Melody
import time
import abc

tempered_dur = [200, 200, 100]
tempered_moll = [200, 100, 200]
archites_enharmonic = ['28/27', '36/35', '5/4']
eratosthenes_encharmonic = ['40/39', '39/38', '19/15']
didimes_encharmonic = ['32/31', '31/30', '5/4']
ptolemy_encharmonic = ['46/45', '24/23', '5/4']
archites_chromatic = ['28/27', '243/224', '32/27']
eratosthenes_chromatic = ['20/19', '19/18', '6/5']
didimes_chromatic = ['16/15', '25/24', '6/5']
ptolemy_chromatic = ['28/27', '15/14', '6/5']
ptolemy_chromatic2 = ['22/21', '12/11', '7/6']
archites_diatonic = ['28/27', '8/7', '9/8'] 
eratosthenes_diatonic = ['256/243', '9/8', '9/8']
didimes_diatonic = ['16/15', '10/9', '9/8']
ptolemy_diatonic_soft = ['21/20', '10/9', '8/7']
ptolemy_diatonic_tonic = ['28/27', '8/7', '9/8']
ptolemy_diatonic_hard = ['16/15', '9/8', '10/9']
ptolemy_diatonic_flat = ['12/11', '11/10', '10/9']
ptolemy_diatonic_double = ['256/243', '9/8', '9/8']

names = ['Темпериран\nмажорен',
         'Темпериран\nминорен',
         'Архит\nенхармоничен',
         'Ератостен\nенхармоничен',
         'Дидим\nенхармоничен',
         'Птолемей\nенхармоничен',
         'Архит\nхроматичен',
         'Ератостен\nхроматичен',
         'Дидим\nхроматичен',
         'Птолемей\nхроматичен\nмек',
         'Птолемей\nхроматичен\nтвърд',
         'Архит\nдиатоничен',
         'Ератостен\nдиатоничен',
         'Дидим\nдиатоничен',
         'Птолемей\nдиатоничен\nмек',
         'Птолемей\nдиатоничен\nтонов',
         'Птолемей\nдиатоничен\nтвърд',
         'Птолемей\nдиатоничен\nравен',
         'Птолемей\nдиатоничен\nдвоен']

intervals = [tempered_dur,
                  tempered_moll,
                  archites_enharmonic,
                  eratosthenes_encharmonic,
                  didimes_encharmonic,
                  ptolemy_encharmonic,
                  archites_chromatic,
                  eratosthenes_chromatic,
                  didimes_chromatic,
                  ptolemy_chromatic,
                  ptolemy_chromatic2,
                  archites_diatonic,
                  eratosthenes_diatonic,
                  didimes_diatonic,
                  ptolemy_diatonic_soft,
                  ptolemy_diatonic_tonic,
                  ptolemy_diatonic_hard,
                  ptolemy_diatonic_flat,
                  ptolemy_diatonic_double]

melodies = {}
for i in range(len(names)):
    new_melody = Melody(Tone(250), names[i])
    for j in range(len(intervals[i])):
        new_melody.add_tone(intervals[i][j])
    melodies[names[i]] = new_melody

#for melody in melodies.values():
#    melody.play()
#    time.sleep(1)

