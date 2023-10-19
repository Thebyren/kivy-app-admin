from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang.builder import Builder
class DashBoard(MDScreen):
    pass

class TemplateScreen(MDScreen):
    pass

class main_screen(MDScreen):
    pass
class Main(MDApp):
    def build(self):
        Builder.load_file("layout.kv")
        self.theme_cls.theme_style = "Light"
        return main_screen()

Main().run()