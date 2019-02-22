import kivy
import InputText

from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.config import Config
from kivy.base import runTouchApp

from Processor import process


if __name__ == '__main__':

    root = FloatLayout()


    # create a button to release everything
    def on_text(instance, value):
        text.setText(value)
    def on_process_btn_release(self):
        process(text.text)

    # show current configuration
    text = InputText.InputText()
    # s = Scatter(pos_hint={'x': .1 ,'y': .2 },
                # size_hint=(.2, .8))
    ti = TextInput(pos_hint={'x': .1 ,'y': .7 }, size_hint=(.8, .2))
    # s.add_widget(ti)
    ti.bind(text=on_text)
    root.add_widget(ti)

    btn = Button(text='Process', pos_hint={'x': .1, 'y': .1}, size_hint=(.8, .2),
            halign='center', on_release=on_process_btn_release)
    # btn.bind(on_release=release_all_keyboard)
    root.add_widget(btn)

    runTouchApp(root)

  

# processText("Мама мыла раму")