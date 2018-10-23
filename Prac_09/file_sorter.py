"""
CP1404
File os sorter
by Matthew Sampson
Prac 09
"""

import shutil
import os


def main():
    """Create and sort files into required sub-directiories"""

    print("Staring dir : {} ".format(os.getcwd()))
    os.chdir('FilesToSort')
    print(os.listdir())
    file_formats = {"Spreadsheets": "xls" or "xlsx", "Images": "png" or "jpg" or "gif",
                    "Docs": "doc" or "docx" or "txt"}

    for file_format in file_formats:
        try:
            os.mkdir(file_format)
        except FileExistsError:
            pass

    for filename in os.listdir():

        print("the returned name", filename)
        # current_dir = os.getcwd()
        for file_format in file_formats:
            get_sorting_param(file_format, file_formats)
            if filename not in file_formats.get(file_format):
                print(file_format)
                if check_file_type(filename, file_formats.get(file_format)):
                    new_dir = "{}".format(file_format)
                    print(filename)
                    print(new_dir)
                    # new_name = os.path.join(new_dir, filename)
                    shutil.move(filename, new_dir)


def get_sorting_param(file_format, file_formats):
    """Prompt user for sorting key input"""
    file_type = file_formats.get(file_format)
    input_choice = input("What category would like to sort {} into? ".format(file_type))
    if input_choice in file_formats:
        return input_choice
    else:
        return None


def check_file_type(filename, file_format):
    """Check file name for .type """
    type_check_string = "{}".format(file_format)
    if filename.find(type_check_string):
        return True
    else:
        return False


main()
