from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from testing import Testing
import os

class MyGrid(GridLayout):
    filechooser = ObjectProperty(None)
    
    def selectedImage(self, filename):
    	try:
    	   self.ids.image.source = filename[0]
    	   print(filename[0])
    	   filename = filename[0]
    	except Exception as e:
    	   pass
    
    def btn(self, filename):
        try:
            self.ids.image.source = filename[0]
            filename = filename[0]
        except Exception as e:
            pass
        show_popup(filename)



class ResultsPopup(GridLayout):
	
    def __init__(self, msg, **kwargs):
        super(ResultsPopup, self).__init__(**kwargs)
        self.cols = 1
        # filename2 = filename
        path = os.path.join(f'Models/')
        All = []
        messages = Testing(msg).run()
        for message in messages:
            self.add_widget(Label(text= message))
            All.append(message)
        messages.clear()

class allclassifierApp(App):
    def build(self):
        return MyGrid()

def show_popup(filename):
       showpopup = ResultsPopup(filename)
       popupWindow = Popup(title="AI Results", content=showpopup, size_hint=(None, None), size=(500, 500))
       popupWindow.open()


if __name__ == '__main__':
    allclassifierApp().run()
