from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock

root = Builder.load_string('''
FloatLayout:
    Scatter:
        id: scatter
        size_hint:None, None
        size: 100, 100
        pos: root.width / 2 - self.width / 2, root.hieght / 2 - self.hieght / 2
        Button:
            text: 'Clock'
''')

class TestApp(App):
    def build(self):
        Clock.schedule_interval(self.rotate, 3)
        return root

    def rotate(self, dt):
        root.ids.scatter.rotation +=3
if __name__ == '__main__':
    TestApp().run()