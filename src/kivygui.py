# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 20:18:45 2019

@author: Slav
"""
import os
os.chdir('../')
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from src.various_melodies import melodies, names 

def callback(instance):
    melodies[instance.text].play()
    
def on_text(instance, value):
    if value == '' or value is None:
        duration = 1
    else:
        duration = float(value)
    print(duration)
    for melody in melodies.values():
        melody.set_duration(duration)
        
class TetrachordsGUI(App):
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
        settings.add_widget(duration_input)
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
        
TetrachordsGUI().run()
