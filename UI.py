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
from HypothesisBuilder import build_hypothesis_by_predicates
import networkx as nx
import matplotlib.pyplot as plt

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)
class MainApp(App):
    
    def _update_rect2(self, instance, value):
        self.rect2.pos = instance.pos
        self.rect2.size = instance.size
    def _update_rect3(self, instance, value):
        self.rect3.pos = instance.pos
        self.rect3.size = instance.size
    def _update_rect4(self, instance, value):
        self.rect4.pos = instance.pos
        self.rect4.size = instance.size

    def build(self):
        Window.clearcolor = (0.93, 0.93, 0.93, 1)
        self.title = 'Text2Pred'
        self.predicates = None
        self.hypothesis = None
        self.root = GridLayout(cols = 2, spacing = 20)

        self.area1 = GridLayout(cols=1)
        self.area2 = GridLayout(cols=1)
        self.area3 = GridLayout(cols=1)
        self.area4 = GridLayout(cols=1)

        with self.area2.canvas.before:
            Color(1, 1, 1, 1)  # green; colors range from 0-1 not 0-255
            self.rect2 = Rectangle(size=self.area2.size, pos=self.area2.pos)
        
        with self.area3.canvas.before:
            Color(1, 1, 1, 1)  # green; colors range from 0-1 not 0-255
            self.rect3 = Rectangle(size=self.area3.size, pos=self.area3.pos)
            
        with self.area4.canvas.before:
            Color(1, 1, 1, 1)  # green; colors range from 0-1 not 0-255
            self.rect4 = Rectangle(size=self.area4.size, pos=self.area4.pos)

        self.area2.bind(size=self._update_rect2, pos=self._update_rect2)
        self.area3.bind(size=self._update_rect3, pos=self._update_rect3)
        self.area4.bind(size=self._update_rect4, pos=self._update_rect4)

        
        self.root.add_widget(self.area1)
        self.root.add_widget(self.area2)
        self.root.add_widget(self.area3)
        self.root.add_widget(self.area4)

       
        self.text = InputText.InputText()

        ti = TextInput(text = '', pos_hint={'x': .1 ,'y': .7 })

        def on_text(instance, value):
            self.text.setText(value)
        ti.bind(text=on_text)
        
        self.area1.add_widget(ti)
        


        def on_process_btn_release(text):
            G = nx.DiGraph()
            self.predicates = process(self.text.text)
            self.hypothesis = build_hypothesis(self.text.text)

            for h in self.hypothesis:
                print(h.to_string())

            two_pos_predicates = []

            build_hypothesis_by_predicates(self.predicates, self.hypothesis)
          
            for index, predicate in enumerate(self.predicates):
                tp = predicate.to_special_form().assign_constant_situation(index).to_two_positional().two_pos_predicates
                for pred in tp:
                    two_pos_predicates.append(pred)

            results = ScrollView()
            self.area4.add_widget(results)

            lt_results = ScrollView()
            self.area2.add_widget(lt_results)

            resultsLayout = GridLayout(size=(200, 200), cols = 1, spacing = 10)
            results.add_widget(resultsLayout)

            lt_resultsLayout = GridLayout(size=(200, 200), cols = 1, spacing = 10)
            lt_results.add_widget(lt_resultsLayout)


            checkboxes_refs = {}
            buttons_refs = {}
            labels_refs = {}


            for index, h in enumerate(self.hypothesis):
                result = GridLayout(size=(200, 200), rows=1)
                my_label = Label(text = '[color=719b7f]{}[color=000000](S{},S{})'.format(h.name, h.first_cs, h.second_cs),
                    markup = True, 
                    size_hint=(1.0, 1.0), halign="left", valign="middle", font_size='20sp')
                my_label.bind(size=my_label.setter('text_size'))    
                result.add_widget(my_label)
                result.add_widget(GridLayout(size=(100,100)))
                resultsLayout.add_widget(result)
                if h.name=='Include':
                    G.add_edge('S{}'.format(h.first_cs), 'S{}'.format(h.second_cs))


            for index, predicate in enumerate(two_pos_predicates):
                result = GridLayout(size=(300, 200), rows=1, size_hint=(1.0, 1.0))
                
                my_label = Label(text = '[color=719b7f]{}[color=000000](S{},{})'.format(predicate.name, predicate.constant_situation, predicate.value),
                    markup = True, 
                    size_hint=(1.0, 1.0), halign="left", valign="middle", font_size='20sp')

                my_label.bind(size=my_label.setter('text_size'))    
                labels_refs[str(index)] = {"label": my_label, "pred": predicate, "ti":None}
                result.add_widget(my_label)
                cb = CheckBox()
                checkboxes_refs["CB" + str(index)] = {"checkbox": cb, "cs": predicate.constant_situation};            
                resultsLayout.add_widget(result)

            for index, predicate in enumerate(self.predicates):
                result = GridLayout(size=(300, 200), rows=1, size_hint=(1.0, 1.0))
                G.add_node('S{}'.format(predicate.roles['constant_situation']))

                for t_p_pred in two_pos_predicates:
                    if (t_p_pred.constant_situation == predicate.roles['constant_situation']):
                        G.add_node(t_p_pred.value)
                        G.add_edge('S{}'.format(predicate.roles['constant_situation']), t_p_pred.value)


                my_label = Label(text = predicate.to_string(),
                    markup = True, 
                    size_hint=(1.0, 1.0), halign="left", valign="middle", font_size='20sp')

                my_label.bind(size=my_label.setter('text_size'))    
                labels_refs[str(index)] = {"label": my_label, "pred": predicate, "ti":None}
                result.add_widget(my_label)
                lt_resultsLayout.add_widget(result)    

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
            # self.root.add_widget(btn_cs)
            btn_cs = Button(text='Заполнить значения предикатов', pos_hint={'x': .1, 'y': .1}, size_hint=(.8, .2),
                halign='center', on_release=on_pred_btn_release)
            # .root.add_widget(btn_cs)

            plt.subplot(121)
            nx.draw(G, with_labels=True, font_size=10, node_size=1000, node_color="#ffffff")
            # plt.subplot(122)
            # nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')
            plt.show()

        btn = Button(text='Обработать текст', pos_hint={'x': .1, 'y': .1}, size_hint=(.8, .2),
                halign='center', 
                on_release=on_process_btn_release,
                background_normal='',
                background_color=(0.67, 0.95, 0.76, 1),
                color=(0,0,0,1),
                font_size='24sp')
        # btn.bind(on_release=release_all_keyboard)
        self.area1.add_widget(btn)

    
    

if __name__ == '__main__':
    MainApp().run()
    
