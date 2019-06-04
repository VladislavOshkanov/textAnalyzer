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
from Processor import process, build_hypothesis
from IdChecker import checkForId
from IncludeChecker import checkForInclude

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)
class MainApp(App):

    def build(self):
        # Window.clearcolor = (1, 1, 1, 1)
        self.title = 'Text2Pred'
        self.predicates = None
        self.hypothesis = None
        self.root = GridLayout(cols = 1, spacing = 10)

        # create a button to release everything
       

        # show current configuration
        self.text = InputText.InputText()
        # s = Scatter(pos_hint={'x': .1 ,'y': .2 },
                    # size_hint=(.2, .8))
        ti = TextInput(text = '', pos_hint={'x': .1 ,'y': .7 }, size_hint=(.8, .2))
        # s.add_widget(ti)
        def on_text(instance, value):
            self.text.setText(value)
        ti.bind(text=on_text)
        
        self.root.add_widget(ti)
        


        def on_process_btn_release(text):
            self.predicates = process(self.text.text)
            self.hypothesis = build_hypothesis(self.text.text)

            for h in self.hypothesis:
                print(h.to_string())

            two_pos_predicates = []

            for index1, predicate1 in enumerate(self.predicates):
                for index2, predicate2 in enumerate(self.predicates):
                    h = checkForId(predicate1, predicate2, index1, index2)
                    if h and index1 > index2: 
                        print(h.to_string())
                        self.hypothesis.append(h)

            for index1, predicate1 in enumerate(self.predicates):
                for index2, predicate2 in enumerate(self.predicates):
                    h = checkForInclude(predicate1, predicate2, index1, index2)
                    if h and index1 != index2: 
                        print(h.to_string())
                        self.hypothesis.append(h)

            for index, predicate in enumerate(self.predicates):
                tp = predicate.to_special_form().assign_constant_situation(index).to_two_positional().two_pos_predicates
                for pred in tp:
                    two_pos_predicates.append(pred)

            results = ScrollView()
            self.root.add_widget(results)

            resultsLayout = GridLayout(size=(1000, 1000), cols = 1, spacing = 10, size_hint_y = None)
            results.add_widget(resultsLayout)

            checkboxes_refs = {}
            buttons_refs = {}
            labels_refs = {}


            for index, h in enumerate(self.hypothesis):
                result = GridLayout(size=(300, 300), rows=1)
                my_label = Label(text = "Гипотеза " + h.to_string())
                result.add_widget(my_label)
                result.add_widget(GridLayout(size=(100,100)))
                button = Button(text='Гипотеза верна')
                def change_text(button):
                    if button.text == 'Гипотеза верна':
                        button.text = 'Гипотеза не верна'
                    else:
                        button.text = 'Гипотеза верна'
                button.bind(on_press=change_text)
                result.add_widget(button)   
                resultsLayout.add_widget(result)


            for index, predicate in enumerate(two_pos_predicates):
                result = GridLayout(size=(300, 300), rows=1)
                my_label = Label(text = predicate.to_string())
                labels_refs[str(index)] = {"label": my_label, "pred": predicate, "ti":None}
                result.add_widget(my_label)
                if (isinstance(predicate.value, str) and not hasNumbers(predicate.value) and predicate.value.find('_') > 0):
                    labels_refs[str(index)]["ti"] = TextInput()
                    result.add_widget(labels_refs[str(index)]["ti"])
                else:
                    result.add_widget(GridLayout(size=(100,100)))

                cb = CheckBox()
                checkboxes_refs["CB" + str(index)] = {"checkbox": cb, "cs": predicate.constant_situation};            
                result.add_widget(cb)
        
                resultsLayout.add_widget(result)
            def on_cs_btn_release(arg):
                cs_set = set()
                for idx, cb in checkboxes_refs.items():
                    print(cb["checkbox"].active)
                    if (cb["checkbox"].active):
                        cs_set.add(cb["cs"])
                print(cs_set)
                if (len(cs_set) > 1): 
                    for predicate in two_pos_predicates:
                        if predicate.constant_situation in cs_set:
                            predicate.constant_situation = list(cs_set)[0]
                    
                for idx, label in labels_refs.items():
                    label["label"].text = label["pred"].to_string()
            def on_pred_btn_release(arg):
                for idx, cb in labels_refs.items():
                    if cb["ti"]:
                        cb["pred"].value = cb["ti"].text
                        cb["label"].text = cb["pred"].to_string()
            btn_cs = Button(text='Объединить константы-ситуации', pos_hint={'x': .1, 'y': .1}, size_hint=(.8, .2),
                halign='center', on_release=on_cs_btn_release)
            self.root.add_widget(btn_cs)
            btn_cs = Button(text='Заполнить значения предикатов', pos_hint={'x': .1, 'y': .1}, size_hint=(.8, .2),
                halign='center', on_release=on_pred_btn_release)
            self.root.add_widget(btn_cs)
        

        btn = Button(text='Обработать текст', pos_hint={'x': .1, 'y': .1}, size_hint=(.8, .2),
                halign='center', on_release=on_process_btn_release)
        # btn.bind(on_release=release_all_keyboard)
        self.root.add_widget(btn)

    
    

if __name__ == '__main__':
    MainApp().run()
    

  

# processText("Мама мыла раму")