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

    def handle_calculate(self):
        """ handle calculation (could be button press or other call), output result to label widget """
        value = self.get_valid_distance()
        result = value * KM_PER_MILE
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, increment):
        """Add increment positive or negative to distance input"""

        value = self.get_valid_distance() + increment
        self.root.ids.input_field.text = str(value)
        self.handle_calculate()

    def get_valid_distance(self):
        """Check for valid distance input"""
        is_valid_input = False

        while not is_valid_input:
            try:
                value = float(self.root.ids.input_field.text)
                if value > 0:
                    is_valid_input = True
                    return value
                else:
                    print("Must be larger than zero")
                    return 0

            except ValueError:
                print("Invalid input!")
                return 0



MileToKmApp().run()
