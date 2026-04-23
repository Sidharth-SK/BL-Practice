"""
Check if digits of a number are strictly increasing left to right
"""
def asce_pattern(num: int) -> str:
    return "YES" if all(x < y for x, y in zip(str(num), str(num)[1:])) else "NO"
