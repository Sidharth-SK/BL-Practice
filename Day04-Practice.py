#PROG2: Comparing size & creation time of list & tuple
import timeit
import sys
list1: list[int] = [i for i in range(100)]
tuple1: tuple[int] = tuple(list1)
print(f"Size of List: {sys.getsizeof(list1)} bytes")
print(f"Size of Tuple: {sys.getsizeof(tuple1)} bytes")
print(f"Time taken to create List: {timeit.timeit('list1 = [i for i in range(100)]', number=10000)} seconds")
print(f"Time taken to create Tuple: {timeit.timeit('tuple1 = tuple([i for i in range(100)])', number=10000)} seconds")

#PROG5: Union set operation
school_friends: list[str] = ["Alice", "Bob", "Charlie", "David"]
college_friends: list[str] = ["Eve", "Alice", "Charlie", "David"]
def all_unique_friends(*friend_lists):
    return list(set().union(*friend_lists))
unique_friends = all_unique_friends(school_friends, college_friends)
print("Unique Friends:", unique_friends)

#EMI Generator Program
def monthly_rate(rate_annual: float) -> float:
    return rate_annual / (12 * 100)


def calculate_emi(principal: float, rate_annual: float, years: int) -> float:
    r = monthly_rate(rate_annual)
    n = years * 12
    return (principal * r * (1 + r)**n) / ((1 + r)**n - 1)


def emi_schedule(principal: float, rate_annual: float, years: int):
    r = monthly_rate(rate_annual)
    emi = calculate_emi(principal, rate_annual, years)

    balance = principal
    schedule = []

    for month in range(1, years * 12 + 1):
        interest = balance * r
        principal_paid = emi - interest
        balance -= principal_paid

        schedule.append({
            "Month": month,
            "EMI": round(emi, 2),
            "Interest": round(interest, 2),
            "Principal": round(principal_paid, 2),
            "Balance": round(max(balance, 0), 2)
        })

    return schedule


def display_schedule(schedule):
    print(f"{'Month':<6}{'EMI':<10}{'Interest':<12}{'Principal':<12}{'Balance':<12}")
    for row in schedule:
        print(f"{row['Month']:<6}{row['EMI']:<10}{row['Interest']:<12}{row['Principal']:<12}{row['Balance']:<12}")


# Main
def main():
    P = float(input("Enter Principal: "))
    R = float(input("Enter Annual Interest Rate (%): "))
    T = int(input("Enter Time (years): "))

    schedule = emi_schedule(P, R, T)
    display_schedule(schedule)


if __name__ == "__main__":
    main()