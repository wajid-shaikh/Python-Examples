from kivy.app import App
from kivy.lang import Builder

root = Builder.load_string('''

Label:
    text:
        ('[b]Hello[/b] [color=ff0033]Kivy[/color]\\n'
        '[u]Hello[/u] [color=ff0033]Kivy[/color]\\n'
        '[i]Hello[/i] [color=ff0033]Kivy[/color]\\n'
        '[s]Hello[/s] [color=ff0033]Kivy[/color]\\n'
        '[font=times]Hello[/font] [color=ff0033]Kivy[/color]')




    font_size:'45pt'
    markup:True
''')

class texttag(App):
    def build(self):
        return root

if __name__ == '__main__':
    texttag().run()