# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 20:18:45 2019

@author: Slav

Натиснѝ зеленото триъгълниче горе.
"""
import os
os.chdir('../')
import pandas as pd
import matplotlib.pyplot as plt
from collections import OrderedDict
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from src.various_melodies import melodies, names 
from src.melodyvisitor import MelodyIntervalExtractor

def callback(instance):
    interval = melodies[instance.text].accept(gui.visitor) # this is definitely NOT the best way of handling the intervals and their graphing...
    if instance.text not in gui.intervals.keys():
        gui.intervals[instance.text] = interval
    melodies[instance.text].play()
    
def callback_chart(instance):
    try:
        a = pd.DataFrame(gui.intervals)
        a.T.plot(kind='bar', stacked=True, rot=0)
    except TypeError:
        print('Моля изпълнете поне един тетрахорд преди да поискате графика.')
    
def on_text(instance, value):
    if value == '' or value is None:
        duration = 1
    else:
        duration = float(value)
    print(duration)
    for melody in melodies.values():
        melody.set_duration(duration)
        
class TetrachordsGUI(App):
    def __init__(self, **kwargs):
        super(TetrachordsGUI, self).__init__(**kwargs)
        self.visitor = MelodyIntervalExtractor()
        self.intervals = OrderedDict()
        
    def build(self):
        self.main_layout = BoxLayout(orientation='vertical')
        layout_list = []
        settings = BoxLayout(orientation='horizontal')
        frequency_text = Label(text='Изберете базова честота \n(не действа все още): ')
        settings.add_widget(frequency_text)
        frequency_input = TextInput(multiline=False)
        frequency_input.bind(text=on_text)
        settings.add_widget(frequency_input)
        duration_text = Label(text='Изберете продължителност \nна тона (сек.)')
        settings.add_widget(duration_text)
        duration_input = TextInput(multiline=False)
        duration_input.bind(text=on_text)
        print(duration_input.text)
        button_chart = Button(text='Натиснете за показване на графиката.')
        button_chart.bind(on_press=callback_chart)
        settings.add_widget(duration_input)
        settings.add_widget(button_chart)
        layout_list.append(settings)
        rows = 4
        layout = BoxLayout()
        for i in range(1, len(melodies)+1):
            btn = Button(text=names[i-1])
            btn.bind(on_press=callback)
            layout.add_widget(btn)
            if (i % rows == 0) or i == len(melodies):
                layout_list.append(layout)
                layout = BoxLayout()
        
        for layout in layout_list:
            self.main_layout.add_widget(layout)
        return self.main_layout
        
    def change_duration(self, instance, value):
        duration = self.main_layout.children[0].children[0].text
        for melody in melodies.values():
            for tone in melody.get_melody():
                tone.set_duration(duration)
        
gui = TetrachordsGUI()
gui.run()
