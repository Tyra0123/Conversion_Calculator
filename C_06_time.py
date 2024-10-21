time_dict = {
    "ms": 86400000,
    "sec": 86400,
    "min": 1440,
    "hr": 24,
    "days": 1,
    "weeks": .142857,
    "months": .0328767,
    "years": .00273973
}

# Get amount and units (assume they are valid)
amount = float(input("Amount? "))
from_unit = input("From Unit? ")
to_unit = input("To Unit? ")

# Multiply to get to our standard value
multiply_by = time_dict[to_unit]
standard = amount * multiply_by

# Divide to get to our desired value
divide_by = time_dict[from_unit]
answer = standard / divide_by

print(f"There are {answer:.2f} {to_unit} in {amount} {from_unit}")
