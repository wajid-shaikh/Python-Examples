# import kivy
# from kivy.app import App
# from kivy.base import runTouchApp
# from kivy.lang import Builder

# runTouchApp(Builder.load_string('''

# BoxLayout:
#     Button:
#         text: 'B'
# '''))

from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text='Hello World')

if __name__ =='__main__':
    MyApp().run()