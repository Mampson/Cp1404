"""
CP 1404
Names widget App
by
Matthew Sampson
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty


class NameWidgetApp(App):
    """main program for name widgets"""

    def __init__(self, **kwargs):
        """Main app construction"""

        super().__init__(**kwargs)
        self.names = {"Matt Sampson", "Steve Jobs", "Bob Kater"}

    def build(self):
        """
        Build the GUI for Names widgets
        """
        self.title = "Names Widgets"
        self.root = Builder.load_file("names_widgets.kv")
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create name tiles"""

        for name in self.names:
            temp_button = Button(text=name, id=name)
            # temp_button.bind(on_release=self.press_entry)
            self.root.ids.name_entries.add_widget(temp_button)

    def clear_all(self):
        """
        Clear all of the widgets of names
        """
        self.root.ids.name_entries.clear_widgets()


NameWidgetApp().run()