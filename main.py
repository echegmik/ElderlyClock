#set kivy config, fullscreen and exist on escape
from kivy.config import Config
Config.set('kivy', 'exit_on_escape', '1')
Config.set('graphics', 'fullscreen', 'auto')
Config.write()

from kivy.app import App
from kivy.uix.widget import Widget
from time import  strftime, localtime
from kivy.clock import Clock



class MegaClock(Widget):
    time = strftime("%H:%M:%S", localtime())
    date = strftime("%a, %d %b %Y", localtime())
    def update(self, *args):
        self.ids["time_label"].text = strftime("%H:%M:%S", localtime())
        self.ids["date_label"].text = strftime("%a, %d %b %Y", localtime())

class MegaClockApp(App):
    def build(self):
        clock = MegaClock()
        Clock.schedule_interval(clock.update, 1)
        return clock

if __name__ == '__main__':
    MegaClockApp().run()
