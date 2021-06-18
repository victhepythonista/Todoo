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
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.checkbox import CheckBox
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.uix.carousel import Carousel
from kivy.uix.dropdown import DropDown
from kivy.uix.screenmanager import Screen
from data import DATAMANAGER
from settings import SETTINGS

class DataLabel(Label):
	def __init__(self,text = ""):
		Label.__init__(self)
		self.text = text

class DeleteButton(Button):
	def on_press(self):
		DATAMANAGER().remove_pending(self.parent.todo_index)
		self.parent.itemsscroll.load_pending_items()
class DoneButton(Button):
	def on_press(self):
		try:
			DATAMANAGER().update_state(self.parent.todo_index)

		except:pass
		self.parent.itemsscroll.load_pending_items()
class CompletedDeleteButton(Button):
	def on_press(self):
		DATAMANAGER().remove_done(self.parent.index)
class CompletedTodoItem(BoxLayout):
	def __init__(self, description,datedone , index ):
		BoxLayout.__init__(self)
		self.padding = 10
		self.size_hint = 1,.1
		self.cols = 3
		self.orientation = 'horizontal'
		self.spacing = 10
		self.index =  index

		descriptionlabel  = DataLabel(text = description)
		datedone =DataLabel(text = datedone)
		delete_button = CompletedDeleteButton(text = 'X')
		self.add_widget(descriptionlabel)
		self.add_widget(datedone)
		self.add_widget(delete_button)


class TodoItem(BoxLayout):

	def __init__(self, todoitemname, todo_index , itemsscroll):
		BoxLayout.__init__(self)
		self.cols = 3
		self.orientation = 'horizontal'
		self.spacing = 10
		self.padding = 10
		self.size_hint_Y=None
		self.itemsscroll = itemsscroll
		self.todo_index = todo_index
		namelabel  = DataLabel(text = todoitemname)
		done_button = DoneButton()
		deletebutton = DeleteButton(text = 'X')

		self.add_widget(namelabel)
		self.add_widget(done_button)
		self.add_widget(deletebutton)

class  ItemsCarousel(Carousel):
	pass
class CompletedItems(FloatLayout):
	completeditems_scroll = ObjectProperty(None)

	def load_completed_items(self):
		self.completeditems_scroll.clear_widgets()

		for item in DATAMANAGER().read_done():
			index = item[0]
			description = item[1]
			date_done = item[2]
			self.completeditems_scroll.add_widget(CompletedTodoItem(description,date_done,index))


class PendingItems(FloatLayout):
	pendingitems_scroll = ObjectProperty(None)
	def load_pending_items(self):

		self.pendingitems_scroll.clear_widgets()
		for item_info in DATAMANAGER().read_pending():
			# iteminfo - index, desc,state
			index =item_info[0]
			description = item_info[1]
			state = item_info[2]

			self.pendingitems_scroll.add_widget(TodoItem(description,index, self))

	pass
class DropButton(Button):
	pass
class NavigationButton(Button):
	pass

class NavigationBar(GridLayout):
	pass

class RoundedButtonContainer(FloatLayout):
	pass
class ItemsContainer(FloatLayout):
	pass
class ItemsScrollView(ScrollView):
	pass

class OthersDropdown(DropDown):
	pass
class ScreenLabel(Label):
	pass
class ContentLayout(FloatLayout):
	pass
class ThemeCheckBox(CheckBox):
	themename = ObjectProperty(None)
	def change_theme(self ):
		if self.state == 'down':
			print('[-]changing theme to > ',self.themename)
			SETTINGS().write('CONFIG','theme',self.themename)
	def on_state(self, instance, value):
		self.change_theme()
class ADDTODOINPUT:
	def show(self):
	 	## initialize the popup screen
		window = Popup()
		window.title = 'NEW TODO'
		window.title_align = 'center'
		window.background_color = 0,.2,0,1
		window.title_color =(0.0, 0.7, 0.8373, 1)
		window.font_size = 30
		window.size_hint = .8,.6
		backend_screen = ADDTODOPOPUPSCREEN()
		backend_screen.par = window
		window.content = backend_screen
		window.color = 0.5255, 0.639 , 0.643
		window.open()

class ADDTODOPOPUPSCREEN(Screen):
	description = ObjectProperty(None)
	par = ObjectProperty(None)

	def add_todo(self):
		if self.description != "":
			DATAMANAGER().add_pending(self.description.text)
			self.description.text = ''
			self.par.dismiss()
class AddButton(Button):
	def on_press(self):
		ADDTODOINPUT().show()
