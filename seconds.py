from kivy.clock import Clock
from scrollLabel import ScrollLabel
from kivy.properties import BooleanProperty

class Seconds(ScrollLabel):

    done = BooleanProperty(False)

    def __init__(self, total, **kwargs):
        self.done = False
        self.curent = 0
        self.total = total
        text = '[color=#000000]' + "Прошло времени: " + str(self.curent) + '[/color]'
        super().__init__(text,**kwargs)

    def restart(self, total, **kwargs):
        self.done = False
        self.curent = 0
        self.total = total
        text = '[color=#000000]'+ "Прошло времени: " + str(self.curent) + '[/color]'
        self.start()

    def start(self):
        Clock.schedule_interval(self.change, 1)
    
    def change(self, dt):
        self.curent += 1
        self.set_text('[color=#000000]' + "Прошло времени: " + str(self.curent) + '[/color]' )
        if self.curent >= self.total:
            self.done = True
            return False

