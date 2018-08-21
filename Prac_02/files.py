# creates output file
OUTPUT_FILE = "name.txt"

# open write outputfile
out_file = open("name.txt", 'w')
# prompts user for name
name = input("Please enter your name, using only letters: ")
print(name, file=out_file)
out_file.close()

# creates output file
OUTPUT_FILE = "name.txt"

# open write outputfile
next_file = open("name.txt", 'w')
# prompts user for name
name = input("Please enter your name, using only letters: ")
print("Your name is: ", name, '\n')
next_file.close()

# calls numbers file
numbers_read = open("numbers", "r")
# reads numbers first line
num1 = int(numbers_read.readline())
# reads numbers next line
num2 = int(numbers_read.readline())
# prints the numbers found on each line and prints their sum
print(num1, " ", num2, "\n")
print("the sum equals: ", num1 + num2, '\n')
numbers_read.close()

# extended file reader, for any number of numbers in a file
numbers2_read = open("numbers2.txt", "r")
file_total = 0

for line in numbers2_read:
    current_number = int(line)
    file_total = file_total + current_number
print("The total sum of this file is:", file_total)
numbers2_read.close()
