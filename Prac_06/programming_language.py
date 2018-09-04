"""
Build first Class Object
by Matthew Sampson
"""


class ProgramingLanguage:
    """Represent Language Object"""

    def __init__(self, title="", typing="", reflection="", year=0):
        """Initialize Language instance

        title = language name
        typing = static or dynamic
        reflection = true or false / yes or no
        year = year created
        """
        self.title = title
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Returns string of language object info"""
        return "Title = {}, Typing status  = {}, Reflection = {}, Year made = {} "

    def is_dynamic(self):
        """determine if typing is dynamic"""

        return self.typing == "dynamic"
    

