"""
User gets 3 attempts to enter correct PIN.
● Correct → ACCESS GRANTED
● All wrong → LOCKED
"""
def check_pin(correct_pin: int, attempts: list[int]) -> str:
    return "ACCESS GRANTED" if any(a == correct_pin for a in attempts) else "LOCKED"