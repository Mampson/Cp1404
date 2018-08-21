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
        return("Invalid score")
    elif score >= 90:
        return("Excellent")
    elif score >= 50:
        return("Passable")
    else:
        return("Bad")


def get_score():
    """Take score input"""
    return float(input("Enter score: "))


main()
