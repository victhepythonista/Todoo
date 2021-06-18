
import kivy , sys
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.config import Config

Window.size = 600,600
Config.set('graphics', 'resizable', '0')


from screens import *



kv_backend =  Builder.load_file("todo.kv")

class Todoo(App):
    def __init__(self):
        App.__init__(self)
        self.kv_backend =kv_backend
    def build(self):
        return self.kv_backend

    def apply_changes(self):
        self.kv_backend = None
        self.build()
if __name__ == "__main__":
	Todoo().run()
