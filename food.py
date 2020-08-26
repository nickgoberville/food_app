from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.vector import Vector
from kivy.clock import Clock

import pandas as pd

users = pd.read_csv('users.csv', header=0)
users_dict = users.set_index('users')['passwords'].to_dict()

class LoginPage(Screen):

    def verify_credentials(self):
        if self.ids["user"].text in users_dict.keys() and self.ids["passw"].text == users_dict[self.ids["user"].text]:
            self.manager.current = "user"

class UserPage(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

class FoodApp(App):
    def build(self):
        return kv


kv = Builder.load_file("food.kv")
if __name__ == "__main__":
    FoodApp().run()