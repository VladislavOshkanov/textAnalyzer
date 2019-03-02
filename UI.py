import kivy
import InputText

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scatter import Scatter
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.config import Config
from kivy.base import runTouchApp
from kivy.uix.checkbox import CheckBox
from Processor import process


class MainApp(App):

    def build(self):
        self.predicates = None
                
        self.root = GridLayout(cols = 1, spacing = 10)

        # create a button to release everything
       

        # show current configuration
        self.text = InputText.InputText()
        # s = Scatter(pos_hint={'x': .1 ,'y': .2 },
                    # size_hint=(.2, .8))
        ti = TextInput(pos_hint={'x': .1 ,'y': .7 }, size_hint=(.8, .2))
        # s.add_widget(ti)
        def on_text(instance, value):
            self.text.setText(value)
        ti.bind(text=on_text)
        
        self.root.add_widget(ti)
        


        def on_process_btn_release(text):
            self.predicates = process(self.text.text)
            two_pos_predicates = []
            for index, predicate in enumerate(self.predicates):
                tp = predicate.to_special_form().assign_constant_situation(index).to_two_positional().two_pos_predicates
                for pred in tp:
                    two_pos_predicates.append(pred)

            results = ScrollView()
            self.root.add_widget(results)

            resultsLayout = GridLayout(size=(1000, 1000), cols = 1, spacing = 10, size_hint_y = None)
            results.add_widget(resultsLayout)
            for index, predicate in enumerate(two_pos_predicates):
                result = GridLayout(size=(300, 300), rows=1)
                my_label = Label(text = predicate.name)
                result.add_widget(my_label)
                result.add_widget(CheckBox())
                with result.canvas.before:
                    Color(0, 1, 0, 1) # green; colors range from 0-1 instead of 0-255
                    result.rect = Rectangle(size=result.size,
                                pos=result.pos)
                resultsLayout.add_widget(result)
        
        btn = Button(text='Process', pos_hint={'x': .1, 'y': .1}, size_hint=(.8, .2),
                halign='center', on_release=on_process_btn_release)
       
        # btn.bind(on_release=release_all_keyboard)
        self.root.add_widget(btn)

    
    

if __name__ == '__main__':
    MainApp().run()
    

  

# processText("Мама мыла раму")