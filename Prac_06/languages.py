"""
Test programing language class
by Matthew Sampson

"""

from Prac_06.programming_language import ProgramingLanguage


def main():
    """ Test programming languages class object """

    ruby = ProgramingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgramingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgramingLanguage("Visual Basic", "Static", False, 1991)
    languages = [ruby, python, visual_basic]

    print(ruby)

    print("Dynamic languages are: ")
    
    for language in languages:
        if language.is_dynamic():
            print(language)


main()
