#Armstrong number
def is_armstrong(number: int) -> str:
    digits = list(map(int, str(number)))
    power = len(digits)

    return (
        "YES"
        if number == sum(d ** power for d in digits)
        else "NO"
    )