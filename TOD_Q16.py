"""
Tank capacity is 1000L. Inflow every minute given.
Stop when overflow occurs and print minute number.
"""
def overflow_minute(inflows: list[int]) -> int:
    total = 0

    for minute, inflow in enumerate(inflows, start=1):
        total += inflow
        if total > 1000:
            return minute

    return -1  # no overflow