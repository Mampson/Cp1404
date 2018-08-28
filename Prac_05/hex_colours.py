"""
Hexidecimal colour code translator
by Matthew Sampson
github.com/
"""

HEX_COLOURS = {"AliceBlue": "#f0f8ff", "aquamarine1": "#7fffd4", "azure1": "#f0ffff", "beige": "#f5f5dc",
               "blue1": "#0000ff", "brown": "#a52a2a", "burlywood": "#deb887", "CadetBlue": "#5f9ea0",
               "chartreuse1": "#7fff00", "chocolate": "#d2691e"}

number_of_colours = len(HEX_COLOURS)
# print(number_of_colours)

# for colour in range(len(HEX_COLOURS)):
# print("{} ".format(HEX_COLOURS.get(colour)))


colour_input = input("Choose your colour from the list: ")

while colour_input != "":
    print(HEX_COLOURS.get(colour_input))

    colour_input = input("Choose your colour from the list: ")
    # print("Not a valid colour.")
    # colour_input = input("Choose your colour from the list: ").lower()
