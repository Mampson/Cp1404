"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    # denominator_checked = denominator
    # 3)This is to so the needs for ZeroDivisionError or just stating the rule in the early prompt to avoid confusion
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
except ValueError:
    print("Numerator and denominator must be valid numbers!")
# except ZeroDivisionError:

print("Finished.")

# 1 when the entered values are not int type or number type
# 2 when the denominatior == 0
# 3 Possibly by re prompting for denomionator if zero is entered before assigning and calculating
