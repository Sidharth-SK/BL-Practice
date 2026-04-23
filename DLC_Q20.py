"""
Problem Statement
Given a number, repeatedly subtract sum of its digits until result is a single digit.
"""

def final_digit(number: int) -> int:
    digit_sum = lambda n: sum(map(int, str(n)))

    while number >= 10:
        number -= digit_sum(number)

    return number