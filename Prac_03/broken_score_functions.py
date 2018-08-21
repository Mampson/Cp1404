"""
CP1404/CP5632 - Practical
Program to determine score strength by Matt Sampson
"""


def main():
    """Determine score strength by Matt Sampson"""

    score = get_score()
    determine_score_strength(score)


def determine_score_strength(score):
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


def get_score():
    """Take score input"""
    return float(input("Enter score: "))


main()
