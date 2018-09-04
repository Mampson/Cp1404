""""
Count name occurence in string input
by Matthew Sampson

"""


def main():
    words_entry = input("Enter your string: ")
    strings = words_entry.split(" ")
    sorted_list = build_string_list(strings)
    print_string_count(sorted_list)


def build_string_list(strings):
    """Build sorted list containing both all string elements and their occurrence count"""

    for i in range(len(strings)):
        string = strings[i]
        count = get_number_of_word(strings[i])
        string_counted_list = [string, count]

    string_counted_list.sort()

    return string_counted_list




def print_string_count(string_list):
    """Print string with value within list of strings"""

    print(string_list)
    #print("{} : ".format(string_list)


def get_number_of_word(strings):
    """ Count the occurrence of word in list of strings"""

    for i in range(len(strings)):
        count = 0
        if strings[i] in strings:
            count = count + 1
        return count


main()
