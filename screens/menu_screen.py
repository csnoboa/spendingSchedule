from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder

kvfile = Builder.load_string(""" 
<MenuScreen>:
    canvas:
        Color:
            rgba: 1,1,1,1
        Rectangle:
            size:self.size
            pos:self.pos
            # source:'images/blue-screen.png'
    BoxLayout:
        id: box
        orientation: 'vertical'
        ActionBar:
            ActionView:
                ActionPrevious:
                    title: 'Spendings Schedule'
                ActionButton:
                    text: 'Schedule'
                    width: 150
                ActionButton:
                    text: 'Credit Cards'
                    on_release: root.editOpen(self)
                ActionButton:
                    text: 'Bank Accounts'
                    on_release: root.searchOpen(self)
                ActionButton:
                    text: 'Help'
        Label:
""")

class MenuScreen(Screen):
    pass
