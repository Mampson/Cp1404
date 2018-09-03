""""
Count name occurence in string input
by Matthew Sampson

"""


def main():
    words_entry = input("Enter your string: ")
    strings = words_entry.split(" ")

    for i in range(len(strings)):
        string = strings[i]
        count = get_number_of_word(strings[i])
        print_string_count(string, count)


def print_string_count(string, number):
    """Print string with value within list of strings"""

    print("{} : {}".format(string, number))


def get_number_of_word(strings):
    """ Count the occurrence of word in list of strings"""

    for i in range(len(strings)):
        count = 0
        if strings[i] in strings:
            count = count + 1
        return count


main()
