"""
CP1404
Wikipedia search prompt engine
by Matt Sampson

"""

import wikipedia


def main():
    """Search wikipedia for user input"""

    search_value = get_search_parameter()
    while search_value != "":
        try:
            summary = wikipedia.search(search_value)
            page = wikipedia.page(search_value)
            print(summary)
            print(page.title)
            print(page.url)
            search_value = get_search_parameter()
        except wikipedia.exceptions.DisambiguationError as e:
            print (e.options)

def get_search_parameter():
    """Prompt for user input """

    search_topic = input("Please enter the topic you wish to search: ")
    return str(search_topic)


main()
