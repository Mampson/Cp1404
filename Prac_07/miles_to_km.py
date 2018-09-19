"""
CP1404 Practical
Kivy GUI program to convert miles to kilometers
Matthew Sampson
Started 19/09/2018
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

KM_PER_MILE = 1.60934

__author__ = 'Matt Sampson'


class MileToKmApp(App):
    """ SquareNumberApp is a Kivy App for squaring a number """

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (600, 400)
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('miles_to_km.kv')
        return self.root

    def handle_calculate(self, value):
        """ handle calculation (could be button press or other call), output result to label widget """
        result = value * KM_PER_MILE
        self.root.ids.output_label.text = str(result)


MileToKmApp().run()
