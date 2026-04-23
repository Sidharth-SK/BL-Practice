"""
Fare rules:
● Distance × ₹2/km
● Senior citizen → 30% discount
● Child (<12) → 50% discount
"""
def calc_fare(distance: int, age: int) -> float:
    """
    Age below 12 is considered a minor
    Age of 65 and above is considered senior citizen (default)
    """
    fare: float = distance * 2
    discount: float = 0.50 if age < 12 else 0.30 if age >= 65 else 0
    return fare * (1 - discount)