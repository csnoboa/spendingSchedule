from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang.builder import Builder
from screens import menu_screen

kvfile = Builder.load_string("""
<Manager>:
    MenuScreen:
        name: 'menu'
""")

class Manager(ScreenManager):
	pass

class TestPrio(App):
    def build(self):
        return Manager()

TestPrio().run()

