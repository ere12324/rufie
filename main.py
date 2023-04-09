import kivy 
from kivy.config import Config

Config.set("graphics","resizable", 0)
Config.set("graphics","width", 700)
Config.set("graphics","height", 600)

from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.app import App
from kivymd.uix.button import  MDRectangleFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield.textfield import MDTextField
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from instructions import instructions0, instructions1, instructions2, instructions3, instructions4, instructions5
from ruffier import ruffie
from kivy.clock import Clock
from seconds import Seconds
from kivy.animation import Animation
from kivy.uix.image import Image
from kivy.graphics import Rectangle 

img_path = b"C:\Users\Algoritmika\AppData\Local\Programs\Algoritmika\vscode\data\extensions\algoritmika.algopython-20230221.174607.0\data\student\1049244\199819\gradients_app.png"
ruffie

name = ""
age = 0
result = 0
one = 0
two = 0
pink = (0, 0, 0, 1)
Window.clearcolor = pink

class ButtonScr(MDRectangleFlatButton):
    def __init__(self, screen, direction, goal, **kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.direction = direction
        self.goal = goal
    def on_press(self):
        self.screen.manager.transition.direction = self.direction 
        self.screen.manager.current = self.goal

class MainScr(Screen):
    def __init__(self, name = 'main'):
        super().__init__(name=name)

        box = BoxLayout(orientation = 'vertical',padding=8, spacing=8)
        MDlabel = MDLabel(text = instructions0, font_size = 21,)
        box.add_widget(MDlabel)
        btn = ButtonScr(screen = self, direction = 'right', 
                                        goal = 'two',text= "Начнём тест твоего сердечка",
                                        size_hint = (0.5, 0.5), 
                                        pos_hint={'center_x':0.5, 'center_y':0},
                                        text_color = (0,0,0))
        btn.on_press = self.next 
        self.ti1 = MDTextField(hint_text = 'Как тебя зовут?', halign = 'left', multiline=False, size_hint = (2, 0.5), font_size = 28)
        self.ti2 = MDTextField(hint_text = 'Сколько ты проживешь в этой галактике?', halign = 'left', multiline=False, size_hint = (2, 0.5), font_size = 28)
        box.add_widget(self.ti1)
        box.add_widget(self.ti2)
        box.add_widget(btn)
        self.add_widget(box)

    def next(self):
        global name, age
        name = self.ti1.text
        age = self.ti2.text
        self.manager.current = 'first'
        print(name, age)

class FirstScr(Screen):
    def __init__(self, name='first'):
        sec1 = Seconds(15,
                       size_hint = (0.6, 0.5), 
                       pos_hint={
                           'center_x':0.7, 
                           'center_y':0.7})

        box = BoxLayout(orientation = 'vertical',padding=8, spacing=8)
        super().__init__(name=name) # имя экрана должно передаваться конструктору класса Screen
        btn = ButtonScr(screen = self, 
                        direction = 'right', 
                        goal = 'two',
                        text= instructions1,
                        size_hint = (0.3, 0.1), 
                        pos_hint={'center_x':0.5, 'center_y':0.})

        btn1 = MDRectangleFlatButton(size_hint = (0.3, 0.1), 
                        pos_hint={'center_x':0.5, 
                        'center_y':0.7}, 
                        text= "Таймер")

        btn.on_press = self.next
        btn1.on_press = sec1.start
        self.ti = MDTextField(text = '', 
                            halign = 'left',
                            font_size = 28,
                            size_hint = (0.5,0.5),
                            pos_hint={
                                'center_x':0.5,
                                'center':0.5})


        box.add_widget(self.ti)
        self.add_widget(box)
        box.add_widget(btn)
        box.add_widget(btn1)
        box.add_widget(sec1)

    def next(self):
        global result
        result = int(self.ti.text)
        self.manager.current = 'two'
        print(result)


class TwoScr(Screen):
    def __init__(self, name='two'):
        box = BoxLayout(orientation = 'vertical',padding=8, spacing=8)
        super().__init__(name=name) # имя экрана должно передаваться конструктору класса Screen
        btn = ButtonScr(screen = self, 
                        direction = 'right', 
                        goal = 'thri',
                        text= instructions2,
                        size_hint = (0.3, 0.1), 
                        pos_hint={'center_x':0.5, 'center_y':0})

        sec2 = Seconds(45,
                       size_hint = (0.6, 0.5), 
                       pos_hint={
                           'center_x':0.7, 
                           'center_y':0.7})

        btn2 = MDRectangleFlatButton(size_hint = (0.3, 0.1), 
                        pos_hint={'center_x':0.5, 
                        'center_y':0}, 
                        text= "Таймер")
                        

        btn2.on_press = sec2.start
        box.add_widget(btn)
        box.add_widget(btn2)
        box.add_widget(sec2)
        self.add_widget(box)
        #Нужен таймер


class ThriScr(Screen):
    def __init__(self, name='thri'):
        sec3 = Seconds(15,
                        size_hint = (0.6, 0.5), 
                        pos_hint={
                           'center_x':0.7, 
                           'center_y':0.7})
        global result,one,two
        super().__init__(name=name) # имя экрана должно передаваться конструктору класса Screen
        box = BoxLayout(orientation = 'vertical',padding=8, spacing=8)
        btn = ButtonScr(screen = self, 
                        direction = 'right', 
                        goal = 'frour',
                        text= instructions3,
                        pos_hint = {'center_x':0.5,
                        'center_y':0.5})

        btn.on_press = self.next
        self.ti = MDTextField(text = '', 
                            halign = 'left', 
                            multiline=False,
                            size_hint = (0.5,0.5),
                            pos_hint={
                                'center_x':0.5,
                                'center':0.5},
                            font_size = 28)
        box.add_widget(self.ti)
        btn3 = MDRectangleFlatButton(size_hint = (0.3, 0.1), 
                        pos_hint={'center_x':0.5, 
                        'center_y':0.5}, 
                        text= "Таймер")
        btn3.on_press = sec3.start
        box.add_widget(btn)
        box.add_widget(btn3)
        box.add_widget(sec3)
        self.add_widget(box)

    def next(self):
        global one
        one = int(self.ti.text)
        self.manager.current = 'frour'
        print(one)
    #Нужен таймер 15


class FrourScr(Screen):
    def __init__(self, name='frour'):
        sec4 = Seconds(30 ,
                        size_hint = (0.5, 0.5),
                        pos_hint = {'center_x':0.65,
                        'center_y':0.6}) 

        box = BoxLayout(orientation = 'vertical',padding=8, spacing=8, center = (30, -110))
        super().__init__(name=name) # имя экрана должно передаваться конструктору класса Screen
        btn = ButtonScr(screen = self, 
                        direction = 'right', 
                        goal = 'Five',
                        text= instructions4,
                        size_hint = (0.3, 0.1),
                        pos_hint={'center_x':0.52, 
                        'center_y':0.5})

        btn4 = MDRectangleFlatButton(size_hint = (0.3, 0.1),
                        pos_hint={'center_x':0.52, 
                        'center_y':0.5}, 
                        text= "Таймер")
        btn4.on_press = sec4.start
        box.add_widget(btn)
        box.add_widget(btn4)
        box.add_widget(sec4)
        self.add_widget(box)


class FiveScr(Screen):
    def __init__(self, name='Five'):
        sec5 = Seconds(15,
                        size_hint = (0.3, 0.1), 
                        pos_hint={
                           'center_x':0.56, 
                           'center_y':0.5})
        box = BoxLayout(orientation = 'vertical',padding=8, spacing=8,center = (30, -110))
        super().__init__(name=name) # имя экрана должно передаваться конструктору класса Screen
        btn = ButtonScr(screen = self, 
                        direction = 'right', 
                        goal = 'Six',
                        text= instructions5,
                        pos_hint={
                            'center_x':0.5,
                            'center':0.5})

        self.add_widget(box)
        btn.on_press = self.next
        self.ti = MDTextField(text = '',
                            halign = 'left', 
                            multiline=False,
                            size_hint = (0.5,0.5),
                            pos_hint={
                                'center_x':0.5,
                                'center':0.5},
                            font_size = 28)


        box.add_widget(self.ti)
        btn5 = MDRectangleFlatButton(size_hint = (0.1, None), 
                        pos_hint={'center_x':0.5}, 
                        text= "Таймер")
        box.add_widget(btn)
        btn5.on_press = sec5.start
        box.add_widget(btn5)
        box.add_widget(sec5)

    def next(self):
        global two
        two = int(self.ti.text)
        self.manager.current = 'Six'
        print(two)
        #Нужен таймер


class SixScr(Screen):
    def __init__(self, name='Six'):
        super().__init__(name=name) 
        global result,one,two
        print("\n\n\n\n", result, one, two)
        box = BoxLayout(orientation = 'vertical',padding=8, spacing=8,center = (80, 50))
        # имя экрана должно передаваться конструктору класса Screen
        btn = MDRectangleFlatButton(text = "Результат",
                                    pos_hint={
                                    'center_x':0.45,
                                    'center_y':10})
        btn.on_press = self.result

       
        self.MDlabel = MDLabel(text = str(''),
                                pos_hint={
                                'center_x':0.9,
                                'center_y':100})
        self.MDlabel1 = MDLabel(text = '',
                                pos_hint={
                                    'center_x':0.9,
                                    'center_y':100})
        box.add_widget(self.MDlabel)
        box.add_widget(self.MDlabel1)
        box.add_widget(btn)
        self.add_widget(box)

    def result(self):
        ruffie_index, ruffie_text = ruffie(result,one,two,age)
        self.MDlabel.text = str(ruffie_index)
        self.MDlabel1.text = str(ruffie_text)


class MyApp(MDApp):
   def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScr())
        sm.add_widget(FirstScr())
        sm.add_widget(TwoScr())
        sm.add_widget(ThriScr())
        sm.add_widget(FrourScr())
        sm.add_widget(FiveScr())
        sm.add_widget(SixScr())
        return sm


app = MyApp()
app.run()