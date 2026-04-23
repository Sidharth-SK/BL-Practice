"""
Problem Statement
Reverse a number and check if original equals reversed.
"""
def is_palindrome(number: int) -> str:
    original = number
    reversed_num = 0

    while number > 0:
        digit = number % 10
        reversed_num = reversed_num * 10 + digit
        number //= 10

    return "PALINDROME" if original == reversed_num else "NOT PALINDROME"
