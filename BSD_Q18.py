"""
Bus has 40 seats. For each booking request:
● If seats available → CONFIRMED
● Else → WAITLISTED
"""
def allocate_seats(requests: list[int]) -> list[str]:
    seats = 40

    def process(req: int) -> str:
        nonlocal seats
        if req <= seats:
            seats -= req
            return "CONFIRMED"
        return "WAITLISTED"

    return [process(r) for r in requests]