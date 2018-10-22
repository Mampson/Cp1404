"""
CP1404/CP5632 Practical
Clean up file program
by Matthew Sampson
"""
import shutil
import os


def main():
    """File clean up program"""
    print("Starting directory is: {}".format(os.getcwd()))
    os.chdir('Lyrics/Christmas')
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))
    print(" Current directory is: {} ".format((os.getcwd())))
    print(" Files/folders in this dir: {} ".format(os.listdir()))
    os.chdir('temp')
    print(" Current directory is: {} ".format((os.getcwd())))
    print(" Files/folders in this dir: {} ".format(os.listdir()))

    for filename in os.getcwd():
        if os.path.isdir(filename):
            combined_name = os.path.join(dir_)
            edited_name = os.path.join(get_fixed_filename(filename))
            os.rename(edited_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    for char in filename:
        if char.isupper():
            upper_case = filename.find(char)
            new_name = filename[:upper_case] + "_" + filename[upper_case:]
    return new_name


def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics/Christmas')
    print(os.getcwd())
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        for filename in filenames:
            combined_name = os.path.join(directory_name, filename)
            edited_name = os.path.join(directory_name, get_fixed_filename(filename))
            os.rename(combined_name, edited_name)
            print(edited_name)


# main()
demo_walk()
