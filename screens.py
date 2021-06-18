import  configparser , random, os
from kivy.uix.screenmanager import Screen,ScreenManager, WipeTransition, FadeTransition
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.textinput import TextInput
from kivy.uix.switch import Switch
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.properties import BooleanProperty, ObjectProperty
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.config import Config

from data import DATAMANAGER
from settings import SETTINGS

from customwidgets import *


Window.clearcolor = SETTINGS().colors('window_clearcolor')

class SCREENMANAGER(ScreenManager):
	pass
# *************************************************************
class HOMESCREEN(Screen):
	pass
#**********************************************************************************************
class LOADINGSCREEN(Screen):
	pass
#**********************************************************************************************
class SETTINGSSCREEN(Screen):
	def reload(self):
		Window.clearcolor = SETTINGS().colors('windows_bg')


class HELPSCREEN(Screen):
    pass
